from src.data import fetch_stock_data
from transformers import pipeline
import os

def get_llm():
    return pipeline(
        "text-generation",
        model="google/flan-t5-small",
        token=os.getenv("HF_TOKEN")
    )

def ask_agent(df, question, llm):
    context = f"Stock data summary:\n{df.describe().to_string()}\n\n"
    prompt = context + f"User question: {question}\nAnswer:"
    response = llm(prompt, max_new_tokens=100)[0]['generated_text']
    return response.split("Answer:")[-1].strip()

if __name__ == "__main__":
    import getpass
    if not os.getenv("HF_TOKEN"):
        os.environ["HF_TOKEN"] = getpass.getpass("Enter your Hugging Face API token: ")

    ticker = input("Enter stock ticker (e.g., AAPL): ")
    df = fetch_stock_data(ticker)
    print(df)
    llm = get_llm()
    while True:
        question = input("Ask a question about this stock (or type 'exit'): ")
        if question.lower() == "exit":
            break
        print(ask_agent(df, question, llm))
