def cargarnombres(alumnos):
    nombre = input("Nombre:")
    while nombre != "x":
        alumnos.add(nombre)
        nombre = input("nombre")
    return alumnos


primaria = set()
secundaria = set()
print("Alumnos de Primaria")
primaria = cargarnombres(primaria)
print("Alumnos de secundaria")
secundaria = cargarnombres(secundaria)
print("Nombre de todos los alumnos:")
for nombre in primaria:
    print(nombre)

print("Nombres Comunes:")
for nombre in primaria & secundaria:
    print(nombre)
print("Nombres de primaria que no se repiten en secundaria")
for nombre in primaria - secundaria:
    print(nombre)


# Ejercicio2
def direcciones(ventas):
    domicilios = set()
    for venta in ventas:
        domicilios.add(venta[3])
    return domicilios
