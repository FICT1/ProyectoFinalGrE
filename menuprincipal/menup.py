from Franklin.funciones.menudonaciones import main as main_franklin
from Jorge.funciones.menu import main as main_jorge
from josue.funciones.menu import main as main_josue
import os, pwinput, time #instalar con pip el pwinput
import pyfiglet #instalar con pip

def lim():
    os.system("cls || clear") #limpiar pantalla

def menu_principal():
    while True:
        lim()

        # Título en grande con pyfiglet
        titulo = pyfiglet.figlet_format("Iglesia Cristiana", font="standard")
        print(titulo)

        # Menú visual con estilo profesional
        print("=" * 40)
        print("              MENÚ PRINCIPAL              ")
        print("=" * 40)
        print("1. Menú de Donaciones (Bonos extra)")
        print("2. Menú de Diezmos")
        print("3. Menú de Ofrendas")
        print("4. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            main_franklin()
        elif opcion == "2":
            main_jorge()
        elif opcion == "3":
            main_josue()
        elif opcion == "4":
            print("\nSaliendo del programa. ¡Que Dios lo bendiga!\n")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")
            time.sleep(2)

            
def iniciar_sesion():
    usarios_claves = ["Usuario: Jorge, Clave: 123J",
                      "Usuario: Frank, Clave: 123F",
                      "Usuario: Josue, Clave: 123S"]
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
