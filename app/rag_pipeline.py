from langchain_ollama import OllamaLLM
from .retriever import retriever
from .config import OLLAMA_MODEL

llm = OllamaLLM(model=OLLAMA_MODEL)

def generate_answer(query):

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Use the context to answer the question.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response