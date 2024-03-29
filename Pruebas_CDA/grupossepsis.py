# -*- coding: utf-8 -*-
"""GruposSepsis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FhLlqVI1EZnBxwAm3MTB7R_TmjmEz3s-

#FUNCIONES
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Función SOFA

def datos_SOFA(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd

  global DFSOFA
  global dTabla

  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  #dTabla = datos[['SaO2', 'FiO2', 'Platelets', 'Bilirubin_total', 'MAP', 'Creatinine', 'SepsisLabel', 'Sepsis_SIRS', 'Sepsis_SOFA', 'Paciente', 'Hora']].copy() # Datos que se utilizan para el analisis SOFA
  #dTabla = datos.sort_values('Paciente')
  dTabla = datos.copy()
 
  #Ciclo 1

  for i in range(0,len(dTabla)): # Ciclo para crear las columna de respiración para puntuación SOFA
     
     if dTabla.loc[i, 'FiO2'] != 0:
         dTabla.loc[i, 'Respiracion'] = dTabla.loc[i, 'SaO2'] / dTabla.loc[i, 'FiO2']
     else:
       dTabla.loc[i, 'Respiracion'] = 0;



  #Ciclo 2

  for i in range(0,len(dTabla)): # Ciclo para crear las columnas de rango SOFA
                                 #.loc para verificar un valor de posición

      if dTabla.loc[i, 'Respiracion']>= 302 or dTabla.loc[i, 'Respiracion'] == 0: # Creación Columna SOFA de saturación de oxigeno
         dTabla.loc[i, 'SOFA_Respiracion'] = 0
      else:
        
        if dTabla.loc[i, 'Respiracion']>= 221 and dTabla.loc[i, 'Respiracion']< 302 : 
           dTabla.loc[i, 'SOFA_Respiracion'] = 1
        else:
          
          if dTabla.loc[i, 'Respiracion']>= 142 and dTabla.loc[i, 'Respiracion']< 221 :
             dTabla.loc[i, 'SOFA_Respiracion'] = 2
          else: 
            
            if dTabla.loc[i, 'Respiracion']>= 67 and dTabla.loc[i, 'Respiracion']< 142 : 
               dTabla.loc[i, 'SOFA_Respiracion'] = 3
            else:
              
              if dTabla.loc[i, 'Respiracion']> 1 and dTabla.loc[i, 'Respiracion']< 67 : 
                 dTabla.loc[i, 'SOFA_Respiracion'] = 4
    

      if dTabla.loc[i, 'Platelets']>= 150 or dTabla.loc[i, 'Platelets'] == 0: # Creación Columna SOFA de plaquetas
         dTabla.loc[i, 'SOFA_Platelets'] = 0
      else:
        
        if dTabla.loc[i, 'Platelets']>= 100 and dTabla.loc[i, 'Platelets'] < 150 : 
           dTabla.loc[i, 'SOFA_Platelets'] = 1
        else:

          if dTabla.loc[i, 'Platelets']>= 50 and dTabla.loc[i, 'Platelets'] < 100 : 
             dTabla.loc[i, 'SOFA_Platelets'] = 2
          else: 
            
            if dTabla.loc[i, 'Platelets']>= 20 and dTabla.loc[i, 'Platelets'] < 50 : 
               dTabla.loc[i, 'SOFA_Platelets'] = 3
            else:
              
              if dTabla.loc[i, 'Platelets']> 1 and dTabla.loc[i, 'Platelets'] < 20 : 
                 dTabla.loc[i, 'SOFA_Platelets'] = 4
 

        
      if dTabla.loc[i, 'Bilirubin_total']< 1.2 or dTabla.loc[i, 'Bilirubin_total'] ==0: # Creación Columna SOFA  de Bilirrubina Total
           dTabla.loc[i, 'SOFA_Bilirubin_total'] = 0
      else:
        
        if dTabla.loc[i, 'Bilirubin_total'] >= 1.2 and dTabla.loc[i, 'Bilirubin_total'] < 2:
             dTabla.loc[i, 'SOFA_Bilirubin_total'] = 1
        else:
          
          if dTabla.loc[i, 'Bilirubin_total'] >= 2 and dTabla.loc[i, 'Bilirubin_total'] < 6:
             dTabla.loc[i, 'SOFA_Bilirubin_total'] = 2
          else: 
            
            if dTabla.loc[i, 'Bilirubin_total'] >= 6 and dTabla.loc[i, 'Bilirubin_total'] < 12:
               dTabla.loc[i, 'SOFA_Bilirubin_total'] = 3
            else:
              
              if dTabla.loc[i, 'Bilirubin_total'] >= 12:
                 dTabla.loc[i, 'SOFA_Bilirubin_total'] = 4


      if dTabla.loc[i, 'MAP']>= 70.0 or dTabla.loc[i, 'MAP']==0 : # Creación Columna SOFA de Presión arterial media
         dTabla.loc[i, 'SOFA_MAP'] = 0
      else:
         dTabla.loc[i, 'SOFA_MAP'] = 1
        
        
        
      if dTabla.loc[i, 'Creatinine'] < 1.2 or dTabla.loc[i, 'Creatinine'] == 0: # Creaion columna SOFA de Creatinine
         dTabla.loc[i, 'SOFA_Creatinine'] = 0
      else:
        
        if dTabla.loc[i, 'Creatinine'] >= 1.2 or dTabla.loc[i, 'Creatinine'] < 2 : 
           dTabla.loc[i, 'SOFA_Creatinine'] = 1
        else:
          
          if dTabla.loc[i, 'Creatinine'] >= 2 or dTabla.loc[i, 'Creatinine'] < 3.4 : 
             dTabla.loc[i, 'SOFA_Creatinine'] = 2
          else: 
            
            if dTabla.loc[i, 'Creatinine'] >= 3.4 or dTabla.loc[i, 'Creatinine'] < 5 :
               dTabla.loc[i, 'SOFA_Creatinine'] = 3
            else:
              
              if dTabla.loc[i, 'Creatinine'] >= 5 : 
                 dTabla.loc[i, 'SOFA_Creatinine'] = 4

  #Ciclo 3
  for i in range(0,len(dTabla)): # Ciclo para crear la columna de resultado de Sepsis
  
      dTabla.loc[i, 'SOFA_Sepsis'] = dTabla.loc[i, 'SOFA_Respiracion'] + dTabla.loc[i, 'SOFA_Platelets'] + dTabla.loc[i, 'SOFA_Bilirubin_total'] + dTabla.loc[i, 'SOFA_MAP'] + dTabla.loc[i, 'SOFA_Creatinine']
      
      if dTabla.loc[i, 'SOFA_Sepsis'] >= 0 and dTabla.loc[i, 'SOFA_Sepsis'] <= 2 :
         dTabla.loc[i, 'GROUP_SOFA'] = 0
      else:

          if dTabla.loc[i, 'SOFA_Sepsis'] >= 3 and dTabla.loc[i, 'SOFA_Sepsis'] <= 5 :
             dTabla.loc[i, 'GROUP_SOFA'] = 1
          else:
        
            if dTabla.loc[i, 'SOFA_Sepsis'] >= 6 and dTabla.loc[i, 'SOFA_Sepsis'] <= 8 :
               dTabla.loc[i, 'GROUP_SOFA'] = 2
            else: 
    
              if dTabla.loc[i, 'SOFA_Sepsis'] >= 9 and dTabla.loc[i, 'SOFA_Sepsis'] <= 11 : 
                 dTabla.loc[i, 'GROUP_SOFA'] = 3
              else:
        
                  if dTabla.loc[i, 'SOFA_Sepsis'] >= 12:
                     dTabla.loc[i, 'GROUP_SOFA'] = 4


  
  DFSOFA = dTabla[['SOFA_Respiracion', 'SOFA_Platelets', 'SOFA_Bilirubin_total', 'SOFA_MAP', 'SOFA_Creatinine', 'SOFA_Sepsis', 'GROUP_SOFA','SepsisLabel']].copy()
  
 #return print(DFSOFA)

#Función SIRS

def datos_SIRS():
  
  import matplotlib.pyplot as plt
  import pandas as pd
  
  global dTabla
  global DFSIRS

  #csv_path = ruta
  #datos = pd.read_csv(csv_path, sep=',')
  #datos2 = datos[['HR', 'Temp', 'WBC', 'SepsisLabel']].copy() # Datos que se utilizan para el analisis SIRS
  #dTabla = datos2.fillna(0) # Cambiando los NaN por 0 para realizar validación

  #Ciclo 1
  for i in range(0,len(dTabla)): # Ciclo para crear las columnas de rangos Boolean
                                 #.loc para verificar un valor de posición
    
    if dTabla.loc[i, 'HR'] == 0:
       dTabla.loc[i, 'SIRS_HR'] = 0 
    else:

      if  (dTabla.loc[i, 'HR']> 60.0 and dTabla.loc[i, 'HR']< 100.0): # Creación Columna SIRS de frecuencia cardiaca
           dTabla.loc[i, 'SIRS_HR'] = False
                       
      else:
            dTabla.loc[i, 'SIRS_HR'] = True
           
        
    if dTabla.loc[i, 'Temp'] == 0:
       dTabla.loc[i, 'SIRS_Temp'] = 0
    else:

      if  (dTabla.loc[i, 'Temp']> 36.0 and dTabla.loc[i, 'Temp']< 38.3): # Creación Columna SIRS de temperatura
           dTabla.loc[i, 'SIRS_Temp'] = False 
      else:
            dTabla.loc[i, 'SIRS_Temp'] = True


    if dTabla.loc[i, 'WBC'] == 0:
       dTabla.loc[i, 'SIRS_WBC'] = 0
    else:
      
      if (dTabla.loc[i, 'WBC']> 4.0 and dTabla.loc[i, 'WBC']< 12.0): # Creación Columna SIRS de Leucocitos
          dTabla.loc[i, 'SIRS_WBC'] = False
      else:
          dTabla.loc[i, 'SIRS_WBC'] = True
          
        
  
  #Ciclo 2
  for i in range(0,len(dTabla)): # Ciclo para crear la columna de resultado de Sepsis

    cont=0

    if dTabla.loc[i, 'SIRS_HR'] == True: # Columana SIRS Frecuencia cardiaca
        cont= cont+1
        
    if dTabla.loc[i, 'SIRS_Temp'] == True: # Columna SIRS Temperatura
        cont= cont+1

    if dTabla.loc[i, 'SIRS_WBC'] == True: # Columna SIRS Leucocitos
        cont= cont+1

    if cont >= 2 :                        # Creación columna sepsis
        dTabla.loc[i, 'SIRS_Sepsis'] = 1
    else:
        dTabla.loc[i, 'SIRS_Sepsis'] = 0


  DFSIRS = dTabla[['SIRS_HR', 'SIRS_Temp', 'SIRS_WBC', 'SIRS_Sepsis', 'SepsisLabel']].copy()

def Agrupacion_SepsisLabel(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd
  
  global positivos_SepsisLabel
  global control_SepsisLabel

  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  paciente = datos.iloc[0]['Paciente']
  band = False
  band2 = False
  positivos_SepsisLabel = 0
  control_SepsisLabel = 0 

  for i in range(0,len(datos)):
    
     if (datos.loc[i, 'Paciente'] != paciente):
        paciente = datos.iloc[i]['Paciente']
       
        if ((band2 == True) and (band == True)):
            band2 = False
            band = False
        else:
           control_SepsisLabel = control_SepsisLabel + 1
   
     if ((datos.loc[i, 'SepsisLabel'] == 1) and (datos.loc[i, 'Paciente'] == paciente) and (band == False)): 
        positivos_SepsisLabel = positivos_SepsisLabel + 1
        band = True
     else:
        band2= True
  
  return (positivos_SepsisLabel, control_SepsisLabel)

def Agrupacion_Sepsis_SIRS(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd
  
  global positivos_Sepsis_SIRS
  global control_Sepsis_SIRS

  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  paciente = datos.iloc[0]['Paciente']
  band = False
  band2 = False
  positivos_Sepsis_SIRS = 0
  control_Sepsis_SIRS = 0 

  for i in range(0,len(datos)):

     if (datos.loc[i, 'Paciente'] != paciente):
        paciente = datos.iloc[i]['Paciente']

        if ((band2 == True) and (band == True)):
            band2 = False
            band = False
        else:
           control_Sepsis_SIRS = control_Sepsis_SIRS + 1
   
     if (datos.loc[i, 'SIRS_Sepsis'] == 1 and datos.loc[i, 'Paciente'] == paciente and band == False): 
        positivos_Sepsis_SIRS = positivos_Sepsis_SIRS + 1
        band = True
     else:
        band2= True
    
  return (positivos_Sepsis_SIRS, control_Sepsis_SIRS)

def Agrupacion_Sepsis_SOFA(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd
  
  global positivos_Sepsis_SOFA
  global control_Sepsis_SOFA

  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  paciente = datos.iloc[0]['Paciente']
  band = False
  band2 = False
  positivos_Sepsis_SOFA = 0
  control_Sepsis_SOFA = 0 

  for i in range(0,len(datos)):

     if (datos.loc[i, 'Paciente'] != paciente):
        paciente = datos.iloc[i]['Paciente']

        if ((band2 == True) and (band == True)):
            band2 = False
            band = False

        else:
           control_Sepsis_SOFA = control_Sepsis_SOFA + 1
   
     if (datos.loc[i, 'GROUP_SOFA'] != 0 and datos.loc[i, 'Paciente'] == paciente and band == False): 
        positivos_Sepsis_SOFA = positivos_Sepsis_SOFA + 1
        band = True
     else:
        band2= True
  
  return (positivos_Sepsis_SOFA, control_Sepsis_SOFA)

def DataGrupos():
  
  global dfgrupos
  g0 = 0
  g1 = 0
  g2 = 0
  g3 = 0
  g4 = 0
  g5 = 0
  g6 = 0
  g7 = 0

  for i in range(0,len(General_Sepsis)):

     if (General_Sepsis.loc[i, 'Grupo'] == '0'):
         g0 = g0 + 1;
     else:

       if (General_Sepsis.loc[i, 'Grupo'] == '1'):
           g1 = g1 + 1;
       else:

          if (General_Sepsis.loc[i, 'Grupo'] == '2'):
              g2 = g2 + 1;
          else:

             if (General_Sepsis.loc[i, 'Grupo'] == '3'):
                 g3 = g3 + 1;
             else:

                if (General_Sepsis.loc[i, 'Grupo'] == '4'):
                   g4 = g4 + 1;
                else:

                  if (General_Sepsis.loc[i, 'Grupo'] == '5'):
                      g5 = g5 + 1;
                  else:

                     if (General_Sepsis.loc[i, 'Grupo'] == '6'):
                        g6 = g6 + 1;
                     else:

                       if (General_Sepsis.loc[i, 'Grupo'] == '7'):
                          g7 = g7 + 1;
        

  columna = ['G0', 'G1','G2', 'G3','G4', 'G5','G6', 'G7'] 
  valores = [g0,g1,g2,g3,g4,g5,g6,g7 ]
  indice =['Grupo']
  
  grupo = { 'G0': [g0], 'G1': [g1], 'G2': [g2], 'G3': [g3], 'G4': [g4], 'G5': [g5], 'G6': [g6], 'G7': [g7] }
  dfgrupos = pd.DataFrame(data=grupo, index= indice)

def DataFrameResult():
  
  global dfresult

  columna = ['Positivos', 'Sanos'] 
  valores = [positivos_SepsisLabel, control_SepsisLabel, positivos_Sepsis_SIRS, control_Sepsis_SIRS, positivos_Sepsis_SOFA, control_Sepsis_SOFA  ]
  indice =['Sepsis_Label', 'Sepsis_SIRS', 'GROUP_SOFA']
  
  result = { 'Positivos': [positivos_SepsisLabel, positivos_Sepsis_SIRS, positivos_Sepsis_SOFA ], 'Sanos':[control_SepsisLabel,control_Sepsis_SIRS, control_Sepsis_SOFA]}
  dfresult = pd.DataFrame(data=result, index= indice)

def Grupos():
  
  import matplotlib.pyplot as plt
  import pandas as pd
  
  for i in range(0,len(General_Sepsis)):

     if (General_Sepsis.loc[i, 'SepsisLabel'] == 0) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 0) and (General_Sepsis.loc[i, 'GROUP_SOFA'] == 0):
         General_Sepsis.loc[i, 'Grupo'] = '0';
     else:

       if (General_Sepsis.loc[i, 'SepsisLabel'] == 1) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 0) and (General_Sepsis.loc[i, 'GROUP_SOFA'] == 0):
          General_Sepsis.loc[i, 'Grupo'] = '1';
       else:

         if (General_Sepsis.loc[i, 'SepsisLabel'] == 0) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 1) and (General_Sepsis.loc[i, 'GROUP_SOFA'] == 0):
             General_Sepsis.loc[i, 'Grupo'] = '2';
         else:

           if (General_Sepsis.loc[i, 'SepsisLabel'] == 0) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 0) and (General_Sepsis.loc[i, 'GROUP_SOFA'] != 0):
              General_Sepsis.loc[i, 'Grupo'] = '3';
           else:

              if (General_Sepsis.loc[i, 'SepsisLabel'] == 1) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 1) and (General_Sepsis.loc[i, 'GROUP_SOFA'] == 0):
                 General_Sepsis.loc[i, 'Grupo'] = '4';
              else:

                 if (General_Sepsis.loc[i, 'SepsisLabel'] == 1) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 0) and (General_Sepsis.loc[i, 'GROUP_SOFA'] != 0):
                    General_Sepsis.loc[i, 'Grupo'] = '5';
                 else:

                   if (General_Sepsis.loc[i, 'SepsisLabel'] == 0) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 1) and (General_Sepsis.loc[i, 'GROUP_SOFA'] != 0):
                      General_Sepsis.loc[i, 'Grupo'] = '6';
                   else:

                     if (General_Sepsis.loc[i, 'SepsisLabel'] == 1) and (General_Sepsis.loc[i, 'SIRS_Sepsis'] == 1) and (General_Sepsis.loc[i, 'GROUP_SOFA'] != 0):
                        General_Sepsis.loc[i, 'Grupo'] = '7';

"""#MENU"""

