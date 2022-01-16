# Ejercicio1
numero = int(input("Numero: "))
if numero < 0:
    numero = numero * -1
print("El Valor absoluito es", numero)

# Ejercicio2
nombre1 = input("Un Nombre:")
nombre2 = input("Otro Nombre:")
indice_final_nombre1 = len(nombre1) - 1
indice_final_nombre2 = len(nombre2) - 1
if nombre1[0] == nombre2[0] or nombre1[indice_final_nombre1] == nombre2[indice_final_nombre2]:
    print("Coincidencia")
else:
    print("No Hay Coincidencia")

# Ejercicio3
candidato = input("Candidato Elegido:")
if candidato.upper() == "A":
    print("Usted a Votado por el partido rojo")
elif candidato.upper() == "B":
    print("Usted a Votado por el partido azul")
elif candidato.upper() == "C":
    print("Usted a Votado por el partido verde")
else:
    print("Opcion erronea")

# Ejercicio4
letra = input("Letra: ")
if len(letra) != 1:
    print("Debe ser solo una letra")
else:
    if letra.lower() in "aeiou":
        print("Es Vocal")

# Ejercicio5
anio = int(input("Año: "))
if anio % 4 != 0:
    print("No es bisiesto")
else:
    if anio % 100 != 0 or anio % 400 == 0:
        print("Es Bisiesto")
    else:
        print("No es bisiesto")
