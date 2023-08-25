import numpy as np
import math as mt
import pandas as pd

lista=[0,1,2,3,4,5,6]

print(lista)

print('el "7" está en la lista?')

if(7 in lista):
    print("True")
else:
    print("False")

print(""" Puedo escribir 
      saltos 
      de linea! """)

pi= mt.pi
pi_redondeado= "%.2f" % pi
print("Redondeo el numero pi:")
print(pi_redondeado)

# Cuestionario N°3 # 

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (matriz.ndim)

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print(matriz.shape)

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (vector.size)

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (matriz [2,2]) 

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (vector [2])

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (vector.reshape ((2,5)))

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (vector [:3])

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (matriz [1:,2:3])

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (vector [3:4])

vector = np.array([3,7,1,9,10,5,4,3,2,1])
matriz = np.array([[5,7,9,8,7],[1,6,3,3,4],[5,9,10,1,3],[2,2,8,8,9],[1,3,9,10,0]])
print (matriz [:3,:3])

df1 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'carrera': ['ISI', 'Civil', 'Civil', 'Mecánica']})
df2 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'año_ingreso':[2022,2019,2018,2022]})
df3 = pd.DataFrame({'alumno':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
df4 = pd.DataFrame({'estudiante':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
print (pd.concat ([df1, df3]), end='\n\n')

df1 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'carrera': ['ISI', 'Civil', 'Civil', 'Mecánica']})
df2 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'año_ingreso':[2022,2019,2018,2022]})
df3 = pd.DataFrame({'alumno':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
df4 = pd.DataFrame({'estudiante':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
print (pd.concat ([df1, df3], ignore_index=True), end='\n\n')

df1 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'carrera': ['ISI', 'Civil', 'Civil', 'Mecánica']})
df2 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'año_ingreso':[2022,2019,2018,2022]})
df3 = pd.DataFrame({'alumno':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
df4 = pd.DataFrame({'estudiante':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
print (df1.append(df3), end='\n\n')

df1 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'carrera': ['ISI', 'Civil', 'Civil', 'Mecánica']})
df2 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'año_ingreso':[2022,2019,2018,2022]})
df3 = pd.DataFrame({'alumno':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
df4 = pd.DataFrame({'estudiante':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
print (pd.merge (df1, df2), end='\n\n')

df1 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'carrera': ['ISI', 'Civil', 'Civil', 'Mecánica']})
df2 = pd.DataFrame({'alumno':['Juan Perez', 'Jorge Diaz', 'Ana Baez', 'Sonia Re'],
'año_ingreso':[2022,2019,2018,2022]})
df3 = pd.DataFrame({'alumno':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
df4 = pd.DataFrame({'estudiante':['Tomás Cerli', 'Joaquín Roa'],
'carrera': ['ISI', 'ISI']})
print (pd.merge (df3, df4, left_on='alumno', right_on='estudiante'), end='\n\n')
