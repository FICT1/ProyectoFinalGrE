#Calcular si recibio algun monto extra o regalo de fuera de la iglesia
#Se le preguntara al usuario si recibio algun monto extra o regalo de fuera de la iglesia
#agregarlo a una opcion de menu 
#hacerlo todo en funciones separadas y en archivos separados
#Se ha hecho alguna donacion extra en la iglesia??
#una bienvenida para el usuario


from operaciones import (
    limpiar_pantalla as lim,
    menu as m,
    agregarmonto,
    eliminarmontos,
    vermontos,
    cargar_donaciones
)


def main ():
    cargar_donaciones()
    while True:
        if m() == "1":
            lim()
            agregarmonto()
        elif m() == "2":
            lim()
            eliminarmontos()
        elif m() == "3":
            lim()
            vermontos()
        elif m() == "4":
            lim()
            break