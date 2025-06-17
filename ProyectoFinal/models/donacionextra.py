class DonacionesExtra:
    TASA_USD = 36.6243

    def __init__(self, nombre, monto, moneda, fecha):
        self.nombre = nombre
        self.monto = monto
        self.moneda = moneda.lower()
        self.fecha = fecha
        self.usd = self.convertir_a_usd()

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
        
    def __str__(self):
        return (
            f"{self.nombre} donó {self.monto} {self.moneda} \n"f"-Equivalente en USD: ${self.usd} \n"f"-Fecha: {self.fecha}")
