CAPACIDADM2 = 4
PORCENTAJEGRADAS = 0.2
PORCENTAJEESPECIALES = 0.3
PORCENTAJECOMUNES = 0.7

dimensiones = float(input("Dimensiones del estadio (en m2): "))
personasengradas = int(input("Cantidad de personas que caben en las gradas"))
porcentajeescenario = int(input("Porcentaje que ocupa el escenario:"))
m2gradas = dimensiones * PORCENTAJEGRADAS
m2escenario = dimensiones * (porcentajeescenario / 100)
m2disponibles = dimensiones - m2gradas - m2escenario
personastotales = (m2disponibles * 4) + personasengradas
print("Caben", personastotales, "personas")
precioentradaespecial = float(input("Precio entrada Especial:"))
precioentradacomun = float(input("Precio entrada Comun:"))
print("Ingreso total de ventas:", (personastotales * PORCENTAJEESPECIALES) * precioentradaespecial + (
        personastotales * PORCENTAJECOMUNES) * precioentradacomun)
