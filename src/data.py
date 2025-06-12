import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "7d", interval: str = "1d") -> pd.DataFrame:
    """
    Fetch stock data from Yahoo Finance
    """

    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    return df

def fetch_crypto_data(ticker: str, period: str = "7d", interval: str = "1d") -> pd.DataFrame:
    """
    Fetch crypto data from Yahoo Finance
    """

    crypto = yf.Ticker(ticker)
    df = crypto.history(period=period, interval=interval)
    return df

df = fetch_stock_data("AAPL")