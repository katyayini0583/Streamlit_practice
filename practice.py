import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import datetime

st.header('MLOps Deployment Practice')
name = st.text_input("May I know your name")

if st.button("Enter"):
    st.write(f'Hello {name}.. Welcome to MLOps Practice')

start_date = st.date_input("Choose start date", datetime.date(2019, 7, 6))
end_date = st.date_input("Choose end date", datetime.date(2019, 7, 6))

data = yf.download("AAPL",progress=False,start=start_date,end=end_date)
#st.write(f'{data}')
st.dataframe(data)
#data['Close'].plot(Title='Apple stocks close chart')

st.line_chart(data['Close'])