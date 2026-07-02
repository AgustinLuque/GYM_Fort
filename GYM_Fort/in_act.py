def inscribir_actividad():
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