import pandas as pd

# MENU DE PRUEBAS Y EJECUCIÓN DE FUNCIONES 

global General_Sepsis
ruta ='/content/GrupoPrueba4.csv'
datos_SOFA(ruta)
datos_SIRS()
General_Sepsis = dTabla.copy()
#General_Sepsis = dTabla[['SepsisLabel', 'SIRS_Sepsis', 'SOFA_Sepsis', 'GROUP_SOFA', 'Paciente', 'Hora']].copy()
General_Sepsis = General_Sepsis.sort_values('Paciente')
Grupos()
General_Sepsis.to_csv('General_Sepsis.csv')

# MENU DE PRUEBAS Y EJECUCIÓN DE FUNCIONES 

ruta='/content/General_Sepsis.csv'
Agrupacion_SepsisLabel(ruta)
Agrupacion_Sepsis_SIRS(ruta)
Agrupacion_Sepsis_SOFA(ruta)
DataFrameResult()
DataGrupos()

"""# CONFIGURACIÓN Y AGRUPACIÓN"""

GSepsis = General_Sepsis
General_Sepsis.to_csv('General_Sepsis2.csv')
General_Sepsis

dfresult

import numpy as np
import pandas as pd

General_Sepsis.groupby(['Grupo']).size().reset_index(name='Cantidad')

