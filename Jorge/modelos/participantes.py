# Clase que representa a un participante que ha realizado una donación.
# Atributos:
# nombre (str): Nombre del participante.
# apellido (str): Apellido del participante.
# donado (float): Cantidad donada por el participante.
# id (int): Identificador aleatorio de 4 dígitos generado automáticamente.
class Participante:

    # Inicializa un nuevo participante con nombre, apellido, cantidad donada y un ID aleatorio.
    def __init__(self, nombre, apellido, donado):
        self.nombre = nombre
        self.apellido = apellido
        self.donado = donado
        self.id = 0
        self.__id_aleatorio__() # Generar ID aleatorio al crear el objeto

    # Genera un ID aleatorio de 4 dígitos (entre 1000 y 9999) para el participante.
    def __id_aleatorio__(self):
        import random
        self.id = random.randint(1000, 9999)

    # Representación en cadena del participante, útil para mostrar por pantalla o guardar en archivo.
    def __str__(self):
        return (
            f"ID-{self.id}) {self.nombre} {self.apellido}: C${self.donado:,}\n"
        )
