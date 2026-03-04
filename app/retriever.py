from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

persist_directory = "./chroma_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

database = Chroma(
    collection_name="my_collection",
    embedding_function=embeddings,
    persist_directory=persist_directory
)

retriever = database.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "fetch_k": 20}
)