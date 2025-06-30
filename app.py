# Importa el módulo que contiene el sistema de menú principal e inicio de sesión
from menuprincipal import menup
import time

# Ejecuta la función de inicio de sesión del módulo 'menup'
resultados = menup.iniciar_sesion()

# Si el inicio de sesión fue exitoso, se da la bienvenida y se lanza el menú principal
if resultados == True:
    print("Bienvenido")
    time.sleep(2)  # Espera breve para que el usuario lea el mensaje
    menup.main()   # Ejecuta el sistema de menú completo (donaciones, diezmos, ofrendas)
