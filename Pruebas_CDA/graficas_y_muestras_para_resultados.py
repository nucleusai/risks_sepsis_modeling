# -*- coding: utf-8 -*-
"""Graficas y muestras para resultados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5Sn5DOEOYspZLU1FrVpQlwfbQJlJQRu

## Librerias
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
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from mlxtend.plotting import plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

"""# Dataset entregado por el CDA creado en mongodb"""

csv_path = '/content/NewDataCompletSepsisMongo.csv'
GSepsis = pd.read_csv(csv_path, sep=',')

GSepsis

x_values = GSepsis['SepsisLabel'].unique()
y_values = GSepsis['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Conteo SepsisLabel')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('SepsiLabel (N)(P)')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = GSepsis['Hora'].unique()
y_values = GSepsis['Hora'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Cantidad de pacientes por horas')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Horas')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

freq = GSepsis.groupby(['SepsisLabel']).count() 
print(freq)

freq2 = GSepsis.groupby(['Hora']).count() 
print(freq2)

x_values = GSepsis['SepsisLabel'].unique()
y_values = GSepsis['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Cantidad de pacientes por horas')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Horas')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

prueba = GSepsis[["SepsisLabel", "Paciente"]].copy()
indexNames = prueba[ prueba['SepsisLabel'] == 0 ].index
# Delete these row indexes from dataFrame
prueba.drop(indexNames , inplace=True)
print(prueba)

csv_path = '/content/Resultados.csv'
Resultados = pd.read_csv(csv_path, sep=',')

Resultados

x_values = Resultados['PacientesTrain']
y_values = Resultados['PacientesTrain']

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Cantidad de pacientes por horas')      #El título
ax = plt.subplot()                   #Axis


ax.set_xlabel('Horas')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

csv_path = '/content/trainset.csv'
Train = pd.read_csv(csv_path, sep=',')

csv_path = '/content/testset.csv'
Test = pd.read_csv(csv_path, sep=',')

Train.head()

x_values = Train['GSepsisBin'].unique()
y_values = Train['GSepsisBin'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Resultados Binarios Train')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = Test['GSepsisBin'].unique()
y_values = Test['GSepsisBin'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Resultados Binarios Test')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

csv_path = '/content/TrainG1.csv'
Train1 = pd.read_csv(csv_path, sep=',')
csv_path = '/content/TestG1.csv'
Test1 = pd.read_csv(csv_path, sep=',')

csv_path = '/content/TrainG2.csv'
Train2 = pd.read_csv(csv_path, sep=',')
csv_path = '/content/TestG2.csv'
Test2 = pd.read_csv(csv_path, sep=',')

csv_path = '/content/TrainG3.csv'
Train3 = pd.read_csv(csv_path, sep=',')
csv_path = '/content/TestG3.csv'
Test3 = pd.read_csv(csv_path, sep=',')

csv_path = '/content/TrainG4.csv'
Train4 = pd.read_csv(csv_path, sep=',')
csv_path = '/content/TestG4.csv'
Test4 = pd.read_csv(csv_path, sep=',')

x_values = Train1['SepsisLabel'].unique()
y_values = Train1['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('train G1')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = Test1['SepsisLabel'].unique()
y_values = Test1['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Test G1')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = Train2['SepsisLabel'].unique()
y_values = Train2['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('train G2')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = Test2['SepsisLabel'].unique()
y_values = Test2['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Test G2')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y





x_values = Train3['SepsisLabel'].unique()
y_values = Train3['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('train G3')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = Test3['SepsisLabel'].unique()
y_values = Test3['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Test G3')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y





x_values = Train4['SepsisLabel'].unique()
y_values = Train4['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('train G4')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

x_values = Test4['SepsisLabel'].unique()
y_values = Test4['SepsisLabel'].value_counts().tolist()

plt.figure(figsize=(10,10))    #Figura. Puede incluirse el tamaño con figsize
plt.bar(x_values, y_values)          #El gráfico
plt.title('Test G4')      #El título
ax = plt.subplot()                   #Axis
ax.set_xticks(x_values)             #Eje x
ax.set_xticklabels(x_values)        #Etiquetas del eje x
ax.set_xlabel('Resultado')  #Nombre del eje x
ax.set_ylabel('Cantidad')  #Nombre del eje y

Tr1 = Train1.groupby(['SepsisLabel']).count() 
te1 = Test1.groupby(['SepsisLabel']).count() 


Tr2 = Train2.groupby(['SepsisLabel']).count() 
te2 = Test2.groupby(['SepsisLabel']).count() 

Tr3 = Train3.groupby(['SepsisLabel']).count() 
te3 = Test3.groupby(['SepsisLabel']).count() 

Tr4 = Train4.groupby(['SepsisLabel']).count() 
te4 = Test4.groupby(['SepsisLabel']).count() 

print("Train1",Tr1)
print("Test1", te1)

print("Train2",Tr2)
print("Test2", te2)

print("Train3",Tr3)
print("Test3", te3)

print("Train4",Tr4)
print("Test4", te4)

