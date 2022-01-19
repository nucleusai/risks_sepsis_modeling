# -*- coding: utf-8 -*-
"""
PACIENTES CON SEPSIS:
- Paciente 9
- Paciente 11
- Paciente 15
- Paciente 18
- Paciente 22
- Paciente 28
- Paciente 34
- Paciente 42
"""


# DATOS PACIENTEs
import pandas as pd

psv_path = '/content/sample_data/p000009.psv'
datos9 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000011.psv'
datos11 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000015.psv'
datos15 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000018.psv'
datos18 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000022.psv'
datos22 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000028.psv'
datos28 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000034.psv'
datos34 = pd.read_table(psv_path, sep='|')

psv_path = '/content/sample_data/p000042.psv'
datos42 = pd.read_table(psv_path, sep='|')



#Agrupación datos HR Resp Hgab pacientes.

dTablaP9 = datos9[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP11 = datos11[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP15 = datos15[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP18 = datos18[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP22 = datos22[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP28 = datos28[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP34 = datos34[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()
dTablaP42 = datos42[['HR', 'Resp', 'Hgb', 'SepsisLabel']].copy()

dTablaP9

dTablaP11

dTablaP15

dTablaP18

dTablaP22

dTablaP28

dTablaP34

dTablaP42

import matplotlib.pyplot as plt
#Analisis HR PACIENTES con Sepsis

#Caracteristicas del grafico
plt.plot(datos9['HR'], label= 'Paciente9', linewidth = 0.5, color = 'blue')
plt.plot(datos11['HR'], label= 'Paciente 11', linewidth = 0.5, color = 'green')
plt.plot(datos15['HR'], label= 'Paciente15', linewidth = 0.5, color = 'yellow')
plt.plot(datos18['HR'], label= 'Paciente18', linewidth = 0.5, color = 'red')
plt.plot(datos22['HR'], label= 'Paciente22', linewidth = 0.5, color = 'CYAN')
plt.plot(datos28['HR'], label= 'Paciente28', linewidth = 0.5, color = 'MAGENTA')
plt.plot(datos34['HR'], label= 'Paciente34', linewidth = 0.5, color = 'BLACK')
plt.plot(datos42['HR'], label= 'Paciente42', linewidth = 0.5, color = 'navy')

#Definir titulo y nombres de los ejes
plt.title("Analisis HR")
plt.ylabel('Escala')
plt.xlabel('Semana')

#Mostrar leyenda, cuadricula y figura

#plt.legend()
plt.grid()
#plt.xlim(0,50) #Limitar grafico
plt.show()

import matplotlib.pyplot as plt
#Analisis Resp PACIENTES con Sepsis

#Caracteristicas del grafico
plt.plot(datos9['Resp'], label= 'Paciente9', linewidth = 0.5, color = 'blue')
plt.plot(datos11['Resp'], label= 'Paciente 11', linewidth = 0.5, color = 'green')
plt.plot(datos15['Resp'], label= 'Paciente15', linewidth = 0.5, color = 'yellow')
plt.plot(datos18['Resp'], label= 'Paciente18', linewidth = 0.5, color = 'red')
plt.plot(datos22['Resp'], label= 'Paciente22', linewidth = 0.5, color = 'CYAN')
plt.plot(datos28['Resp'], label= 'Paciente28', linewidth = 0.5, color = 'MAGENTA')
plt.plot(datos34['Resp'], label= 'Paciente34', linewidth = 0.5, color = 'BLACK')
plt.plot(datos42['Resp'], label= 'Paciente42', linewidth = 0.5, color = 'navy')

#Definir titulo y nombres de los ejes
plt.title("Analisis Resp")
plt.ylabel('Escala')
plt.xlabel('Semana')

#Mostrar leyenda, cuadricula y figura

#plt.legend()
plt.grid()
plt.xlim(0,50)
plt.ylim(10,40)
plt.show()

import matplotlib.pyplot as plt
#Analisis Hgb PACIENTES con Sepsis

#Caracteristicas del grafico
plt.plot(datos9['Hgb'],'o-', label= 'Paciente9', linewidth = 1, color = 'blue')
plt.plot(datos11['Hgb'],'o-', label= 'Paciente 11', linewidth = 1, color = 'green')
plt.plot(datos15['Hgb'],'o-', label= 'Paciente15', linewidth = 1, color = 'yellow')
plt.plot(datos18['Hgb'],'o-', label= 'Paciente18', linewidth = 1, color = 'red')
plt.plot(datos22['Hgb'],'o-', label= 'Paciente22', linewidth = 1, color = 'CYAN')
plt.plot(datos28['Hgb'],'o-', label= 'Paciente28', linewidth = 1, color = 'MAGENTA')
plt.plot(datos34['Hgb'],'o-', label= 'Paciente34', linewidth = 1, color = 'BLACK')
plt.plot(datos42['Hgb'],'o-', label= 'Paciente42', linewidth = 1, color = 'navy')

#Definir titulo y nombres de los ejes
plt.title("Analisis Hgb")
plt.ylabel('Escala')
plt.xlabel('Semana')

#Mostrar leyenda, cuadricula y figura

#plt.legend()
plt.xlim(0,50)
plt.grid()
plt.show()

import matplotlib.pyplot as plt
#Analisis HR PACIENTES con Sepsis

#Caracteristicas del grafico
plt.plot(datos9['SepsisLabel'], 'o', label= 'Paciente9', linewidth = 0.1, color = 'blue')
plt.plot(datos11['SepsisLabel'],'o', label= 'Paciente 11', linewidth = 0.1, color = 'green')
plt.plot(datos15['SepsisLabel'],'o', label= 'Paciente15', linewidth = 0.1, color = 'yellow')
plt.plot(datos18['SepsisLabel'],'o', label= 'Paciente18', linewidth = 0.1, color = 'red')
plt.plot(datos22['SepsisLabel'],'o', label= 'Paciente22', linewidth = 0.1, color = 'CYAN')
plt.plot(datos28['SepsisLabel'],'o', label= 'Paciente28', linewidth = 0.1, color = 'MAGENTA')
plt.plot(datos34['SepsisLabel'],'o', label= 'Paciente34', linewidth = 0.1, color = 'BLACK')
plt.plot(datos42['SepsisLabel'],'o', label= 'Paciente42', linewidth = 0.1, color = 'navy')

#Definir titulo y nombres de los ejes
plt.title("Analisis SepsisLabel")
plt.ylabel('Escala')
plt.xlabel('Semana')

#Mostrar leyenda, cuadricula y figura

#plt.legend()
#plt.xlim(0,50)
plt.grid()
plt.show()

import matplotlib.pyplot as plt

#Analisis paciente 11

plt.subplot(411)
p1,= plt.plot(datos11['SepsisLabel'],'o', label= 'Paciente42', linewidth = 0.5, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Semana')

plt.subplot(412)
p2,= plt.plot(datos11['HR'],'o-', label= 'Paciente42', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Semana')
plt.subplot(413)
p3,= plt.plot(datos11['Resp'],'o-', label= 'Paciente42', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Semana')
plt.subplot(414)
p4,= plt.plot(datos11['Hgb'],'o-', label= 'Paciente42', linewidth = 1, color = 'navy')
plt.ylabel('Escala')
plt.xlabel('Semana')


#Mostrar leyenda, cuadricula y figura

#plt.legend()
#plt.grid()
#plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


sns.countplot(datos11['HR'], palette = 'ocean')

import matplotlib.pyplot as plt
import numpy as np

#Analisis HR PACIENTES con Sepsis

#Caracteristicas del grafico

plt.hist(datos11['HR'],label= 'Paciente 11',color = 'green')
plt.hist(datos15['HR'],label= 'Paciente15', color = 'yellow')
plt.hist(datos22['HR'],label= 'Paciente22', color = 'CYAN')

#Definir titulo y nombres de los ejes
plt.title("Analisis HR")
plt.ylabel('Escala')
plt.xlabel('Semana')

#Mostrar leyenda, cuadricula y figura

plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt
#Analisis HR PACIENTES con Sepsis

#Caracteristicas del grafico


plt.plot(datos11['HR'], label= 'Paciente 11', linewidth = 0.5, color = 'green')

#Definir titulo y nombres de los ejes
plt.title("Analisis HR")
plt.ylabel('Escala')
plt.xlabel('Semana')

#Mostrar leyenda, cuadricula y figura

plt.legend()
plt.show()