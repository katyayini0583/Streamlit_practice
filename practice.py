import pandas as pd
import numpy as np
import streamlit as st

st.header('MLOps Deployment Practice')
name = st.text_input("May I know your name")

st.button("Enter", type="primary")
st.write(f'Hello {name}.. Welcome to MLOps Practice')