G1 = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
G1 = G1.drop(G1[G1['Grupo']== '2'].index)
G1 = G1.drop(G1[G1['Grupo']== '3'].index)
G1 = G1.drop(G1[G1['Grupo']== '4'].index)
G1 = G1.drop(G1[G1['Grupo']== '5'].index)
G1 = G1.drop(G1[G1['Grupo']== '6'].index)

G2 = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
G2 = G2.drop(G2[G2['Grupo']== '1'].index)
G2 = G2.drop(G2[G2['Grupo']== '3'].index)
G2 = G2.drop(G2[G2['Grupo']== '4'].index)
G2 = G2.drop(G2[G2['Grupo']== '5'].index)
G2 = G2.drop(G2[G2['Grupo']== '6'].index)

G3 = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
G3 = G3.drop(G3[G3['Grupo']== '1'].index)
G3 = G3.drop(G3[G3['Grupo']== '2'].index)
G3 = G3.drop(G3[G3['Grupo']== '4'].index)
G3 = G3.drop(G3[G3['Grupo']== '5'].index)
G3 = G3.drop(G3[G3['Grupo']== '6'].index)

G4 = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
G4 = G4.drop(G4[G4['Grupo']== '1'].index)
G4 = G4.drop(G4[G4['Grupo']== '2'].index)
G4 = G4.drop(G4[G4['Grupo']== '3'].index)
G4 = G4.drop(G4[G4['Grupo']== '5'].index)
G4 = G4.drop(G4[G4['Grupo']== '6'].index)

