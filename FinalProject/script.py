import streamlit as st
import pandas as pd
from backEnd import *


st.title('K-Means Clustering')
uploaded_file = st.file_uploader("Choose a file", type=["csv"])
if st.button("Cargar"):
    if uploaded_file is not None:
        file = uploaded_file
        df = pd.read_csv(file)
        df.head()
        st.write(df)
        
