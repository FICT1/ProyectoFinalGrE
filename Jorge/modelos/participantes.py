class Participante:
    def __init__(self, nombre, apellido, donado):
        self.nombre = nombre
        self.apellido = apellido
        self.donado = donado
        self.id = 0
        self.__id_aleatorio__()

    def __id_aleatorio__(self):
        import random
        self.id = random.randint(1000, 9999)

    def __str__(self):
        return (
            f"ID-{self.id}) {self.nombre} {self.apellido}: C${self.donado:,}\n"
        )
