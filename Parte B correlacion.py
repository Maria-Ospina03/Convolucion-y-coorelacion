# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:18:48 2026

@author: pipe1
"""
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parámetros
# =========================
Ts = 1.25e-3        # 1.25 ms
n = np.arange(0, 9) # 0 ≤ n < 9

# =========================
# Definición de señales
# =========================
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)

# =========================
# Correlación cruzada
# =========================
r = np.correlate(x1, x2, mode='full')

# Eje de retardos
lags = np.arange(-len(x1)+1, len(x1))

# =========================
# Representación secuencial
# =========================
print("Correlación cruzada r_x1x2[k] =")
print(r)

# =========================
# Representación gráfica
# =========================
plt.figure()
plt.stem(lags, r)
plt.title("Correlación cruzada entre x1[n] y x2[n]")
plt.xlabel("Retardo k")
plt.ylabel("r_x1x2[k]")
plt.grid(True)
plt.show()