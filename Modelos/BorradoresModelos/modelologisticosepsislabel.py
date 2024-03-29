# -*- coding: utf-8 -*-
"""ModeloLogisticoSepsisLabel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Epo96RtFGPwBp31eXs6VWiL8rHU61oPe

# MODELO LOGISTICO

#Librerias
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

"""# Dataset utilizado"""

# Se carga la data seleccionada para el estudio
csv_path = '/content/General_SepsisCompleto.csv'
General_Sepsis = pd.read_csv(csv_path, sep=',')

General_Sepsis

"""#Pre-Procesamiento"""

# Se escogen la variables en X que se van a verificar para el analisis, y en y para el atributo que queremos identificar
X = (General_Sepsis[["HR","Respiracion","Platelets","Bilirubin_total","MAP","Creatinine","Temp","WBC"]])
y = (General_Sepsis["SepsisLabel"])

#Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0)

#Se utiliza el estandarizador de variables, media cero y desviación estandar uno
sc= StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Predictoras de entrenamiento
X_train

# Se utiliza regresión logistica
model = LogisticRegression(max_iter=20000)

# Se acciona el modelo
model.fit(X_train,y_train)

# Se predice
y_pred = model.predict(X_train)
y_pred

# Score de predicción
model.score(X_test, y_test)

#Matriz de Confusión
cm= confusion_matrix(y_train, y_pred)
cm

#Matriz de Confusión

cmPd = pd.DataFrame(cm)
sn.set(font_scale=1.4) 
sn.heatmap(cmPd, annot=True, annot_kws={"size" : 20}, fmt='g', center=0, linewidths=1, cbar=False)
plt.show()

#Curva ROC

logit_roc_auc = roc_auc_score(y_train, y_pred)
fpr, tpr, thresholds = roc_curve(y_train, y_pred)

