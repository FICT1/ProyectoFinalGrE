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
    
    def respaldar(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "r") as archivo:
                contenido = archivo.readlines()
            with open("Respaldo.txt","w") as respaldo:
                respaldo.writelines(contenido)
                for i in contenido:
                    if i.startswith("Lista de Diezmos:\n"):
                        contenido.remove(i)
                    self.guardar_componentes(i)
            print(f"Respaldo creado: Respaldo.txt")
        else:
            print("El archivo no existe, no se puede crear un respaldo.")