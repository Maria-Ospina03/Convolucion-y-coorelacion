# Convolucion-y-coorelacion
## Segundo Laboratorio, procesamiento digital de señales

**Maria Camila Ospina Jara, Juan Felipe Serna Alarcón**

### Descripción
Esta práctica de laboratorio se centra en la aplicación de la convolución para determinar la respuesta de sistemas discretos, la correlación para medir la similitud entre señales y la Transformada de Fourier para el análisis espectral en el dominio de la frecuencia. 

### Introducción
En el análisis de señales y sistemas, existen operaciones matemáticas que permiten estudiar cómo se relacionan diferentes funciones o señales. Dos de las más importantes son la convolución y la correlación, las cuales se utilizan para analizar la interacción y similitud entre señales.

La convolución es una operación que combina dos funciones para describir su superposición. Este proceso consiste en desplazar una de las funciones sobre la otra, multiplicar sus valores en los puntos donde coinciden y sumar los productos obtenidos para generar una nueva función. Por otro lado, la correlación permite medir el grado de similitud entre dos señales cuando una se desplaza respecto a la otra.

Estas herramientas son ampliamente utilizadas en el procesamiento de señales, ya que permiten comprender mejor el comportamiento de los sistemas y la relación entre distintas señales.

### Desarrollo de la práctica 
## Parte A
Para ésta sección se crearon los sistemas h(n) y x(n), siendo h(n) los digitos del codigo de estudiante y x(n) los digitos del numero de cedula, con esto se encontró la señal y(n) resultante de la convolución de las dos señales, de la cual se obtuvo su representación gráfica y secuencial. Ésto se hizo a mano y programando en python, este apartado se realizo para todos los integrantes del grupo.

### Sección de código donde se hace la convolucion

```python

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

```

#### Diagrama de flujo general del código :
![Diagrama de flujo del código](2ParteA.png)

```python

# Definir las señales
h = np.array([5, 6, 0, 0, 9, 0, 1])
x = np.array([1, 0, 1, 3, 0, 0, 6, 4, 7, 6])

```

#### Gráfico (Camila Ospina)
![Diagrama de flujo del código](2senalA.png)


Representación secuencial: Señal resultante y[n] = 
[ 5  6  5 21 27  0 40 83 60 75 90 36 69 58  7  6]


```python 
# Definir las señales
x = np.array([1, 0, 1, 6, 8, 3, 4, 4, 4, 8])
h = np.array([5, 6, 0, 0, 8, 8, 7])
```

#### Gráfico (Juan Serna)
<img width="540" height="387" alt="image" src="https://github.com/user-attachments/assets/ca47eadb-8214-4887-b0b6-33866ac589ab" />



Representación secuencial: Señal resultante y[n] = 
[  5   6   5  36  84  71  53 100 163 194 160  85  92 124  92  56]



Ahora se hace la convolución a mano por cada integrante del grupo.

#### Manual (Camila Ospina): 
<img width="692" height="948" alt="image" src="https://github.com/user-attachments/assets/4b242ea9-0cd7-4554-b205-0eeae3d5e721" />


#### Manual (Juan Serna):
<img width="552" height="720" alt="image" src="https://github.com/user-attachments/assets/261590bd-724a-4780-9660-2c1eb55b713b" />




## Parte B
En este apartado se busco encontrar la correlación cruzada de 2 señales estipuladas :

<img width="371" height="72" alt="image" src="https://github.com/user-attachments/assets/309baa57-fe24-4448-9e4e-fa2408ba89ec" />


mostrando su representación gráfica y secuencial por medio de python teniendo encuenta los parametros dados.


#### Diagrama de flujo general del código :

![Diagrama de flujo parte B](2ParteB.png)

```python

# Parámetros
Ts = 1.25e-3        # 1.25 ms
n = np.arange(0, 9) # 0 ≤ n < 9
# =========================
# Definición de señales
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)
# =========================
# Correlación cruzada
r = np.correlate(x1, x2, mode='full')

# Eje de retardos
lags = np.arange(-len(x1)+1, len(x1))

# =========================
# Representación secuencial
print("Correlación cruzada r_x1x2[k] =")
print(r)

```
La correlacion resultante entre las 2 señales definidas fue

r x1 x2 [k] =

[-2.44929360e-16 -7.07106781e-01 -1.50000000e+00 -1.41421356e+00
 -1.66533454e-16  2.12132034e+00  3.50000000e+00  2.82842712e+00
  8.81375476e-17 -2.82842712e+00 -3.50000000e+00 -2.12132034e+00
  3.33066907e-16  1.41421356e+00  1.50000000e+00  7.07106781e-01
  0.00000000e+00]

Descripción de la secuencia: Inicia con valores muy cercanos a cero los cuales van disminuyendo hasta valores negativos y esto cambia progresivamente al luego los valores ser números positivos, siendo esto un ciclo que se repite 2 veces antes de que la señal vuelva a dar cero, teniendo como dato que mas se repite el cero o valores cercanos al mismo.

¿En qué situaciones resulta útil aplicar la correlación cruzada en 
el procesamiento digital de señales? 

Es útil en los ámbitos de detección de señales que es saber si una señal está contenida dentro de otra ( ejemplo los radares, comunicaciones), otro campo seria la estimación de retardo lo cual es calcular cuánto está desplazada una señal respecto a otra ( ejemplo micrófonos al determinar dirección del sonido o los GPS que cálculan el tiempo de llegada). Tambien esta la medición de similitud para determinar qué tan parecidas son dos señales.

Para la representación grafica:

```python

plt.figure()
plt.stem(lags, r)
plt.title("Correlación cruzada entre x1[n] y x2[n]")
plt.xlabel("Retardo k")
plt.ylabel("r_x1x2[k]")
plt.grid(True)
plt.show()

```

