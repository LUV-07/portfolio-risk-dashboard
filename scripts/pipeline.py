import numpy as np
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "SPY"]
START_DATE = "2023-01-01"
END_DATE = "2026-01-01"

DB_CONNECTION_URL = "postgresql://postgres:your_password@localhost:5432/portfolio_db"

def fetch_and_process_data(tickers, start, end):
    prices_df = yf.download(tickers, start=start, end=end)["Close"]
    
    if isinstance(prices_df.columns, pd.MultiIndex):
        prices_df.columns = prices_df.columns.droplevel(0)
        
    returns_df = prices_df.pct_change().dropna()
    
    return prices_df, returns_df

def save_to_postgres(prices_df, returns_df, db_url):
    engine = create_engine(db_url)
    
    prices_reset = prices_df.reset_index()
    returns_reset = returns_df.reset_index()
    
    prices_reset.to_sql("portfolio_prices", engine, if_exists="replace", index=False)
    returns_reset.to_sql("portfolio_returns", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    prices, returns = fetch_and_process_data(TICKERS, START_DATE, END_DATE)
    
    try:
        save_to_postgres(prices, returns, DB_CONNECTION_URL)
    except Exception as e:
        prices.to_csv("portfolio_prices.csv")
        returns.to_csv("portfolio_returns.csv")
