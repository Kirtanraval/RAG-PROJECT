import os

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.config import (
    DATA_DIR,
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def load_documents():

    loader = DirectoryLoader(
        DATA_DIR,
        glob="**/*.txt",
        show_progress=True
    )

    documents = loader.load()

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    return chunks


def create_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings


def store_in_chroma(chunks, embeddings):

    vectordb = Chroma(
        collection_name="my_collection",
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    vectordb.add_documents(chunks)

    print("Stored embeddings in Chroma.")


def run_ingestion():

    print("Starting ingestion pipeline...")

    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    chunks = split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    embeddings = create_embeddings()

    store_in_chroma(chunks, embeddings)

    print("Ingestion completed.")


if __name__ == "__main__":

    run_ingestion()