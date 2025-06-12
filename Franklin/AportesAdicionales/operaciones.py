#Calcular si recibio algun monto extra o regalo de fuera de la iglesia
#Se le preguntara al usuario si recibio algun monto extra o regalo de fuera de la iglesia
#agregarlo a una opcion de menu 
#hacerlo todo en funciones separadas y en archivos separados
#Se ha hecho alguna donacion extra en la iglesia??
#una bienvenida para el usuario
# operaciones.py

import os
from datetime import datetime

TASA_CAMBIO = 36.6243
ARCHIVO_DONACIONES = "donaciones.txt"
ARCHIVO_ESPECIES = "especies.txt"

donaciones = []
especies = []

def limpiarpantalla():
    os.system("cls" if os.name == "nt" else "clear")

def cargar_datos():
    global donaciones, especies
    donaciones.clear()
    especies.clear()
    try:
        with open(ARCHIVO_DONACIONES, "r", encoding="utf-8") as f:
            for linea in f:
                nombre, monto, moneda, en_dolares, fecha = linea.strip().split(" - ")
                donaciones.append({
                    "nombre": nombre,
                    "monto": float(monto),
                    "moneda": moneda,
                    "usd": float(en_dolares),
                    "fecha": fecha
                })
    except FileNotFoundError:
        pass
    try:
        with open(ARCHIVO_ESPECIES, "r", encoding="utf-8") as f:
            for linea in f:
                nombre, objeto, fecha = linea.strip().split(" - ")
                especies.append({
                    "nombre": nombre,
                    "objeto": objeto,
                    "fecha": fecha
                })
    except FileNotFoundError:
        pass

def guardar_donaciones():
    with open(ARCHIVO_DONACIONES, "w", encoding="utf-8") as f:
        for d in donaciones:
            f.write(f"{d['nombre']} - {d['monto']:.2f} - {d['moneda']} - {d['usd']:.2f} - {d['fecha']}\n")

def guardar_especies():
    with open(ARCHIVO_ESPECIES, "w", encoding="utf-8") as f:
        for e in especies:
            f.write(f"{e['nombre']} - {e['objeto']} - {e['fecha']}\n")

def menu():
    limpiarpantalla()
    print("--Bienvenido al apartado de donaciones extras--")
    print("=============================================================")
    print("(1). Agregar donación monetaria")
    print("(2). Agregar donación en especie")
    print("(3). Ver donaciones monetarias")
    print("(4). Ver donaciones en especie")
    print("(5). Eliminar donación monetaria")
    print("(6). Eliminar donación en especie")
    print("(7). Salir")
    print("=============================================================")
    return input("-> ")

def agregarmonto():
    try:
        nombre = input("Nombre del donante: ").capitalize()
        monto = float(input("Monto entregado: "))
        moneda = input("Tipo de moneda (cordobas/dolares): ").lower()
        fecha = input("Fecha de la donación (dd-mm-aaaa): ")

        if moneda == "cordobas":
            usd = monto / TASA_CAMBIO
        elif moneda == "dolares":
            usd = monto
        else:
            print("Moneda no reconocida. Usa 'cordobas' o 'dolares'.")
            input("Presiona Enter para continuar...")
            return

        donaciones.append({
            "nombre": nombre,
            "monto": monto,
            "moneda": moneda,
            "usd": usd,
            "fecha": fecha })
        guardar_donaciones()
        print("Donación monetaria guardada con éxito.")
    except ValueError:
        print("Error: valor no válido.")
    input("Presiona Enter para continuar...")

def agregarespecie():
    try:
        nombre = input("Nombre del donante: ").capitalize()
        objeto = input("Descripción del objeto donado: ")
        fecha = input("Fecha de la donación (dd-mm-aaaa): ")
        especies.append({
            "nombre": nombre,
            "objeto": objeto,
            "fecha": fecha })
        guardar_especies()
        print("Donación en especie guardada con éxito.")
    except Exception:
        print("Error al guardar la donación.")
    input("Presiona Enter para continuar...")

def vermontos():
    if not donaciones:
        print("No hay donaciones monetarias registradas.")
    else:
        print("Donaciones monetarias:")
        total_usd = 0
        for i, d in enumerate(donaciones, start=1):
            print(f"{i}. {d['nombre']} dio {d['monto']} {d['moneda']} (USD ${d['usd']:.2f}) el {d['fecha']}")
            total_usd += d['usd']
        print(f"\nTotal equivalente en USD: ${total_usd:.2f}")
    input("Presiona Enter para continuar...")

def verespecies():
    if not especies:
        print("No hay donaciones en especie registradas.")
    else:
        print("Donaciones en especie:")
        for i, e in enumerate(especies, start=1):
            print(f"{i}. {e['nombre']} donó '{e['objeto']}' el {e['fecha']}")
    input("Presiona Enter para continuar...")

def eliminarmontos():
    vermontos()
    if not donaciones:
        return
    try:
        indice = int(input("Ingrese el número de la donación a eliminar: ")) - 1
        if 0 <= indice < len(donaciones):
            eliminado = donaciones.pop(indice)
            guardar_donaciones()
            print(f"Eliminada donación de {eliminado['nombre']}")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida.")
    input("Presiona Enter para continuar...")

def eliminarespecie():
    verespecies()
    if not especies:
        return
    try:
        indice = int(input("Ingrese el número de la donación a eliminar: ")) - 1
        if 0 <= indice < len(especies):
            eliminado = especies.pop(indice)
            guardar_especies()
            print(f"Eliminada donación de {eliminado['nombre']}")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida.")
    input("Presiona Enter para continuar...")
