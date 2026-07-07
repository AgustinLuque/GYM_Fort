from datetime import datetime
dt = datetime.now()

def registrar_socio():
    def DNI():
        while True:
            dni = input('Ingrese el DNI del socio: ')
            if dni.isdigit() and len(dni) == 8:
                return dni
            else:
                print("\n<<<<<<Error. Por favor, ingrese un número de DNI válido de 8 dígitos.>>>>>>\n")

    def ayn():
        while True:
            a = input('Ingrese el apellido del socio: ')
            n = input('Ingrese el nombre del socio: ')
            if a.replace(" ", "").isalpha() and n.replace(" ", "").isalpha():
                return a + "," + n
            else:
                print("\n<<<<<<Error. Por favor, ingrese un apellido o nombre válido.>>>>>>\n")

    def edad():
        while True:
            i = input('Ingrese la edad del socio: ')
            if i.isdigit() and int(i) > 13:
                return str(i)
            else:
                print("\n<<<<<<Error. Por favor, ingrese un número positivo mayor a 13.>>>>>>\n")

    def telefono():
        while True:
            i = input('Ingrese el teléfono del socio: ')
            if i.isdigit() and len(i) == 10:
                return str(i)
            else:
                print("\n<<<<<<Error. Por favor, ingrese un número de teléfono válido de 10 dígitos.>>>>>>\n")

    def cargar_datos_actividades():
        registro_actividades = ("", "", "", "", "")
        actividades_str, fechas_str, hab_str, coma, nombre_actividad = registro_actividades
        x=0
        while x < 3:
            print("""
            INGRESE EL TIPO DE ACTIVIDAD A LA QUE SE INSCRIBIRÁ EL SOCIO: (hasta 3 actividades por socio)
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
                nombre_actividad = "Funcional"
            elif opcion == "2":
                nombre_actividad = "Musculacion"
            elif opcion == "3":
                nombre_actividad = "Spinning"
            elif opcion == "4":
                nombre_actividad = "HIIT"
            elif opcion == "5":
                nombre_actividad = "Pilates"
            elif opcion == "6":
                nombre_actividad = "Yoga"
            elif opcion == "7":
                nombre_actividad = "Boxeo"
            elif opcion == "8":
                break
            else:
                print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 8.>>>>>>\n")
                continue

            x+=1
            actividades_str = actividades_str + coma + nombre_actividad
            fechas_str = fechas_str + coma + dt.strftime("%d/%m/%Y")
            hab_str = hab_str + coma + "1"
            coma = ","

        return (actividades_str, fechas_str, hab_str)

######################################################################################################################

    while True:
        print("""
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><}><>   
        En este apartado agregará socios al gimnasio. Por favor, ingrese los datos solicitados en el orden solicitado:
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        """)
        
        registro_socio = (
            DNI(), 
            ayn(), 
            edad(), 
            telefono(), 
            dt.strftime("%d/%m/%Y")
            )
        linea_socio = "|".join(registro_socio)

        with open("socios.txt","a") as arch_socios:
            arch_socios.write("\n" + linea_socio)

        actividades_str, fechas_str, hab_str = cargar_datos_actividades()
        registro_cuotas = (registro_socio[0], 
                           actividades_str, 
                           fechas_str, 
                           hab_str)
        linea_cuotas = "|".join(registro_cuotas)

        with open("cuotas maestro","a") as arch_cuotas:
            arch_cuotas.write("\n" + linea_cuotas)

        print("""\n<<<<<<Socio registrado exitosamente.>>>>>>\n
              ¿Desea registrar otro socio? 
>>>Presione S para continuar o cualquier otra tecla para salir.<<<
              """)
        if input().strip().upper() != "S":
            break