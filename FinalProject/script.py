import streamlit as st
import pandas as pd
# from backEnd import *

st.title('K-Means Clustering')
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    file = uploaded_file
    df = pd.read_csv(file)
    df.head()
    st.write(df)

    print("=======================================================")
    df = pd.DataFrame(df)
    st.subheader("Columnas del Dataset")
    df.columns.values
    print(df.columns.values)
    
    columns_name = df.columns.values
    option = st.selectbox( 'Seleccione la primera columna: ', options=columns_name, index=0)
    st.write('Has selecionado en tu primera columna:', option)

    option = st.selectbox( 'Seleccione la segunda columna: ', options=columns_name, index=1)
    st.write('Has selecionado en tu sugunda columna:', option)

    values = st.slider('¿Cual es la cantidad de cluster que desea ver?', min_value=2, max_value=5, step=1)
    st.write('Su cantidad selecciona de cluester:', values)