import os
import ollama
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def zaladuj_i_podziel(folder="."):
    dokumenty = []
    for plik in os.listdir(folder):
        if plik.endswith(".txt"):
            loader = TextLoader(os.path.join(folder, plik))
            dokumenty.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    return splitter.split_documents(dokumenty)


def stworz_vector_store(chunki):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma.from_documents(chunki, embeddings)


def zapytaj_rag(vector_store, zapytanie):
    wyniki = vector_store.similarity_search(zapytanie, k=3)
    kontekst = "\n".join([w.page_content for w in wyniki])
    prompt = f"""Answer based only on context below.
If answer not in context, say "I don't know".

Context:
{kontekst}

Question: {zapytanie}
"""
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def main():
    print("Initializing RAG system...")
    chunki = zaladuj_i_podziel()
    vector_store = stworz_vector_store(chunki)
    print("Ready! Type 'quit' to exit.\n")

    while True:
        zapytanie = input("Your question: ")
        if zapytanie.lower() == "quit":
            break
        odpowiedz = zapytaj_rag(vector_store, zapytanie)
        print(f"Answer: {odpowiedz}\n")


if __name__ == "__main__":
    main()
