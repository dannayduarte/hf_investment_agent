import gradio as gr
from src.data import fetch_stock_data
from huggingface_hub import InferenceClient
import os

def get_hf_token():
    token = os.getenv("HF_TOKEN")
    if not token:
        token = input("Enter your Hugging Face API token: ")
        os.environ["HF_TOKEN"] = token
    return token

def get_client():
    token = get_hf_token()
    return InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=token)

client = get_client()

def chat_agent(message, history, ticker, df):
    # Allow user to change ticker with a command like '/ticker TSLA'
    if message.strip().lower().startswith('/ticker '):
        new_ticker = message.strip().split(' ', 1)[1].upper()
        try:
            new_df = fetch_stock_data(new_ticker)
            return f"Ticker changed to {new_ticker}. You can now ask about {new_ticker}.", new_ticker, new_df
        except Exception as e:
            return f"Failed to load data for ticker '{new_ticker}': {e}", ticker, df
    context = f"Stock data summary for {ticker}:\n{df.describe().to_string()}\n\n"
    prompt = context + f"User: {message}\nAssistant:"
    response = client.text_generation(prompt, max_new_tokens=100, temperature=0.7)
    # The response may include the prompt, so extract only the answer
    answer = response.split("Assistant:")[-1].strip()
    return answer, ticker, df

with gr.Blocks() as demo:
    gr.Markdown("# Stock Chat Agent\nAsk anything about a stock!\n\n- To change ticker, type `/ticker SYMBOL` (e.g., `/ticker TSLA`) in the chat.")
    state_ticker = gr.State("AAPL")
    state_df = gr.State(fetch_stock_data("AAPL"))
    def chat_wrapper(message, history, ticker, df):
        result, new_ticker, new_df = chat_agent(message, history, ticker, df)
        return result, new_ticker, new_df
    chatbot = gr.ChatInterface(
        fn=chat_wrapper,
        additional_inputs=[state_ticker, state_df],
        additional_outputs=[state_ticker, state_df],
        title=None,
        description=None
    )
    gr.Markdown("""\n- Example tickers: AAPL, MSFT, TSLA, GOOGL, AMZN\n- To change ticker, type `/ticker SYMBOL` in the chat (e.g., `/ticker TSLA`).\n""")

if __name__ == "__main__":
    demo.launch()
