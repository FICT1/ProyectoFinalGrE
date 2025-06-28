from menuprincipal import menup
import time

resultados = menup.iniciar_sesion()

if resultados == True:
    print("Bienvenido")
    time.sleep(2)
    menup.main()