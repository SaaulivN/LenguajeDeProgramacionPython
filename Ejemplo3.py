# IMPORTANDO RECURSOS
import numpy as np # Módulo para trabajar matrices 
import matplotlib.image as mpimg  # Para  leer imágenes
import matplotlib.pyplot as plt # Para mostrar imágenes
import cv2  # Libreria de visión por computadora

# OPERADOR INVERSO O NEGATIVO
image = mpimg.imread('imagenes/pulmones_radiografia.jpg') # Leer imagen a color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
negativo = 255 - gray 
f, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.set_title('Imagen original')
ax1.imshow(image, cmap='gray')
ax2.set_title('Imagen en grises')
ax2.imshow(gray, cmap='gray')
ax3.set_title('Imagen negativa')
ax3.imshow(negativo, cmap='gray')
plt.show()

# OPERADOR UMBRAL O BINARIZACION
image = mpimg.imread('imagenes/monedas.jpg') # Leer imagen a color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
_, binarizacion = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
f, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.set_title('Imagen original')
ax1.imshow(image, cmap='gray')
ax2.set_title('Imagen en grises')
ax2.imshow(gray, cmap='gray')
ax3.set_title('Imagen binarizada')
ax3.imshow(binarizacion, cmap='gray')
plt.show()

# TRANSFORMACION DE VECINDAD
image = mpimg.imread('imagenes/retrato.jpg') # Leer imagen a color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
mascara = np.array([[ -1, -2, -1], # mascara para obtener bordes horizontales
                    [ 0, 0, 0],
                    [ 1, 2, 1]])
transformada = cv2.filter2D(gray, -1, mascara)
f, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.set_title('Imagen original')
ax1.imshow(image, cmap='gray')
ax2.set_title('Imagen en grises')
ax2.imshow(gray, cmap='gray')
ax3.set_title('Imagen transformada')
ax3.imshow(transformada, cmap='gray')
plt.show()