# Módulo responsable del manejo de datos relacionados a las donaciones,
# tanto monetarias como en especie, en archivo plano.

from Franklin.models.donacionextra import DonacionesExtra
from Franklin.models.donacion_especie import DonacionesEspecie
import os

# Archivos donde se almacenan las donaciones
ARCHIVO_DONACIONES = "Donaciones Monetarias.txt"
ARCHIVO_ESPECIE = "Donaciones Especie.txt"

class DonacionesDAO:
    # Clase encargada de la lectura, escritura, agregación y eliminación
    # de donaciones monetarias y en especie.

    def __init__(self):
        self.donaciones = []                    # Lista de objetos DonacionesExtra
        self.donaciones_especie = []            # Lista de objetos DonacionesEspecie

    # Carga las donaciones desde archivos de texto en las listas internas.
    # El archivo de donaciones monetarias debe tener el formato:
    # nombre - monto - moneda - usd - fecha
    # El archivo de especies:
    # nombre - especie - fecha
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
            # El archivo no existe, no se cargan donaciones
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
   
    # Guarda la lista de donaciones monetarias al archivo.
    def guardar_donaciones(self):
        with open(ARCHIVO_DONACIONES, "w", encoding="utf-8") as f:
            for d in self.donaciones:
                f.write("==Donaciones monetarias==\n")
                f.write(f"*{d.nombre}* dono '{d.monto:.2f}C$' {d.moneda} \n-En dolares: {d.usd:.2f}$ \n-Fecha: {d.fecha}\n")

    # Guarda la lista de donaciones en especie al archivo.
    def guardar_especies(self):
        with open(ARCHIVO_ESPECIE, "w", encoding="utf-8") as f:
            for e in self.donaciones_especie:
                f.write("==Donaciones en especie==\n")
                f.write(f"*{e.nombre}* dono {e.especie} \n-Fecha: {e.fecha}\n")

    # Agrega una donación monetaria a la lista y la guarda en archivo.
    def agregar_donacion_extra(self, donacion: DonacionesExtra):
        self.donaciones.append(donacion)
        self.guardar_donaciones()
        
    # Agrega una donación en especie a la lista y la guarda en archivo.
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

    # Elimina una donación en especie por índice.
    # Retorna el objeto eliminado o None si el índice es inválido.
    def eliminar_donacion_especie(self, indice):
        if 0 <= indice < len(self.donaciones_especie):
            eliminado = self.donaciones_especie.pop(indice)
            self.guardar_especies()
            return eliminado
        else:
            return None

#Donaciones EXTRAS (monetarias y en especies)
# DonacionesDAO gestiona tanto las donaciones monetarias como las donaciones en especie,
# manteniéndolas sincronizadas con archivos de texto para persistencia local.
