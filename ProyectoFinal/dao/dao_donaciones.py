import os  
from models.donacionextra import DonacionesExtra
from models.donacion_especie import DonacionesEspecie

ARCHIVO_DONACIONES = "Donaciones Monetarias.txt"
ARCHIVO_DONACIONES_ESPECIE = "Donaciones Especie.txt"

class DonacionesDAO:
    def __init__(self):
        self.donaciones = []
        self.donaciones_especie = []

    