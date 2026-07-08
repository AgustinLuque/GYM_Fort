from as_y_es import asistencias_y_estadisticas
from sya import socios_y_actividades
from subacciones import *
import datetime as dt

hoy = dt.datetime.now()
######################################
def actualizar_fecha():
    with open("fecha.txt", "w") as arch_fecha:
        arch_fecha.write(hoy.strftime("%d/%m/%Y"))

def detectar_dia():
    with open("fecha.txt", "r+") as arch_fecha:
        fecha_guardada = arch_fecha.read().strip()
        fecha_actual = hoy.strftime("%d/%m/%Y")
        if fecha_guardada != fecha_actual:
            actualizar_fecha()
            actualizar_cuotas_y_socios(hoy,dt)


def main ():
    while True:
        detectar_dia()
        print("""
              ########################################

              Bienvenido a GYM Fort, que desea hacer?
              1_ Socios y Actividades
              2_ Asistencia y Estadísticas
              3_ Ver archivos
              4_Salir

              ########################################
              """)
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            socios_y_actividades()
        elif opcion == "2":
            asistencias_y_estadisticas()
        elif opcion == "3":
            mostrar_arch()
        elif opcion == "4":
            break
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 4.>>>>>>\n")


if __name__ == "__main__":
    main()