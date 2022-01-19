# -*- coding: utf-8 -*-
"""Información corpus de datos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ej1k9ApHk1spcgH8lhaioGkEJCTzrl7v
"""

#HR = Frecuencia cardiaca latidos por minuto.
#O2sat = Saturación de oxigeno, mide en porcentaje. oxigeno en el cuerpo.
#Temp = Temperatura en grados Centigrado.
#SBD= Presión arterial Sistolica mide la contracción cardiaca se interpreta en milimetros de mercurio.
#MAP= Presión arterial media capacida de eyección del corazón milimetros de mercurio
#DBP = Presión arterial diastolica mide la relajación del corazon milimetros de mercurio
#Resp= Frecuencia de respiración por minutos 
#Etco2= Dioxido de carbono milimetros de mercurio.
#BaseExcess = Exceso de bicabonato milimol en litros
#Hco3 = Bicarbonato mmol por litro
#Fio2 = Fracción de oxigeno inspirado (%)
#pH = Ph en sangre
#Paco2 = Presión parcial de dioxido de carbono en sangre arterial se mide en %
#Sao2 = Saturación de oxigeno en sangre arterial se mide en porcentaje.
#AST= Aspartato transaminasa Unidades internacionales sobre litros.
#BUN = Nitrogeno ureico en sangre miligramos sobre desilitros.
#Alkalinephos=  Fosfatasa de alcalina  Unidades internacionales sobre litros.
#Calcium = calcio miligramos sobre decilitros
#Chloride = Colruro milimol sobre litros
#Creatinine = creatinina Miligramos sobre decilitros
#Bilirubin direct = Bilirrubina directa miligramos sobre decilitros.
#Glucose = glucosa serica miligramos sobre decilitros
#Lactate = Acido lactico miligramos sobre decilitro
#Magnesium = Magnesio milimol sobre decilitros
#Phosphate = Fosforo miligramos sobre decilitros
#Potassium = Potasio milimol sobre litro
#Bilirubin total = bilirubinas totales miligramos sobre decilitros
#Troponinl = Troponina nanogramos sobre mililitros
#Hct = Hematocrito en %
#Hgb = Hemoglobina Gramos sobre decilitros
#PTT = Tiempo de Tomboplastina parcial segundos
#WBC = leucocitos se mide cantidad de leucositos sobre litro
#Fibrinogen = Cantidad de fibrinogeno miligramos sobre decilitro
#Platelets = plaquetas recuento de plaquetas en sangre cantidad sobre mililitro
#Age = edad
#Gender = Genero
#Unit 1 = Identificador administrativo booleano UCI
#Unit 2 = Identificado administrativo booleano  UCIM
#HospAdmTime = Tiempo ingreso en hospital y UCI
#ICULOS = Tiempo Estancia en UCI
#SepsisLabel =

#glob.glob Revisar
# Luego realizar split para traer nombre del archivo
# Recorrer archivo (Traer variable HR por semana, de cada paciente (plot))
# Numero de respiraciones y hemoglobina y plot a los 3 
# Buscar pacientes con sepsis (Listo)
# Dentro paper variables de correlación (analisar y verificar)

# DATOS PACIENTE 1
import pandas as pd

psv_path = '/content/sample_data/p000001.psv'
datos = pd.read_table(psv_path, sep='|')

print(datos)

# DATOS PACIENTE 2
import pandas as pd

psv_path = '/content/sample_data/p000002.psv'
datos2 = pd.read_table(psv_path, sep='|')

print(datos2)

# DATOS PACIENTE 3
import pandas as pd

psv_path = '/content/sample_data/p000003.psv'
datos3 = pd.read_table(psv_path, sep='|')

print(datos3)

# DATOS PACIENTE 4
import pandas as pd

psv_path = '/content/sample_data/p000004.psv'
datos4 = pd.read_table(psv_path, sep='|')

print(datos3)

# DATOS PACIENTE 5
import pandas as pd

psv_path = '/content/sample_data/p000005.psv'
datos5 = pd.read_table(psv_path, sep='|')

print(datos5)

# DATOS PACIENTE 6
import pandas as pd

psv_path = '/content/sample_data/p000006.psv'
datos6 = pd.read_table(psv_path, sep='|')
print(datos6)

# DATOS PACIENTE 7
import pandas as pd

psv_path = '/content/sample_data/p000007.psv'
datos7 = pd.read_table(psv_path, sep='|')
print(datos7)

# DATOS PACIENTE 8
import pandas as pd

psv_path = '/content/sample_data/p000008.psv'
datos8 = pd.read_table(psv_path, sep='|')
print(datos8)

# DATOS PACIENTE 9
import pandas as pd

