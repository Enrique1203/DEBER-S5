def sumatoria(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma


def numerosmenores(lista, limite):
    nueva = []
    for n in lista:
        if n < limite:
            nueva.append(n)
    return nueva


def frecuencias(lista):
    nueva = []
    for n in lista:
        if (n, lista.count(n)) not in nueva:
            nueva.append()


# Ejercicio1
numeros = []
nro = int(input("Numero:"))
while nro != 0:
    numeros.append(nro)
    nro = int(input("Numero"))

# Ejercicio2
eliminar = int(input("Numero a eliminar:"))
if eliminar in numeros:
    numeros.remove((eliminar))
else:
    print("Ese numero no esta entre los ingresados")

# Ejercicio3
print("Sumatoria de los numeros:", sumatoria(numeros))

# Ejercicio4
limite = int(input("Filtrar numeros menores a :"))
for n in numerosmenores(numeros, limite):
    print(n)

# Ejercicio5
print("Frecuencias")
for tupla in frecuencias(numeros):
    print(tupla[0], "aparece", tupla[1], "veces")
