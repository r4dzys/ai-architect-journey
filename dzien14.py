import os
import ollama
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
    print(f"Załadowano {len(dokumenty)} dokumentów")
    return dokumenty


def podziel_na_chunki(dokumenty, chunk_size=200, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunki = splitter.split_documents(dokumenty)
    print(f"Liczba chunków: {len(chunki)}")
    return chunki


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


def main():
    print("Loading documents...")
    dokumenty = zaladuj_dokumenty()
    chunki = podziel_na_chunki(dokumenty)

    print("Creating vector store...")
    vector_store = stworz_vector_store(chunki)
    print("Ready!\n")

    pytania = [
        "What is Azure AI Search?",
        "What skills does an AI Business Analyst need?",
        "What is LangChain used for?"
    ]

    for pytanie in pytania:
        print(f"Question: {pytanie}")
        kontekst = wyszukaj_kontekst(vector_store, pytanie)
        odpowiedz = zapytaj_llm(kontekst, pytanie)
        print(f"Answer: {odpowiedz}")
        print("---\n")


if __name__ == "__main__":
    main()