G5 = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
G5 = G5.drop(G5[G5['Grupo']== '1'].index)
G5 = G5.drop(G5[G5['Grupo']== '2'].index)
G5 = G5.drop(G5[G5['Grupo']== '3'].index)
G5 = G5.drop(G5[G5['Grupo']== '4'].index)
G5 = G5.drop(G5[G5['Grupo']== '6'].index)

G6 = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
G6 = G6.drop(G6[G6['Grupo']== '1'].index)
G6 = G6.drop(G6[G6['Grupo']== '2'].index)
G6 = G6.drop(G6[G6['Grupo']== '3'].index)
G6 = G6.drop(G6[G6['Grupo']== '4'].index)
G6 = G6.drop(G6[G6['Grupo']== '5'].index)

"""#DATAFRAME DE TODOS LOS PACIENTES CON LOS GRUPOS CON SEPSIS"""

#DATAFRAME DE TODOS LOS PACIENTES CON LOS GRUPOS CON SEPSIS

GSepsis = GSepsis.drop(GSepsis[GSepsis['Grupo']== '0'].index)
GSepsis = GSepsis.sort_values('Grupo')

GSepsis

#DESCRIBE PARA EL DATAFRAME DE TODOS LOS GRUPOS

GSepsis.describe()

#GRAFICA DE HR POR GRUPO DE HORAS

