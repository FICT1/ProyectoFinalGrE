# Módulo de menú interactivo para gestionar donaciones monetarias y en especie.
# Este archivo actúa como interfaz de usuario para las funcionalidades del DAO.

from Franklin.dao.dao_donaciones import DonacionesDAO
from Franklin.models.donacionextra import DonacionesExtra
from Franklin.models.donacion_especie import DonacionesEspecie

# Funcion que muestra el menu principal de donaciones y retorna la opción elegida
def sub_menu():
    print("-------Bienvenido al apartado de donaciones extras-------")
    print("=============================================================")
    print("(1). Agregar donación monetaria")
    print("(2). Agregar donación en especie")
    print()
    print("(3). Ver donaciones monetarias")
    print("(4). Ver donaciones en especie")
    print()
    print("(5). Eliminar donación monetaria")
    print("(6). Eliminar donación en especie")
    print("(7). Salir")
    print("=============================================================")
    return input("-> ")

# Funcion encargada de limpiar la pantalla
def lim():
    import os
    os.system("cls || clear")

# Pausa la ejecución hasta que el usuario presione Enter
def pausa():
    input("Presiona Enter para continuar...")

# Función principal que controla el flujo del menu
def main ():

    dao=DonacionesDAO()
    dao.cargar_datos()      # Cargar datos almacenados desde archivos de texto

    while True:
        lim()
        op=sub_menu()

        # Opción 1: Agregar donación monetaria
        if op=="1":
            nombre=input("Ingrese su nombre \n-> ")
            try:
                monto=float(input("Ingrese el monto \n-> "))
                moneda=input("Ingrese la moneda (cordobas|dolares) \n-> ")
                fecha=input("Ingrese la fecha (dd-mm-aa) \n-> ")
                donacion=DonacionesExtra(nombre,monto,moneda,fecha)
                dao.agregar_donacion_extra(donacion)
                print("Donacion agregada con exito")
            except ValueError:
                print(f"Error: Porfavor ingrese un monto valido")
            pausa()
        
        # Opción 2: Agregar donación en especie
        elif op == "2":
            nombre = input("Ingrese su nombre \n-> ")
            especie = input("Ingrese la especie \n-> ")
            fecha = input("Ingrese la fecha (dd-mm-aa) \n-> ")
            especie = DonacionesEspecie(nombre, especie, fecha)
            dao.agregar_donacion_especie(especie)
            print("Donacion agregada con exito")
            pausa()
        
        # Opción 3: Ver donaciones monetarias
        elif op == "3":
            if not dao.donaciones:
                print("No hay donaciones monetarias")
            else: 
                print("Donaciones monetarias:")
                total_usd = 0
                for i, d in enumerate(dao.donaciones, start=1):
                    print(f"({i}) {d}")
                    total_usd += d.usd
                print(f"\nTotal equivalente en USD: ${total_usd:.2f}")
            pausa()

        # Opción 4: Ver donaciones en especie
        elif op == "4":
            if not dao.donaciones_especie:
                print("No hay donaciones en especie")
            else:
                print("Donaciones en especie:")
                for i, d in enumerate(dao.donaciones_especie, start=1):
                    print(f"({i}) {d}")
            pausa()

        # Opción 5: Eliminar donación monetaria
        elif op == "5":
            if not dao.donaciones:
                print("No hay donaciones monetarias para eliminar.")
            else:
                print("Donaciones monetarias:")
                for i, d in enumerate(dao.donaciones, start=1):
                    print(f"({i}) {d}")
                try:
                    indice = int(input("Ingrese el número de la donación a eliminar: ")) - 1
                    eliminado = dao.eliminar_donacion_extra(indice)
                    if eliminado:
                        print(f"Donación de {eliminado.nombre} eliminada.")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Entrada inválida.")
            pausa()

        # Opción 6: Eliminar donación en especie
        elif op == "6":
            if not dao.donaciones_especie:
                print("No hay donaciones en especie para eliminar.")
            else:
                print("Donaciones en especie:")
                for i, d in enumerate(dao.donaciones_especie, start=1):
                    print(f"({i}) {d}")
                try:
                    indice = int(input("Ingrese el número de la donación a eliminar: ")) - 1
                    eliminado = dao.eliminar_donacion_especie(indice)
                    if eliminado:
                        print(f"Donación de {eliminado.nombre} eliminada.")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Entrada inválida.")
            pausa()

        # Opción 7: Salir del menu
        elif op == "7":
            print("Regresando al menu principal...")
            break
        
        # Por si el usuario no introdujo una de las 7 opciones disponibles
        else: 
            print("Opcion no valida")
            pausa()

    # Guardar datos al salir
    dao.guardar_donaciones()
    dao.guardar_especies()