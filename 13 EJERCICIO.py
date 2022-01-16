# Ejercicio1
cantidad = 0
n = int(input("Numero:"))
while n != 0:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        cantidad += 1
    n = int(input("Numero:"))
print("Primos:", cantidad)
# Ejercicio2
anioInicio = int(input("Año Inicial:"))
anioFin = int(input("Año Final:"))
for anio in range(anioInicio, anioFin + 1):
    if anio % 10 == 0:
        if anio % 4 == 0:
            if anio % 100 != 0 or anio % 400 == 0:
                print(anio)
