# Ejercicio 1
print(not True)
print(not 1 + 2 != 3)
x = (len("jugar") > 5) and (len("jugar") < 10)
print(x)
print("alto"[2] == "t" and x)
print(842913 % 10 != 3 and len("café") == 3)
print(0 != 0 or "a" < "y")
print(True or int("50") >= 50)
edad = 20
print(not (x) or edad % 2 == 0)
es_cliente = False
print(not (es_cliente and not (edad < 18)))

# Ejercicio 2

numero = 0
km = 0
modelo = 0
porcentaje_completo = 0
miembro_agrupacion = True
es_invierno = True
tiene_calefaccion = True
esta_abrigada = True
print(numero % 4 == 0 and numero < 0)
print(km < 30000 and (modelo > 2015 and modelo <= 2017))
print(porcentaje_completo > 30 and not (miembro_agrupacion))
print(es_invierno and not tiene_calefaccion and not esta_abrigada)
print(es_invierno and not (tiene_calefaccion or esta_abrigada))