bins = [-1, 16, 42, 72, 300]
rango= ["1","2","3","4"]
GSepsis["HoraG"] = pd.cut(GSepsis["Hora"], bins, labels= rango)

GSepsisG1 = GSepsis
GSepsisG2 = GSepsis
GSepsisG3 = GSepsis
GSepsisG4 = GSepsis

GSepsisG1 = GSepsisG1.drop(GSepsisG1[GSepsisG1['HoraG']== '2'].index)
GSepsisG1 = GSepsisG1.drop(GSepsisG1[GSepsisG1['HoraG']== '3'].index)
GSepsisG1 = GSepsisG1.drop(GSepsisG1[GSepsisG1['HoraG']== '4'].index)

GSepsisG2 = GSepsisG2.drop(GSepsisG2[GSepsisG2['HoraG']== '1'].index)
GSepsisG2 = GSepsisG2.drop(GSepsisG2[GSepsisG2['HoraG']== '3'].index)
GSepsisG2 = GSepsisG2.drop(GSepsisG2[GSepsisG2['HoraG']== '4'].index)

GSepsisG3 = GSepsisG3.drop(GSepsisG3[GSepsisG3['HoraG']== '2'].index)
GSepsisG3 = GSepsisG3.drop(GSepsisG3[GSepsisG3['HoraG']== '1'].index)
GSepsisG3 = GSepsisG3.drop(GSepsisG3[GSepsisG3['HoraG']== '4'].index)

