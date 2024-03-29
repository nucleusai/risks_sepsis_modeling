# -*- coding: utf-8 -*-
"""PruebaModeloLineal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VC_syAatQUilgAlQJ95t467uZe6pSrpc

# Librerias
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sn
import pandas as pd
from math import e
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import linear_model
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import  accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import  roc_curve
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

"""# DataSet Utilizado"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/General_SepsisCompleto.csv'
Datamodelo = pd.read_csv(csv_path, sep=',')

Datamodelo

Datamodelo.groupby(['SepsisLabel']).size().reset_index(name='Cantidad')

"""# Reducción del dataset y validación de datos

"""

DatosReducido = Datamodelo[['Bilirubin_total', 'Creatinine', 'HR', 'MAP', 'Platelets', 'Temp', 'WBC', 'SepsisLabel']].copy() # Datos que se utilizan para el analisis SOFA
DatosReducido

DatosReducido.info()

DatosReducido.describe()

DatosReducido.isna().sum()

"""# Modelo Regresión lineal"""

datos_entrenamiento = DatosReducido.sample(frac=0.8, random_state=0)
datos_test = DatosReducido.drop(datos_entrenamiento.index)

etiquetas_entrenamiento = datos_entrenamiento.pop('SepsisLabel')
etiquetas_test = datos_test.pop('SepsisLabel')

modelo = LogisticRegression()
modelo.fit(datos_entrenamiento,etiquetas_entrenamiento)

predicciones = modelo.predict(datos_test)
predicciones

error = np.sqrt(mean_squared_error(etiquetas_test, predicciones))
print("Error porcentual : %f" % (error*100))