psv_path = '/content/sample_data/p000009.psv'
datos9 = pd.read_table(psv_path, sep='|')
print(datos9)

# DATOS PACIENTE 10
import pandas as pd

psv_path = '/content/sample_data/p000010.psv'
datos10 = pd.read_table(psv_path, sep='|')
print(datos10)

# DATOS PACIENTE 11
import pandas as pd

psv_path = '/content/sample_data/p000011.psv'
datos11 = pd.read_table(psv_path, sep='|')
print(datos11)

# DATOS PACIENTE 12
import pandas as pd

psv_path = '/content/sample_data/p000012.psv'
datos12 = pd.read_table(psv_path, sep='|')
print(datos12)

# DATOS PACIENTE 13
import pandas as pd

psv_path = '/content/sample_data/p000013.psv'
datos13 = pd.read_table(psv_path, sep='|')
print(datos13)

# DATOS PACIENTE 14
import pandas as pd

psv_path = '/content/sample_data/p000014.psv'
datos14 = pd.read_table(psv_path, sep='|')
print(datos14)

# DATOS PACIENTE 15
import pandas as pd

psv_path = '/content/sample_data/p000015.psv'
datos15 = pd.read_table(psv_path, sep='|')
print(datos15)

# DATOS PACIENTE 16
import pandas as pd

psv_path = '/content/sample_data/p000016.psv'
datos16 = pd.read_table(psv_path, sep='|')
print(datos16)

# DATOS PACIENTE 17
import pandas as pd

psv_path = '/content/sample_data/p000017.psv'
datos17 = pd.read_table(psv_path, sep='|')
print(datos17)

# DATOS PACIENTE 18
import pandas as pd

psv_path = '/content/sample_data/p000018.psv'
datos18 = pd.read_table(psv_path, sep='|')
print(datos18)

# DATOS PACIENTE 19
import pandas as pd

psv_path = '/content/sample_data/p000019.psv'
datos19 = pd.read_table(psv_path, sep='|')
print(datos19)

# DATOS PACIENTE 20
import pandas as pd

psv_path = '/content/sample_data/p000020.psv'
datos20 = pd.read_table(psv_path, sep='|')
print(datos20)

# DATOS PACIENTE 21
import pandas as pd

psv_path = '/content/sample_data/p000021.psv'
datos21 = pd.read_table(psv_path, sep='|')
print(datos21)

# DATOS PACIENTE 22
import pandas as pd

psv_path = '/content/sample_data/p000022.psv'
datos22 = pd.read_table(psv_path, sep='|')
print(datos22)

# DATOS PACIENTE 23
import pandas as pd

psv_path = '/content/sample_data/p000023.psv'
datos23 = pd.read_table(psv_path, sep='|')
print(datos23)

# DATOS PACIENTE 24
import pandas as pd

psv_path = '/content/sample_data/p000024.psv'
datos24 = pd.read_table(psv_path, sep='|')
print(datos24)

# DATOS PACIENTE 25
import pandas as pd

psv_path = '/content/sample_data/p000025.psv'
datos25 = pd.read_table(psv_path, sep='|')
print(datos25)

# DATOS PACIENTE 26
import pandas as pd

psv_path = '/content/sample_data/p000026.psv'
datos26 = pd.read_table(psv_path, sep='|')
print(datos26)

# DATOS PACIENTE 27
import pandas as pd

psv_path = '/content/sample_data/p000027.psv'
datos27 = pd.read_table(psv_path, sep='|')
print(datos27)

# DATOS PACIENTE 28
import pandas as pd

psv_path = '/content/sample_data/p000028.psv'
datos28 = pd.read_table(psv_path, sep='|')
print(datos28)

# DATOS PACIENTE 29
import pandas as pd

psv_path = '/content/sample_data/p000029.psv'
datos29 = pd.read_table(psv_path, sep='|')
print(datos29)

# DATOS PACIENTE 30
import pandas as pd

psv_path = '/content/sample_data/p000030.psv'
datos30 = pd.read_table(psv_path, sep='|')
print(datos30)

# DATOS PACIENTE 31
import pandas as pd

psv_path = '/content/sample_data/p000031.psv'
datos31 = pd.read_table(psv_path, sep='|')
print(datos31)

# DATOS PACIENTE 32
import pandas as pd

psv_path = '/content/sample_data/p000032.psv'
datos32 = pd.read_table(psv_path, sep='|')
print(datos32)

# DATOS PACIENTE 33
import pandas as pd

psv_path = '/content/sample_data/p000033.psv'
datos33 = pd.read_table(psv_path, sep='|')
print(datos33)

# DATOS PACIENTE 34
import pandas as pd

