# IMPORTANDO RECURSOS
import numpy as np # Módulo para trabajar matrices 
import matplotlib.image as mpimg  # Para  leer imágenes
import matplotlib.pyplot as plt # Para mostrar imágenes
import cv2  # Libreria de visión por computadora

# SUAVIZADO DE IMÁGENES, PROMEDIADO DEL ENTORNO DE VECINDAD
image = mpimg.imread('imagenes/camarografo.jpg') # Leer imagen a color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen de color a grises
mascara = np.array([[ 1/9, 1/9, 1/9], # mascara para promediado del entorno de vecindad
                    [ 1/9, 1/9, 1/9],
                    [ 1/9, 1/9, 1/9]])
transformada = cv2.filter2D(gray, -1, mascara) # Convolución de imagen con mascara
f, (ax1, ax2) = plt.subplots(1, 2) # Subplot para dos imágenes
ax1.set_title('Imagen gris') # Título imagen 1
ax1.imshow(gray, cmap='gray') # Mostrar imagen 1
ax2.set_title('Mascara 1/9') # Título imagen 2
ax2.imshow(transformada, cmap='gray') # Mostrar imagen 2
plt.show()

# Ejercicio: agrega dos imágenes, una usando la siguiente mascara 
# y otra haciendo un promediado de un entorno de vecindad de 5x5
# mascara = (1/16)*np.array([[ 1, 2, 1]
#                            [ 2, 4, 2],
#                            [ 1, 2, 1]])

# SUAVIZADO DE IMÁGENES, FILTRADO DE LA MEDIANA
image = mpimg.imread('imagenes/monedas_ruido.jpg') # Leer imagen a color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
transformada = cv2.medianBlur(gray, ksize=3) # Filtrado de la mediana con vecindad de 3x3
f, (ax1, ax2) = plt.subplots(1, 2) # Subplot para dos imágenes
ax1.set_title('Imagen gris') # Título imagen 1
ax1.imshow(gray, cmap='gray') # Mostrar imagen 1
ax2.set_title('Filtrado de la mediana 3x3') # Título imagen 2
ax2.imshow(transformada, cmap='gray') # Mostrar imagen 2
plt.show()

# Ejercicio: agrega dos imágenes, una usando un filtrado de la 
# mediana con vecindad de 5x5 y otra usando una vecindad de 7x7


# EXTRACCIÓN DE BORDES, OPERADORES DE SOBEL
image = mpimg.imread('imagenes/retrato.jpg') # Leer imagen a color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
mascarah = np.array([[ -1, -2, -1], # mascara para obtener bordes horizontales
                    [ 0, 0, 0],
                    [ 1, 2, 1]])
mascarav = np.array([[ 1, 0, -1], # mascara para obtener bordes verticales
                    [ 2, 0, -2],
                    [ 1, 0, -1]])
transformadah = cv2.filter2D(gray, -1, mascarah) # Obteniendo bordes horizontales
transformadav = cv2.filter2D(gray, -1, mascarav) # Obteniendo bordes verticales
f, (ax1, ax2, ax3) = plt.subplots(1, 3) # Subplot para tres imágenes
ax1.set_title('Imagen gris') # Título imagen 1
ax1.imshow(gray, cmap='gray') # Mostrar imagen 2
ax2.set_title('Bordes horizontales') # Título imagen 2
ax2.imshow(transformadah, cmap='gray') # Mostrar imagen 2
ax3.set_title('Bordes verticales') # Título imagen 3
ax3.imshow(transformadav, cmap='gray') # Mostrar imagen 3
plt.show()

# Ejercicio: agrega dos imágenes extendiendo los operadores de Sobel para un 
# entorno de vecindad de 5x5.

#OBTENIENDO EL HISTOGRAMA DE IMAGEN
monedas = cv2.imread('imagenes/monedas.jpg',0) # Leer imagen original
brillantes = cv2.imread('imagenes/monedas_brillantes.jpg',0) # Leer imagen con aumento de brillo
oscuras = cv2.imread('imagenes/monedas_oscuras.jpg',0) # Leer imagen con disminución de brillo
contraste = cv2.imread('imagenes/monedas_contraste.jpg',0) # Leer imagen con disminución de contraste
hist_monedas = cv2.calcHist([monedas],[0],None,[255],[0,255]) # Creando histograma de monedas originales
hist_brillantes = cv2.calcHist([brillantes],[0],None,[255],[0,255]) # Creando histograma de monedas brillantes 
hist_oscuras = cv2.calcHist([oscuras],[0],None,[255],[0,255]) # Creando histograma de monedas oscuras
hist_contraste = cv2.calcHist([contraste],[0],None,[255],[0,255]) # Creando histograma de monedas con bajo contraste
plt.subplot(241), plt.title('Original'), plt.imshow(monedas, 'gray'), # Mostrando monedas originales
plt.subplot(242), plt.title('Aumento brillo'), plt.imshow(brillantes,'gray') # Mostrando monedas brillantes
plt.subplot(243), plt.title('Disminucion brillo'), plt.imshow(oscuras,'gray') # Mostrando monedas oscuras
plt.subplot(244), plt.title('Disminucion contraste'), plt.imshow(contraste,'gray') # Mostrando monedas poco contraste
plt.subplot(245), plt.plot(hist_monedas) # Mostrando histograma monedas originales
plt.subplot(246), plt.plot(hist_brillantes) # Mostrando histograma monedas brillantes
plt.subplot(247), plt.plot(hist_oscuras) # Mostrando histograma monedas oscuras
plt.subplot(248), plt.plot(hist_contraste) # Mostrando histograma monedas poco contraste
plt.xlim([0,256])
plt.show()

# Ejercicio: Haz una copia de la imagen monedas, auméntale el contraste 
# y muéstrala junto con su histograma en la gráfica. 