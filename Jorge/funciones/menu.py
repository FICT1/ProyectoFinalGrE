def limpiar():
    import os
    os.system("cls || clear")

def esperar():
    import time
    time.sleep(2)

def pantalla_buscando():
    import time
    for i in range(1,11):
        limpiar()
        print(f"Buscando", "*" * i, " "*1, f"{i*10}%")
        time.sleep(0.4)
    limpiar()

def terminar():
    print("=========================\nOperaciones terminadas\n=========================")
    exit()

def regresar():
    input(" \nPresione enter para regresar   ")

def menu():
    print("1 = Agregar diezmos \n2 = Mostrar total diezmos \n3 = Buscar diezmos")
    print("4 = Eliminar diezmos \n5 = Salir")

def realizar(op):
    from modelos.participantes import Participante
    from dao.manipular import Manipular
    from dao.guardar import Archivo

    manipular = Manipular()
    mi_archivo = Archivo("Lista.txt")
    mi_archivo.generar_archivo()

    lista_diezmo = []

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
            lista_diezmo.append(donado) 

            salir = input(" \n¿Terminar? (s/n): ").strip()
            if salir.lower() == "s":
                break
        
        limpiar()

        for p in manipular.mostrar():
            mi_archivo.guardar_componentes(p)

        mi_archivo.mostrar_componentes()

        print("==========================================")
        print("Informacion guardada en el archivo 'Lista.txt'")
        mi_archivo.respaldar()
        print("==========================================")

        regresar()

    elif op == "2":
        limpiar()
        pantalla_buscando()
        manipular.obtener()
        regresar()

    elif op == "3":
        limpiar()
        resultados = mi_archivo.comprobar()
        if resultados == True:
            print("Sin contenido")
        else:
            print("1 = Buscar por ID \n2 = Buscar por nombre y apellido")
            decision = input(" \nIngrese su decision: ")
            if decision == "1":
                limpiar()
                id = input("Introduzca el ID del donante a buscar: ")
                pantalla_buscando()
                manipular.buscar(id)
            elif decision == "2":
                limpiar()
                nombre = input("Escriba el nombre del donante a buscar: ")
                apellido = input("Escriba el apellido del donante a buscar: ")
                d = f"{nombre.title()} {apellido.title()}"
                pantalla_buscando()
                manipular.buscar(d)
        regresar()

    elif op == "4":
        limpiar()
        resultados = mi_archivo.comprobar()
        if resultados == True:
            print("Sin contenido")
        else:
            print("1 = Buscar por ID para eliminar \n2 = Buscar por nombre y apellido para eliminar\n")
            decision = input("Ingrese su decision: ")
            if decision == "1":
                limpiar()
                id = input("Introduzca el ID del donante para eliminar: ")
                pantalla_buscando()
                manipular.eliminar(id)
                manipular.eliminar_en_respaldo(id)
            elif decision == "2":
                limpiar()
                nombre = input("Escriba el nombre del donante a eliminar: ")
                apellido = input("Escriba el apellido del donante a eliminar: ")
                g = f"{nombre.title()} {apellido.title()}"
                pantalla_buscando()
                manipular.eliminar(g)
                manipular.eliminar_en_respaldo(g)
        regresar()

    elif op == "5":
        limpiar()
        terminar()
        
def main():
    while True:
        limpiar()
        menu()
        opcion = input(" \nIntroduzca la operacion a realizar: ").lower()
        try:
            opcion = int(opcion)
            if opcion > 5:
                print("Debe introducir una de las cinco opciones")
                esperar()
            else:
                realizar(str(opcion))
        except ValueError:
            regresar()
