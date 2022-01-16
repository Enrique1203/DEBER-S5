# Ejercicio1
N = input("Tu nombre: ")
print("Ahora estas en la matrix, ", N)

# Ejercicio2
costo = float(input("Costo de la cena: $"))
servicio = costo * 0.062
propina = costo * 0.1
print("Costo total de la comida: $", costo + servicio + propina)

# Ejercicio3
dia = int(input("Dia de tu nacimiento:"))
mes = int(input("Mes de tu nacimiento:"))
anio = int(input("Año de tu nacimiento:"))
print(dia, "/", mes, "/", anio)

# Ejercicio4
fecha = int(input("Fecha en formato DDMMAAAA: "))
anio = fecha % 10000
dia = fecha // 1000000
mes = (fecha // 10000) % 100
print(dia, "/", mes, "/", anio)

# Ejercicio5
capacidad = float(input("Capacidad del Tanque:"))
kmxl = float(input("Rendimiento (km por litro):"))
recorrido = float(input("Km totales a recorrer: "))
kmxtanque = capacidad * kmxl
print("Seran necesarios", recorrido / kmxtanque, "tanques.")
