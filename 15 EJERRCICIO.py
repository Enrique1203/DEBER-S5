# Ejercicio1
def coordenadaZ(x, y):
    x = x + 10
    y = y + 15
    return x + y


x = int(input("Coordenada eje x:"))
y = int(input("Coordenada eje y:"))
for i in range(3):
    z = coordenadaZ(x, y)
    x = x + 1
    y = y + 1
print(x, " . ", y)


# Ejercicio2

def maximo(a, b):
    if x > y:
        return x
    else:
        return y


def minimo(a, b):
    if x < y:
        return x
    else:
        return y


x = int(input("Un Numero:"))
y = int(input("Otro Numero:"))
print(maximo(x - 3, minimo(x + 2, y - 5)))
