#Calcular si recibio algun monto extra o regalo de fuera de la iglesia
#Se le preguntara al usuario si recibio algun monto extra o regalo de fuera de la iglesia
#agregarlo a una opcion de menu 
#hacerlo todo en funciones separadas y en archivos separados
#Se ha hecho alguna donacion extra en la iglesia??
#una bienvenida para el usuario

from operaciones import (
    cargar_datos, menu, agregarmonto, agregarespecie,
    vermontos, verespecies, eliminarmontos, eliminarespecie
)

def main():
    cargar_datos()
    while True:
        opcion = menu()
        if opcion == '1':
            agregarmonto()
        elif opcion == '2':
            agregarespecie()
        elif opcion == '3':
            vermontos()
        elif opcion == '4':
            verespecies()
        elif opcion == '5':
            eliminarmontos()
        elif opcion == '6':
            eliminarespecie()
        elif opcion == '7':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")
            input("Presiona Enter para continuar...")

main()