GSepsisG4 = GSepsisG4.drop(GSepsisG4[GSepsisG4['HoraG']== '2'].index)
GSepsisG4 = GSepsisG4.drop(GSepsisG4[GSepsisG4['HoraG']== '3'].index)
GSepsisG4 = GSepsisG4.drop(GSepsisG4[GSepsisG4['HoraG']== '1'].index)

GSepsisG1.plot.scatter(x="Hora", y="HR",c='green')
GSepsisG2.plot.scatter(x="Hora", y="HR")
GSepsisG3.plot.scatter(x="Hora", y="HR",c='red')
GSepsisG4.plot.scatter(x="Hora", y="HR",c='orange')

GSepsisG1.plot.scatter(x="Hora", y="MAP",c='green')
GSepsisG2.plot.scatter(x="Hora", y="MAP")
GSepsisG3.plot.scatter(x="Hora", y="MAP",c='red')
GSepsisG4.plot.scatter(x="Hora", y="MAP",c='orange')

"""# PACIENTES GRUPO 1 SEPSISLABEL"""

G1 # PACIENTES GRUPO 1 SEPSISLABEL

G1.describe()

#GRAFICA DE HR POR GRUPO DE HORAS

bins = [-1, 16, 42, 72, 300]
rango= ["1","2","3","4"]
GSepsis["HoraG"] = pd.cut(GSepsis["Hora"], bins, labels= rango)

G1H1 = G1
G1H2 = G1
G1H3 = G1
G1H4 = G1

G1H1 = G1H1.drop(G1H1[G1H1['HoraG']== '2'].index)
G1H1 = G1H1.drop(G1H1[G1H1['HoraG']== '3'].index)
G1H1 = G1H1.drop(G1H1[G1H1['HoraG']== '4'].index)

G1H2 = G1H2.drop(G1H2[G1H2['HoraG']== '1'].index)
G1H2 = G1H2.drop(G1H2[G1H2['HoraG']== '3'].index)
G1H2 = G1H2.drop(G1H2[G1H2['HoraG']== '4'].index)

G1H3 = G1H3.drop(G1H3[G1H3['HoraG']== '2'].index)
G1H3 = G1H3.drop(G1H3[G1H3['HoraG']== '1'].index)
G1H3 = G1H3.drop(G1H3[G1H3['HoraG']== '4'].index)

G1H4 = G1H4.drop(G1H4[G1H4['HoraG']== '2'].index)
G1H4 = G1H4.drop(G1H4[G1H4['HoraG']== '3'].index)
G1H4 = G1H4.drop(G1H4[G1H4['HoraG']== '1'].index)

G1H1.plot.scatter(x="Hora", y="HR",c='green')
G1H2.plot.scatter(x="Hora", y="HR")
G1H3.plot.scatter(x="Hora", y="HR",c='red')
G1H4.plot.scatter(x="Hora", y="HR",c='orange')

G1H1.plot.scatter(x="Hora", y="MAP",c='green')
G1H2.plot.scatter(x="Hora", y="MAP")
G1H3.plot.scatter(x="Hora", y="MAP",c='red')
G1H4.plot.scatter(x="Hora", y="MAP",c='orange')

"""# PACIENTES GRUPO 2 SEPSIS-SIRS"""

G2 # PACIENTES GRUPO 2 SEPSIS-SIRS

G2.describe()

#GRAFICA DE HR POR GRUPO DE HORAS

bins = [-1, 16, 42, 72, 300]
rango= ["1","2","3","4"]
GSepsis["HoraG"] = pd.cut(GSepsis["Hora"], bins, labels= rango)

G2H1 = G2
G2H2 = G2
G2H3 = G2
G2H4 = G2

G2H1 = G2H1.drop(G2H1[G2H1['HoraG']== '2'].index)
G2H1 = G2H1.drop(G2H1[G2H1['HoraG']== '3'].index)
G2H1 = G2H1.drop(G2H1[G2H1['HoraG']== '4'].index)

G2H2 = G2H2.drop(G2H2[G2H2['HoraG']== '1'].index)
G2H2 = G2H2.drop(G2H2[G2H2['HoraG']== '3'].index)
G2H2 = G2H2.drop(G2H2[G2H2['HoraG']== '4'].index)

