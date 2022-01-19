# -*- coding: utf-8 -*-
"""DatosUnificados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UwMYc-hYR3cdMbePZZ9ISR-aF83PCr46

Codigo para llamar datos unificados de los pacientes
"""

import pandas as pd

DFT1 = pd.read_csv('/content/sample_data/SEPSISLABEL_PACIENTES.csv', index_col=0)
DFSepsis = DFT1.T

DFT2 = pd.read_csv('/content/sample_data/Temp_PACIENTES.csv', index_col=0)
DFTemp = DFT2.T

DFT3 = pd.read_csv('/content/sample_data/Resp_PACIENTES.csv', index_col=0)
DFResp = DFT3.T

DFT4 = pd.read_csv('/content/sample_data/O2sat_PACIENTES.csv', index_col=0)
DFO2sat = DFT4.T

DFT5 = pd.read_csv('/content/sample_data/MAP_PACIENTES.csv', index_col=0)
DFMap = DFT5.T

DFT6 = pd.read_csv('/content/sample_data/HR_PACIENTES.csv', index_col=0)
DFHR = DFT6.T

DFT7 = pd.read_csv('/content/sample_data/Glucose_PACIENTES.csv', index_col=0)
DFGlucose = DFT7.T

DFSepsis

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize=(15,15))
fig.tight_layout()

X = np.linspace(0, 258)
plt.plot(X, DFSepsis[1],'o-', label= 'datos', linewidth = 0.5) #Datos filtrados
plt.ylim(0,1) # Limite en en Y
plt.ylabel('Escala') # Titulo Y
plt.xlabel('Semana') # Titulo X
plt.title("Sepsis pacientes") # Titulo grafica
plt.show
  
#plt.plot(DFSepsis,'o-', label= 'datos', linewidth = 0.5) #Datos filtrados

DFHR

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize=(15,15))
fig.tight_layout()

X = np.linspace(0, 258)
plt.plot(X,DFHR[1],'o', label= 'datos', linewidth = 0.5) #Datos filtrados
plt.ylabel('Escala') # Titulo Y
plt.xlabel('Semana') # Titulo X
plt.title("HR") # Titulo grafica
plt.show

# Llamar Semana

def semanas(numero):
  
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd

  fig = plt.figure(figsize=(20,20))
  fig.tight_layout()


  plt.subplot(3,3,1) # Subplot para visualizar las graficas en un mismo plot
  X = np.linspace(0, 258)
  plt.plot(X, DFSepsis[num],'o', label= 'datos', linewidth = 0.5) #Datos filtrados
  plt.ylim(0,1) # Limite en en Y
  plt.ylabel('Escala') # Titulo Y
  plt.xlabel('Semana') # Titulo X
  plt.title("Sepsis pacientes") # Titulo grafica
  
  plt.subplot(3,3,2) # Subplot para visualizar las graficas en un mismo plot
  X = np.linspace(0, 258)
  plt.plot(X, DFHR[num],'o', label= 'datos', linewidth = 1)  #Datos filtrados
  plt.ylim(40,120) # Limite en en Y
  plt.axhline(y=60, xmin=0, color= 'red') # Maximo normal de presión arterial
  plt.axhline(y=100, xmin=0, color= 'red') # Minimo normal de presión arterial
  plt.title("Frecuencia cardiaca (HR)")
  plt.ylabel('Escala')
  plt.xlabel('Semana')

  plt.subplot(3,3,3) # Subplot para visualizar las graficas en un mismo plot
  X = np.linspace(0, 258)
  plt.plot(X, DFO2sat[num],'o', label= 'datos', linewidth = 1) #Datos filtrados
  plt.ylim(80,110) # Limite en en Y
  plt.axhline(y=90, xmin=0, color= 'red') # Maximo normal de presión arterial
  plt.axhline(y=100, xmin=0, color= 'red') # Minimo normal de presión arterial
  plt.title("Saturación de O2 (O2Sat)")
  plt.ylabel('Escala')
  plt.xlabel('Semana')
  
  plt.subplot(3,3,4)
  X = np.linspace(0, 258)
  plt.plot(X, DFResp[num],'o', label= 'datos', linewidth = 1)
  plt.ylim(10,30)
  plt.axhline(y=12, xmin=0, color= 'red')
  plt.axhline(y=18, xmin=0, color= 'red')
  plt.title("Respiración (Resp)")
  plt.ylabel('Escala')
  plt.xlabel('Semana')

  plt.subplot(3,3,5)
  X = np.linspace(0, 258)
  plt.plot(X, DFTemp[num],'o', label= 'datos', linewidth = 1)
  plt.ylim(35,40)
  plt.axhline(y=36, xmin=0, color= 'red')
  plt.axhline(y=37, xmin=0, color= 'red')
  plt.title("Temperatura (Temp)")
  plt.ylabel('Escala')
  plt.xlabel('Semana')

  plt.subplot(3,3,6)
  X = np.linspace(0, 258)
  plt.plot(X, DFGlucose[num],'o', label= 'datos', linewidth = 1)
  plt.ylim(50,160)
  plt.axhline(y=70, xmin=0, color= 'red')
  plt.axhline(y=100, xmin=0, color= 'red')
  plt.title("Glucosa (Glucose)")
  plt.ylabel('Escala')
  plt.xlabel('Semana')
  
  plt.subplot(3,3,7)
  X = np.linspace(0, 258)
  plt.plot( X, DFMap[num],'o', label= 'datos', linewidth = 0.5) #Datos filtrados
  plt.ylim(45,140) # Limite en en Y
  plt.axhline(y=120, xmin=0, color= 'red') # Maximo normal de presión arterial
  plt.axhline(y=80, xmin=0, color= 'red') # Minimo normal de presión arterial
  plt.title("Presión arterial media (MAP)") # Titulo grafica
  plt.ylabel('Escala') # Titulo Y
  plt.xlabel('Semana') # Titulo X

