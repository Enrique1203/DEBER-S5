def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma


sumatoria = 0
num = int(input("Numero a Procesar:"))
while num != 0:
    print("Suma:", sumaDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("Numero a procesar:"))
print("Sumatoria:", sumatoria)
print("Digitos:", sumaDigitos(sumatoria))