plt.figure(figsize=(15,15))
plt.plot(fpr, tpr, label = 'Regresión Logistica (area = %0.2f)' % logit_roc_auc)
plt.plot([0,1], [0,1], 'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('% de Falsos positivos')
plt.ylabel('% de Verdaderos positivos')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.show()

#Información Guardada

X_trainTemp = open("X_trainTemp.txt","w")
X_trainTemp.write(str((X_train)))
X_trainTemp.close()

X_testTemp = open("X_testTemp.txt","w")
X_testTemp.write(str((X_test)))
X_testTemp.close()

y_trainTemp = open("y_trainTemp.txt","w")
y_trainTemp.write(str((y_train)))
y_trainTemp.close()

y_testTemp = open("y_testTemp.txt","w")
y_testTemp.write(str((X_test)))
y_testTemp.close()

#Leer TXT
ruta = "/content/X_testTemp.txt"
X_testTemp = open(ruta, 'r')
print(X_testTemp.read())

#Leer TXT
ruta = "/content/X_trainTemp.txt"
X_trainTemp = open(ruta, 'r')
print(X_trainTemp.read())

#Leer TXT
ruta = "/content/y_testTemp.txt"
y_testTemp = open(ruta, 'r')
print(y_testTemp.read())

#Leer TXT
ruta = "/content/y_trainTemp.txt"
y_trainTemp = open(ruta, 'r')
print(y_trainTemp.read())

#Realice un dataframe diferente para el entrenamiento
DataPrediction = General_Sepsis[['HR', 'Respiracion', 'Platelets', 'Bilirubin_total', 'MAP', 'Creatinine', 'Temp', 'WBC']].copy() 

prediccion = model.predict(DataPrediction)
DFprediccion = pd.DataFrame(prediccion, columns=["Prediction"])

for i in range(0,len(General_Sepsis)):
   General_Sepsis.loc[i, 'Prediction_SOFA'] = DFprediccion.loc[i,'Prediction']

#General_Sepsis.to_csv('ModeloEjecutado.csv')
General_Sepsis

#csv_path = '/content/ModeloEjecutado.csv'
#ModeloEjecutado = pd.read_csv(csv_path, sep=',')

groups = General_Sepsis.groupby(General_Sepsis.Paciente)
P897 = groups.get_group("p000897")
P1040 = groups.get_group("p001040")

num1= 0
num2=0

for i in range(0,len(General_Sepsis)):

  if General_Sepsis.loc[i, 'Paciente'] == 'p000897':
     if General_Sepsis.loc[i, 'SepsisLabel'] == 1:
        num1= General_Sepsis.loc[i, 'Hora']
        break
   
for i in range(0,len(General_Sepsis)):

  if General_Sepsis.loc[i, 'Paciente'] == 'p000897':
     if General_Sepsis.loc[i, 'Prediction_SOFA'] == 1:
        num2= General_Sepsis.loc[i, 'Hora']
        break


num3= 0
num4=0

for i in range(0,len(General_Sepsis)):

  if General_Sepsis.loc[i, 'Paciente'] == 'p001040':
     if General_Sepsis.loc[i, 'SepsisLabel'] == 1:
        num3= General_Sepsis.loc[i, 'Hora']
        break
   
for i in range(0,len(General_Sepsis)):

  if General_Sepsis.loc[i, 'Paciente'] == 'p001040':
     if General_Sepsis.loc[i, 'Prediction_SOFA'] == 1:
        num4= General_Sepsis.loc[i, 'Hora']
        break

#Analisis paciente 897

plt.figure(figsize=(15,15))

plt.subplot(511)
plt.plot(P897['Hora'], P897['Prediction_SOFA'], color='navy', linestyle='solid', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num1 !=0:
   plt.axvline(num1, 0, 150, color='red')
if num2 !=0:
   plt.axvline(num2, 0, 150, color='navy')
plt.ylabel('Prediction_SOFA')
plt.xlabel('Hora')

plt.subplot(512)
plt.plot(P897['Hora'], P897['HR'], color='navy', linestyle='solid', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num1 !=0:
   plt.axvline(num1, 0, 150, color='red')
if num2 !=0:
   plt.axvline(num2, 0, 150, color='navy')
plt.ylabel('HR')
plt.xlabel('Hora')

plt.subplot(513)
plt.plot(P897['Hora'], P897['Respiracion'], color='navy', linestyle='solid', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num1 !=0:
   plt.axvline(num1, 0, 150, color='red')
if num2 !=0:
   plt.axvline(num2, 0, 150, color='navy')
plt.ylabel('Respiracion')
plt.xlabel('Hora')


plt.subplot(514)
plt.plot(P897['Hora'], P897['MAP'], color='navy', linestyle='dashed', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num1 !=0:
   plt.axvline(num1, 0, 150, color='red')
if num2 !=0:
   plt.axvline(num2, 0, 150, color='navy')
plt.ylabel('MAP')
plt.xlabel('Hora')


plt.subplot(515)
plt.plot(P897['Hora'], P897['Temp'], color='navy', linestyle='dashed', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num1 !=0:
   plt.axvline(num1, 0, 150, color='red')
if num2 !=0:
   plt.axvline(num2, 0, 150, color='navy')
plt.ylabel('Temp')
plt.xlabel('Hora')

# Paciente 1041

#Analisis paciente 

plt.figure(figsize=(15,15))

plt.subplot(511)
plt.plot(P1040['Hora'], P1040['Prediction_SOFA'], color='navy', linestyle='solid', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num3 !=0:
   plt.axvline(num3, 0, 150, color='red')
if num4 !=0:
   plt.axvline(num4, 0, 150, color='navy')
plt.ylabel('Prediction_SOFA')
plt.xlabel('Hora')

plt.subplot(512)
plt.plot(P1040['Hora'], P1040['HR'], color='navy', linestyle='solid', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num3 !=0:
   plt.axvline(num3, 0, 150, color='red')
if num4 !=0:
   plt.axvline(num4, 0, 150, color='navy')
plt.ylabel('HR')
plt.xlabel('Hora')

plt.subplot(513)
plt.plot(P1040['Hora'], P1040['Respiracion'], color='navy', linestyle='solid', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num3 !=0:
   plt.axvline(num3, 0, 150, color='red')
if num4 !=0:
   plt.axvline(num4, 0, 150, color='navy')
plt.ylabel('Respiracion')
plt.xlabel('Hora')


plt.subplot(514)
plt.plot(P1040['Hora'], P1040['MAP'], color='navy', linestyle='dashed', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num3 !=0:
   plt.axvline(num3, 0, 150, color='red')
if num4 !=0:
   plt.axvline(num4, 0, 150, color='navy')
plt.ylabel('MAP')
plt.xlabel('Hora')


plt.subplot(515)
plt.plot(P1040['Hora'], P1040['Temp'], color='navy', linestyle='dashed', linewidth = 0.05, marker = 'o', markersize=8, markerfacecolor='orange', label='HR' )
if num3 !=0:
   plt.axvline(num3, 0, 150, color='red')
if num4 !=0:
   plt.axvline(num4, 0, 150, color='navy')
plt.ylabel('Temp')
plt.xlabel('Hora')