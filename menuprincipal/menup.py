from Franklin.funciones.menudonaciones import main as main_franklin
from Jorge.funciones.menu import main as main_jorge
from josue.funciones.menu import main as main_josue
import os, pwinput, time

def lim():
    os.system("cls || clear")

def menu_principal():
    while True:
        lim()
        print("======= Menú Principal =======")
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
            
def iniciar_sesion():
    usarios_claves = ["Usuario: Jorge, Clave: 123J","Usuario: Frank, Clave: 123F","Usuario: Josue, Clave: 123S"]
    while True:
        lim()
        print("======= Confirmacion de acceso =======")
        print("="*40)
        usuario = input("Introduzca el usuario: ").strip()
        clave = pwinput.pwinput("Introduzca la clave: ",mask="*").strip()
        print("="*40)
        
        comprobando = f"Usuario: {usuario}, Clave: {clave}"
        
        for linea in usarios_claves:
            if comprobando == linea:
                return True
        
        print("Acceso denegado, intentelo de nuevo")
        time.sleep(2)

def main():
    menu_principal()
