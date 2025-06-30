# Modelo de datos para representar una donación monetaria.

# Clase que representa una donación monetaria realizada por una persona.
# Atributos:
# nombre (str): Nombre del donante.
# monto (float): Monto donado.
# moneda (str): Tipo de moneda ('cordobas' o 'dolares').
# fecha (str): Fecha de la donación.
# usd (float): Monto convertido a dólares estadounidenses.
class DonacionesExtra:

    # Tasa fija de cambio de córdobas a dólares
    TASA_USD = 36.6243

    # Constructor de la clase DonacionesExtra.
    # Parámetros:
    # nombre (str): Nombre del donante.
    # monto (float): Monto de la donación.
    # moneda (str): Tipo de moneda ('cordobas' o 'dolares').
    # fecha (str): Fecha en que se realizó la donación.
    def __init__(self, nombre, monto, moneda, fecha):
        self.nombre = nombre
        self.monto = monto
        self.moneda = moneda.lower()
        self.fecha = fecha
        self.usd = self.convertir_a_usd()

    # Convierte el monto a dólares usando la tasa definida.
    # Retorna:
    # float: Monto equivalente en dólares.
    def convertir_a_usd(self):
        try:
            if self.moneda == "cordobas":
                return round(self.monto / DonacionesExtra.TASA_USD, 2)
            elif self.moneda == "dolares":
                return round(self.monto, 2)
            else:
                raise ValueError("Moneda no válida: debe ser 'cordobas' o 'dolares'.")
        except ValueError as e:
            print(e)
            return None
        
    # Retorna una representación legible de la donación.
    def __str__(self):
        return (
            f"{self.nombre} donó {self.monto} {self.moneda} \n"f"-Equivalente en USD: ${self.usd} \n"f"-Fecha: {self.fecha}")
