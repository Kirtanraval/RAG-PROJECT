from fastapi import FastAPI
from pydantic import BaseModel
from .rag_pipeline import generate_answer

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QueryRequest):

    result = generate_answer(request.question)

    return result