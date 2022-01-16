# Ejercicio1
total = 0
monto = float(input("Monto de una Venta: $"))
while monto != 0:
    if monto < 0:
        print("Monto No Valido")
    else:
        total += monto
    monto = float(input("Monto de una Venta: $"))
if total > 1000:
    total -= total * 0.1
print("Monto total a pagar: $", total)

# Ejercicio2
totalpares = 0
totalImpares = 0
numero = int(input("Numero:"))
while numero != 0:
    pares = 0
    impares = 0
    while numero != 0:
        ultimodigito = numero % 10
        if ultimodigito % 2 == 0:
            pares += 1
            totalpares += 1
        else:
            impares += 1
            totalImpares += 1
        numero = numero // 10
    print("El Numero ingresado tiene", pares, "digitos pares y", impares, "digitos impares")
    numero = int(input("Numero:"))
print("Total de digitos pares:", totalpares)
print("Total de digitos Impares:", totalImpares)

# Ejercicio3
digitosenlinea = 0
cantlineas = 0
titulo = input("Titulo del libro:")
while titulo != "*":
    if titulo == "/":
        cantlineas += 1
        print("Linea completa Aparecen", digitosenlinea, "digitos")
        digitosenlinea = 0
    else:
        for caracter in titulo:
            if caracter in "0123456789":
                digitosenlinea += 1
    titulo = input("Titulo del libro:")
print("Fin. Se leyeron", cantlineas, "lineas")
