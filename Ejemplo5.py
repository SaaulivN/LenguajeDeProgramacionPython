# IMPORTANDO RECURSOS
import numpy as np # Módulo para trabajar matrices 
import matplotlib.image as mpimg  # Para  leer imágenes
import matplotlib.pyplot as plt # Para mostrar imágenes
import cv2  # Libreria de visión por computadora

# TRANSFORMACIONES GEOMÉTRICAS
image = cv2.imread('imagenes/camarografo.jpg',0) # Leer imagen a color
rows,cols = image.shape
M = np.float32([[1,0,100],[0,1,50]]) # desplazamiento en x: 100, en y: 50
traslated = cv2.warpAffine(image,M,(cols,rows)) # Transformacion de traslacion
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1) # cols-1 y rows-1 son los lImites de coordenada
rotated = cv2.warpAffine(image,M,(cols,rows)) # Transformacion de rotacion
scaled = cv2.resize(image,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC ) #Transformacion de escalado

# CONSTRUCCION DE LA GRAFICA
f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4) # Subplot para dos imágenes
ax1.set_title('Imagen original') # Imagen original
ax1.imshow(image, cmap='gray') # Mostrar imagen original
ax2.set_title('Imagen trasladada') # Imagen trasladada
ax2.imshow(traslated, cmap='gray') # Mostrar imagen trasladada
ax3.set_title('Imagen rotada') # Título imagen rotada
ax3.imshow(rotated, cmap='gray') # Mostrar imagen rotada
ax4.set_title('Imagen escalada') # Título imagen escalada
ax4.imshow(scaled, cmap='gray') # Mostrar imagen escalada
plt.show()

# REFERENCES
# https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html


