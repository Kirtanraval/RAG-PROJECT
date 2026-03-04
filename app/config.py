import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 5
FETCH_K = 20
SEARCH_TYPE = "mmr"
OLLAMA_MODEL = "llama3"
OLLAMA_BASE_URL = "http://localhost:11434"
TEMPERATURE = 0.2
MAX_TOKENS = 512
API_HOST = "0.0.0.0"
API_PORT = 8000