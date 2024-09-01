import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf

st.header('MLOps Deployment Practice')
name = st.text_input("May I know your name")

if st.button("Enter"):
    st.write(f'Hello {name}.. Welcome to MLOps Practice')

data = yf.download("SPY AAPL", period="1mo",progress=False)
#st.write(f'{data}')
st.dataframe(data)

ticker = yf.Ticker('AAPL',progress=False)
aapl_df = ticker.history(period="1y")
aapl_df['Close'].plot(title="APPLE's stock price")


tickers = yf.Tickers('msft aapl goog')

# access each ticker using (example)
tickers.tickers['MSFT'].info
tickers.tickers['AAPL'].history(period="1mo")
tickers.tickers['GOOG'].actions