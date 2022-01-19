# -*- coding: utf-8 -*-
"""ComparativoSepsisModificado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WthL-ha4LJJJ2FnM_S7cRElZH4ptPpej
"""

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

GSepsis = General_Sepsis
General_Sepsis.to_csv('General_Sepsis2.csv')
General_Sepsis

SepLabel = General_Sepsis['SepsisLabel'].value_counts() 
SepSirs = General_Sepsis['SIRS_Sepsis'].value_counts() 
SepSofa = General_Sepsis['GROUP_SOFA'].value_counts() 
Sepgrupo = General_Sepsis['Grupo'].value_counts() 

print('{}\n{}\n{}\n{}'.format(SepLabel,SepSirs,SepSofa,Sepgrupo))

dfresult # Total de pacientes sin repetir

dfgrupos # Cantidad total del dataset separado en los grupos creados

# G0 = Paciente sin sepsis
# G1 = Paciente con SEPSIS-LABEL
# G2 = Paciente con SEPSIS-SIRS
# G3 = Paciente con SEPSIS-SOFA
# G4 = Paciente con SEPSIS-LABEL y SEPSIS-SIRS
# G5 = Paciente con SEPSIS-LABEL y SEPSIS-SOFA
# G6 = Paciente con SEPSIS-SIRS y SEPSIS-SOFA
# G7 = Paciente con SEPSIS-LABEL - SEPSIS-SIRS - SEPSIS-SOFA

import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np

dfresult.plot(kind = 'bar',figsize=(10,10));

import pandas as pd

# SEPSISLABEL VS SEPSIS SIRS

dfSLavsSSi = pd.DataFrame(General_Sepsis, columns = ['SepsisLabel' , 'SIRS_Sepsis', 'Paciente', 'Hora']) 

for i in range(0,len(dfSLavsSSi)): 
  
  if dfSLavsSSi.loc[i, 'SepsisLabel'] == 1 and dfSLavsSSi.loc[i, 'SIRS_Sepsis'] == 1 :
     dfSLavsSSi.loc[i, 'Concuerda'] = True
  else:
    dfSLavsSSi.loc[i, 'Concuerda'] = False

SLabelvsSSirs = dfSLavsSSi.groupby('Concuerda')
print(SLabelvsSSirs.get_group(True))

import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np

# SEPSISLABEL VS SEPSIS SIRS

dfSLavsSSi.groupby('Concuerda')['Concuerda'].count().plot(kind='bar', figsize=(10,10))

import pandas as pd
import numpy as np

# SEPSISLABEL VS SEPSIS SOFA

dfSLavsSSo = pd.DataFrame(General_Sepsis, columns = ['SepsisLabel' , 'SOFA_Sepsis', 'GROUP_SOFA', 'Paciente', 'Hora']) 

for i in range(0,len(dfSLavsSSo)): 
  
  if dfSLavsSSo.loc[i, 'SepsisLabel'] == 1 and dfSLavsSSo.loc[i, 'SOFA_Sepsis'] != 0 :
     dfSLavsSSo.loc[i, 'Concuerda'] = True
  else:
    dfSLavsSSo.loc[i, 'Concuerda'] = False

SLabelvsSSofa = dfSLavsSSo.groupby('Concuerda')
print(SLabelvsSSofa.get_group(True))

import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np

# SEPSISLABEL VS SEPSIS SOFA

dfSLavsSSo.groupby('Concuerda')['Concuerda'].count().plot(kind='bar',figsize=(10,10))

import pandas as pd
import numpy as np

# SEPSIS SIRS VS SEPSIS SOFA

dfSSivsSSo = pd.DataFrame(General_Sepsis, columns = ['SIRS_Sepsis' , 'SOFA_Sepsis', 'GROUP_SOFA', 'Paciente', 'Hora']) 

for i in range(0,len(dfSSivsSSo)): 
  
  if dfSSivsSSo.loc[i, 'SIRS_Sepsis'] == 1 and dfSSivsSSo.loc[i, 'SOFA_Sepsis'] != 0 :
     dfSSivsSSo.loc[i, 'Concuerda'] = True
  else:
    dfSSivsSSo.loc[i, 'Concuerda'] = False

