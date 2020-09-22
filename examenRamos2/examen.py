
#  Examen

## 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros


import numpy as np
import pandas as pd
arr_pand = np.random.randint(0,80,60).reshape(10,6)

df1 = pd.DataFrame(arr_pand)


tercero = df1.iloc[0:5,0:5]


## 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
df2 = pd.DataFrame(np.random.random((6,4)))
df2.index=['2013-01-01','2013-01-02','2013-01-03','2013-01-04','2013-01-05','2013-01-06']
df2.columns=['A','B','C','D']
df2


## 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del 
##Dataframe mostrar las columnas, con otro comando mostrar los valores.

arr_pand4 = np.random.randint(0,80,60).reshape(10,6)

df4 = pd.DataFrame(arr_pand4)
df4.columns = ['A', 'B', 'C', 'D', 'E','F']


columna1 = df4.iloc[0] # Serie
valores = df4.iloc[0:1] # Primeras cinco filas
print(columna1)
print(valores)

## 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del
## Dataframe describir estadisticamente el Dataframe
arr_pand5 = np.random.randint(0,80,60).reshape(10,6)

df5 = pd.DataFrame(arr_pand4)
df5.columns = ['A', 'B', 'C', 'D', 'E','F']
print("unicos en A")

print(pd.unique(df5['A']))
print("DESCRIBE en A")

print(df5['A'].describe())

## 6) Crear un Dataframe con 10 registros y 
##6 columnas y con una funcion del Dataframe transponer los datos


arr_pand6 = np.random.randint(0,80,60).reshape(10,6)

df6 = pd.DataFrame(arr_pand4)
df6.columns = ['A', 'B', 'C', 'D', 'E','F']
df61 = df6.transpose()

## 7) Crear un Dataframe con 10 registros y 6 columnas y 
##Ordenar el dataframe 1 vez por cada columna, ascendente y descendente


arr_pand7 = np.random.randint(0,80,60).reshape(10,6)

df7 = pd.DataFrame(arr_pand4)
df7.columns = ['A', 'B', 'C', 'D', 'E','F']

df71 = df7.sort_values("A", ascending=True)
df72 = df7.sort_values("A",ascending=False)

## 8) Crear un Dataframe con 10 registros y 6 columnas 
## llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

arr_pand8 = np.random.randint(1,10,60).reshape(10,6)

df8 = pd.DataFrame(arr_pand4)
df8.columns = ['A', 'B', 'C', 'D', 'E','F']

df81= df8.where(df8>7) 
df81

## 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos 
##del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

df9 = pd.DataFrame(np.random.randint(0,10,60).reshape(10,6))
df91 = df9.where(df9<7)

df92 = df9.fillna(0)



## 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio
df10 = pd.DataFrame(np.random.randint(0,10,60).reshape(10,6))
media = df10.mean()
media
mediana = df10.median()
mediana
promedio = np.average(df10)
promedio


## 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, 
##luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe
df111 = pd.DataFrame(np.random.randint(1, 10, 60).reshape(-1,6), columns=list('ABCDEF'))
df111
df112 = pd.DataFrame(np.random.randint(1, 10, 60).reshape(-1,6), columns=list('ABCDEF'))
df112
df113=pd.concat([df111, df112], axis=0)



## 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. 
##Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.
strings = np.random.choice(['A', 'B', 'C', 'D', 'E', 'F'], 60).reshape(10,6)
df12 = pd.DataFrame(strings)
df12

a = df12[0].append(df12[1])
b = df12[2].append(df12[3])
c = df12[4].append(df12[5])
df121 = pd.DataFrame(a)
df121[1] = b
df121[2] = c
df121

## 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros,
## obtener la frecuencia de repeticion de los numeros enteros en cada columna


arr_pand13 = np.random.randint(1,10,60).reshape(10,6)

df13 = pd.DataFrame(arr_pand4)
df13.columns = ['A', 'B', 'C', 'D', 'E','F']

df131 = df13.apply(pd.value_counts)
df131

## 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. 
##Crear una nueva columna con el calculo por fila (A * B ) / C

arr_pand14 = np.random.randint(1,10,60).reshape(10,6)

df14 = pd.DataFrame(arr_pand4)
df14.columns = ['A', 'B', 'C', 'D', 'E','F']


calculo = (df14['A'] * df14['B'])/(df14['C'])
df14['Calculo']=calculo
df14


