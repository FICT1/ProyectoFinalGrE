# Representa una entrada individual en el historial de ofrendas.
# Atributos:
# monto (float): Monto de la ofrenda realizada.
# fecha (str): Fecha en la que se realizó la ofrenda (formato sugerido: 'YYYY-MM-DD').
class HistoriaOfrendas_dao:

    # Inicializa una instancia de HistoriaOfrendas_dao con un monto y una fecha.
    # monto (float): Valor monetario de la ofrenda.
    # fecha (str): Fecha en la que se realizó la ofrenda.
    def __init__(self, monto, fecha):
        self.monto = float(monto)       # Asegura que el monto siempre sea numérico
        self.fecha = fecha              # Se espera una cadena tipo '2025-06-30'
    
    # Retorna una representación legible de la ofrenda.
    def __str__(self):
        return f"Fecha : {self.fecha} Monto : {self.monto}"