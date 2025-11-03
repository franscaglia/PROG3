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


