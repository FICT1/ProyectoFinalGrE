from josue.dao.OfrendasDao import Gestion_ofrendasDao
import os
from datetime import datetime

# Muestra el menú principal de opciones para gestionar las ofrendas.
def mostrar_menu():
    print("\n======= Gestión de Ofrendas =======")
    print("===================================")
    print("1. Agregar ofrenda")
    print("2. Eliminar ofrenda")
    print("3. Mostrar ofrendas")
    print("4. Calcular total de ofrendas")
    print("5. Salir")
    print("===================================")

# Valida si una cadena tiene el formato correcto de fecha: 'YYYY-MM-DD'.
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Limpia la pantalla del terminal 
def limpiar_pantalla():
    os.system("cls")

# Función principal que ejecuta el menú de gestión de ofrendas.
def main():

    gestion = Gestion_ofrendasDao()    # Instancia del gestor de ofrendas
    
    while True:
        limpiar_pantalla()  # Limpia la consola en cada iteración
        mostrar_menu()      # Muestra el menú de opciones

        opcion = input("Elige una opción (1-5): ")
        try:
            
            # Opcion 1: Agregar una nueva ofrenda
            if opcion == "1":
                    monto = float(input("Ingresa el monto de la ofrenda: C$ "))
                    gestion.archivar_ofrendas(monto)
                    input("Presiona Enter para continuar...")
            
            # Opcion 2: Eliminar un ofrenda por monto
            elif opcion == "2":
                    monto = float(input("Ingresa el monto a eliminar: C$ "))
                    gestion.eliminar_ofrenda(monto)
                    input("Presiona Enter para continuar...")

            # Opcion 3: Mostrar historial de ofrendas
            elif opcion == "3":
                gestion.mostrar_ofrendas()
                input("Presiona Enter para continuar...")

            # Opcion 4: Calcular el total de ofrendas
            elif opcion == "4":
                gestion.calcular_total_ofrendas()
                input("Presiona Enter para continuar...")

            # Opcion 5: Salir del sistema de gestion de ofrendas
            elif opcion == "5":
                print("Regresando al menu principal...")
                input("Presiona Enter para continuar...")
                break
            
            # Verifica si la opcion introducida es valida
            else:
                print("Opción inválida. Por favor, elige entre 1 y 5.")
                input("Presiona Enter para continuar...")

        # Error por si la entrada no es cadena
        except ValueError:
             print("error")
             continue
        
