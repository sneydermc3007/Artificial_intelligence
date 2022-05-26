import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans 
#from backEnd import *

st.title('K-Means Clustering')
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    file = uploaded_file
    df = pd.read_csv(file)
    df_original = df.copy()
    st.subheader("Dataframe")
    st.dataframe(df)
    for column in df:
        print('Índice de la columna: ', column)
        print('Contenido de la columna: ', df[column].dtypes)
        if (df[column].dtypes == "object"):
            uniqueValues = df[column].unique().tolist()
            i=0
            for uV in uniqueValues:
                df[column] = df[column].replace(uV, i)
                i+=1
                
            #print(df[column].values)
        else: print("int") 

    st.subheader("Discretized dataframe")
    st.dataframe(df)

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
    st.write('Su cantidad selecciona de cluester:', values)
    df = np.array(df)
    if st.button('Ejecutar'):
        optionx=int(optionx)
        optiony=int(optiony)
        data = df[:,[optionx, optiony]] # se seleccionan las del input
        st.subheader("values ​​for clustering")
        st.dataframe(data)
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(data)
        st.subheader("Scaled dataframe")
        st.dataframe(X_train)

        color_theme = np.array(['c', 'b', 'y', 'g', 'grey', 'violet'])
        k = int(values)
        #Creating the model by KMeans
        clustering = KMeans(n_clusters=k).fit(X_train)
        labels = clustering.labels_
        centroids = clustering.cluster_centers_
        df_original['Output'] = labels
        st.subheader("Output from Kmeans model")
        st.dataframe(df_original)
        
        import matplotlib.pyplot as plt

        def fig1():      
            fig = plt.figure(figsize = (10, 5)) 
            plt.plot(data[:,0], data[:,1], 'ob')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Data')
            st.subheader("Original data")
            st.pyplot(fig)

        def fig2():
            #Plot centroids with data
            fig = plt.figure(figsize = (10, 5)) 
            st.subheader("centroids")
            st.write(centroids)
            plt.plot(X_train[:,0], X_train[:,1], 'ob')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Centroids inside data')
            plt.plot(centroids[:,0], centroids[:,1], 'or')
            st.subheader("Plot with centroids")
            st.pyplot(fig)

        def fig3():
            fig = plt.figure(figsize = (10, 5)) 
            plt.scatter(x = X_train[:,0], y = X_train[:,1], c=color_theme[clustering.labels_], s=50)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('K-Means classification')
            plt.plot(centroids[:,0], centroids[:,1], '*r')
            st.subheader("Plot with different colors by clostering")
            st.pyplot(fig)

        fig1()
        fig2()
        fig3()    

