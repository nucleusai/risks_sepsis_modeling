# -*- coding: utf-8 -*-
"""EstudioEtiquetado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BTeUEYnJ3Yee9NAWLD8DJiPWIuQKa7t_
"""

# FUNCTION TO CALL THE PATIENT
# Creation of dictionary to call patients

def diccionario(numero):

  global ruta
  Tupla_Pacientes= ["Vacio",
                           "/content/sample_data/Paciente1.csv",
                           "/content/sample_data/Paciente2.csv",
                           "/content/sample_data/Paciente3.csv",
                           "/content/sample_data/Paciente4.csv",
                           "/content/sample_data/Paciente5.csv",
                           "/content/sample_data/Paciente6.csv",
                           "/content/sample_data/Paciente7.csv",
                           "/content/sample_data/Paciente8.csv",
                           "/content/sample_data/Paciente9.csv",
                           "/content/sample_data/Paciente10.csv",
                           "/content/sample_data/Paciente11.csv",
                           "/content/sample_data/Paciente12.csv",
                           "/content/sample_data/Paciente13.csv",
                           "/content/sample_data/Paciente14.csv",
                           "/content/sample_data/Paciente15.csv",
                           "/content/sample_data/Paciente16.csv",
                           "/content/sample_data/Paciente17.csv",
                           "/content/sample_data/Paciente18.csv",
                           "/content/sample_data/Paciente19.csv",
                           "/content/sample_data/Paciente20.csv", 
                           "/content/sample_data/Paciente21.csv",
                           "/content/sample_data/Paciente22.csv",
                           "/content/sample_data/Paciente23.csv",
                           "/content/sample_data/Paciente24.csv",
                           "/content/sample_data/Paciente25.csv",
                           "/content/sample_data/Paciente26.csv",
                           "/content/sample_data/Paciente27.csv",
                           "/content/sample_data/Paciente28.csv",
                           "/content/sample_data/Paciente29.csv",
                           "/content/sample_data/Paciente30.csv",
                           "/content/sample_data/Paciente31.csv",
                           "/content/sample_data/Paciente32.csv",
                           "/content/sample_data/Paciente33.csv",
                           "/content/sample_data/Paciente34.csv",
                           "/content/sample_data/Paciente35.csv",
                           "/content/sample_data/Paciente36.csv",
                           "/content/sample_data/Paciente37.csv",
                           "/content/sample_data/Paciente38.csv",
                           "/content/sample_data/Paciente39.csv",
                           "/content/sample_data/Paciente40.csv",
                           "/content/sample_data/Paciente40.csv",
                           "/content/sample_data/Paciente41.csv",
                           "/content/sample_data/Paciente42.csv",
                           "/content/sample_data/Paciente43.csv",
                           "/content/sample_data/Paciente44.csv",
                           "/content/sample_data/Paciente45.csv",
                           "/content/sample_data/Paciente46.csv",
                           "/content/sample_data/Paciente47.csv",
                           "/content/sample_data/Paciente48.csv",
                           "/content/sample_data/Paciente49.csv",
                           "/content/sample_data/Paciente50.csv"]

  DPacientes= { Tupla_Pacientes[0]:"Vacio",
                Tupla_Pacientes[1]:"/content/sample_data/Paciente1.csv",
                Tupla_Pacientes[2]:"/content/sample_data/Paciente2.csv",
                Tupla_Pacientes[3]:"/content/sample_data/Paciente3.csv",
                Tupla_Pacientes[4]:"/content/sample_data/Paciente4.csv",
                Tupla_Pacientes[5]:"/content/sample_data/Paciente5.csv",
                Tupla_Pacientes[6]:"/content/sample_data/Paciente6.csv",
                Tupla_Pacientes[7]:"/content/sample_data/Paciente7.csv",
                Tupla_Pacientes[8]: "/content/sample_data/Paciente8.csv",
                Tupla_Pacientes[9]:"/content/sample_data/Paciente9.csv",
                Tupla_Pacientes[10]:"/content/sample_data/Paciente10.csv",
                Tupla_Pacientes[11]:"/content/sample_data/Paciente11.csv",
                Tupla_Pacientes[12]:"/content/sample_data/Paciente12.csv",
                Tupla_Pacientes[13]:"/content/sample_data/Paciente13.csv",
                Tupla_Pacientes[14]:"/content/sample_data/Paciente14.csv",
                Tupla_Pacientes[15]:"/content/sample_data/Paciente15.csv",
                Tupla_Pacientes[16]: "/content/sample_data/Paciente16.csv",
                Tupla_Pacientes[16]:"/content/sample_data/Paciente17.csv",
                Tupla_Pacientes[18]:"/content/sample_data/Paciente18.csv",
                Tupla_Pacientes[19]:"/content/sample_data/Paciente19.csv",
                Tupla_Pacientes[20]:"/content/sample_data/Paciente20.csv",
                Tupla_Pacientes[21]:"/content/sample_data/Paciente21.csv",
                Tupla_Pacientes[22]:"/content/sample_data/Paciente22.csv",
                Tupla_Pacientes[23]:"/content/sample_data/Paciente23.csv",
                Tupla_Pacientes[24]:"/content/sample_data/Paciente24.csv",
                Tupla_Pacientes[25]:"/content/sample_data/Paciente25.csv",
                Tupla_Pacientes[26]:"/content/sample_data/Paciente26.csv",
                Tupla_Pacientes[27]:"/content/sample_data/Paciente27.csv",
                Tupla_Pacientes[28]:"/content/sample_data/Paciente28.csv",
                Tupla_Pacientes[29]:"/content/sample_data/Paciente29.csv",
                Tupla_Pacientes[30]:"/content/sample_data/Paciente30.csv",
                Tupla_Pacientes[31]:"/content/sample_data/Paciente31.csv",
                Tupla_Pacientes[32]: "/content/sample_data/Paciente32.csv",
                Tupla_Pacientes[33]:"/content/sample_data/Paciente33.csv",
                Tupla_Pacientes[34]:"/content/sample_data/Paciente34.csv",
                Tupla_Pacientes[35]: "/content/sample_data/Paciente35.csv",
                Tupla_Pacientes[36]: "/content/sample_data/Paciente36.csv",
                Tupla_Pacientes[37]: "/content/sample_data/Paciente37.csv",
                Tupla_Pacientes[38]: "/content/sample_data/Paciente38.csv",
                Tupla_Pacientes[39]: "/content/sample_data/Paciente39.csv",
                Tupla_Pacientes[40]: "/content/sample_data/Paciente40.csv",
                Tupla_Pacientes[41]:"/content/sample_data/Paciente41.csv",
                Tupla_Pacientes[42]: "/content/sample_data/Paciente42.csv",
                Tupla_Pacientes[43]: "/content/sample_data/Paciente43.csv",
                Tupla_Pacientes[44]: "/content/sample_data/Paciente44.csv",
                Tupla_Pacientes[45]:"/content/sample_data/Paciente45.csv",
                Tupla_Pacientes[46]:"/content/sample_data/Paciente46.csv",
                Tupla_Pacientes[47]:"/content/sample_data/Paciente47.csv",
                Tupla_Pacientes[48]:"/content/sample_data/Paciente48.csv",
                Tupla_Pacientes[49]:"/content/sample_data/Paciente49.csv",
                Tupla_Pacientes[50]:"/content/sample_data/Paciente50.csv"
                }

  ruta= DPacientes[Tupla_Pacientes[numero]]

