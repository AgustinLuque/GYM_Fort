import shutil
#>>>>>>>>>Para pedir datos de socio
def DNI():
    while True:
        dni = input("Ingrese el DNI del socio: ")
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

def membresia():
    while True:
        print("""
        INGRESE EL TIPO DE MEMBRESÍA O PROMOCIÓN DEL SOCIO:
        1_ Mensual
        2_ Trimestral
        3_ Semestral
        4_ Anual
        5_ Promo Estudiante
        6_ Promo Familiar
        """)
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            return "Mensual"
        elif opcion == "2":
            return "Trimestral"
        elif opcion == "3":
            return "Semestral"
        elif opcion == "4":
            return "Anual"
        elif opcion == "5":
            return "Promo Estudiante"
        elif opcion == "6":
            return "Promo Familiar"
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 6.>>>>>>\n")

def elegir_actividad_nueva():
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
        8_ >>>>>Cancelar/Terminar
        """)
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            return "Funcional"
        elif opcion == "2":
            return "Musculacion"
        elif opcion == "3":
            return "Spinning"
        elif opcion == "4":
            return "HIIT"
        elif opcion == "5":
            return "Pilates"
        elif opcion == "6":
            return "Yoga"
        elif opcion == "7":
            return "Boxeo"
        elif opcion == "8":
            return None
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 8.>>>>>>\n")

#>>>>>>>>>>Validacion de socio 
def socio_existe(dni):
    with open("socios.txt", "r") as arch_socios:
        for linea in arch_socios:
            dni_linea, resto = linea.strip().split("|", 1)
            if dni_linea == dni:
                return True
    return False

#>>>>>>>>>>Para tratar cadenas en registros
def agregar_campo(cadena, valor):
    coma = "," if cadena != "" else ""
    return cadena + coma + valor

def campo(cadena, posicion):
    campo1, campo2, campo3 = "", "", ""
    restante = cadena

    if "," in restante:
        campo1, restante = restante.split(",", 1)
    else:
        campo1, restante = restante, ""

    if "," in restante:
        campo2, restante = restante.split(",", 1)
    else:
        campo2, restante = restante, ""

    campo3 = restante

    if posicion == 1:
        return campo1
    elif posicion == 2:
        return campo2
    else:
        return campo3
    
def reemplazar_campo(cadena, posicion, valor_nuevo):
    resultado = ""
    coma = ""
    for i in range(1, 4):
        valor = campo(cadena, i) if i != posicion else valor_nuevo
        resultado = resultado + coma + valor
        coma = ","
    return resultado

def buscar_datos_cuotas(dni):
    with open("cuotas_maestro.txt", "r") as arch_cuotas:
        next(arch_cuotas)
        for linea in arch_cuotas:
            linea = linea.strip()
            if linea == "":
                continue

            dni_linea, resto = linea.split("|", 1)
            if dni_linea == dni:
                actividades_str, resto = resto.split("|", 1)
                fechas_str, hab_str = resto.split("|", 1)
                return actividades_str, fechas_str, hab_str

    return "", "", ""

#>>>>>>> Se usa una ve<     
def mostrar_arch():
    while True:
        print("""

>>>>>>>>>Que desea ver?
        1_  Archivo de socios
        2_  Archivo de Cuotas y actividades
        3_  Archivo de Asistencias
        4_  Volver
              
            """)
        op = input("Ingrese su opcion: ")
        if op == "1":
            with open ("socios.txt","r") as arch_socios:
                mostrar(arch_socios)
        elif op == "2":
            with open ("cuotas_maestro.txt","r") as arch_cya:
                mostrar(arch_cya)
        elif op == "3":
            with open("asistencias.txt","r") as arch_asist:
                mostrar(arch_asist)
        elif op == "4":
            break
        else:
            print("\n<<<<<<Opción inválida. Por favor, ingrese un número del 1 al 4.>>>>>>\n")
def mostrar(x):
    for l in x:
        print(l)

##########>>>>>>> Actualizacion secuenciasl de Socios y Cuotas <<<<<<<##########
def comparar_habilitacion(hoy, fechas_str, hab_str, dt):
    hab_actualizado = ""
    coma = ""

    for i in range(1, 4):
        fecha_str = campo(fechas_str, i)
        if fecha_str == "":
            break
        hab_actual = campo(hab_str, i)

        fecha = dt.datetime.strptime(fecha_str, "%d/%m/%Y")
        if fecha + dt.timedelta(days=30) < hoy:
            hab_actual = "0"
            print("cuota vencida")
        elif fecha + dt.timedelta(days=30) > hoy and hab_actual == "0":
            hab_actual = "1"

        hab_actualizado = hab_actualizado + coma + hab_actual
        coma = ","

    return hab_actualizado

def actualizar_cuotas_y_socios(hoy,dt):
    with open("cuotas_maestro.txt","r") as a:
        encabezado = next(a)
        lineas = a.readlines()
    
    with open("cuotas_novedades.txt", "w") as n:
        n.write(encabezado)
        for l in lineas:
            dni, actividades_str, fechas_str, hab_str = l.strip().split("|")
            hab_actualizado = comparar_habilitacion(hoy, fechas_str, hab_str, dt)
            registro_actualizado = (dni, actividades_str, fechas_str, hab_actualizado)
            linea_actualizada = "|".join(registro_actualizado) + "\n"
            print(linea_actualizada)
            n.write(linea_actualizada)
    
    shutil.copy("cuotas_novedades.txt", "cuotas_maestro.txt")
    print("<<<archivo actualizado>>>\n")