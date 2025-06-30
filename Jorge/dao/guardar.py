# Módulo encargado de crear un archivo para almacenar el registro de diezmos.

# Clase encargada de manejar un archivo de texto para almacenar datos relacionados
# con diezmos. Permite crear el archivo si no existe, guardar elementos en memoria,
# escribirlos al archivo, y verificar si el archivo contiene registros.
class Archivo:

    # Constructor que inicializa la ruta del archivo y una lista temporal de registros.
    # Parámetros:
    # ruta_archivo (str): Ruta donde se ubicará o leerá el archivo.
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.lista = []

    # Verifica si el archivo existe. Si no existe, lo crea e inicia con un encabezado.
    def generar_archivo(self):
        try:
            with open(self.ruta_archivo, "r") as archivo:
                archivo.read()  # Solo intenta abrirlo para confirmar existencia
        except FileNotFoundError:
            with open(self.ruta_archivo, "w") as archivo:
                archivo.write("Lista de Diezmos:\n")
            self.lista = []

    # Guarda un componente (dato) en la lista temporal.
    # Parámetros:
    # p (objeto): Objeto a guardar.
    def guardar_componentes(self, p):
        self.lista.append(str(p))

    # Escribe todos los elementos guardados en la lista temporal al archivo.
    def mostrar_componentes(self):
        with open(self.ruta_archivo, "a") as archivo:
            for i in self.lista:
                archivo.write(i)

    # Verifica si el archivo contiene registros además del encabezado.  
    # Retorna:
    # bool: True si solo tiene el encabezado (o está vacío), False si contiene más líneas.
    def comprobar(self):
        with open(self.ruta_archivo,"r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) == 1 or len(lineas) == 0:
                return True
            else:
                return False