#Elaborado por Franklin

import os 
from models.donacionextra import DonacionesExtra
from models.donacion_especie import DonacionesEspecie
ARCHIVO_DONACIONES = "Donaciones Monetarias.txt"
ARCHIVO_ESPECIE = "Donaciones Especie.txt"

class DonacionesDAO:
    def __init__(self):
        self.donaciones = []
        self.donaciones_especie = []

    def cargar_datos(self):
        self.donaciones.clear()
        self.donaciones_especie.clear()

    def guardar_donaciones(self, donaciones, donaciones_especie):
        try:
            with open(ARCHIVO_ESPECIE, "r", encoding="utf-8") as f:
                for linea in f:
                    nombre, descripcion, fecha = linea.strip().split(" - ")
                    e = DonacionesEspecie(nombre, descripcion, fecha)
                    self.especies.append(e)
        except FileNotFoundError:
            pass

    def guardar_donaciones(self):
        with open(ARCHIVO_DONACIONES, "w", encoding="utf-8") as f:
            for d in self.donaciones:
                f.write(f"{d.nombre} dono '{d.monto:.2f}C$' {d.moneda} \n-En dolares: {d.usd:.2f}$ \n-Fecha: {d.fecha}")

    def guardar_especies(self):
        with open(ARCHIVO_ESPECIE, "w", encoding="utf-8") as f:
            for e in self.especies:
                f.write(f"{e.nombre} dono {e.descripcion} \n-Fecha: {e.fecha}\n")

    def agregar_donacion_extra(self, donacion: DonacionesExtra):
        self.donaciones.append(donacion)
        self.guardar_donaciones()

    def agregar_donacion_especie(self, especie: DonacionesEspecie):
        self.especies.append(especie)
        self.guardar_especies()

    # Métodos para eliminar por índice
    def eliminar_donacion_extra(self, indice):
        if 0 <= indice < len(self.donaciones):
            eliminado = self.donaciones.pop(indice)
            self.guardar_donaciones()
            return eliminado
        else:
            return None

    def eliminar_donacion_especie(self, indice):
        if 0 <= indice < len(self.especies):
            eliminado = self.especies.pop(indice)
            self.guardar_especies()
            return eliminado
        else:
            return None
#Donaciones EXTRAS (monetarias y en especies)