SSirsvsSSofa = dfSSivsSSo.groupby('Concuerda')
print(SSirsvsSSofa.get_group(True))

import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np

# SEPSIS SIRS VS SEPSIS SOFA

dfSSivsSSo.groupby('Concuerda')['Concuerda'].count().plot(kind='bar',figsize=(10,10))

import pandas as pd
import numpy as np

# SEPSISLABEL VS SEPSIS SIRS VS SEPSIS SOFA

dfSLavsSSivsSSo = pd.DataFrame(General_Sepsis, columns = ['SepsisLabel' , 'SIRS_Sepsis', 'SOFA_Sepsis', 'GROUP_SOFA', 'Paciente', 'Hora']) 

for i in range(0,len(dfSLavsSSivsSSo)): 
  
  if dfSLavsSSivsSSo.loc[i, 'SepsisLabel'] == 1 and dfSLavsSSivsSSo.loc[i, 'SIRS_Sepsis'] == 1 and dfSLavsSSivsSSo.loc[i, 'SOFA_Sepsis'] != 0 :
     dfSLavsSSivsSSo.loc[i, 'Concuerda'] = True
  else:
    dfSLavsSSivsSSo.loc[i, 'Concuerda'] = False

SLavsSSirsvsSSofa = dfSLavsSSivsSSo.groupby('Concuerda')
print(SLavsSSirsvsSSofa.get_group(True))

import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np

General_Sepsis.groupby('Grupo')['Grupo'].count().plot(kind='bar',figsize=(10,10))

GSepsis = General_Sepsis[['Age', 'Bilirubin_total', 'Creatinine', 'FiO2', 'Gender', 'HR', 'MAP', 'Platelets', 'SaO2', 'Temp', 'WBC','Hora','Paciente','SepsisLabel','GROUP_SOFA','SIRS_Sepsis','Grupo']].copy() 
GSepsis

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

GSepsis.describe()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

print(GSepsis.groupby('Grupo').size())

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split


X_multiple =GSepsis.values[:, 0:10]
y_multiple =GSepsis.values[:,11]

# Separación de datos de prueba y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

#Defino el algorito a utilizar 
lr_multiple = linear_model.LinearRegression()

#Entreno el modelo
lr_multiple.fit(X_train, y_train)

#Realiza una predicción
Y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESIÓN LINEAL MULTIPLE')
print()
print('Valor de las pendientes o coeficientes "a": ')
print(lr_multiple.coef_)
print('Valor de las intersección o coeficientes "b": ')
print(lr_multiple.intercept_)
print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

sns.set_style('darkgrid')
nuevo = General_Sepsis[['Age', 'Bilirubin_total', 'Creatinine', 'FiO2', 'Gender', 'HR', 'MAP', 'Platelets', 'SaO2', 'Temp', 'WBC','Hora','Paciente','SepsisLabel','GROUP_SOFA','SIRS_Sepsis','Grupo']].copy() 

g=sns.pairplot(nuevo,hue='Grupo', diag_kind="hist")

for ax in g.axes.flat:
  plt.setp(ax.get_xticklabels(),rotation=45)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

HR= GSepsis['HR'].values
Wbc= GSepsis['WBC'].values
Temp= GSepsis['Temp'].values
Plaquetas = GSepsis['Platelets'].values
Sao2= GSepsis['SaO2'].values
Grupos= GSepsis['Grupo'].values

X =np.array([HR,Wbc,Temp,Plaquetas,Sao2]).T
Y =np.array(Grupos)

reg=LinearRegression()
reg =reg.fit(X,Y)
Y_pred = reg.predict(X)
error = np.sqrt(mean_squared_error(Y,Y_pred ))
r2 = reg.score(X,Y)
print("El valor del error es: ", error)
print("El valor de R2 es: ", r2)
print("Los coeficientes son: \n'", reg.coef_)

HR=100
Wbc=9.0
Temp=36.5
Plaquetas=213
Sao2=97.0
print("Grupo de infección es: \n'", reg.predict([[HR,Wbc,Temp,Plaquetas,Sao2]]))