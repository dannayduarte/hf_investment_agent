# Stock Chat Agent

A conversational AI agent that answers questions about any stock ticker using real-time data from Yahoo Finance and a large language model (LLM) from Hugging Face. The agent loads the latest stock data, summarizes it, and allows users to ask questions in natural language—just like ChatGPT, but for stocks!

## Features
- Fetches real-time stock data for any ticker (e.g., AAPL, MSFT, TSLA)
- Conversational interface powered by a Hugging Face LLM
- Users can change the stock ticker at any time by typing `/ticker SYMBOL` in the chat
- Runs locally or can be deployed publicly (e.g., Hugging Face Spaces)

## Example Use Cases
- "What was the highest closing price for TSLA this week?"
- "Did Apple stock go up or down?"
- "What is the average trading volume for MSFT?"
- "Switch to Google stock" (type `/ticker GOOGL`)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Create and Activate a Virtual Environment
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get a Hugging Face API Token
- Go to https://huggingface.co/settings/tokens
- Click "New token" (read access is enough)
- Copy the token

### 5. Set Your Hugging Face API Token (Server-Side Only)
```bash
export HF_TOKEN=your_huggingface_token
```

---

## Running Locally

```bash
python -m src.web_agent
```
- Open the local URL printed in your terminal (e.g., http://127.0.0.1:7860)
- Type `/ticker SYMBOL` (e.g., `/ticker TSLA`) in the chat to switch stocks
- Ask any question about the current stock!

---



## License
MIT
