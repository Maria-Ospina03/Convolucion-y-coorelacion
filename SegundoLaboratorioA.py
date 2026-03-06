# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 10:49:45 2026

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir las señales
h = np.array([5, 6, 0, 0, 9, 0, 1])
x = np.array([1, 0, 1, 3, 0, 0, 6, 4, 7, 6])

# Convolución
y = np.convolve(x, h)

# Mostrar resultado
print("Señal h[n]:", h)
print("Señal x[n]:", x)
print("Convolución y[n]:", y)

# Crear ejes de tiempo
n_h = np.arange(len(h))
n_x = np.arange(len(x))
n_y = np.arange(len(y))

# Graficar
plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.stem(n_h, h)
plt.title("Señal h[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(3,1,2)
plt.stem(n_x, x)
plt.title("Señal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(3,1,3)
plt.stem(n_y, y)
plt.title("Convolución y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()

plt.show()
