import pandas as pd
from app.rag_pipeline import generate_answer

df = pd.read_csv("evaluation/test_questions.csv")

correct = 0

for _, row in df.iterrows():

    result = generate_answer(row["question"])

    answer = result["answer"].lower()

    if row["expected_answer"].lower() in answer:
        correct += 1

accuracy = correct / len(df)

print("Evaluation accuracy:", accuracy)