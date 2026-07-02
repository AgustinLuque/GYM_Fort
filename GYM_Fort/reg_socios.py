from datetime import datetime
dt = datetime.now()
arch_cuotas = open("cuotas.txt", "a")
arch_socios = open("socios.txt", "a")
######################################################################################################################
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
                return a, n
            else:
                print("\n<<<<<<Error. Por favor, ingrese un apellido  o nombre válido.>>>>>>\n")
    def edad():
        while True:
            i = input('Ingrese la edad del socio: ')
            if i.isdigit() and int(i) > 13:
                return str(i)
            else:
                print("\n<<<<<<Error. Por favor, ingrese un número positivo mayor a 13 para la edad valida o permitida.>>>>>>\n")
    def telefono():
        while True:
            i = input('Ingrese el teléfono del socio: ')
            if i.isdigit() and len(i) == 10:
                return str(i)
            else:
                print("\n<<<<<<Error. Por favor, ingrese un número de teléfono válido de 10 dígitos.>>>>>>\n")
    def actividades():
        x = 0
        actividades=[]
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
                actividades.append("Funcional")  
            elif opcion == "2":
                actividades.append("Musculacion")
            elif opcion == "3":
                actividades.append("Spinning")
            elif opcion == "4":
                actividades.append("HIIT")
            elif opcion == "5":
                actividades.append("Pilates")
            elif opcion == "6":
                actividades.append("Yoga")
            elif opcion == "7":
                actividades.append("Boxeo")
            elif opcion == "8":
                break
            else:
                
                print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 8.>>>>>>\n")
                continue
            x += 1
        return actividades
    def fecha(act):
        f = []
        for i in range(len(act)):
            f.append(dt.strftime("%d/%m/%Y"))
        return f
    def habilitado(act):
        h = []
        for i in range(len(act)):
            h.append("1")
        return h
    
######################################################################################################################
    while True:
        print("""
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><}><>   
        En este apartado agregará socios al gimnasio. Por favor, ingrese los datos solicitados en el orden solicitado:
        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        """)
        idd = DNI()
        registro_socios = "|".join([
            idd,
            ",".join(ayn()),   
            edad(),
            telefono(),
            dt.strftime("%d/%m/%Y"),
        ])
        arch_socios.write(registro_socios + "\n")

        act = actividades()
        registro_cuotas = "|".join([
            idd,
            ",".join(act),
            ",".join(fecha(act)),
            ",".join(habilitado(act)),
        ])
        arch_cuotas.write(registro_cuotas + "\n")

        arch_socios.close()
        arch_cuotas.close()

        print("""\n<<<<<<Socio registrado exitosamente.>>>>>>\n
              ¿Desea registrar otro socio? 
>>>Presione S para continuar o cualquier otra tecla para salir.<<<
              """)
        if input().strip().upper() != "S":
            break