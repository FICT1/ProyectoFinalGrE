class HistoriaOfrendas_dao:

    def __init__(self, monto, fecha):
        self.monto = float(monto)
        self.fecha = fecha 
    
    def __str__(self):
        return f"Fecha : {self.fecha} Monto : {self.monto}"