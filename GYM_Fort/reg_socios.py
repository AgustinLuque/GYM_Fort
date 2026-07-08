import datetime as dt
from subacciones import *

def registrar_socio():
    def cargar_datos_actividades():
        actividades_str = ""
        fechas_str = ""
        hab_str = ""
        x = 0
        while x < 3:
            nueva_actividad = elegir_actividad_nueva()
            if nueva_actividad is None:
                break
            x += 1
            actividades_str = agregar_campo(actividades_str, nueva_actividad)
            fechas_str = agregar_campo(fechas_str, dt.datetime.now().strftime("%d/%m/%Y"))
            hab_str = agregar_campo(hab_str, "1")

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
            membresia(),
            dt.datetime.now().strftime("%d/%m/%Y")
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

        with open("cuotas_maestro.txt","a") as arch_cuotas:
            arch_cuotas.write("\n" + linea_cuotas)

        print("""\n<<<<<<Socio registrado exitosamente.>>>>>>\n
              ¿Desea registrar otro socio? 
>>>Presione S para continuar o cualquier otra tecla para salir.<
              """)
        if input().strip().upper() != "S":
            break