#Solicitar semanas

numero = int(input('Semana que desea verificar: '))
print("Datos de la semana",numero,"\n")
semanas(numero)

"""Modelo para analisar la sepsis 

"""

# Modificación de NaN
DFHR = DFHR.fillna(-1)
DFSepsis = DFSepsis.fillna(-1)
DFMap = DFMap.fillna(-1)
DFResp = DFResp.fillna(-1)
DFTemp = DFTemp.fillna(-1)
DFO2sat = DFO2sat.fillna(-1)
DFGlucose = DFGlucose.fillna(-1)

# Descripción de valores
DFHR.describe()

# Normalización de valores

DFHR_norm = (DFHR - DFHR.min()) / (DFHR.max() - DFHR.min())
DFHR_norm = DFHR_norm.fillna(0.000000)
DFHR_norm

# Estadisticos de datos normalizados
DFHR_norm.describe()

# Codo de Jambu para definir cuantos K vamos a utilizar

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

wcss = []

for i in range (1,50):

  kmeans = KMeans(n_clusters=i, max_iter=300)
  kmeans.fit(DFHR_norm)
  wcss.append(kmeans.inertia_)


plt.plot(range(1,50), wcss)
plt.title("Codo de Jambú")
plt.xlabel('Numero de Clusters')
plt.ylabel('WCSS')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

clustering = KMeans(n_clusters= 5, max_iter= 300) # Creación del modelo
clustering.fit(DFHR_norm) # Aplicación del modelo en los datos

DFHR['KMeans_Clusters'] = clustering.labels_ # Se guardan los resultados del clustering en el modelo
DFHR.head()

# Analisis de componentes principales para darnos una idea de como se forman los clusters

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_DFHR = pca.fit_transform(DFHR_norm)
pca_DFHR_df= pd.DataFrame(data= pca_DFHR, columns=['Componente_1','Componente_2'])
pca_nombres_DFHR= pd.concat([pca_DFHR_df, DFHR[['KMeans_Clusters']]], axis=1)

pca_nombres_DFHR

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize= (15,15))

ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Componente 1', fontsize = 15)
ax.set_ylabel('Componente 2', fontsize = 15)
ax.set_title('Compoonentes Principales', fontsize = 20)

color_theme = np.array(['blue', 'green', 'orange'])
ax.scatter(x =pca_nombres_DFHR.Componente_1, y=pca_nombres_DFHR.Componente_2, 
           c= color_theme[pca_nombres_DFHR.KMeans_Clusters], s=50)
plt.show()

import matplotlib.pyplot as plt


plt.scatter(DFHR[1], DFHR[50])
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5).fit(DFHR)
centroids = kmeans.cluster_centers_
print(centroids)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

plt.scatter(DFHR[1], DFHR[50], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=50)
plt.show()

"""Modelos del analaisis de la sepsis 

"""