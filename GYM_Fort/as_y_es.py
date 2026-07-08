from asistencias import registrar_asistencia
from estadisticas import menu_estadisticas
def asistencias_y_estadisticas():
    while True:
        print("""
 <<<<Aquí la gestión de asistencias y estadísticas>>>>
        ########################################
        1_ Registrar Asistencias
        2_ Ingresar a Estadísticas
        3_ Ver ver registro de asistencias completo
        4_Volver
        ########################################
        """)
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_asistencia()
        elif opcion == "2":
            menu_estadisticas()
        elif opcion == "3":
            break
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 4.>>>>>>\n")