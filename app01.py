import os
import ollama
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def zaladuj_dokumenty(folder="."):
    dokumenty = []
    for plik in os.listdir(folder):
        if plik.endswith(".txt"):
            loader = TextLoader(os.path.join(folder, plik))
            dokumenty.extend(loader.load())
    return dokumenty


def podziel_na_chunki(dokumenty, chunk_size=200, chunk_overlap=50):
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
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# Streamlit UI
st.title("RAG Document Q&A")
st.write("Ask questions based on loaded documents.")

if "vector_store" not in st.session_state:
    with st.spinner("Loading documents and creating vector store..."):
        dokumenty = zaladuj_dokumenty()
        chunki = podziel_na_chunki(dokumenty)
        st.session_state.vector_store = stworz_vector_store(chunki)
    st.success(f"Ready! Loaded {len(dokumenty)} documents.")

zapytanie = st.text_input("Your question:")

if zapytanie:
    with st.spinner("Searching..."):
        kontekst = wyszukaj_kontekst(st.session_state.vector_store, zapytanie)
        odpowiedz = zapytaj_llm(kontekst, zapytanie)
    st.write("**Answer:**")
    st.write(odpowiedz)
    with st.expander("Context used"):
        st.write(kontekst)
