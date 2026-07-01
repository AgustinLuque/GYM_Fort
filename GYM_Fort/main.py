from reg_socios import registrar_socio
######################################

def main ():
    while True:
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