# RAG-PROJECT

## RAG Project(FastAPI + Chroma + Ollama)

A production-style Retrieval-Augmented Generation (RAG) system that retrieves information from a document database and generates answers using a local LLM.

This project demonstrates how modern AI systems combine vector search with large language models to answer questions grounded in real documents.

---

## Overview

This project implements a full RAG pipeline:

1. Documents are ingested and split into smaller chunks.
2. Chunks are converted into embeddings using a transformer model.
3. Embeddings are stored in a Chroma vector database.
4. A retriever searches for relevant chunks based on a user query.
5. Retrieved context is sent to a local LLM via Ollama.
6. The LLM generates an answer grounded in the retrieved context.

The entire system is exposed as an API using FastAPI and can be deployed inside a Docker container.

---

## Architecture

User Query
↓
FastAPI API
↓
Retriever (Chroma Vector DB)
↓
Relevant Document Chunks
↓
Local LLM (Ollama)
↓
Generated Answer

---

## Tech Stack

Python
FastAPI
LangChain
ChromaDB
Sentence Transformers
Ollama (local LLM runtime)
Docker

---

## Project Structure

RAG_PROJECT/

app/

- main.py (FastAPI API)
- rag_pipeline.py (RAG logic)
- retriever.py (vector retrieval)
- config.py (configuration)
- logger.py (logging)

ingestion/

- ingestion_pipeline.py (document ingestion)

evaluation/

- evaluate.py (evaluation scripts)

data/

- source documents

chroma_db/

- vector database storage

requirements.txt
Dockerfile
README.md

---

## Features

Document ingestion pipeline
Semantic chunking
Local embedding model
Vector search with ChromaDB
MMR-based retrieval
Local LLM inference using Ollama
FastAPI API endpoint
Dockerized deployment

---

## Installation

### 1. Clone the repository

git clone https://github.com/Kirtanraval/RAG-PROJECT.git

cd rag-project

---

### 2. Create a virtual environment

python -m venv .venv

Activate:

Windows
.venv\Scripts\activate

Mac/Linux
source .venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Install Ollama

Install Ollama from:

https://ollama.com

Pull a model:

ollama pull llama3

Start the model:

ollama run llama3

---

## Document Ingestion

Add documents to the data folder.

Run ingestion:

python ingestion/ingestion_pipeline.py

This will:

- load documents
- split them into chunks
- generate embeddings
- store them in ChromaDB

---

## Running the API

Start the FastAPI server:

uvicorn app.main:app --reload

Open the API docs:

http://localhost:8000/docs

Example request:

POST /ask

{
"question": "Where did Falcon 1 launch from?"
}

---

## Docker Deployment

Build the image:

docker build -t rag-service .

Run the container:

docker run -p 8000:8000 rag-service

API will be available at:

http://localhost:8000/docs

---

## Evaluation

Run evaluation script:

python evaluation/evaluate.py

This measures retrieval and answer accuracy against a small test dataset.

---

## Example Use Cases

Internal knowledge base search
Company documentation assistant
Technical support bot
Research paper assistant
Developer documentation search

---

## Future Improvements

Cross-encoder reranking
Streaming responses
Prompt injection protection
Query caching
Document metadata filtering
LangSmith observability

---

## Author

RK
AI / ML Engineering Projects


