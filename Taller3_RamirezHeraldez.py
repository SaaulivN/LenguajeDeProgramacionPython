# Ejercicio 1
print ("\n=== Ejercicio 1 ===\n")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
numTemp = 0

if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print ("\nEl número mayor es: ", num1)
    numTemp = num2
    print ("El número menor es: ", num3)
    print ("El número del medio es: ", num2)
elif num1 >= num2 and num1 >= num3 and num3 >= num2:
    print ("\nEl número mayor es: ", num1)
    numTemp = num3
    print ("El número menor es: ", num2)
    print ("El número del medio es: ", num3)
elif num2 >= num1 and num2 >= num3 and num1 >= num3:
    print ("\nEl número mayor es: ", num2)
    numTemp = num1
    print ("El número menor es: ", num3)
    print ("El número del medio es: ", num1)
elif num2 >= num1 and num2 >= num3 and num3 >= num1:
    print ("\nEl número mayor es: ", num2)
    numTemp = num3
    print ("El número menor es: ", num1)
    print ("El número del medio es: ", num3)
elif num3 >= num1 and num3 >= num2 and num1 >= num2:
    print ("\nEl número mayor es: ", num3)
    numTemp = num1
    print ("El número menor es: ", num2)
    print ("El número del medio es: ", num1)
elif num3 >= num1 and num3 >= num2 and num2 >= num1:
    print ("\nEl número mayor es: ", num3)
    numTemp = num2
    print ("El número menor es: ", num1)
    print ("El número del medio es: ", num2)
    
# Ejercicio 2
print ("\n=== Ejercicio 2 ===\n")
seg1 = int(input("Ingrese el primer segmento: "))
seg2 = int(input("Ingrese el segundo segmento: "))
seg3 = int(input("Ingrese el tercer segmento: "))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print ("Los segmentos ingresados forman un triángulo.\n")
else:
    print ("Los segmentos ingresados no forman un triángulo.\n")
    
# Ejercicio 3
print ("\n=== Ejercicio 3 ===\n")
contrasena = str(input("Ingrese la contraseña: "))

if len(contrasena) < 6 or len(contrasena) > 16:
    print("La contraseña debe tener entre 6 y 16 caracteres.\n")
elif not any(c.isalpha() for c in contrasena):
    print("La contraseña debe contener al menos una letra.\n")
elif not any(c.isdigit() for c in contrasena):
    print("La contraseña debe contener al menos un número.\n")
elif not any(c in "$#@" for c in contrasena):
    print("La contraseña debe contener al menos un carácter especial [$#@].\n")
else:
    print("Contraseña válida.\n")
    
# Ejercicio 4
print ("\n=== Ejercicio 4 ===\n")
salario = float(input("Ingrese el salario del usuario: ")) 
if salario < 10000:
    impuesto = salario * 0.05
    print("El impuesto es: ", impuesto, "\n")
elif salario >= 10000 and salario <= 20000:
    impuesto = salario * 0.15
    print("El impuesto es: ", impuesto, "\n")
elif salario >= 20000 and salario <= 35000:
    impuesto = salario * 0.20
    print("El impuesto es: ", impuesto, "\n")
elif salario >= 35000 and salario <= 60000:
    impuesto = salario * 0.30
    print("El impuesto es: ", impuesto, "\n")
elif salario > 60000:
    impuesto = salario * 0.45
    print("El impuesto es: ", impuesto, "\n")