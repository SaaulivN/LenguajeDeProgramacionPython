# Ejercicio 1 - fibonacci
print ("\n=== Ejercicio 1 ===\n")
n = int(input("Ingrese el número de términos: "))
fibonacci = []
a = 0
b = 1

while len(fibonacci) < n:
    fibonacci.append(a)
    temp = a
    a = b
    b = temp + b

print(fibonacci)

# Ejercicio 2 - Conversion
print ("\n=== Ejercicio 2 ===\n")
binario = input("Ingrese un número binario: ")
decimal = 0
exponente = 0

for bit in binario[::-1]:
    if bit == '1':
        decimal += 2 ** exponente
    exponente += 1

print("La conversión a decimal es: ")
print(decimal)

# Ejercicio 3 - Multiplicación de matrices
print ("\n=== Ejercicio 3 ===\n")
A = [[1, 2], [4, 5], [7, 8]]
B = [[1, 2, 3], [0, 5, 2]]

resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        k = 0
        while k < len(B):
            resultado[i][j] += A[i][k] * B[k][j]
            k += 1

print("Resultado de A x B:")  
print(resultado)
print("\n")