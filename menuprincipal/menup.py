from franklin.funciones.menudonaciones import main as main_franklin
from jorge.funciones.menu import main as main_jorge
from josue.funciones.menu import main as main_josue
import os

def lim():
    os.system("cls || clear")

def menu_principal():
    while True:
        lim()
        print("\n======= Menú Principal =======")
        print("1. Menú de donaciones (Bonos extra)")
        print("2. Menú de diezmos")
        print("3. Menú de ofrendas")
        print("4. Salir")
        print("================================")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            main_franklin()
        elif opcion == "2":
            main_jorge()
        elif opcion == "3":
            main_josue()
        elif opcion == "4":
            print("Saliendo del programa. ¡Gracias!")
            break  # Termina todo el programa
        else:
            print("Opción inválida. Intente nuevamente.")
            

def main():
    menu_principal()
