fecha = input("Fecha (formato 'dia, DD/MM'):")
fecha = fecha.lower()
diasemana = fecha[0:fecha.find(',')]
dianro = int(fecha[fecha.find(' ') + 1:fecha.find('/')])
mesnro = int(fecha[fecha.find('/') + 1:])
if dianro > 31 or mesnro > 12:
    print("Fecha Incorrecta")
else:
    if diasemana in "lunes,martes,miercoles":
        respuesta = int("¿Se tomaron examenes? (S/N)")
        if respuesta.lower() == "s":
            aprobados = int(input("Cantidad de Aprobados"))
            reprobados = int(input("Cantidad de reprobados"))
            print("Porcentaje de Aprobados:", (aprobados * 100) / (aprobados + reprobados), '%')
    elif diasemana == "jueves":
        asistencia = int(input("Porcentaje de asistencia:"))
        if asistencia > 50:
            print("Asistio la mayoria")
        else:
            print("No Asistio La Mayoria")
    elif diasemana == "viernes":
        if dianro == 1 and (mesnro == 1 or mesnro == 7):
            print("Comienzo de nuevo ciclo")
            alumnos = int(input("Cantidad de alumnos:"))
            arancel = float(input("Arancel: $"))
            print("Ingreso Total: $", alumnos * arancel)
    else:
        print("Fecha Incorrecta")
print("Fin del Programa")
