# Importaciones de las funciones 'main' desde cada módulo funcional
from Franklin.funciones.menudonaciones import main as main_franklin
from Jorge.funciones.menu import main as main_jorge
from josue.funciones.menu import main as main_josue

# Módulos estándar y externos necesarios
import os, pwinput, time    # Instalar con pip el pwinput para ocultar la clave
import pyfiglet             # Instalar con pip para crear texto ASCII estilizado

# Limpia la consola del sistema.
def lim():
    os.system("cls || clear")

# Muestra el menú principal de la aplicación.
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

        # Redirige segun la opcion seleccionada
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

# Solicita al usuario un nombre de usuario y contraseña,
# y verifica si coinciden con alguna entrada en la lista de accesos permitidos.
# Returns: True si las credenciales son válidas, False si no.
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
        
        # Verifica si las credenciales estan registradas
        for linea in usarios_claves:
            if comprobando == linea:
                return True
        
        print("Acceso denegado, intentelo de nuevo")
        time.sleep(2)

# Punto de entrada principal de la aplicación. Ejecuta el menú general si el inicio de sesión es exitoso.
def main():
    menu_principal()
