# IMPORTANDO RECURSOS
import numpy as np # Módulo para trabajar matrices 
import matplotlib.image as mpimg  # Para  leer imágenes
import matplotlib.pyplot as plt # Para mostrar imágenes
import cv2  # Libreria de visión por computadora

# LEER Y MOSTRAR LA IMAGEN
image = mpimg.imread('imagenes/waymo_car.jpg') # Leer imagen a color
plt.figure() # Crear figura para imagen a color.
plt.imshow(image) # Preparar imagen a color
plt.show() # Mostrar imagen a color
print('Dimensiones de imagen:', image.shape) # Dimensiones de imagen a color
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
plt.figure() # Crear figura para imagen en grises
plt.imshow(gray_image, cmap='gray') # Preparar imagen en grises
plt.show() # Mostrar imagen en grises
print('Dimensiones de imagen:', gray_image.shape) # Dimensiones de imagen en grises

# IMPRIMIR VALOR ESPECÍFICO DE PIXEL
x = 400 # Columna
y = 300 # Renglon
print(gray_image[y,x])

# VALORES DE GRIS MÁXIMO Y MÍNIMO
max_val = np.amax(gray_image)
min_val = np.amin(gray_image)
print('Max: ', max_val)
print('Min: ', min_val)

# CREANDO IMAGEN DE 5X5 USANDO VALORES EN ESCALA DE GRISES
tiny_image = np.array([[0, 20, 30, 150, 120],
                      [200, 200, 250, 70, 3],
                      [50, 180, 85, 40, 90],
                      [240, 100, 50, 255, 10],
                      [30, 0, 75, 190, 220]])
plt.matshow(tiny_image, cmap='gray') # Mostrar cuadrícula usando matshow
plt.show()

# CREA TU PROPIA IMAGEN Y MUÉSTRALA