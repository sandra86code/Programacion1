'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 2 - Ejercicio Extra 6
 @enunciado: 
 Realizar un programa que pregunte el número de partidos jugados en esta jornada. 
 Luego para cada uno de los partidos debe preguntar el número de goles del equipo local 
 y del equipo visitante y el programa debe determinar el resultado de la quiniela. 
 Debe asegurarse que los valores son correctos.
'''

#Pido los datos del número de partidos en la jornada
numPartidos=int(input("Inserta el número de partidos de esta jornada: "))
#Si los datos son erróneos, vuelvo a pedirlos
while numPartidos<=0:
    numPartidos=int(input("Error. Inserta el número de partidos de esta jornada: "))

#Creo un bucle cuyo número de iteraciones es igual a los partidos jugados
for i in range (numPartidos):
    #Pido datos de los goles del equipo local
    golLocal=int(input("Goles del equipo local: "))
    #Si los datos son erróneos, vuelvo a pedirlos
    while golLocal<0:
        golLocal=int(input("Error. Goles del equipo local: "))
    #Pido datos de los goles del equipo visitante
    golVisitante=int(input("Goles del equipo visitante: "))
    #Si los datos son erróneos, vuelvo a pedirlos
    while golVisitante<0:
        golVisitante=int(input("Error. Goles del equipo visitante: "))
    
    #Estructura para comparar el resultado de la quiniela, que guardo en una variable
    if golLocal==golVisitante:
        quiniela="X"
    elif golLocal>golVisitante:
        quiniela="1"
    else:
        quiniela="2"
    #Imprimo el resultado de la quiniela
    print("Resultado de la quiniela: %s" % (quiniela))