from act_socios import actualizar_cuotas_y_socios
from reg_socios import registrar_socio
from in_act import inscribir_actividad
from datetime import datetime

hoy = datetime.now()
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
            actualizar_cuotas_y_socios(hoy)


def main ():
    while True:
        detectar_dia()
        print("""
              ########################################
              Bienvenido a GYM Fort, que desea hacer?

              1_ Registrar socios 
              2_ Inscripción a actividades 
              3_ Asistencias 
              4_  Control de cuotas 
              5_ Estadísticas 
              6_ Salir 
              ########################################
              """)
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_socio()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            break
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 6.>>>>>>\n")


if __name__ == "__main__":
    main()