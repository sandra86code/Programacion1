'''
Ejercicio que solicite nombre y lo guarde en una lista para imprimirlos
luego.
Después de cada nombre debe preguntar si quiere introducir más o no (s/n)
'''

names=[]

respuesta='s'
while respuesta=='s':
    nombre=input("Introduce un nombre: ")
    names.append(nombre)
    respuesta=input("Quieres continuar? (s/n): ")
    while respuesta not in ['s', 'n']:
        respuesta=input("Quieres continuar? (s/n): ")

print(names)
