from datetime import datetime
from subacciones import *

def mostrar_actividad(numero, actividad, habilitada):
    if actividad != "":
        if habilitada == "1":
            estado = "Habilitada"
        else:
            estado = "Cuota vencida"

        print(numero, "_", actividad, "-", estado)


def elegir_actividad(actividades_str, hab_str):
    while True:
        print("\nActividades del socio:")
        for i in range(1, 4):
            actividad = campo(actividades_str, i)
            if actividad != "":
                habilitada = campo(hab_str, i)
                estado = "Habilitada" if habilitada == "1" else "Cuota vencida"
                print(i, "_", actividad, "-", estado)

        opcion = input("Seleccione la actividad a la que asistió: ")

        if opcion in ("1", "2", "3"):
            posicion = int(opcion)
            actividad = campo(actividades_str, posicion)
            habilitada = campo(hab_str, posicion)
            if actividad == "":
                print("\n<<<<<<Opción inválida.>>>>>>\n")
            elif habilitada == "1":
                return actividad
            else:
                print("\n<<<<<<No puede registrar asistencia. La cuota está vencida.>>>>>>\n")
        else:
            print("\n<<<<<<Opción inválida.>>>>>>\n")


def registrar_asistencia():
    print("""
    ########################################
    REGISTRO DE ASISTENCIA
    ########################################
    """)

    dni = DNI()

    if not socio_existe(dni):
        print("\n<<<<<<No existe un socio registrado con ese DNI.>>>>>>\n")
        return

    actividades_str, fechas_str, hab_str = buscar_datos_cuotas(dni)

    if actividades_str == "":
        print("\n<<<<<<El socio no tiene registro de cuotas.>>>>>>\n")
        return

    actividad = elegir_actividad(actividades_str, hab_str)

    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    arch_asistencias = open("asistencias.txt", "a")
    arch_asistencias.write(dni + "|" + actividad + "|" + fecha_hora + "\n")
    arch_asistencias.close()

    print("\n<<<<<<Asistencia registrada correctamente.>>>>>>\n")