#Calcular si recibio algun monto extra o regalo de fuera de la iglesia
#Se le preguntara al usuario si recibio algun monto extra o regalo de fuera de la iglesia
#agregarlo a una opcion de menu 
#hacerlo todo en funciones separadas y en archivos separados
#Se ha hecho alguna donacion extra en la iglesia??
#una bienvenida para el usuario
import os 
def limpiarpantalla ():
    os.system("cls || clear")


donaciones = []

def menu():
    limpiarpantalla()
    try:
        print("--Bienvenido al apartado de donaciones extras--")
        print("=============================================================")
        print("(1). Desea agregar un monto dado")
        print("(2). Desea eliminar un monto dado")
        print("(3). Desea ver los montos dados")
        print("(4). Desea regresar al menu principal")
        print("=============================================================")
    except ValueError:
        print("Error al mostrar el menu, seleccione una opcion correcta")
    return input("-> ")

def agregarmonto():
    try:
        nombre = input("Introduzca el nombre del donante \n-> ").capitalize()
        monto = float(input("Introduzca el monto entregado \n-> "))
        donaciones.append({"nombre": nombre, "monto": monto})
        print("Monto agregado con exito")
    except ValueError:
        print("Error al agregar el monto, seleccione una opcion correcta")
    input("Presione enter para continuar...")

def vermontos():
    if not donaciones:
        print("No hay donaciones registradas")
        input("Presione enter para continuar...")
        return
    try:
        for donacion in donaciones:
            print(f"El donante {donacion['nombre']} dio {donacion['monto']}")
    except ValueError:
        print("Error al ver los montos dados, seleccione una opcion correcta")
    input("Presione enter para continuar...")

def eliminarmontos():
    if not donaciones:
        print("No hay donaciones registradas")
        input("Presione enter para continuar...")
        return
    try:
        for donacion in donaciones:
            print(f"El donante {donacion['nombre']} dio {donacion['monto']}")
        donaciones.clear()
        print("Donaciones eliminadas con exito")
    except ValueError:
        print("Error al eliminar los montos dados, seleccione una opcion correcta")
    input("Presione enter para continuar...")

