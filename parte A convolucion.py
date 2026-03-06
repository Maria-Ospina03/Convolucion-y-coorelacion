# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:31:25 2026

@author: pipe1
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir las señales
x = np.array([1, 0, 1, 6, 8, 3, 4, 4, 4, 8])
h = np.array([5, 6, 0, 0, 8, 8, 7])

# Convolución
y = np.convolve(x, h)

# Mostrar representación secuencial
print("Señal resultante y[n] = ")
print(y)

# Crear eje n
n = np.arange(len(y))

# Graficar señal resultante
plt.figure()
plt.stem(n, y)
plt.title("Convolución y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)

plt.show()