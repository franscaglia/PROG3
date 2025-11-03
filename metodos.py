import math

def promedio(vector):
    return sum(vector) / len(vector)

def raizCuadrada(numero): 
    return math.sqrt(numero)

def varianza(vector):
    sumatoria = 0
    media = promedio(vector)
    n = len(vector)

    for i in range(n):
        sumatoria += (vector[i] - media)**2
    
    return sumatoria / n

def distanciaEuclidiana(puntoA, puntoB):
    sumatoria = 0
    n = len(puntoA)

    for i in range(n):
        sumatoria += (puntoA[i] - puntoB[i] )**2

    return raizCuadrada(sumatoria)