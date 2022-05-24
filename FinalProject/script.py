import streamlit as st
import pandas as pd
from backEnd import *
from backEnd import data_types

st.title('K-Means Clustering')
uploaded_file = st.file_uploader("Choose a file", type=["csv"])
if st.button("Cargar"):
    if uploaded_file is not None:
        file = uploaded_file
        df = pd.read_csv(file)
        df.head()
        st.write(df)
        data_types(df)


x = st.selectbox("Seleccione el indice #1")
y = st.number_input('Indice Y')
if x and y is not None:
    if st.button("Set"):
        index(x,y,df)