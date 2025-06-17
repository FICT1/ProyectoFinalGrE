class DonacionesEspecie:
    
    def __init__(self, nombre, especie, fecha):
        self.nombre = nombre
        self.especie = especie
        self.fecha = fecha

    def __str__(self):
        return f"{self.nombre} dono: '{self.especie}' \n-Fecha: {self.fecha}"