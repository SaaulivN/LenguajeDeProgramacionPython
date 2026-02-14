# Ejercicio 1
# 42 = n
    
# Ejercicio 2
print ("\nEjercicio 2")
x = y = 1
print (x, y)

# Ejercicio 3
print ("\nEjercicio 3")

# Ejercicio 4
#print ("Ejercicio 4").

# Ejercicio 5
print ("\nEjercicio 5")
pi = 3.1416
r = 5
volumen = (4/3) * pi * (r*r*r)
print ("El volumen de la esfera es: ", volumen)

# Ejercicio 6
print ("\nEjercicio 6")
CostoLibro = 24.95
Descuento = 0.4
CostoFinalPorLibro = CostoLibro - (CostoLibro * Descuento)

CostoEnvioPrimerLibro = 3
CostoEnvioLibrosAdicionales = 0.75

TotalPrimerLibro = CostoFinalPorLibro + CostoEnvioPrimerLibro
TotalLibrosAdicionales = (CostoFinalPorLibro + CostoEnvioLibrosAdicionales) * 59
Total = TotalPrimerLibro + TotalLibrosAdicionales
print ("El costo total de los 60 libros es: ", Total)

# Ejercicio 7
print ("\nEjercicio 7")
Salida = 6 * 60 + 52

PrimerCardio = 8 * 60 + 30
SegundoCardio = (7 * 60 + 20) * 3
TercerCardio = 8 * 60 + 30
TotalCardio = TotalCardioSegundos // 60

Llegada = Salida + TotalCardio

print ("El tiempo total de cardio fue de: ", TotalCardio, "minutos")
HoraLlegada = Llegada // 60
MinutosLlegada = Llegada % 60
print ("La hora de llegada es: ", HoraLlegada, ":", MinutosLlegada)

