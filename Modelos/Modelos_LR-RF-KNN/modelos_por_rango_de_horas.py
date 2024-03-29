# -*- coding: utf-8 -*-
"""Modelos por rango de horas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KnaxqZIEZd3_gNKDHyRQzm3ee38V3RtC

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
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from mlxtend.plotting import plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score, roc_curve
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

"""# Modelo Regresión logistica G1"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG1.csv'
TrainG1 = pd.read_csv(csv_path, sep=',')

TrainG1.Respiracion = TrainG1.Respiracion.replace(["No valido"], -1)
TrainG1.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG1.csv'
TestG1 = pd.read_csv(csv_path, sep=',')

TestG1.Respiracion = TestG1.Respiracion.replace(["No valido"], -1)
TestG1.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG1[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG1["SepsisLabel"])

X_test =(TestG1[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG1["SepsisLabel"])

# Se utiliza un modelo de regresión logistica
model = LogisticRegression(max_iter=5000)
# Se acciona el modelo
model.fit(X,y)

# Se realiza la predicción
y_pred = model.predict(X_test)
y_pred

# Score de predicción
model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

plot_confusion_matrix(conf_mat=cm, figsize=(4,4), show_normed= False)
plt.tight_layout()

"""# Random Forest G1"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG1.csv'
TrainG1 = pd.read_csv(csv_path, sep=',')

TrainG1.Respiracion = TrainG1.Respiracion.replace(["No valido"], -1)
TrainG1.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG1.csv'
TestG1 = pd.read_csv(csv_path, sep=',')

TestG1.Respiracion = TestG1.Respiracion.replace(["No valido"], -1)
TestG1.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG1[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG1["SepsisLabel"])

X_test =(TestG1[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG1["SepsisLabel"])

# Creaamos el modelo de Bosques Aleatorios (y configuramos el número de estimadores (árboles de decisión))
BA_model = RandomForestClassifier(n_estimators = 19, random_state = 2016,min_samples_leaf = 8,)

BA_model.fit(X, y)

# Accuracy promedio
BA_model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

# Predicción del modelo usando los datos de prueba
y_pred = BA_model.predict(X_test)
matriz = confusion_matrix(y_test,y_pred)

plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)
plt.tight_layout()

#Predecir resultados en el conjunto de evaluación
y_test_pred = BA_model.predict(X_test)
y_test_prob = BA_model.predict_proba(X_test)

#Crear metricas

auc = roc_auc_score(y_test, y_test_prob[:,1])
print("- Precisión: ", round(precision_score(y_test, y_test_pred),2))
print("- Recall: ", round(recall_score(y_test, y_test_pred),2))
print("- F-Score: ", round(f1_score(y_test, y_test_pred),2))
print("- AUC: ", round(auc,2))

#Curva AUC

fpr, tpr, thrs = roc_curve(y_test, y_test_prob[:,1])
plt.plot(fpr,tpr)
plt.plot([0,1], [0,1], "r--")
plt.title("ROC")
plt.xlabel("Falsos Positivos")
plt.ylabel ("Verdaderos Psotivos")
plt.show()

"""# KNeighbors G1


"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG1.csv'
TrainG1 = pd.read_csv(csv_path, sep=',')

TrainG1.Respiracion = TrainG1.Respiracion.replace(["No valido"], -1)
TrainG1.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG1.csv'
TestG1 = pd.read_csv(csv_path, sep=',')

TestG1.Respiracion = TestG1.Respiracion.replace(["No valido"], -1)
TestG1.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG1[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG1["SepsisLabel"])

X_test =(TestG1[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG1["SepsisLabel"])

neighbors = np.arange(1,10)
train_exactitud = np.empty(len(neighbors))
test_exactitud = np.empty(len(neighbors))

for i,k in enumerate(neighbors):
  knn=KNeighborsClassifier(n_neighbors=k)
  knn.fit(X,y)
  train_exactitud[i]=knn.score(X,y)
  test_exactitud[i]=knn.score(X_test,y_test)

plt.title('Variación vecinos en Knn')
plt.plot(neighbors, test_exactitud,label='Test exactitud')
plt.plot(neighbors, train_exactitud,label='Entrenamiento exactitud')
plt.legend()
plt.xlabel('Vecinos')
plt.ylabel('Exactitud')

#Predecir resultados en el conjunto de evaluación
y_test_pred = clf.predict(X_test)
y_test_prob = clf.predict_proba(X_test)

#Crear metricas

auc = roc_auc_score(y_test, y_test_prob[:,1])
print("- Precisión: ", round(precision_score(y_test, y_test_pred),2))
print("- Recall: ", round(recall_score(y_test, y_test_pred),2))
print("- F-Score: ", round(f1_score(y_test, y_test_pred),2))
print("- AUC: ", round(auc,2))

"""# Modelo Regresión logistica G2"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG2.csv'
TrainG2 = pd.read_csv(csv_path, sep=',')

TrainG2.Respiracion = TrainG2.Respiracion.replace(["No valido"], -1)
TrainG2.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG2.csv'
TestG2 = pd.read_csv(csv_path, sep=',')

TestG2.Respiracion = TestG2.Respiracion.replace(["No valido"], -1)
TestG2.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG2[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG2["SepsisLabel"])

X_test =(TestG2[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG2["SepsisLabel"])

# Se utiliza un modelo de regresión logistica
model = LogisticRegression(max_iter=5000)
# Se acciona el modelo
model.fit(X,y)

# Se realiza la predicción
y_pred = model.predict(X_test)
y_pred

# Score de predicción
model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

plot_confusion_matrix(conf_mat=cm, figsize=(4,4), show_normed= False)
plt.tight_layout()

"""# Random Forest G2"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG2.csv'
TrainG2 = pd.read_csv(csv_path, sep=',')

TrainG2.Respiracion = TrainG2.Respiracion.replace(["No valido"], -1)
TrainG2.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG2.csv'
TestG2 = pd.read_csv(csv_path, sep=',')

TestG2.Respiracion = TestG2.Respiracion.replace(["No valido"], -1)
TestG2.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG2[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG2["SepsisLabel"])

X_test =(TestG2[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG2["SepsisLabel"])

# Creaamos el modelo de Bosques Aleatorios (y configuramos el número de estimadores (árboles de decisión))
BA_model = RandomForestClassifier(n_estimators = 19, random_state = 2016,min_samples_leaf = 8,)

BA_model.fit(X, y)

# Accuracy promedio
BA_model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

# Predicción del modelo usando los datos de prueba
y_pred = BA_model.predict(X_test)
matriz = confusion_matrix(y_test,y_pred)

plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)
plt.tight_layout()

"""# Modelo Regresión logistica G3"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG3.csv'
TrainG3 = pd.read_csv(csv_path, sep=',')

TrainG3.Respiracion = TrainG3.Respiracion.replace(["No valido"], -1)
TrainG3.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG3.csv'
TestG3 = pd.read_csv(csv_path, sep=',')

TestG3.Respiracion = TestG3.Respiracion.replace(["No valido"], -1)
TestG3.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG3[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG3["SepsisLabel"])

X_test =(TestG3[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG3["SepsisLabel"])

# Se utiliza un modelo de regresión logistica
model = LogisticRegression(max_iter=5000)
# Se acciona el modelo
model.fit(X,y)

# Se realiza la predicción
y_pred = model.predict(X_test)
y_pred

# Score de predicción
model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

plot_confusion_matrix(conf_mat=cm, figsize=(4,4), show_normed= False)
plt.tight_layout()

"""# Random Forest G3"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG3.csv'
TrainG3 = pd.read_csv(csv_path, sep=',')

TrainG3.Respiracion = TrainG3.Respiracion.replace(["No valido"], -1)
TrainG3.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG3.csv'
TestG3 = pd.read_csv(csv_path, sep=',')

TestG3.Respiracion = TestG3.Respiracion.replace(["No valido"], -1)
TestG3.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG3[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG3["SepsisLabel"])

X_test =(TestG3[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG3["SepsisLabel"])

# Creaamos el modelo de Bosques Aleatorios (y configuramos el número de estimadores (árboles de decisión))
BA_model = RandomForestClassifier(n_estimators = 19, random_state = 2016,min_samples_leaf = 8,)

BA_model.fit(X, y)

# Accuracy promedio
BA_model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

# Predicción del modelo usando los datos de prueba
y_pred = BA_model.predict(X_test)
matriz = confusion_matrix(y_test,y_pred)

plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)
plt.tight_layout()

"""# Modelo Regresión logistica G4"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG4.csv'
TrainG4 = pd.read_csv(csv_path, sep=',')

TrainG4.Respiracion = TrainG4.Respiracion.replace(["No valido"], -1)
TrainG4.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG4.csv'
TestG4 = pd.read_csv(csv_path, sep=',')

TestG4.Respiracion = TestG4.Respiracion.replace(["No valido"], -1)
TestG4.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG4[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG4["SepsisLabel"])

X_test =(TestG4[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG4["SepsisLabel"])

# Se utiliza un modelo de regresión logistica
model = LogisticRegression(max_iter=5000)
# Se acciona el modelo
model.fit(X,y)

# Se realiza la predicción
y_pred = model.predict(X_test)
y_pred

# Score de predicción
model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

plot_confusion_matrix(conf_mat=cm, figsize=(4,4), show_normed= False)
plt.tight_layout()

"""# Random Forest G4"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/TrainG4.csv'
TrainG4 = pd.read_csv(csv_path, sep=',')

TrainG4.Respiracion = TrainG4.Respiracion.replace(["No valido"], -1)
TrainG4.astype({'Respiracion':'float64'}).dtypes

csv_path = '/content/TestG4.csv'
TestG4 = pd.read_csv(csv_path, sep=',')

TestG4.Respiracion = TestG4.Respiracion.replace(["No valido"], -1)
TestG4.astype({'Respiracion':'float64'}).dtypes

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar (De la data de entrenamiento)
X = (TrainG4[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y = (TrainG4["SepsisLabel"])

X_test =(TestG4[["Bilirubin_total","Creatinine","MAP","Platelets","Respiracion","HR"]])
y_test =(TestG4["SepsisLabel"])

# Creaamos el modelo de Bosques Aleatorios (y configuramos el número de estimadores (árboles de decisión))
BA_model = RandomForestClassifier(n_estimators = 19, random_state = 2016,min_samples_leaf = 8,)

BA_model.fit(X, y)

# Accuracy promedio
BA_model.score(X_test, y_test)

puntaje = f1_score(y_test, y_pred)
print(puntaje)

#Matriz de Confusión
cm= confusion_matrix(y_test, y_pred)
cm

# Predicción del modelo usando los datos de prueba
y_pred = BA_model.predict(X_test)
matriz = confusion_matrix(y_test,y_pred)

plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)
plt.tight_layout()