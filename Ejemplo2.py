# IMPORTANDO RECURSOS
import matplotlib.pyplot as plt # Para mostrar imágenes
import matplotlib.image as mpimg # Para leer imágenes

# LEER UNA IMAGEN
image = mpimg.imread('imagenes/opencv.jpg') # Leer imagen a color
plt.figure() # Crear figura para imagen a color
plt.imshow(image) # Preparar imagen a color
plt.show() # Mostrar imagen a color

# SEPARANDO CANALES RGB
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

plt.figure() # Crear figura para canal rojo
plt.imshow(r,cmap='gray') # Preparar imagen para canal rojo
plt.show() # Mostrar imagen del canal rojo

plt.figure() # Crear figura para canal verde
plt.imshow(g,cmap='gray') # Preparar imagen para canal verde
plt.show() # Mostrar imagen del canal verde

plt.figure() # Crear figura para canal azul
plt.imshow(b,cmap='gray') # Preparar imagen para canal azul
plt.show() # Mostrar imagen del canal azul

# CUÁL ES EL VALOR MÁXIMO Y MÍNINO DE CADA CANAL