# BRING DEMOGRAPHIC DATA

def datos_demograficos_paciente(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd
  
  global Demograficos
  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')
  

  Demograficos = datos[['Age', 'Gender', 'Unit1', 'Unit2', 'HospAdmTime', 'ICULOS', 'SepsisLabel']].copy()
  
  #return print(dTabla)

# TABLE OF CLINICAL DATA USED FOR SIRS AND SOFA

def tabla_Paciente(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd

  global ClinicalData
  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  ClinicalData = datos[['HR', 'Temp', 'WBC', 'Resp', 'O2Sat', 'FiO2', 'Platelets', 'Bilirubin_total', 'MAP', 'Creatinine']].copy()
  
  #return print(dTabla)

#Función SIRS

def datos_SIRS(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd

  global DFSIRS
  global TablaSIRS

  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  TablaSIRS = datos[['SepsisLabel']].copy()

  datos2 = datos[['HR', 'Temp', 'WBC', 'SepsisLabel']].copy() # Datos que se utilizan para el analisis SIRS
  dTabla = datos2.fillna(0) # Cambiando los NaN por 0 para realizar validación


  #Ciclo 1
  for i in range(0,len(dTabla)): # Ciclo para crear las columnas de rangos Boolean
                                 #.loc para verificar un valor de posición
    
    if (dTabla.loc[i, 'HR'] == 0) or (dTabla.loc[i, 'Temp'] == 0) or (dTabla.loc[i, 'WBC'] == 0) :
       
       dTabla.loc[i, 'SIRS_HR'] = 0 
       dTabla.loc[i, 'SIRS_Temp'] = 0
       dTabla.loc[i, 'SIRS_WBC'] = 0
       print()

    else:
        
        if  (dTabla.loc[i, 'HR']> 60.0 and dTabla.loc[i, 'HR']< 100.0): # Creación Columna SIRS de frecuencia cardiaca
            dTabla.loc[i, 'SIRS_HR'] = False
            #TablaSIRS.loc[i, 'SIRS_HR'] = False
            
        else:
            dTabla.loc[i, 'SIRS_HR'] = True
           # TablaSIRS.loc[i, 'SIRS_HR'] = True

        
        if  (dTabla.loc[i, 'Temp']> 36.0 and dTabla.loc[i, 'Temp']< 38.3): # Creación Columna SIRS de temperatura
            dTabla.loc[i, 'SIRS_Temp'] = False
           # TablaSIRS.loc[i, 'SIRS_Temp'] = False
            
        else:
            dTabla.loc[i, 'SIRS_Temp'] = True
           # TablaSIRS.loc[i, 'SIRS_Temp'] = True


        if (dTabla.loc[i, 'WBC']> 4.0 and dTabla.loc[i, 'WBC']< 12.0): # Creación Columna SIRS de Leucocitos
           dTabla.loc[i, 'SIRS_WBC'] = False
          # TablaSIRS.loc[i, 'SIRS_WBC'] = False
           
        else:
           dTabla.loc[i, 'SIRS_WBC'] = True
          # TablaSIRS.loc[i, 'SIRS_WBC'] = True

        # Leucocitos se maneja por mil en la data lo encontramos decimales 7.5
  


  #Ciclo 2
  for i in range(0,len(TablaSIRS)): # Ciclo para crear la columna de resultado de Sepsis
    
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

  #TablaSIRS = dTabla
  DFSIRS = dTabla[['SIRS_HR', 'SIRS_Temp', 'SIRS_WBC', 'SIRS_Sepsis', 'SepsisLabel']].copy()
 #return print(DFSIRS)

#Función SOFA

def datos_SOFA(ruta):
  
  import matplotlib.pyplot as plt
  import pandas as pd

  global DFSOFA
  global TablaSOFA

  csv_path = ruta
  datos = pd.read_csv(csv_path, sep=',')

  datos2 = datos[['O2Sat', 'FiO2', 'Platelets', 'Bilirubin_total', 'MAP', 'Creatinine', 'SepsisLabel']].copy() # Datos que se utilizan para el analisis SOFA
  dTabla = datos2.fillna(0) # Cambiando los NaN por 0 para realizar validación


  #Ciclo 1

  for i in range(0,len(dTabla)): # Ciclo para crear las columna de respiración para puntuación SOFA
     
     if dTabla.loc[i, 'FiO2'] != 0:
         dTabla.loc[i, 'Respiracion'] = dTabla.loc[i, 'O2Sat'] / dTabla.loc[i, 'FiO2']
     else:
       dTabla.loc[i, 'Respiracion'] = 0;



  #Ciclo 2

  for i in range(0,len(dTabla)): # Ciclo para crear las columnas de rango SOFA
                                 #.loc para verificar un valor de posición


      if (dTabla.loc[i, 'Respiracion'] == 0) or (dTabla.loc[i, 'Platelets'] == 0) or (dTabla.loc[i, 'Bilirubin_total'] == 0 ) or (dTabla.loc[i, 'MAP'] == 0) or (dTabla.loc[i, 'Creatinine'] == 0):

          dTabla.loc[i, 'SOFA_Respiracion'] = False
          dTabla.loc[i, 'SOFA_Platelets'] = False
          dTabla.loc[i, 'SOFA_Bilirubin_total'] = False
          dTabla.loc[i, 'SOFA_MAP'] = False
          dTabla.loc[i, 'SOFA_Creatinine'] = False

      else:

          if dTabla.loc[i, 'Respiracion']>= 302: # Creación Columna SOFA de saturación de oxigeno
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
    

          if dTabla.loc[i, 'Platelets']>= 150: # Creación Columna SOFA de plaquetas
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
 


          if dTabla.loc[i, 'Bilirubin_total']< 1.2 : # Creación Columna SOFA  de Bilirrubina Total
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


      
          if dTabla.loc[i, 'MAP']>= 70.0 : # Creación Columna SOFA de Presión arterial media
             dTabla.loc[i, 'SOFA_MAP'] = 0
          else:
             dTabla.loc[i, 'SOFA_MAP'] = 1

      

          if dTabla.loc[i, 'Creatinine'] < 1.2 : # Creaion columna SOFA de Creatinine
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

     if (dTabla.loc[i, 'SOFA_Respiracion'] == False) or (dTabla.loc[i, 'SOFA_Platelets'] == False) or (dTabla.loc[i, 'SOFA_Bilirubin_total'] == False) or (dTabla.loc[i, 'SOFA_MAP'] == False) or (dTabla.loc[i, 'SOFA_Creatinine'] == False):
         dTabla.loc[i, 'SOFA_Sepsis'] = False
     else:
         dTabla.loc[i, 'SOFA_Sepsis'] = dTabla.loc[i, 'SOFA_Respiracion'] + dTabla.loc[i, 'SOFA_Platelets'] + dTabla.loc[i, 'SOFA_Bilirubin_total'] + dTabla.loc[i, 'SOFA_MAP'] + dTabla.loc[i, 'SOFA_Creatinine']


  TablaSOFA = dTabla
  DFSOFA = dTabla[['SOFA_Respiracion', 'SOFA_Platelets', 'SOFA_Bilirubin_total', 'SOFA_MAP', 'SOFA_Creatinine', 'SOFA_Sepsis', 'SepsisLabel']].copy()
  
 #return print(DFSOFA)

# TEST MENU EXECUTION OF SIRS AND SOFA FUNCTIONS

numero = int(input('Numero de paciente que desea verificar 1-50: '))
#print("Datos del paciente",numero,"\n")

diccionario(numero)
datos_demograficos_paciente(ruta)
tabla_Paciente(ruta)
datos_SIRS(ruta)
datos_SOFA(ruta)

#Creación de archivos csv
#archivoscsv(ruta)

#PACIENTES DE ESTUDIO ETIQUETADO CON SEPSIS
#Paciente 9
#Paciente 11
#Paciente 15
#Paciente 18
#Paciente 22
#Paciente 28
#Paciente 34
#Paciente 42

print("DATOS DEMOGRAFICOS PACIENTE: ",numero,"\n")
Demograficos

print("DATOS CLINICOS PACIENTE: ",numero,"\n")
ClinicalData

print("DATOS SIRS SEPSIS: ",numero,"\n")
DFSIRS

print("DATOS SOFA SEPSIS: ",numero,"\n")
DFSOFA

import matplotlib.pyplot as plt
import pandas as pd

csv_path = "/content/sample_data/p000001.cvs"
datos = pd.read_csv(csv_path, sep=',')
datos