# -*- coding: utf-8 -*-
"""Diferentes Modelos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12nfCX-yrDXKOSCd8qSC1B0ZpFPs-QOe8

# MODELO LOGISTICO Separados

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

for i in range(0,len(General_Sepsis)): # Ciclo para crear las columna de respiración para puntuación SOFA
     
     if General_Sepsis.loc[i, 'SOFA_Sepsis'] == 0:
         General_Sepsis.loc[i, 'Sepsis_SOFA'] = 0
     else:
       General_Sepsis.loc[i, 'Sepsis_SOFA'] = 1;

General_Sepsis

groups = General_Sepsis.groupby(General_Sepsis.Paciente)
P897 = groups.get_group("p000897")
P1040 = groups.get_group("p001040")
P897

#Graficamos los datos para observar su comportamiento y elegir el tipo de modelo

plt.figure(figsize=(8,5))
x_P897, y_P897 = (P897["Hora"].values, P897["HR"].values ) #Tomamos los datos
plt.plot(x_P897, y_P897, 'ro') #Lo graficamos
plt.ylabel("HR")
plt.xlabel("Hora")
plt.show()

#Graficamos los datos para observar su comportamiento y elegir el tipo de modelo

plt.figure(figsize=(8,5))
x_P897, y_P897 = (P897["Hora"].values, P897["MAP"].values ) #Tomamos los datos
plt.plot(x_P897, y_P897, 'ro') #Lo graficamos
plt.ylabel("HR")
plt.xlabel("Hora")
plt.show()

#Definimos una funcion llamada sigmoide
def sigmoide (x,beta1,beta2):
  y = 1 / (1 + np.exp(-beta1*(x-beta2)))
  return y

#Graficamos una linea sigmoide que pueda representar los datos
#supongamos beta1 y beta2

beta1= 84.0
beta2= 160

#Utilizamos al funcion, para realizar un prediccion inicial
y_pred = sigmoide(x_P897,beta1,beta2)

#Graficamos la prediccion inicial
plt.plot(x_P897, y_pred*15000000000000.)
plt.plot(x_P897, y_P897, 'ro')
plt.show()

# Como se puede observar necesitamos unos parametros mejores
# Normalicemos los datos
xP897 = x_P897/max(x_P897)
yP897 = y_P897/max(y_P897)

#Utilizamos "Curve_fit" que usa minimos cuadrados no lineales(metrica) para
# ajustar nuestra funcion sigmoide a los datos

from scipy.optimize import curve_fit #importamos libreria y funcion
betas, pcov = curve_fit(sigmoide, xP897, yP897) #Modificamos betas
print( "beta_1 = %f, beta_2 = %f" % (betas[0], betas[1]))

#Graficamos el nuevo modelo sigmoide en funcion de los datos

x = np.linspace (120, 220, 160)
x = x/max(x)
plt.figure(figsize=(8,5))
y = sigmoide(x, *betas)
plt.plot(xP897, yP897, 'ro', label='Datos')
plt.plot(x,y, linewidth=3.0, label='FIT')
plt.legend(loc='best')
plt.ylabel('HR')
plt.xlabel('Horas')
plt.show()

#Creamos una mascara para seleccionar el 80% de datos al azar para entrenamiento el otro 
# 20% sera para testeo

msk = np.random.rand(len(P897)) < 0.8
entreno_x = xP897[msk]
entreno_y = yP897[msk]

test_x = xP897[~msk]
test_y = yP897[~msk]

# Graficamos los datos que vamos a usar para entreno
plt.scatter(entreno_x, entreno_y, color='yellow')
plt.xlabel("Hora")
plt.ylabel("HR")
plt.show()

#Empezamos a entrenar los datos con la funcion curvefit
betas, pcov = curve_fit(sigmoide, entreno_x, entreno_y)

#Realizamos la prediccion utilizando la funcion que creamos, pero con los datos que separamos para testear
yf = sigmoide(test_x, *betas)

# Realizamos la evaluacion con metricas
print("Error absoluto medio: %.2f" %np.mean(np.absolute(yf - test_y)))
print("Suma residual de cuadrados (MSE): %.2f" % np.mean((yf -test_y) ** 2))
from sklearn.metrics import r2_score
print("Efectividad: %.2f" % r2_score(yf, test_y))