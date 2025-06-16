class DonacionesExtra:
    def __init__(self, nombre, monto, moneda, usd, fecha):
        self.nombre = nombre
        self.monto = monto
        self.moneda = moneda
        self.usd = usd
        self.fecha = fecha

    def __str__(self):
        return f"{self.nombre}: Dono: {self.monto}, Moneda:{self.moneda} \nEn (USD): {self.usd} \nFecha: {self.fecha}"
    
