import os
import tempfile
from groq import Groq
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def zaladuj_dokument(sciezka, rozszerzenie):
    if rozszerzenie == ".pdf":
        loader = PyPDFLoader(sciezka)
    elif rozszerzenie == ".txt":
        loader = TextLoader(sciezka)
    elif rozszerzenie == ".docx":
        loader = Docx2txtLoader(sciezka)
    return loader.load()


def podziel_na_chunki(dokumenty, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(dokumenty)


def stworz_vector_store(chunki):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma.from_documents(chunki, embeddings)


def wyszukaj_kontekst(vector_store, zapytanie, k=3):
    wyniki = vector_store.similarity_search(zapytanie, k=k)
    return "\n".join([w.page_content for w in wyniki])


def zapytaj_llm(kontekst, zapytanie):
    prompt = f"""Answer the question based only on the context below.
If the answer is not in the context, say "I don't know".

Context:
{kontekst}

Question: {zapytanie}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# Streamlit UI
st.title("RAG Document Q&A")
st.write("Upload your documents and ask questions.")

uploaded_files = st.file_uploader(
    "Upload documents (PDF, TXT, DOCX)",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    if "vector_store" not in st.session_state or st.session_state.get("loaded_files") != [f.name for f in uploaded_files]:
        with st.spinner("Processing documents..."):
            wszystkie_dokumenty = []

            for uploaded_file in uploaded_files:
                rozszerzenie = os.path.splitext(uploaded_file.name)[1].lower()

                with tempfile.NamedTemporaryFile(delete=False, suffix=rozszerzenie) as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name

                dokumenty = zaladuj_dokument(tmp_path, rozszerzenie)
                wszystkie_dokumenty.extend(dokumenty)
                os.unlink(tmp_path)

            chunki = podziel_na_chunki(wszystkie_dokumenty)
            st.session_state.vector_store = stworz_vector_store(chunki)
            st.session_state.loaded_files = [f.name for f in uploaded_files]

        st.success(f"Ready! Loaded {len(uploaded_files)} documents, {len(chunki)} chunks.")

    zapytanie = st.text_input("Your question:")

    if zapytanie:
        with st.spinner("Searching..."):
            kontekst = wyszukaj_kontekst(st.session_state.vector_store, zapytanie)
            odpowiedz = zapytaj_llm(kontekst, zapytanie)
        st.write("**Answer:**")
        st.write(odpowiedz)
        with st.expander("Context used"):
            st.write(kontekst)
else:
    st.info("Please upload at least one document to start.")
