# -*- coding: utf-8 -*-
"""DataSepsisMongo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J_hTR18RQfEi4b3tprcaLdHP8pOWTf2T
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

csv_path = "/content/NewDataComplet.csv"
  dTabla = pd.read_csv(csv_path, sep=',')
  dTabla

for i in range(0,len(dTabla)): # Ciclo para crear la columna de resultado de Sepsis
 
 dTabla.loc[i, 'Puntaje_SOFA'] = dTabla.loc[i, 'Bilirubin_total_SOFA'] + dTabla.loc[i, 'Creatinine_SOFA'] + dTabla.loc[i, 'MAP_SOFA'] + dTabla.loc[i, 'Platelets_SOFA'] + dTabla.loc[i, 'Respiracion_SOFA']

for i in range(0,len(dTabla)):

 if dTabla.loc[i, 'Puntaje_SOFA'] >= 0 and dTabla.loc[i, 'Puntaje_SOFA'] <= 2 :
         dTabla.loc[i, 'Grupo_SOFA'] = 0
 else:
      if dTabla.loc[i, 'Puntaje_SOFA'] >= 3 and dTabla.loc[i, 'Puntaje_SOFA'] <= 6 :
         dTabla.loc[i, 'Grupo_SOFA'] = 1
      else:
        
        if dTabla.loc[i, 'Puntaje_SOFA'] >= 7 and dTabla.loc[i, 'Puntaje_SOFA'] <= 9 :
           dTabla.loc[i, 'Grupo_SOFA'] = 2
        else: 
          if dTabla.loc[i, 'Puntaje_SOFA'] >= 10 and dTabla.loc[i, 'Puntaje_SOFA'] <= 12 : 
                 dTabla.loc[i, 'Grupo_SOFA'] = 3
          else:
            if dTabla.loc[i, 'Puntaje_SOFA'] >= 13:
               dTabla.loc[i, 'Grupo_SOFA'] = 4

for i in range(0,len(dTabla)): # Ciclo para crear la columna de resultado de Sepsis

 cont=0
 if dTabla.loc[i, 'HR_SIRS'] == 1: # Columana SIRS Frecuencia cardiaca
    cont= cont+1
 if dTabla.loc[i, 'TEMP_SIRS'] == 1: # Columna SIRS Temperatura
    cont= cont+1
 if dTabla.loc[i, 'WBC_SIRS'] == 1: # Columna SIRS Leucocitos
    cont= cont+1
 if cont >= 2 :                        # Creación columna sepsis
     dTabla.loc[i, 'Sepsis_SIRS'] = 1
 else:
     dTabla.loc[i, 'Sepsis_SIRS'] = 0

for i in range(0,len(dTabla)): # Ciclo para crear la columna de resultado de Sepsis

    if dTabla.loc[i, 'Grupo_SOFA'] == 0 :    
        dTabla.loc[i, 'Sepsis_SOFA'] = 0
    else:
        dTabla.loc[i, 'Sepsis_SOFA'] = 1

dTabla.to_csv('NewDataCompletSepsisMongo.csv')