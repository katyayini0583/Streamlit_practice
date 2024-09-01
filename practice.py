import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import datetime

st.header('Stock Trends')

symbols = ['MSFT', 'GOOGL', 'AMZN', 'TSLA']

st.selectbox('Select the stock',symbols)
col1,col2 = st.columns(2)
start_date = col1.date_input("Choose start date", datetime.date(2019, 7, 6))
end_date = col2.date_input("Choose end date", datetime.date(2019, 7, 6))

data = yf.download("AAPL",progress=False,start=start_date,end=end_date)
#st.write(f'{data}')
#st.dataframe(data)
#data['Close'].plot(Title='Apple stocks close chart')

st.subheader(f'Apple stocks closing trend between {start_date} and {end_date}')
st.line_chart(data['Close'])
