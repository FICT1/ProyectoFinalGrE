
from dao.OfrendasDao import Gestion_ofrendasDao
import os
from datetime import datetime

def mostrar_menu():
    print("\n======= Gestión de Ofrendas =======")
    print("===================================")
    print("1. Agregar ofrenda")
    print("2. Eliminar ofrenda")
    print("3. Mostrar ofrendas")
    print("4. Calcular total de ofrendas")
    print("5. Salir")
    print("===================================")

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def limpiar_pantalla():
    
    os.system("cls")

def main():
    gestion = Gestion_ofrendasDao() 
    while True:
        limpiar_pantalla()  
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        try:

            if opcion == "1":
                    monto = float(input("Ingresa el monto de la ofrenda: C$ "))
                    gestion.archivar_ofrendas(monto)
                    input("Presiona Enter para continuar...")

            elif opcion == "2":
                    monto = float(input("Ingresa el monto a eliminar: C$ "))
                    gestion.eliminar_ofrenda(monto)
                    input("Presiona Enter para continuar...")

            elif opcion == "3":
                gestion.mostrar_ofrendas()
                input("Presiona Enter para continuar...")

            elif opcion == "4":
                gestion.calcular_total_ofrendas()
                input("Presiona Enter para continuar...")

            elif opcion == "5":
                print("Saliendo del programa...")
                exit()

            else:
                print("Opción inválida. Por favor, elige entre 1 y 5.")
                input("Presiona Enter para continuar...")
        except ValueError:
             print("error")
             continue
    main()