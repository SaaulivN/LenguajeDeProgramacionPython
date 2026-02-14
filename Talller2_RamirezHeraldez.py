# ----- TALLER 2 -----

# Ejercicio 1: Contar las consonantes de una cadena, por ejemplo, para la cadena materia = ‘lenguaje
# de programacion python’ la respuesta debe ser 17.
print("\nEjercicio 1")
materia = 'lenguaje de programacion python'
count_Consonantes = 0
for letter in materia:
    if letter != 'a' and letter != "e" and letter != 'i' and letter != 'o' and letter != 'u' and letter != ' ' :
        count_Consonantes = count_Consonantes + 1
print(count_Consonantes)
print("\n")

# Ejercicio 2: Tomar una lista de listas de enteros y sumar los elementos de todas las listas anidadas, 
# por ejemplo, para la lista enteros = [[1, 2], [3], [4, 5, 6]] el resultado debe ser 21.
print("Ejercicio 2")
suma = 0
enteros = [[1, 2], [3], [4, 5, 6]]
for sublista in enteros:
    for entero in sublista:
        suma += entero
print(suma)

# Ejercicio 3: Procesar una cadena y generar un diccionario con sus palabras y números de vocales,
# por ejemplo, para la cadena escuela = ‘universidad autonoma de baja california’ la
# respuesta debe ser dicc = {‘universidad’:5, ‘autonoma’:5, ‘de’:1, ‘baja’:2, ‘california’:5}.
print("\nEjercicio 3")
universidad = 'universidad autonoma de baja california'
vocales = "aeiou"
diccionario = {}
palabras = universidad.split()

for palabra in palabras:
    contador = 0 
    for letra in palabra:
        if letra in vocales:
            contador += 1 
    diccionario[palabra] = contador

print(diccionario)

# Ejercicio 4
# Tomar una cadena y determinar si se trata de un palíndromo, el cual, es una palabra que
# se escribe igual al derecho y al revés, por ejemplo, para la cadena palabra = ‘reconocer’
# la respuesta debe ser true y para la cadena palabra = ‘reyes’ la respuesta debe ser false.
print("\nEjercicio 4")
palabra = "reconocer"
palabraInvertida = palabra[::-1]

if palabra == palabraInvertida:
    print("true")
else:
    print("false")
    
# Ejercicio 5
# Procesar la lista enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e imprimir sólo los números
# primos, los cuales sólo son divisibles entre sí mismos y la unidad, para este ejemplo la
# respuesta debe ser 2, 3, 5 y 7.
print("\nEjercicio 5")
listaEnteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaPrimos = [] 

for caracter in listaEnteros:
    numero = int(caracter)
    if numero > 1:
        es_primo = True
        for dividendo in range (2, numero):
            if numero % dividendo == 0:
                es_primo = False
                
        if es_primo:
            listaPrimos += str(numero)
        
print(listaPrimos)
  

    

