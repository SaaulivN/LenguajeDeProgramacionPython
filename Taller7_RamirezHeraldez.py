# IMPORTANDO RECURSOS
import numpy as np # Módulo para trabajar matrices 
import matplotlib.image as mpimg  # Para  leer imágenes
import matplotlib.pyplot as plt # Para mostrar imágenes
import cv2  # Libreria de visión por computadora

# EJERCICIO 1

marioPixel = np.array([[255, 255, 255, 255, 255, 255, 80, 80, 80, 80, 80, 255, 255, 170, 170, 170, 255],
                       [255, 255, 255, 255, 255, 80, 80, 80, 80, 80, 80, 80, 80, 80, 170, 170, 255],
                       [255, 255, 255, 255, 255, 80, 80, 80, 170, 170, 0, 170, 255, 80, 80, 80, 255],
                       [255, 255, 255, 255, 80, 170, 80, 170, 170, 170, 0, 170, 170, 170, 80, 80, 255],
                       [255, 255, 255, 255, 80, 170, 80, 80, 170, 170, 170, 0, 170, 170, 170, 80, 255],
                       [255, 255, 255, 255, 80, 80, 170, 170, 170, 170, 0, 0, 0, 0, 80, 255, 255],
                       [255, 255, 255, 255, 255, 255, 170, 170, 170, 170, 170, 170, 170, 80, 80, 255, 255],
                       [170, 170, 170, 80, 80, 80, 80, 40, 80, 80, 80, 40, 80, 80, 255, 255, 80],
                       [170, 170, 170, 80, 80, 80, 80, 80, 40, 80, 80, 80, 40, 255, 255, 80, 80],
                       [255, 170, 255, 255, 255, 80, 80, 80, 40, 40, 40, 40, 130, 40, 40, 80, 80],
                       [255, 255, 255, 255, 255, 255, 40, 40, 40, 130, 40, 40, 40, 40, 40, 80, 80],
                       [255, 255, 255, 255, 80, 80, 40, 40, 40, 40, 40, 40, 40, 40, 40, 80, 80],
                       [255, 255, 255, 80, 80, 80, 40, 40, 40, 40, 40, 40, 255, 255, 255, 255, 255],
                       [255, 255, 255, 80, 80, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]])

plt.matshow(marioPixel, cmap='gray')
plt.show()

# EJERCICIO 2

rgb = mpimg.imread('imagenes/RGB.jpg') # Leer imagen a color

r = rgb[:,:,0]
g = rgb[:,:,1]
b = rgb[:,:,2]

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
ax1.set_title('Imagen original')
ax1.imshow(rgb)

ax2.set_title('Imagen Rojos')
ax2.imshow(r, cmap='gray')

ax3.set_title('Imagen Verdes')
ax3.imshow(g, cmap='gray')

ax4.set_title('Imagen Azules')
ax4.imshow(b, cmap='gray')

plt.show()

# EJERCICIO 3

silueta = mpimg.imread('imagenes/silueta.jpg')
gray = cv2.cvtColor(silueta, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
_, umbral = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
negativo = 255 - umbral
f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.set_title('Imagen original')
ax1.imshow(silueta, cmap='gray')

ax2.set_title('Imagen en grises')
ax2.imshow(gray, cmap='gray')

ax3.set_title('Imagen con umbral')
ax3.imshow(negativo, cmap='gray')

plt.show()

# EJERCICIO 4

monedasConRuido = mpimg.imread('imagenes/monedas_ruido.jpg') # Leer imagen a color
gray = cv2.cvtColor(monedasConRuido, cv2.COLOR_RGB2GRAY) # Cambiar imagen a color a grises
suavizado3x3 = cv2.medianBlur(gray, 3)
suavizado5x5 = cv2.medianBlur(gray, 5) 

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(1, 4))
ax1.set_title('Original (Gris)')
ax1.imshow(gray, cmap='gray')
ax2.set_title('Mediana 3x3')
ax2.imshow(suavizado3x3, cmap='gray')
ax3.set_title('Mediana 5x5')
ax3.imshow(suavizado5x5, cmap='gray')
ax4.set_title('Original Color')
ax4.imshow(monedasConRuido)

# EJERCICIO 5

retrato = mpimg.imread('imagenes/retrato.jpg')
gray = cv2.cvtColor(retrato, cv2.COLOR_RGB2GRAY)
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])
sobel = sobel_x + sobel_y
retratoSobel = cv2.filter2D(gray, -1, sobel)

prewitt_x = np.array([[-1, 0, 1],
                      [-1, 0, 1],
                      [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1],
                      [ 0,  0,  0],
                      [ 1,  1,  1]])
prewitt = prewitt_x + prewitt_y
retratoPrewitt = cv2.filter2D(gray, -1, prewitt)

roberts_x = np.array([[1,  0],
                      [0, -1]])
roberts_y = np.array([[ 0, 1],
                      [-1, 0]])
roberts = roberts_x + roberts_y
retratoRoberts = cv2.filter2D(gray, -1, roberts)

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
ax1.set_title('Grises')
ax1.imshow(gray, cmap='gray')
ax2.set_title('Sobel')
ax2.imshow(retratoSobel, cmap='gray')
ax3.set_title('Prewitt')
ax3.imshow(retratoPrewitt, cmap='gray')
ax4.set_title('Roberts')
ax4.imshow(retratoRoberts, cmap='gray')
plt.show()

# EJERCICIO 6

camarografo = mpimg.imread('imagenes/camarografo.jpg')
gray = cv2.cvtColor(camarografo, cv2.COLOR_RGB2GRAY)
rows,cols = gray.shape
M = np.float32([[1,0,75],[0,1,75]])
trasladada = cv2.warpAffine(camarografo,M,(cols,rows))
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),315,1)
rotada = cv2.warpAffine(trasladada,M,(cols,rows))
terminada = cv2.resize(rotada,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC )


f, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title('Original')
ax1.imshow(camarografo, cmap='gray')
ax2.set_title('terminada')
ax2.imshow(terminada, cmap='gray')

plt.show()