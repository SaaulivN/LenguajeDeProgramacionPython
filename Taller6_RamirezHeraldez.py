#------------------------ Apartado de funciones -----------------------------
# Función para convertir archivos a listas
def convertirArchivoALista(archivo):
    txt = open(archivo, "r")
    lista = []
    for linea in txt:
        lista.extend(linea.split())
    txt.close()
    return lista

# Función para convertir una lista a minúsculas con el tema de comprensión de listas
def limpiarLista(lista):
    listaEnMinusculas = [palabra.strip(".,\n\t").lower() for palabra in lista]
    return listaEnMinusculas

def obtenerFrecuencia(par):
    return par[1]

#----------------------------------------------------------------------------


listaDePalabrasVacias = convertirArchivoALista("palabras_vacias.txt")
listaDelTexto = convertirArchivoALista("texto.txt")

listaDelTextoEnMinusculas = limpiarLista(listaDelTexto)

listaSinPalabrasVacias = [palabra for palabra in listaDelTextoEnMinusculas if palabra not in listaDePalabrasVacias]

contadorDePalabras = {}
for palabra in listaSinPalabrasVacias:
    if palabra in contadorDePalabras:
        contadorDePalabras[palabra] += 1
    else:
        contadorDePalabras[palabra] = 1
palabrasPorOcurrencia = sorted(contadorDePalabras.items(), key = obtenerFrecuencia, reverse=True)

palabrasImportantes = open("palabras_importantes.txt", "w")
for palabra, ocurrencia in palabrasPorOcurrencia:
    linea = f"{palabra}, {ocurrencia}\n"   
    palabrasImportantes.write(linea)

print(palabrasImportantes.read())
palabrasImportantes.close()

# f = open("palabras_importantes.txt", "r")
# print(f.read())
# f.close()