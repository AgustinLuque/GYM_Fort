from datetime import datetime
dt = datetime.now()
def registrar_socio():
    while True:
        print("""
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>   
        En este apartado agregará socios al gimnasio. Por favor, ingrese los datos solicitados en el orden solicitado:
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        """)
        with open("socios.txt", "a") as arch_socios:
            ###########
            while True:
                i = input ('ingrese el DNI del socio:  ')
                if i.isdigit() and len(i) == 8:
                    arch_socios.write(str(i))
                    break
                else:
                    print("\n<<<<<<Error. Por favor, ingrese un número de DNI válido de 8 dígitos.>>>>>>\n")
            ###########
            arch_socios.write("|"+input('Ingrese el apellido del socio: '))
            ###########
            arch_socios.write("|"+input('Ingrese el nombre del socio: '))
            ###########
            while True:
                i = input('Ingrese la edad del socio: ')
                if i.isdigit() and int(i) > 13:
                    arch_socios.write("|"+str(i))
                    break
                else:
                    print("\n<<<<<<Error. Por favor, ingrese un número positivo mayor a 13 para la edad valida o permitida.>>>>>>\n")
            ###########
            while True:
                i = input('Ingrese el teléfono del socio: ')
                if i.isdigit() and len(i) == 10:
                    arch_socios.write("|"+str(i)+"|")
                    break
                else:
                        print("\n<<<<<<Error. Por favor, ingrese un número de teléfono válido de 10 dígitos.>>>>>>\n")
            ###########
            while True:
                print("""
                INGRESE EL TIPO DE ACTIVIDAD A LA QUE SE INSCRIBIRÁ EL SOCIO:
                1_ Funcional
                2_ Musculación
                3_ Spinning
                4_ HIIT
                5_ Pilates
                6_ Yoga
                7_ Boxeo
                8_ >>>>>Terminar
                """)
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    arch_socios.write(",Funcional")
                elif opcion == "2":
                    arch_socios.write(",Musculacion")
                elif opcion == "3":
                    arch_socios.write(",Spinning")
                elif opcion == "4":
                    arch_socios.write(",HIIT")
                elif opcion == "5":
                    arch_socios.write(",Pilates")
                elif opcion == "6":
                    arch_socios.write(",Yoga")
                elif opcion == "7":
                    arch_socios.write(",Boxeo")
                elif opcion == "8":
                    arch_socios.write("|")
                    break
                else:
                    print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 8.>>>>>>\n")
            ###########
            arch_socios.write("|1")
            ###########
            arch_socios.write("|"+dt.strftime("%d/%m/%Y,(%H:%M:%S)"))
        break   