G2H3 = G2H3.drop(G2H3[G2H3['HoraG']== '2'].index)
G2H3 = G2H3.drop(G2H3[G2H3['HoraG']== '1'].index)
G2H3 = G2H3.drop(G2H3[G2H3['HoraG']== '4'].index)

G2H4 = G2H4.drop(G2H4[G2H4['HoraG']== '2'].index)
G2H4 = G2H4.drop(G2H4[G2H4['HoraG']== '3'].index)
G2H4 = G2H4.drop(G2H4[G2H4['HoraG']== '1'].index)

G2H1.plot.scatter(x="Hora", y="HR",c='green')
G2H2.plot.scatter(x="Hora", y="HR")
G2H3.plot.scatter(x="Hora", y="HR",c='red')
G2H4.plot.scatter(x="Hora", y="HR",c='orange')

G2H1.plot.scatter(x="Hora", y="MAP",c='green')
G2H2.plot.scatter(x="Hora", y="MAP")
G2H3.plot.scatter(x="Hora", y="MAP",c='red')
G2H4.plot.scatter(x="Hora", y="MAP",c='orange')

"""# PACIENTES GRUPO 3 SEPSIS SOFA"""

G3 # PACIENTES GRUPO 3 SEPSIS SOFA

G3.describe()

#GRAFICA DE HR POR GRUPO DE HORAS

bins = [-1, 16, 42, 72, 300]
rango= ["1","2","3","4"]
GSepsis["HoraG"] = pd.cut(GSepsis["Hora"], bins, labels= rango)

G3H1 = G3
G3H2 = G3
G3H3 = G3
G3H4 = G3

G3H1 = G3H1.drop(G3H1[G3H1['HoraG']== '2'].index)
G3H1 = G3H1.drop(G3H1[G3H1['HoraG']== '3'].index)
G3H1 = G3H1.drop(G3H1[G3H1['HoraG']== '4'].index)

G3H2 = G3H2.drop(G3H2[G3H2['HoraG']== '1'].index)
G3H2 = G3H2.drop(G3H2[G3H2['HoraG']== '3'].index)
G3H2 = G3H2.drop(G3H2[G3H2['HoraG']== '4'].index)

G3H3 = G3H3.drop(G3H3[G3H3['HoraG']== '2'].index)
G3H3 = G3H3.drop(G3H3[G3H3['HoraG']== '1'].index)
G3H3 = G3H3.drop(G3H3[G3H3['HoraG']== '4'].index)

G3H4 = G3H4.drop(G3H4[G3H4['HoraG']== '2'].index)
G3H4 = G3H4.drop(G3H4[G3H4['HoraG']== '3'].index)
G3H4 = G3H4.drop(G3H4[G3H4['HoraG']== '1'].index)

G3H1.plot.scatter(x="Hora", y="HR",c='green')
G3H2.plot.scatter(x="Hora", y="HR")
G3H3.plot.scatter(x="Hora", y="HR",c='red')
G3H4.plot.scatter(x="Hora", y="HR",c='orange')

G3H1.plot.scatter(x="Hora", y="MAP",c='green')
G3H2.plot.scatter(x="Hora", y="MAP")
G3H3.plot.scatter(x="Hora", y="MAP",c='red')
G3H4.plot.scatter(x="Hora", y="MAP",c='orange')

"""# PACIENTES GRUPO 4 SEPSIS LABEL Y SEPSIS SIRS"""

G4 # PACIENTES GRUPO 4 SEPSIS LABEL Y SEPSIS SIRS

G4.describe()

#GRAFICA DE HR POR GRUPO DE HORAS

bins = [-1, 16, 42, 72, 300]
rango= ["1","2","3","4"]
GSepsis["HoraG"] = pd.cut(GSepsis["Hora"], bins, labels= rango)

G4H1 = G4
G4H2 = G4
G4H3 = G4
G4H4 = G4

G4H1 = G4H1.drop(G4H1[G4H1['HoraG']== '2'].index)
G4H1 = G4H1.drop(G4H1[G4H1['HoraG']== '3'].index)
G4H1 = G4H1.drop(G4H1[G4H1['HoraG']== '4'].index)

G4H2 = G4H2.drop(G4H2[G4H2['HoraG']== '1'].index)
G4H2 = G4H2.drop(G4H2[G4H2['HoraG']== '3'].index)
G4H2 = G4H2.drop(G4H2[G4H2['HoraG']== '4'].index)

G4H3 = G4H3.drop(G4H3[G4H3['HoraG']== '2'].index)
G4H3 = G4H3.drop(G4H3[G4H3['HoraG']== '1'].index)
G4H3 = G4H3.drop(G4H3[G4H3['HoraG']== '4'].index)

