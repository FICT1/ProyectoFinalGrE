from dao.dao_donaciones import DonacionesDAO
from models.donacionextra import DonacionesExtra
from models.donacion_especie import DonacionesEspecie

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
    os.system("cls ||clear")

def pausa():
    input("Presiona Enter para continuar...")


def main ():
    dao=DonacionesDAO()
    dao.cargar_datos()
    while True:
        lim()
        op=sub_menu()
        if op=="1":
            donacion=DonacionesExtra()
            donacion.ingresar_datos()
            dao.agregar_donacion_extra(donacion)
            pausa()
        elif op=="2":
            donacion=DonacionesEspecie()
            donacion.ingresar_datos()
            dao.agregar_donacion_especie(donacion)
            pausa()
        elif op=="3":
            dao.mostrar_donaciones()
            pausa()
        elif op=="4":
            dao.mostrar_especies()
            pausa()
        elif op=="5":
            dao.mostrar_donaciones()
            indice=int(input("Ingrese el indice de la donacion que desea eliminar: "))
            dao.eliminar_donacion_extra(indice)
            pausa()
        elif op=="6":
            dao.mostrar_especies()
            indice=int(input("Ingrese el indice de la donacion que desea eliminar: "))
            dao.eliminar_donacion_especie(indice)
            pausa()
        elif op=="7":
            break
        else:
            print("Opcion no valida")
            pausa()

