import datetime as dt
import shutil

def comparar_habilitacion(hoy, fechas_str, hab_str):
    fechas_restantes = fechas_str
    hab_restantes = hab_str
    hab_actualizado = ""
    coma = ""

    for x in range(3):
        if fechas_restantes == "":
            break

        if "," in fechas_restantes:
            fecha_actual, fechas_restantes = fechas_restantes.split(",", 1)
        else:
            fecha_actual, fechas_restantes = fechas_restantes, ""

        if "," in hab_restantes:
            hab_actual, hab_restantes = hab_restantes.split(",", 1)
        else:
            hab_actual, hab_restantes = hab_restantes, ""

        fecha = dt.datetime.strptime(fecha_actual, "%d/%m/%Y")
        if fecha + dt.timedelta(days=30) < hoy:
            hab_actual = "0"
            print("cuota vencida")
        elif fecha + dt.timedelta(days=30) > hoy and hab_actual == "0":
            hab_actual = "1"

        hab_actualizado = hab_actualizado + coma + hab_actual
        coma = ","

    return hab_actualizado

def actualizar_cuotas_y_socios(hoy):
    with open("cuotas_maestro.txt","r") as a:
        lineas = a.readlines()
    
    with open("cuotas_novedades.txt", "w") as n:
        for l in lineas:
            dni, actividades_str, fechas_str, hab_str = l.strip().split("|")
            hab_actualizado = comparar_habilitacion(hoy, fechas_str, hab_str)
            registro_actualizado = (dni, actividades_str, fechas_str, hab_actualizado)
            linea_actualizada = "|".join(registro_actualizado) + "\n"
            print(linea_actualizada)
            n.write(linea_actualizada)
    
    shutil.copy("cuotas_novedades.txt", "cuotas_maestro.txt")
    print("<<<archivo actualizado>>>\n")