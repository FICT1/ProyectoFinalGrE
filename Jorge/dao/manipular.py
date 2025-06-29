import os

class Manipular:
    def __init__(self):
        self.lista = []

    def agregar(self, participante):
        self.lista.append(participante)

    def obtener(self):
        if os.path.exists("Lista.txt"):
            total = float()
            with open("Lista.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                lineas = [linea.strip() for linea in lineas if linea.strip()]
                for i in lineas:
                    limpio = i.split(":")
                    if len(limpio) > 1:
                        donacion = limpio[1].replace("C$", "").replace(",", "")
                        try:
                            total += float(donacion)
                        except ValueError:
                            pass

            print(f"Total de donaciones: C${total:,.2f}")

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
    
    def eliminar(self,d):
        if os.path.exists("Lista.txt"):
            with open("Lista.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
            with open("Lista.txt", "w", encoding="utf-8") as archivo:
                for linea in lineas:
                    if d in linea:
                        lineas.remove(linea)
                        print(f"Diezmo '{d}' eliminado correctamente")
                        break
                archivo.writelines(lineas)
        else:
<<<<<<< HEAD
            print("El archivo no existe.")      
=======
            print("El archivo no existe.")        
>>>>>>> origin

    def mostrar(self):
        return self.lista
