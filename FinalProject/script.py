import streamlit as st
import pandas as pd
#from backEnd import *

st.title('K-Means Clustering')
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    file = uploaded_file
    df = pd.read_csv(file)
    df.head()
    st.write(df)

    print("=======================================================")
    df = pd.DataFrame(df)
    df = df.fillna(0)
    st.subheader("Columnas del Dataset")
    df.columns.values
    print(df.columns.values)
    
    columns_name = df.columns.values
    val = []
    for i in range(len(columns_name)):
        val.append(i)
    print(val)

    optionx = st.selectbox( 'Seleccione la primera columna: ', options=val, index=0)
    st.write('Has selecionado en tu primera columna:', optionx)

    optiony = st.selectbox( 'Seleccione la segunda columna: ', options=val, index=0)
    st.write('Has selecionado en tu sugunda columna:', optiony)
 
    values = st.slider('¿Cual es la cantidad de cluster que desea ver?', min_value=2, max_value=5, step=1)
    z = st.write('Su cantidad selecciona de cluester:', values)

    if st.button('Ejecutar'):
        st.write(optionx)
        optionx=int(optionx)
        st.write(optiony)
        optiony=int(optiony)
        data = df[:,[optionx, optiony]] # se seleccionan las del input
