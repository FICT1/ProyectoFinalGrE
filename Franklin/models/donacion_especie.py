# Modelo de datos para representar una donación en especie.

# Clase que representa una donación en especie realizada por una persona.
# Atributos:
# nombre (str): Nombre del donante.
# especie (str): Descripción de lo donado (ej. alimentos, ropa, etc.).
# fecha (str): Fecha de la donación.
class DonacionesEspecie:

    # Constructor de la clase DonacionesEspecie.
    # Parámetros:
    # nombre (str): Nombre del donante.
    # especie (str): Tipo de artículo donado.
    # fecha (str): Fecha en la que se hizo la donación.
    def __init__(self, nombre, especie, fecha):
        self.nombre = nombre
        self.especie = especie
        self.fecha = fecha

    # Representación en texto legible de la donación.
    def __str__(self):
        return f"{self.nombre} dono: '{self.especie}' \n-Fecha: {self.fecha}"