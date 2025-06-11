import os

os.system("cls || clear")
eventos = []
participantes = []
print ("**Evento Especifico/Dia de servicio \n(Dentro de Iglesia)")
evento = input("Escriba el dia del servicio o evento \n-> ")
cant_participantes = int(input("Escriba la cantidad de personas que participaron en el evento \n-> "))
eventos.append(evento)

for i in range(cant_participantes):
    participantes.append([])
    os.system("cls || clear")
    for j in range(1):
        nombre = input(f"Escriba el nombre del participante {i+1}: ").capitalize()
        cant_donado = float(input("Introduzca la cantidad donada por el participante: "))
        participantes[i].append(nombre)
        participantes[i].append(str(cant_donado))

os.system("cls || clear")
a = 1
b = 0
c = ""
for i in participantes:
    c = "".join(i[1])
    c = float(c)
    b += c

d = f"Durante el evento, un total de {len(participantes)} participantes donaron un total de {b:,}"
print(d)

c = "Lista de participantes:"
print(c)

archivo = open("C:\\Users\\USUARIO\\Documents\\Documentos\\o.txt","r")
texto_ini = archivo.read()
archivo = open("o.txt","w")
archivo.close()
archivo = open("o.txt","w")
archivo.write(texto_ini)
archivo.write(d)
archivo.write("\n")
archivo.write(c)
archivo.close()

for i in participantes:
    b = f"{a}) {"".join(i[0])} dono: C$ {"".join(i[1])}"
    archivo = open("o.txt","r")
    texto_ini = archivo.read()
    archivo = open("o.txt","w")
    archivo.close()
    archivo = open("o.txt","w")
    archivo.write(texto_ini)
    archivo.write("\n")
    archivo.write(b)
    archivo.close()
    print(b)
    a += 1