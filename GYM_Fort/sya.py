from reg_socios import registrar_socio
from in_actvidad import inscribir_actividad

def mostrar_arch():
    while True:
        print("""
              
>>>>>>>>>Que desea ver?
        1_  Archivo de socios
        2_  Archivo de Cuotas y actividades
        3_  Volver
              
            """)
        op = input("Ingrese su opcion: ")
        if op == "1":
            with open ("socios.txt","r") as arch_socios:
                mostrar(arch_socios)
        elif op == "2":
            with open ("cuotas_maestro.txt","r") as arch_cya:
                mostrar(arch_cya)
        elif op == "3":
            break
def mostrar(x):
    for l in x:
        print(l)

def socios_y_actividades():
    while True:
        print("""
    <<<<Aquí la gestión de socios, actividades y cuotas>>>>
        ########################################
        1_ Registrar Socios
        2_ Inscripcion a actividad
        3_Volver
        ########################################
        """)
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_socio()
        elif opcion == "2":
            inscribir_actividad()
        elif opcion == "3":
            break
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 4.>>>>>>\n")