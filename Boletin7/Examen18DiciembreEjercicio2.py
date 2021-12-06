'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 18 Diciembre 2020 - Ejercicio 2 
 @enunciado: 
 Estamos trabajando en una empresa que se dedica a realizar desafíos entre dos 
contrincantes, por ejemplo, contrincante A y contrincante B. 

Un revisor calificalos dos desafíos, otorgando puntos en una escala del 1 al 100 
para tres categorías: claridad del problema, originalidad y dificultad a cada 
uno de los contrincantes.

Al final de la revisión tendremos un array o lista con las calificaciones del 
contrincante A y otro array o lista con las calificaciones del contrincante B. 

En cada array o lista tendremos la calificación a la claridad del problema, 
luego a la originalidad y luego a la dificultad por cada uno de los retos. 
Por ejemplo si han realizado 2 retos, tenemos el siguiente array para el 
contrincante A

[[50,80,20],[60,70,75]]

Lo que indica que en el primer reto en claridad del problema obtuvo un 50, 
en originalidad un 80 y en dificultad un 20, y en el segundo reto obtuvo un 
60 en claridad del problema, un 70 en originalidad y un 75 en dificultad.

El contrincante que gana cada reto será el que obtenga más puntos sumando 
la claridad del problema, la originalidad y la dificultad.


Realizar una función que dado dos listas de calificaciones de los dos contrincantes, 
nos devuelva el número de partidas que ha ganado el primer contrincante.

Realizar un programa que usando la función anterior, pregunte cuántos retos 
van a jugar, luego pregunte la valoración para cada reto y cada participante, 
y por último informe de las partidas ganadas por cada participante.
'''


def sumaPuntosReto(lista):
    
    suma=0
    for i in lista:
        suma+=i
    
    return suma



def compruebaGanadorReto(lista1,lista2):
    
    puntosA=sumaPuntosReto(lista1)
    puntosB=sumaPuntosReto(lista2)
    if puntosA>puntosB:
        ganador="A"
    elif puntosA<puntosB:
        ganador="B"
        
    return ganador



def calculaPartidasJugador (jugadorA, jugadorB):
    
    partidasGanadasA=0
    partidasGanadasB=0
    for partidas in range (len(jugadorA)):
        for j in range (len(jugadorA[partidas])):
            if compruebaGanadorReto(jugadorA[partidas][j], jugadorB[partidas][j])=="A":
                partidasGanadasA+=1
            else:
                partidasGanadasB+=1
            
    return [partidasGanadasA, partidasGanadasB]


# Realizar un programa que usando la función anterior, pregunte cuántos retos 
# van a jugar, luego pregunte la valoración para cada reto y cada participante, 
# y por último informe de las partidas ganadas por cada participante.

def introducirPuntuaciones():
    
    puntuaciones=["Claridad del problema", "Originalidad", "Dificultad"]
    lista=[]
    for i in range (len(puntuaciones)):
        variable=int(input("%s (1-100): " % puntuaciones[i]))
        while variable<1 or variable>100:
            print("Datos incorrectos.")
            variable=int(input("%s (1-100): " % puntuaciones[i]))
        lista.append(variable)
    
    return lista

def main():
    
    numRetos=int(input("¿Cuántos retos van a jugar? "))
    while numRetos<=0:
        print("Datos incorrectos. Introduzca un número mayor que 0.")
        numRetos=int(input("¿Cuántos retos van a jugar? "))
    
    jugadorA=[]
    jugadorB=[]

    for i in range (numRetos):
        jugadorA.append([])
        jugadorB.append([])
        print("\n---- RETO %s ----" % (i+1))
        print("\n-- Puntuaciones del jugador A --")
        jugadorA[i]=introducirPuntuaciones()
        print("\n-- Puntuaciones del jugador B --")
        jugadorB[i]=introducirPuntuaciones()

    partidasGanadasJugadores=calculaPartidasJugador(jugadorA, jugadorB)
    print("El jugador A ha ganado %s partidas." % partidasGanadasJugadores[0])
    print("El jugador B ha ganado %s partidas." % partidasGanadasJugadores[1])
    

main()    