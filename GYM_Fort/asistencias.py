from datetime import datetime


def socio_existe(dni):
    arch_socios = open("socios.txt", "r")
    next(arch_socios)

    for linea in arch_socios:
        datos = linea.strip().split("|")

        if datos[0] == dni:
            arch_socios.close()
            return True

    arch_socios.close()
    return False


def buscar_actividades(dni):
    arch_cuotas = open("cuotas.txt", "r")
    next(arch_cuotas)

    for linea in arch_cuotas:
        datos = linea.strip().split("|")

        if datos[0] == dni:
            actividades = datos[1].split(",")
            habilitadas = datos[3].split(",")

            arch_cuotas.close()
            return actividades, habilitadas

    arch_cuotas.close()
    return [], []


def elegir_actividad(actividades, habilitadas):
    while True:
        print("\nActividades del socio:")

        for i in range(len(actividades)):
            if habilitadas[i] == "1":
                estado = "Habilitada"
            else:
                estado = "Cuota vencida"

            print(i + 1, "_", actividades[i], "-", estado)

        opcion = input("Seleccione la actividad a la que asistió: ")

        if opcion.isdigit():
            opcion = int(opcion)

            if opcion >= 1 and opcion <= len(actividades):
                posicion = opcion - 1

                if habilitadas[posicion] == "1":
                    return actividades[posicion]
                else:
                    print("\n<<<<<<No puede registrar asistencia. La cuota está vencida.>>>>>>\n")
            else:
                print("\n<<<<<<Opción fuera de rango.>>>>>>\n")
        else:
            print("\n<<<<<<Debe ingresar un número.>>>>>>\n")


def registrar_asistencia():
    print("""
    ########################################
    REGISTRO DE ASISTENCIA
    ########################################
    """)

    dni = input("Ingrese el DNI del socio: ")

    if not dni.isdigit() or len(dni) != 8:
        print("\n<<<<<<DNI inválido. Debe tener 8 dígitos.>>>>>>\n")
        return

    if not socio_existe(dni):
        print("\n<<<<<<No existe un socio registrado con ese DNI.>>>>>>\n")
        return

    actividades, habilitadas = buscar_actividades(dni)

    if len(actividades) == 0:
        print("\n<<<<<<El socio no tiene actividades registradas.>>>>>>\n")
        return

    actividad = elegir_actividad(actividades, habilitadas)

    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    arch_asistencias = open("asistencias.txt", "a")
    arch_asistencias.write(dni + "|" + actividad + "|" + fecha_hora + "\n")
    arch_asistencias.close()

    print("\n<<<<<<Asistencia registrada correctamente.>>>>>>\n")