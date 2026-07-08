import datetime as dt
import shutil
from subacciones import *

def inscribir_actividad():

    def contar_actividades(actividades_str):
        if actividades_str == "":
            return 0

        cantidad = 1
        restante = actividades_str
        while "," in restante:
            _, restante = restante.split(",", 1)
            cantidad += 1

        return cantidad

    def agregar_actividad(actividades_str, fechas_str, hab_str, nueva_actividad):
        fecha_hoy = dt.datetime.now().strftime("%d/%m/%Y")
        actividades_str = agregar_campo(actividades_str, nueva_actividad)
        fechas_str = agregar_campo(fechas_str, fecha_hoy)
        hab_str = agregar_campo(hab_str, "1")
        return actividades_str, fechas_str, hab_str

    def todas_habilitadas(hab_str):
        for i in range(1, 4):
            if campo(hab_str, i) == "0":
                return False
        return True

    def mostrar_actividades_actuales(actividades_str, hab_str):
        print("\nActividades actuales del socio:")
        for i in range(1, 4):
            actividad = campo(actividades_str, i)
            habilitada = campo(hab_str, i)
            estado = "Habilitada" if habilitada == "1" else "Cuota vencida"
            print(i, "_", actividad, "-", estado)

    def elegir_posicion_a_reemplazar(hab_str):
        while True:
            opcion = input("\nSeleccione el número de actividad a reemplazar (0 para cancelar): ")
            if opcion == "0":
                return None
            if opcion in ("1", "2", "3"):
                posicion = int(opcion)
                if campo(hab_str, posicion) == "0":
                    return posicion
                print("\n<<<<<<Esa actividad todavía tiene la cuota habilitada. No se puede reemplazar.>>>>>>\n")
            else:
                print("\n<<<<<<Opción inválida.>>>>>>\n")

    def reemplazar_actividad(actividades_str, fechas_str, hab_str, posicion, nueva_actividad):
        fecha_hoy = dt.datetime.now().strftime("%d/%m/%Y")
        actividades_str = reemplazar_campo(actividades_str, posicion, nueva_actividad)
        fechas_str = reemplazar_campo(fechas_str, posicion, fecha_hoy)
        hab_str = reemplazar_campo(hab_str, posicion, "1")
        return actividades_str, fechas_str, hab_str

    def actualizar_archivo_cuotas(dni, actividades_str, fechas_str, hab_str):
        with open("cuotas_maestro.txt", "r") as arch_cuotas:
            lineas = arch_cuotas.readlines()

        with open("cuotas_novedades.txt", "w") as arch_novedades:
            for linea in lineas:
                linea_limpia = linea.strip()

                if linea_limpia == "":
                    continue

                if "|" not in linea_limpia:
                    arch_novedades.write(linea)
                    continue

                dni_linea, resto = linea_limpia.split("|", 1)

                if dni_linea == dni:
                    linea_actualizada = dni + "|" + actividades_str + "|" + fechas_str + "|" + hab_str + "\n"
                else:
                    linea_actualizada = dni_linea + "|" + resto + "\n"

                arch_novedades.write(linea_actualizada)

        shutil.copy("cuotas_novedades.txt", "cuotas_maestro.txt")

######################################################################################################################

    while True:
        print("""
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        INSCRIPCIÓN A ACTIVIDADES
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        """)

        dni = DNI()
        if not socio_existe(dni):
            print("\n<<<<<<No existe un socio registrado con ese DNI.>>>>>>\n")

        else:
            actividades_str, fechas_str, hab_str = buscar_datos_cuotas(dni)

            if actividades_str == "":
                print("\n<<<<<<El socio no tiene un registro de cuotas cargado.>>>>>>\n")

            else:
                cantidad = contar_actividades(actividades_str)
                

                cantidad = contar_actividades(actividades_str)

                if cantidad < 3:
                    nueva_actividad = elegir_actividad_nueva()
                    if nueva_actividad is not None:
                        actividades_str, fechas_str, hab_str = agregar_actividad(
                            actividades_str, fechas_str, hab_str, nueva_actividad)
                        actualizar_archivo_cuotas(dni, actividades_str, fechas_str, hab_str)
                        print("\n<<<<<<Actividad inscripta exitosamente.>>>>>>\n")

                elif todas_habilitadas(hab_str):
                    print("""
            <<<<<<El socio ya tiene 3 actividades con la cuota habilitada.
        No puede inscribirse a una nueva actividad hasta que alguna de sus cuotas venza.>>>>>>\n
                    """)

                else:
                    mostrar_actividades_actuales(actividades_str, hab_str)
                    posicion = elegir_posicion_a_reemplazar(hab_str)

                    if posicion is not None:
                        nueva_actividad = elegir_actividad_nueva()
                        if nueva_actividad is not None:
                            actividades_str, fechas_str, hab_str = reemplazar_actividad(
                                actividades_str, fechas_str, hab_str, posicion, nueva_actividad)
                            actualizar_archivo_cuotas(dni, actividades_str, fechas_str, hab_str)
                            print("\n<<<<<<Actividad reemplazada exitosamente.>>>>>>\n")

        print("""\n¿Desea inscribir a otro socio en una actividad?
>>>Presione S para continuar o cualquier otra tecla para salir.<<<
              """)
        if input().strip().upper() != "S":
            break