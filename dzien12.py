from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def zaladuj_i_podziel(sciezka, chunk_size=200, chunk_overlap=50):
    loader = TextLoader(sciezka)
    dokument = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(dokument)


def stworz_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma.from_documents(chunks, embeddings)


def wyszukaj(vector_store, zapytanie, k=3):
    wyniki = vector_store.similarity_search(zapytanie, k=k)
    return wyniki


def wypisz_wyniki(wyniki):
    for i, wynik in enumerate(wyniki):
        print(f"Wynik {i+1}:")
        print(wynik.page_content)
        print("---")


def main():
    chunks = zaladuj_i_podziel("dokument.txt")
    print(f"Liczba chunków: {len(chunks)}")

    print("Tworzenie embeddingów...")
    vector_store = stworz_vector_store(chunks)
    print("Vector store gotowy!\n")

    zapytanie = "What is RAG and how does it work?"
    print(f"Zapytanie: {zapytanie}\n")
    wyniki = wyszukaj(vector_store, zapytanie)
    wypisz_wyniki(wyniki)


if __name__ == "__main__":
    main()