<img width="527" height="382" alt="image" src="https://github.com/user-attachments/assets/e0bd2a6b-8547-4459-aa83-3a3c7dea093e" />


## Parte C
En este apartado con ayuda del generador de señales biológicas se guardo una señal de un electrooculograma la cual se digitalizo con una frecuancia de muestreo de aproximadamente 909 hz, con la cual se caracterizo para obtener su media, mediana, desviación estándar, máximo, mínimo y al ser una señal fisiologica bioelectrica se puede decir que es aleatoria y aperiodica, aunque su forma si puede seguir ciertos patrones no es igual en todos los casos y aunque naturalmente es analogica a la hora de estudiarse se vuelve digital con la frecuencia de muestreo. Posteriormente se le aplico la transformada de fourier y se grafico tanto su transformada como su densidad espectral de potencia y luego se encontro la frecuencia media, frecuencia mediana, desviación estándar, histograma de frecuencias.


#### Diagrama de flujo general del codigo


<img width="1806" height="3688" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/2d420f07-1e75-417e-a7af-49619a1e16fe" />



En el codigo la señal guardada se puede observar asi:


<img width="936" height="495" alt="image" src="https://github.com/user-attachments/assets/c3fc9f7d-d3c1-47cf-a9f9-7627bc650d71" />

----Esta señal tiene unos estadisticos de 

Media: 0.10335489650533682

Mediana: 0.129795987041573

Desviacion estandar: 0.39196472592570697

Valor minimo: -0.5404063721695511

Valor maximo: 0.8431046115824024




Su transformada de Fourier se ve asi:


<img width="757" height="578" alt="image" src="https://github.com/user-attachments/assets/a5ed6b85-10a8-4d33-b683-a4edce1baf43" />

```python

            fft_vals = np.fft.rfft(senal)
            freqs = np.fft.rfftfreq(N, 1/fs)

            magnitud = np.abs(fft_vals) / N

            # ===== GRAFICAR TRANSFORMADA =====
            fig_fft = Figure()
            ax_fft = fig_fft.add_subplot(111)
            canvas_fft = FigureCanvas(fig_fft)

            ax_fft.plot(freqs, magnitud)
            ax_fft.set_title("Transformada de Fourier (FFT)")
            ax_fft.set_xlabel("Frecuencia (Hz)")
            ax_fft.set_ylabel("Magnitud")
            ax_fft.set_xlim(0, 12)
            ax_fft.grid(True)

            canvas_fft.show()
```



Su densidad espectral de potencia se ve asi:


<img width="740" height="586" alt="image" src="https://github.com/user-attachments/assets/382b3746-9acc-44a2-a822-dab7f925d477" />

```python
            psd = (1/(fs*N)) * (np.abs(fft_vals)**2)

            fig_psd = Figure()
            ax_psd = fig_psd.add_subplot(111)
            canvas_psd = FigureCanvas(fig_psd)

            ax_psd.plot(freqs, psd)
            ax_psd.set_title("Densidad Espectral de Potencia (PSD)")
            ax_psd.set_xlabel("Frecuencia (Hz)")
            ax_psd.set_ylabel("Potencia")
            ax_psd.set_xlim(0, 10)
            ax_psd.grid(True)

            canvas_psd.show()
```





y su histograma de frecuencias se ve asi:


<img width="756" height="585" alt="image" src="https://github.com/user-attachments/assets/36b74b10-28b5-4cda-8653-4875bfede0a5" />


```python

            fig_hist_f = Figure()
            ax_hist_f = fig_hist_f.add_subplot(111)
            canvas_hist_f = FigureCanvas(fig_hist_f)

            # Limitar frecuencias a 0-10 Hz (rango típico EOG)
            mask = freqs <= 10
            freqs_eog = freqs[mask]
            psd_eog = psd[mask]

            ax_hist_f.hist(freqs_eog, bins=20, weights=psd_eog)

            ax_hist_f.set_title("Histograma de Frecuencias (0–10 Hz)")
            ax_hist_f.set_xlabel("Frecuencia (Hz)")
            ax_hist_f.set_ylabel("Potencia")
            ax_hist_f.set_xlim(0,10)
            ax_hist_f.grid(True)

            canvas_hist_f.show()
```

Sus estadisticas en el dominio de la frecuencia fueron:


Frecuencia media: 1.6234659751739906 Hz

Frecuencia mediana: 1.3343923749007147 Hz

Desviacion estandar espectral: 1.4154599027701842 Hz


```python
            # Potencia total
            potencia_total = np.sum(psd)

            # Frecuencia media
            frecuencia_media = np.sum(freqs * psd) / potencia_total

            # Frecuencia mediana
            potencia_acumulada = np.cumsum(psd)
            frecuencia_mediana = freqs[np.where(potencia_acumulada >= potencia_total/2)[0][0]]

            # Desviación estándar espectral
            varianza_freq = np.sum(((freqs - frecuencia_media)**2) * psd) / potencia_total
            desviacion_freq = np.sqrt(varianza_freq)

            print("----- ANALISIS EN FRECUENCIA -----")
            print("Frecuencia media:", frecuencia_media, "Hz")
            print("Frecuencia mediana:", frecuencia_mediana, "Hz")
            print("Desviacion estandar espectral:", desviacion_freq, "Hz")
```


### Análisis

## Referencias
[1] M. Wyant, “Convolución,” MATLAB & Simulink. https://la.mathworks.com/discovery/convolution.html
[2] E. De Redacción De La Universidad Internacional De La Rioja, “¿Qué es un análisis de correlación? Características y Ejemplos,” UNIR México, Feb. 21, 2024. [Online]. Available: https://mexico.unir.net/noticias/economia/analisis-correlacion/
