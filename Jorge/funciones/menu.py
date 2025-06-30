from Jorge.dao.manipular import Manipular
from Jorge.dao.guardar import Archivo
from Jorge.modelos.participantes import Participante

import os
import time

# Funcion que limpia la pantalla de la consola.
def limpiar():
    os.system("cls || clear")

# Funcion que pausa la ejecucion por dos segundos
def esperar():
    time.sleep(2)

# Funcion que muestra un progreso en la accion elegida
def pantalla_buscando():
    for i in range(1, 11):
        limpiar()
        print(f"Buscando", "*" * i, " " * 1, f"{i*10}%")
        time.sleep(0.4)
    limpiar()

# Funcion que pone fin al modulo y regresa al menu principal
def terminar():
    print("=========================\nOperaciones terminadas\n=========================")
    exit()

# Funcion que pausa el programa hasta que el usuario presione enter, para regresar a la funcion main
def regresar():
    input(" \nPresione enter para regresar   ")

# Muestra el menú principal de opciones para la gestión de diezmos.
def menu():
    print("\n======= Gestion de Diezmos =======")
    print("="*34)
    print("1 = Agregar diezmos \n2 = Mostrar total diezmos \n3 = Buscar diezmos")
    print("4 = Eliminar diezmos \n5 = Regresar al menu principal")
    print("="*34)

# Ejecuta la operación seleccionada por el usuario.
def realizar(op):

    # Instanciar clases necesarias para manejar datos y archivo
    manipular = Manipular()
    mi_archivo = Archivo("Lista.txt")
    mi_archivo.generar_archivo()

    # Opcion 1: Agregar diezmos
    if op == "1":
        i = 0

        while True:
            limpiar()
            i += 1
            print(f"Participante #{i}:")
            nombre = input("Escriba el nombre del participante (solo el nombre): ").strip()
            apellido = input("Escriba el apellido del participante (solo el apellido): ").strip()
            donado = float(input("Introduzca la cantidad donada por el participante: "))

            part = Participante(nombre.title(), apellido.title(), donado)
            manipular.agregar(part)

            salir = input(" \n¿Terminar? (s/n): ").strip()
            if salir.lower() == "s":
                break
        
        limpiar()

        # Guardar todos los participantes en el archivo
        for p in manipular.mostrar():
            mi_archivo.guardar_componentes(p)

        mi_archivo.mostrar_componentes()

        print("==========================================")
        print("Informacion guardada en el archivo 'Lista.txt'")
        print("==========================================")

        regresar()

    # Opcion 2: Mostrar total de diezmos
    elif op == "2":
        limpiar()
        pantalla_buscando()
        manipular.obtener()
        regresar()

    # Opcion 3: Buscar diezmos
    elif op == "3":
        limpiar()
        resultados = mi_archivo.comprobar()
        if resultados == True:
            print("Sin contenido")
        else:
            print("1 = Buscar por ID \n2 = Buscar por nombre y apellido")
            decision = input(" \nIngrese su decision: ").strip()
            if decision == "1":
                limpiar()
                id = input("Introduzca el ID del donante a buscar: ").strip()
                pantalla_buscando()
                manipular.buscar(id)
            elif decision == "2":
                limpiar()
                nombre = input("Escriba el nombre del donante a buscar: ").strip()
                apellido = input("Escriba el apellido del donante a buscar: ").strip()
                d = f"{nombre.title()} {apellido.title()}"
                pantalla_buscando()
                manipular.buscar(d)
        regresar()

    # Opcion 4: Eliminar diezmos
    elif op == "4":
        limpiar()
        resultados = mi_archivo.comprobar()
        if resultados == True:
            print("Sin contenido")
        else:
            print("1 = Buscar por ID para eliminar \n2 = Buscar por nombre y apellido para eliminar\n")
            decision = input("Ingrese su decision: ").strip()
            if decision == "1":
                limpiar()
                id = input("Introduzca el ID del donante para eliminar: ").strip()
                pantalla_buscando()
                manipular.eliminar(id)
            elif decision == "2":
                limpiar()
                nombre = input("Escriba el nombre del donante a eliminar: ").strip()
                apellido = input("Escriba el apellido del donante a eliminar: ").strip()
                g = f"{nombre.title()} {apellido.title()}"
                pantalla_buscando()
                manipular.eliminar(g)
        regresar()

    # Opcion 5: Regresar al menu principal
    elif op == "5":
        limpiar()
        print("Regresando al menu principal...")
        return

# Función principal que ejecuta el ciclo infinito del menú, permitiendo al usuario seleccionar opciones
# hasta que decida salir.
def main():
    while True:
        limpiar()
        menu()
        opcion = input(" \nIntroduzca la operacion a realizar: ").lower()
        try:
            opcion = int(opcion)
            if opcion == 5:
                print("Regresando al menu principal...")
                break
            elif opcion > 5:
                print("Debe introducir una de las cinco opciones")
                esperar()
            else:
                realizar(str(opcion))
        except ValueError:
            # Si el usuario introduce un valor no numérico, espera hasta que presione enter para regresar
            print("Introduzca un numero real")
            regresar()
