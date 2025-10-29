# Enlace TP

# https://aulavirtual.instituto.ort.edu.ar/mod/assign/view.php?id=133054 
# 

# Ejercicio 1
#Dada una lista de enteros, calcular cuál es el que más veces aparece.

# Ejercicio 2
#Hacer kmeans sobre un dataset dado (con un k adecuado), luego informar el contenido del cluster de más puntos, y su radio.

# Ejercicio 3
# Otro ejercicio: determinar si todos los clusters resultaron con igual cantidad de puntos o no.

# Ejercicio 4
# Escribir un script para obtener un clustering a partir del archivo clientes.csv,
# empleando como número de clusters un valor razonable calculado por el script,
# que grafique los clusters cada uno representado por un ícono distinto, 
# y que imprima la mediana de las edades para cada cluster y el mínimo de los radios de estos. 
# No se asume conocido el número de filas, debiendo la función calcularlo si hiciera falta.

# Ejercicio 5
# Escribir una función que reciba un valor c y un valor f, 
# y usando un algoritmo adecuado, arme un árbol de decisión sobre mushrooms.csv 
# con el fin de predecir si un hongo es comestible, 
# teniendo en cuenta sólo los datos de las columnas 2 hasta la c, 
# usando como testing f filas pares tomadas al azar entre las 800 últimas, 
# y como entrenamiento el resto de las filas del archivo. 
# No se asumen conocidos el número de filas ni el de columnas, 
# debiendo la función calcularlos si hiciera falta. Luego, 
# escribir una función o script que determine la proporción de predicciones 
# sobre el conjunto de testing que marcan como comestible un hongo venenoso.


# resolucion ? 2
from sklearn import datasets
iris = datasets.load_iris()

print(iris.data)
print(iris.target)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

import matplotlib.pyplot as plt

data = list(zip(iris.data[:,0],iris.data[:,1],iris.data[:,2],iris.data[:,3]))

kmeans = KMeans(n_clusters=4)
kmeans.fit(data)

plt.scatter(iris.data[:,0],iris.data[:,1],c=kmeans.labels_)
plt.show()


#otra forma
from collections import Counter
arr = [10, 15, 10, 5, 15, 20]
counts = Counter(arr)
print("Unique Values:", list(counts.keys()))
print("Counts:", list(counts.values()))



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = np.array([2, 5, 0, 1, 2, 1, 0, 0, 0, 1, 2, 3, 0])
F = np.bincount(A,minlength=7)

print(F) # [5 3 3 1 0 1 0]



from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Supongamos que X es tu dataset de puntos
inercia = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    inercia.append(kmeans.inertia_)  # Medimos la inercia

plt.plot(range(1, 10), inercia, marker='o')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inercia')
plt.title('Método del codo')
plt.show()



