numeros = [10, 10, 3, 11, 43, 43, 55, 77, 2, 1, 1, ]

mas_frecuentes = []
max_frecuencia = -1

for numero in numeros : 
    frecuencia = numeros.count(numero)
    if frecuencia > max_frecuencia : 
        max_frecuencia = frecuencia

for numero in numeros :
    if numeros.count(numero) == max_frecuencia :  
        if numero not in mas_frecuentes : 
            mas_frecuentes.append(numero)

print(mas_frecuentes)


