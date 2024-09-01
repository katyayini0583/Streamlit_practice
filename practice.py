import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf

st.header('MLOps Deployment Practice')
name = st.text_input("May I know your name")

if st.button("Enter"):
    st.write(f'Hello {name}.. Welcome to MLOps Practice')

data = yf.download("AAPL", period="1mo",progress=False)
#st.write(f'{data}')
st.dataframe(data)
data['close'].plot(Title='Apple stocks close chart')