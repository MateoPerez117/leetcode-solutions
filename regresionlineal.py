import numpy as np
import matplotlib.pyplot as plt

# 1) Datos
x = np.array([2, 4, 6, 7, 10, 11, 14, 17, 20], dtype=float)
y = np.array([1, 2, 5, 2, 8, 7, 6, 9, 12], dtype=float)

n = len(x)

# 2) Sumatorias con for (como en tu práctica)
Sx = 0
Sy = 0

for i in range(n):
    Sx += x[i]
    Sy += y[i]

# 3) Arreglos auxiliares
xy = np.zeros(n)
x2 = np.zeros(n)
y2 = np.zeros(n)

for i in range(n):
    xy[i] = x[i] * y[i]
    x2[i] = x[i] ** 2
    y2[i] = y[i] ** 2

# 4) Sumatorias con numpy
Sxy = np.sum(xy)
Sx2 = np.sum(x2)
Sy2 = np.sum(y2)

# 5) Cálculo de la recta (mínimos cuadrados): y = a*x + b
a = (n * Sxy - Sx * Sy) / (n * Sx2 - (Sx ** 2))
b = (Sy - a * Sx) / n

# 6) Línea ajustada
y_fit = a * x + b

# 7) Imprimir resultados
print("RESULTADOS")
print("n =", n)
print("Sx =", Sx)
print("Sy =", Sy)
print("Sxy =", Sxy)
print("Sx2 =", Sx2)
print("Sy2 =", Sy2)
print("\nRecta final:")
print("a =", a)
print("b =", b)
print("y = a*x + b")

# 8) Gráfica
plt.scatter(x, y)
plt.plot(x, y_fit)
plt.title("Ajuste lineal (mínimos cuadrados)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()