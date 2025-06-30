# Modulo encargado de manipular el contenido del registro de diezmos

import os

# Clase para manipular una lista de participantes y gestionar donaciones almacenadas en un archivo "Lista.txt".
# Atributos:
# lista (list): Lista interna para almacenar objetos participantes (opcional, no ligada al archivo).
class Manipular:

    # Inicializa la instancia con una lista vacía.
    def __init__(self):
        self.lista = []
    
    # Funcion encargada de agregar un participante a la lista interna.
    # participante: Objeto que representa un participante
    def agregar(self, participante):
        self.lista.append(participante)

    # Funcion encargadad de leer el archivo "Lista.txt" y calcular el total de diezmos registrados.
    # Cada línea del archivo debe tener formato "clave:valor", donde valor es una cantidad monetaria
    # con prefijo "C$" (ejemplo: "C$1,234.56").
    # Imprime el total acumulado de donaciones con formato monetario.
    def obtener(self):
        if os.path.exists("Lista.txt"):
            total = float()
            with open("Lista.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                # Eliminar líneas vacías y espacios en blanco
                lineas = [linea.strip() for linea in lineas if linea.strip()]
                for i in lineas:
                    limpio = i.split(":")
                    if len(limpio) > 1:
                        donacion = limpio[1].replace("C$", "").replace(",", "")
                        try:
                            total += float(donacion)
                        except ValueError:
                            # Ignorar líneas con valores no numéricos
                            pass

            print(f"Total de donaciones: C${total:,.2f}")

    # Funcion que busca una cadena específica dentro del archivo "Lista.txt".
    # d (str): Cadena que se desea buscar.
    # Imprime la línea donde se encontró la coincidencia o no imprime nada si no se encuentra.
    def buscar(self, d):
        if os.path.exists("Lista.txt"):
            with open("Lista.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                lineas = [linea.strip() for linea in lineas]
                for linea in lineas:
                    if d in linea:
                        print("Diezmo encontrado:")
                        print(linea)
                        break
    
    # Funcion que elimina la primera línea que contenga la cadena especificada del archivo "Lista.txt".
    # d (str): Cadena que identifica la línea a eliminar.
    # Si se encuentra la línea, la elimina y sobrescribe el archivo con las líneas restantes.
    # Imprime un mensaje confirmando la eliminación o indica si el archivo no existe.
    def eliminar(self,d):
        if os.path.exists("Lista.txt"):
            with open("Lista.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
            with open("Lista.txt", "w", encoding="utf-8") as archivo:
                for linea in lineas:
                    if d in linea:
                        # Eliminar la línea solo la primera vez que se encuentra
                        lineas.remove(linea)
                        print(f"Diezmo '{d}' eliminado correctamente")
                        break
                archivo.writelines(lineas)
        else:
            print("El archivo no existe.")        

    # Funcion que devuelve la lista interna de participantes.
    # Returns:
    # list: Lista de participantes almacenados en memoria.
    def mostrar(self):
        return self.lista
