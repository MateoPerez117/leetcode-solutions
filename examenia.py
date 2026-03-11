
import numpy as np

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

transpuesta = []

for j in range(len(matriz[0])):   
    nueva_fila = []
    
    for i in range(len(matriz)): 
        nueva_fila.append(matriz[i][j])
    
    transpuesta.append(nueva_fila)

print("\nMatriz transpuesta:")

for fila in transpuesta:
    print(fila)

            