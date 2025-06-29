import os

class Archivo:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.lista = []

    def generar_archivo(self):
        try:
            with open(self.ruta_archivo, "r") as archivo:
                archivo.read()
        except FileNotFoundError:
            with open(self.ruta_archivo, "w") as archivo:
                archivo.write("Lista de Diezmos:\n")
            self.lista = []

    def guardar_componentes(self, p):
        self.lista.append(str(p))

    def mostrar_componentes(self):
        with open(self.ruta_archivo, "a") as archivo:
            for i in self.lista:
                archivo.write(i)
    
    def comprobar(self):
        with open(self.ruta_archivo,"r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) == 1 or len(lineas) == 0:
                return True
            else:
                return False