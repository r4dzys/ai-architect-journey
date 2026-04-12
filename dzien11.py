from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def zaladuj_dokument(sciezka):
    loader = TextLoader(sciezka)
    return loader.load()


def podziel_na_chunki(dokument, chunk_size=200, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(dokument)


def wypisz_chunki(chunks):
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(chunk.page_content)
        print("---")


def main():
    dokument = zaladuj_dokument("dokument.txt")
    chunks = podziel_na_chunki(dokument, chunk_size=200, chunk_overlap=100)
    wypisz_chunki(chunks)
    print(f"chunk_size=200, overlap=100: {len(chunks)} chunków")


if __name__ == "__main__":
    main()
