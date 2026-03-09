import math
# ====================================================================================
# ===== Ejemplos =====
# Ejemplo 1: 
def obtenerLongitud(cadena):
    longitud = 0
    for caracter in cadena:
        longitud += 1
    return longitud

#print(obtenerLongitud("Hola Mundo"))

# Ejemplo 2:
def sumaLista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    print(suma)

#sumaLista([1, 2, 3, 4, 5])

def areaCirculo(radio):
    area = math.pi * radio ** 2
    return area

#print(areaCirculo(5))
# ====================================================================================

# Ejercicio 1 - 
print("\n=== Ejercicio 1 ===\n")
def contarEspacios(cadena):
    contadorEspacios = 0
    for espacios in cadena:
        if espacios == " ":
            contadorEspacios += 1
    return contadorEspacios

cad = str(input("Ingresa una cadena: "))
print(contarEspacios(cad))

# Ejercicio 2 - 
print("\n=== Ejercicio 2 ===\n")
def volumenEsfera(radio):
    volumen = (4/3) * math.pi * radio**3
    return volumen

radio = int(input("Ingresa el radio: "))
print(volumenEsfera(radio))

# Ejercicio 3 - 
print("\n=== Ejercicio 3 ===\n")
def multiplicaLista(lista):
    multiplicacion = 1
    for numero in lista:
        multiplicacion *= numero
    return multiplicacion

print(multiplicaLista([1, 2, 3, 4]))

# Ejercicio 4 - 
print("\n=== Ejercicio 4 ===\n")
def factorial(n):
    resultado = 1
    for numero in range(1, n + 1):
        resultado *= numero
        numero -= 1
    return resultado

numero = int(input("Factorial de: "))
print(factorial(numero))
print('\n')

# Ejercicio 5 -

def dibujaCuadricula():
    print("\n=== Ejercicio 5 ===\n")
    for i in range(2):
        print("+ - - - -  + - - - -  +")
        for j in range(4):
            print("|          |          |")
    print("+ - - - -  + - - - -  +\n")

print(dibujaCuadricula())
# ====================================================================================
