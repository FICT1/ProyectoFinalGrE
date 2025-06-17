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
        # Cargar donaciones monetarias
        try:
            with open(ARCHIVO_DONACIONES, "r", encoding="utf-8") as f:
                for linea in f:
                    # El formato en archivo debe ser: nombre - monto - moneda - usd - fecha
                    partes = linea.strip().split(" - ")
                    if len(partes) == 5:
                        nombre, monto, moneda, usd, fecha = partes
                        d = DonacionesExtra(nombre, float(monto), moneda, fecha)
                        self.donaciones.append(d)
        except FileNotFoundError:
            pass

        # Cargar donaciones en especie
        try:
            with open(ARCHIVO_ESPECIE, "r", encoding="utf-8") as f:
                for linea in f:
                    # El formato en archivo debe ser: nombre - especie - fecha
                    partes = linea.strip().split(" - ")
                    if len(partes) == 3:
                        nombre, especie, fecha = partes
                        e = DonacionesEspecie(nombre, especie, fecha)
                        self.donaciones_especie.append(e)
        except FileNotFoundError:
            pass
   
   
    def guardar_donaciones(self):
        with open(ARCHIVO_DONACIONES, "w", encoding="utf-8") as f:
            for d in self.donaciones:
                f.write(f"{d.nombre} dono '{d.monto:.2f}C$' {d.moneda} \n-En dolares: {d.usd:.2f}$ \n-Fecha: {d.fecha}")

    def guardar_especies(self):
        with open(ARCHIVO_ESPECIE, "w", encoding="utf-8") as f:
            for e in self.donaciones_especie:
                f.write(f"{e.nombre} dono {e.especie} \n-Fecha: {e.fecha}\n")

    
    
    def agregar_donacion_extra(self, donacion: DonacionesExtra):
        self.donaciones.append(donacion)
        self.guardar_donaciones()

    def agregar_donacion_especie(self, especie: DonacionesEspecie):
        self.donaciones_especie.append(especie)
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
        if 0 <= indice < len(self.donaciones_especie):
            eliminado = self.donaciones_especie.pop(indice)
            self.guardar_especies()
            return eliminado
        else:
            return None
#Donaciones EXTRAS (monetarias y en especies)
