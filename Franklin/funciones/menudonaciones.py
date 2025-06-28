from franklin.dao.dao_donaciones import DonacionesDAO
from franklin.models.donacionextra import DonacionesExtra
from franklin.models.donacion_especie import DonacionesEspecie

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

def lim():
    import os
    os.system("cls || clear")

def pausa():
    input("Presiona Enter para continuar...")


def main ():
    dao=DonacionesDAO()
    dao.cargar_datos()
    while True:
        lim()
        op=sub_menu()
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
        
        elif op == "2":
            nombre = input("Ingrese su nombre \n-> ")
            especie = input("Ingrese la especie \n-> ")
            fecha = input("Ingrese la fecha (dd-mm-aa) \n-> ")
            especie = DonacionesEspecie(nombre, especie, fecha)
            dao.agregar_donacion_especie(especie)
            print("Donacion agregada con exito")
            pausa()

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

        elif op == "4":
            if not dao.donaciones_especie:
                print("No hay donaciones en especie")
            else:
                print("Donaciones en especie:")
                for i, d in enumerate(dao.donaciones_especie, start=1):
                    print(f"({i}) {d}")
            pausa()

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

        elif op == "7":
            print("Regresando al menu principal...")
            break

        else: 
            print("Opcion no valida")
            pausa()

    dao.guardar_donaciones()
    dao.guardar_especies()