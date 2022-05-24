from xml.dom.minidom import Element
from sklearn.cluster import KMeans 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#Kmeans Sklearn

#Import data
#rimer input, path del archivo <-------------------------------------
input1 = '../docs/credit_test.csv'
df_original = pd.read_csv(input1)
df = pd.read_csv(input1)
#print(df.shape)


for column in df:
    df = df.fillna(0)
    print('Índice de la columna: ', column)
    print('Contenido de la columna: ', df[column].dtypes)
    if (df[column].dtypes == "object"):
        uniqueValues = df[column].unique().tolist()
        i=0
        for uV in uniqueValues:
            df[column] = df[column].replace(uV, i)
            i+=1
           
        print(df[column].values)
    else: print("int") 

df = np.array(df)

#dos input: las dos columnas para kmeans
# debe ser en (int) para seleccionarlas por indice

input2 = 3 #Ejemplo  <----------------------------------
input3 = 4 #Ejemplo  <----------------------------------

data = df[:,[input2, input3]] # se seleccionan las del input
#print(data)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(data)

#colors for plot after the clustering
color_theme = np.array(['c', 'b', 'y', 'g', 'grey', 'violet'])

#numero de cluster otro inpunt
n_k = 4 #Ejemplo  <----------------------------------

#Creating the model by KMeans
clustering = KMeans(n_clusters=n_k).fit(X_train)
labels = clustering.labels_
# predict = clustering.predict([[90, 50], [12, 3]]) #Predict the cluster to which it belongs
centroids = clustering.cluster_centers_


#--------------------------------------------------------------------------------------------#
#---------------- Para mostrar en el html---------------------------------#

df_original['Output'] = labels
#print(df_original)

plt.subplot(2,2,1)
plt.plot(data[:,0], data[:,1], 'ob')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data')
#Plot for centroids from MKmeas
plt.subplot(2,2,2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centroids')
plt.plot(centroids[:,0], centroids[:,1], 'or')

#Plot centroids with data
plt.subplot(2,2,3)
plt.plot(X_train[:,0], X_train[:,1], 'ob')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centroids inside data')
plt.plot(centroids[:,0], centroids[:,1], 'or')

#Plot with different colors by clostering

#Plot centroids with data
plt.subplot(2,2,4)
plt.scatter(x = X_train[:,0], y = X_train[:,1], c=color_theme[clustering.labels_], s=50)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means classification')
plt.plot(centroids[:,0], centroids[:,1], '*r')

# plt.legend()
plt.show()
