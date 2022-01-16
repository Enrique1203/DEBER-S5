contadores = {}
for i in range(3):
    cadena = input("Cadena de Caracteres")
    for caracter in cadena:
        if caracter not in contadores.keys():
            contadores[caracter] = 1
        else:
            contadores[caracter] += 1

for caracter, cantidad in contadores.items():
    print(caracter, ":", cantidad)
