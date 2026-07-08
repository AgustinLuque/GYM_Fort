from subacciones import *

def contar_actividad(actividad, cont_funcional, cont_musculacion,
                     cont_spinning, cont_hiit, cont_pilates,
                     cont_yoga, cont_boxeo, cont_otros):

    if actividad == "":
        return (cont_funcional, cont_musculacion, cont_spinning,
                cont_hiit, cont_pilates, cont_yoga, cont_boxeo, cont_otros)

    if actividad == "Funcional":
        cont_funcional += 1
    elif actividad == "Musculacion" or actividad == "Musculación":
        cont_musculacion += 1
    elif actividad == "Spinning":
        cont_spinning += 1
    elif actividad == "HIIT":
        cont_hiit += 1
    elif actividad == "Pilates":
        cont_pilates += 1
    elif actividad == "Yoga":
        cont_yoga += 1
    elif actividad == "Boxeo":
        cont_boxeo += 1
    else:
        cont_otros += 1

    return (cont_funcional, cont_musculacion, cont_spinning,
            cont_hiit, cont_pilates, cont_yoga, cont_boxeo, cont_otros)


def obtener_contadores_actividades():
    cont_funcional = 0
    cont_musculacion = 0
    cont_spinning = 0
    cont_hiit = 0
    cont_pilates = 0
    cont_yoga = 0
    cont_boxeo = 0
    cont_otros = 0
    total_inscripciones = 0

    arch_cuotas = open("cuotas_maestro.txt", "r")
    next(arch_cuotas)

    for linea in arch_cuotas:
        linea = linea.strip().strip("|").strip()

        if linea != "" and linea[0].isdigit():
            dni, actividades_str, fechas_str, hab_str = linea.split("|")

            for i in range(1, 4):
                actividad = campo(actividades_str, i)

                if actividad != "":
                    total_inscripciones += 1

                (cont_funcional, cont_musculacion, cont_spinning, cont_hiit,
                 cont_pilates, cont_yoga, cont_boxeo, cont_otros) = contar_actividad(
                    actividad, cont_funcional, cont_musculacion, cont_spinning,
                    cont_hiit, cont_pilates, cont_yoga, cont_boxeo, cont_otros)

    arch_cuotas.close()

    return (total_inscripciones, cont_funcional, cont_musculacion,
            cont_spinning, cont_hiit, cont_pilates, cont_yoga,
            cont_boxeo, cont_otros)


def cantidad_inscriptos():
    datos = obtener_contadores_actividades()

    total_inscripciones = datos[0]
    cont_funcional = datos[1]
    cont_musculacion = datos[2]
    cont_spinning = datos[3]
    cont_hiit = datos[4]
    cont_pilates = datos[5]
    cont_yoga = datos[6]
    cont_boxeo = datos[7]
    cont_otros = datos[8]

    print("\nCantidad total de inscripciones a actividades:", total_inscripciones)

    opcion = input("\n¿Desea ver la cantidad por actividad? S/N: ")

    if opcion.strip().upper() == "S":
        print("\nINSCRIPTOS POR ACTIVIDAD")
        print("Funcional:", cont_funcional)
        print("Musculación:", cont_musculacion)
        print("Spinning:", cont_spinning)
        print("HIIT:", cont_hiit)
        print("Pilates:", cont_pilates)
        print("Yoga:", cont_yoga)
        print("Boxeo:", cont_boxeo)

        if cont_otros > 0:
            print("Otras actividades:", cont_otros)


def cantidad_cuotas_vencidas():
    cuotas_vencidas = 0

    arch_cuotas = open("cuotas_maestro.txt", "r")
    next(arch_cuotas)

    for linea in arch_cuotas:
        linea = linea.strip().strip("|").strip()

        if linea != "" and linea[0].isdigit():
            dni, actividades_str, fechas_str, hab_str = linea.split("|")

            for i in range(1, 4):
                actividad = campo(actividades_str, i)
                habilitada = campo(hab_str, i)
                if actividad != "" and habilitada == "0":
                    cuotas_vencidas += 1

    arch_cuotas.close()

    print("\nCantidad total de cuotas vencidas:", cuotas_vencidas)


def actividad_mas_inscriptos():
    datos = obtener_contadores_actividades()

    cont_funcional = datos[1]
    cont_musculacion = datos[2]
    cont_spinning = datos[3]
    cont_hiit = datos[4]
    cont_pilates = datos[5]
    cont_yoga = datos[6]
    cont_boxeo = datos[7]
    cont_otros = datos[8]

    mayor = cont_funcional
    actividad = "Funcional"

    if cont_musculacion > mayor:
        mayor = cont_musculacion
        actividad = "Musculación"
    if cont_spinning > mayor:
        mayor = cont_spinning
        actividad = "Spinning"
    if cont_hiit > mayor:
        mayor = cont_hiit
        actividad = "HIIT"
    if cont_pilates > mayor:
        mayor = cont_pilates
        actividad = "Pilates"
    if cont_yoga > mayor:
        mayor = cont_yoga
        actividad = "Yoga"
    if cont_boxeo > mayor:
        mayor = cont_boxeo
        actividad = "Boxeo"
    if cont_otros > mayor:
        mayor = cont_otros
        actividad = "Otras actividades"

    if mayor == 0:
        print("\nNo hay actividades inscriptas todavía.")
    else:
        print("\nLa actividad con más inscriptos es:", actividad)
        print("Cantidad de inscriptos:", mayor)


def estado_general_socios():
    socios_al_dia = 0
    socios_con_deuda = 0

    arch_cuotas = open("cuotas_maestro.txt", "r")
    next(arch_cuotas)

    for linea in arch_cuotas:
        linea = linea.strip().strip("|").strip()

        if linea != "" and linea[0].isdigit():
            dni, actividades_str, fechas_str, hab_str = linea.split("|")

            tiene_deuda = False
            for i in range(1, 4):
                actividad = campo(actividades_str, i)
                habilitada = campo(hab_str, i)
                if actividad != "" and habilitada == "0":
                    tiene_deuda = True

            if tiene_deuda:
                socios_con_deuda += 1
            else:
                socios_al_dia += 1

    arch_cuotas.close()

    print("\nESTADO GENERAL DE SOCIOS")
    print("Socios al día:", socios_al_dia)
    print("Socios con al menos una cuota vencida:", socios_con_deuda)


def menu_estadisticas():
    while True:
        print("""
        ########################################
        ESTADÍSTICAS DEL GIMNASIO

        1_ Cantidad de inscriptos
        2_ Cantidad de cuotas vencidas
        3_ Actividad con más inscriptos
        4_ Estado general de socios
        5_ Volver al menú principal
        ########################################
        """)

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            cantidad_inscriptos()
        elif opcion == "2":
            cantidad_cuotas_vencidas()
        elif opcion == "3":
            actividad_mas_inscriptos()
        elif opcion == "4":
            estado_general_socios()
        elif opcion == "5":
            break
        else:
            print("\n<<<<<<Opción inválida. Ingrese un número del 1 al 5.>>>>>>\n")