G4H4 = G4H4.drop(G4H4[G4H4['HoraG']== '2'].index)
G4H4 = G4H4.drop(G4H4[G4H4['HoraG']== '3'].index)
G4H4 = G4H4.drop(G4H4[G4H4['HoraG']== '1'].index)

G4H1.plot.scatter(x="Hora", y="HR",c='green')
G4H2.plot.scatter(x="Hora", y="HR")
G4H3.plot.scatter(x="Hora", y="HR",c='red')
G4H4.plot.scatter(x="Hora", y="HR",c='orange')

G4H1.plot.scatter(x="Hora", y="MAP",c='green')
G4H2.plot.scatter(x="Hora", y="MAP")
G4H3.plot.scatter(x="Hora", y="MAP",c='red')
G4H4.plot.scatter(x="Hora", y="MAP",c='orange')

"""# PACIENTES GRUPO 6 SEPSIS SIRS Y SEPSIS SOFA"""

G6 # PACIENTES GRUPO 6 SEPSIS SIRS Y SEPSIS SOFA

"""# GRUPO PACIENTES HORAS 120 a 220"""

csv_path = '/content/DataPacientes.csv'
datos = pd.read_csv(csv_path, sep=',')
datos

bins = [-1, 119, 220,400]
rango= ["1","2","3"]
datos["HoraG"] = pd.cut(datos["Hora"], bins, labels= rango)

GSepsis = datos.copy()

GSepsis = GSepsis.drop(GSepsis[GSepsis['HoraG']== '1'].index)
GSepsis = GSepsis.drop(GSepsis[GSepsis['HoraG']== '3'].index)
GSepsis.to_csv('GHoraSepsis.csv')
GSepsis

GSepsis.groupby(['Paciente']).size().reset_index(name='Cantidad')

import pandas as pd

groups = GSepsis.groupby(GSepsis.Paciente)

P401 = groups.get_group("p000401")
P541 = groups.get_group("p000541")
P587 = groups.get_group("p000587")
P897 = groups.get_group("p000897")

import matplotlib.pyplot as plt

#Analisis paciente 11

plt.figure(figsize=(20,20))
plt.subplot(611)

p1,= plt.plot(P401['HR'],'o', label= 'P401', linewidth = 0.5, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(612)
p2,= plt.plot(P401['MAP'],'o', label= 'P401', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(613)
p3,= plt.plot(P401['Temp'],'o', label= 'P401', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(614)
p4,= plt.plot(P401['WBC'],'o', label= 'P401', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(615)
p5,= plt.plot(P401['Creatinine'],'o', label= 'P401', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(616)
p5,= plt.plot(P401['FiO2'],'o', label= 'P401', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')


#Mostrar leyenda, cuadricula y figura

#plt.legend()
#plt.grid()
#plt.show()

import matplotlib.pyplot as plt

#Analisis paciente 11

plt.figure(figsize=(20,20))
plt.subplot(611)

p1,= plt.plot(P541['HR'],'o', label= 'P541', linewidth = 0.5, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(612)
p2,= plt.plot(P541['MAP'],'o', label= 'P541', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(613)
p3,= plt.plot(P541['Temp'],'o', label= 'P541', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(614)
p4,= plt.plot(P541['WBC'],'o', label= 'P541', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(615)
p5,= plt.plot(P541['Creatinine'],'o', label= 'P541', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(616)
p5,= plt.plot(P541['FiO2'],'o', label= 'P401', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

import matplotlib.pyplot as plt

#Analisis paciente 11

plt.figure(figsize=(20,20))
plt.subplot(611)

p1,= plt.plot(P587['HR'],'o', label= 'P587', linewidth = 0.5, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(612)
p2,= plt.plot(P587['MAP'],'o', label= 'P587', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(613)
p3,= plt.plot(P587['Temp'],'o', label= 'P587', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(614)
p4,= plt.plot(P587['WBC'],'o', label= 'P587', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(615)
p5,= plt.plot(P587['Creatinine'],'o', label= 'P587', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(616)
p5,= plt.plot(P401['FiO2'],'o', label= 'P587', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

import matplotlib.pyplot as plt

#Analisis paciente 11

plt.figure(figsize=(20,20))
plt.subplot(611)

p1,= plt.plot(P897['HR'],'o', label= 'P897', linewidth = 0.5, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(612)
p2,= plt.plot(P897['MAP'],'o', label= 'P897', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(613)
p3,= plt.plot(P897['Temp'],'o', label= 'P897', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(614)
p4,= plt.plot(P897['WBC'],'o', label= 'P897', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(615)
p5,= plt.plot(P897['Creatinine'],'o', label= 'P897', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')

plt.subplot(616)
p5,= plt.plot(P897['FiO2'],'o', label= 'P897', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Hora')