psv_path = '/content/sample_data/p000034.psv'
datos34 = pd.read_table(psv_path, sep='|')
print(datos34)

# DATOS PACIENTE 35
import pandas as pd

psv_path = '/content/sample_data/p000035.psv'
datos35 = pd.read_table(psv_path, sep='|')
print(datos35)

# DATOS PACIENTE 36
import pandas as pd

psv_path = '/content/sample_data/p000036.psv'
datos36 = pd.read_table(psv_path, sep='|')
print(datos36)

# DATOS PACIENTE 37
import pandas as pd

psv_path = '/content/sample_data/p000037.psv'
datos37 = pd.read_table(psv_path, sep='|')
print(datos37)

# DATOS PACIENTE 38
import pandas as pd

psv_path = '/content/sample_data/p000038.psv'
datos38 = pd.read_table(psv_path, sep='|')
print(datos38)

# DATOS PACIENTE 39
import pandas as pd

psv_path = '/content/sample_data/p000039.psv'
datos39 = pd.read_table(psv_path, sep='|')
print(datos39)

# DATOS PACIENTE 40
import pandas as pd

psv_path = '/content/sample_data/p000040.psv'
datos40 = pd.read_table(psv_path, sep='|')
print(datos40)

# DATOS PACIENTE 41
import pandas as pd

psv_path = '/content/sample_data/p000041.psv'
datos41= pd.read_table(psv_path, sep='|')
print(datos41)

# DATOS PACIENTE 42
import pandas as pd

psv_path = '/content/sample_data/p000042.psv'
datos42 = pd.read_table(psv_path, sep='|')
print(datos42)

# DATOS PACIENTE 43
import pandas as pd

psv_path = '/content/sample_data/p000043.psv'
datos43 = pd.read_table(psv_path, sep='|')
print(datos43)

# DATOS PACIENTE 44
import pandas as pd

psv_path = '/content/sample_data/p000044.psv'
datos44 = pd.read_table(psv_path, sep='|')
print(datos44)

# DATOS PACIENTE 45
import pandas as pd

psv_path = '/content/sample_data/p000045.psv'
datos45 = pd.read_table(psv_path, sep='|')
print(datos45)

# DATOS PACIENTE 46
import pandas as pd

psv_path = '/content/sample_data/p000046.psv'
datos46 = pd.read_table(psv_path, sep='|')
print(datos46)

# DATOS PACIENTE 47
import pandas as pd

psv_path = '/content/sample_data/p000047.psv'
datos47 = pd.read_table(psv_path, sep='|')
print(datos47)

# DATOS PACIENTE 48
import pandas as pd

psv_path = '/content/sample_data/p000048.psv'
datos48 = pd.read_table(psv_path, sep='|')
print(datos48)

# DATOS PACIENTE 49
import pandas as pd

psv_path = '/content/sample_data/p000049.psv'
datos49 = pd.read_table(psv_path, sep='|')
print(datos49)

# DATOS PACIENTE 50
import pandas as pd

psv_path = '/content/sample_data/p000050.psv'
datos50 = pd.read_table(psv_path, sep='|')
print(datos50)

"""PACIENTES CON SEPSIS:
- Paciente 9
- Paciente 11
- Paciente 15
- Paciente 18
- Paciente 22
- Paciente 28
- Paciente 34
- Paciente 42
"""

list(datos.columns)

#Agrupación datos HR Resp Hgab pacientes.

dtPaciente9 = datos9[['HR', 'Resp', 'Hgb']].copy()
dtPaciente11 = datos11[['HR', 'Resp', 'Hgb']].copy()
dtPaciente15 = datos15[['HR', 'Resp', 'Hgb']].copy()
dtPaciente18 = datos18[['HR', 'Resp', 'Hgb']].copy()
dtPaciente22 = datos22[['HR', 'Resp', 'Hgb']].copy()
dtPaciente28 = datos28[['HR', 'Resp', 'Hgb']].copy()
dtPaciente34 = datos34[['HR', 'Resp', 'Hgb']].copy()
dtPaciente42 = datos42[['HR', 'Resp', 'Hgb']].copy()
dtPaciente1 = datos[['HR', 'Resp', 'Hgb']].copy()
dtPaciente2 = datos2[['HR', 'Resp', 'Hgb']].copy()
dtPaciente3 = datos3[['HR', 'Resp', 'Hgb']].copy()
dtPaciente4 = datos4[['HR', 'Resp', 'Hgb']].copy()
dtPaciente5 = datos5[['HR', 'Resp', 'Hgb']].copy()
dtPaciente6 = datos6[['HR', 'Resp', 'Hgb']].copy()
dtPaciente7 = datos7[['HR', 'Resp', 'Hgb']].copy()

