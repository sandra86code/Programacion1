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


#===============================================================================
# Esta función suma los números de una lista
# Recibe: una lista de números
# Devuelve: la suma de los números
#===============================================================================
def sumaPuntosReto(lista):
    
    suma=0
    for i in range (len(lista)):
        suma+=lista[i]
    
    return suma


#===============================================================================
# Esta función comprueba qué jugador tiene más puntos en un reto y, por tanto, lo
# ha ganado
# Recibe: dos listas con los puntos de los jugadores en la partida
# Devuelve:
# "A", si tiene más puntos el jugador "A"
# "B", si tiene más puntos el jugador "B"
# "empate", si ambos jugadores tienen los mismos puntos
#===============================================================================
def compruebaGanadorReto(lista1,lista2):
    
    puntosA=sumaPuntosReto(lista1)
    puntosB=sumaPuntosReto(lista2)
    if puntosA>puntosB:
        ganador="A"
    elif puntosA<puntosB:
        ganador="B"
    else:
        ganador="empate"    
    
    return ganador


#===============================================================================
# Esta función calcula el número de partidas que ha ganado cada jugador y las
# partidas que han empatado
# Recibe: dos listas, cada una de ella con sublistas de enteros positivos que son
# los puntos que ha recibido cada jugador en cada partida.
# Devuelve: una lista con 3 posiciones: la 0 con el número de partidas ganadas por
# el jugador A, la 1 con el número de partidas ganadas por el jugador B, y la 3
# con el número de partidas que han empatado
#===============================================================================
def calculaPartidasJugador (jugadorA, jugadorB):
    
    partidasGanadasA=0
    partidasGanadasB=0
    empates=0
    #Recorro la lista jugadorA (la lista jugadorB tiene la misma dimensión, pues
    #han jugado el mismo número de partidas)
    for partidas in range (len(jugadorA)):
        #Guardo en la variable el resultado de la función que calcula el ganador
        #(o empate) de cada partida
        ganador=compruebaGanadorReto(jugadorA[partidas], jugadorB[partidas])
        if ganador=="A":
            partidasGanadasA+=1
        elif ganador=="B":
            partidasGanadasB+=1
        else:
            empates+=1
        
    return [partidasGanadasA, partidasGanadasB, empates]


#===============================================================================
# Esta función introduce las 3 puntuaciones de una partida en una lista.
# Recibe: no tiene parámetros de entrada
# Devuelve: una lista con las puntuaciones del jugador en la partida
# 
#===============================================================================
def introducirPuntuaciones():
    
    #Creo una lista para no tener que crear 3 variables, ya que todas tienen
    #las mismas condiciones y validación.
    puntuaciones=["Claridad del problema", "Originalidad", "Dificultad"]
    lista=[]
    for i in range (len(puntuaciones)):
        variable=int(input("%s (1-100): " % puntuaciones[i]))
        while variable<1 or variable>100:
            print("Datos incorrectos.")
            variable=int(input("%s (1-100): " % puntuaciones[i]))
        lista.append(variable)
    
    return lista


#===============================================================================
# Esta función es la principal del programa
#===============================================================================
def main():
    #Número de partidas que se van a jugar y validación
    numRetos=int(input("¿Cuántos retos van a jugar? "))
    while numRetos<=0:
        print("Datos incorrectos. Introduzca un número mayor que 0.")
        numRetos=int(input("¿Cuántos retos van a jugar? "))
    
    #Creación de una lista vacía por jugador
    jugadorA=[]
    jugadorB=[]
    
    for i in range (numRetos):
        #Por cada reto se crea una lista vacía dentro de cada jugador
        jugadorA.append([])
        jugadorB.append([])
        #Imprimimos el número de reto
        print("\n---- RETO %s ----" % (i+1))
        #Imprimimos que son las puntuaciones del jugador A
        print("\n-- Puntuaciones del jugador A --")
        #Llamamos a la función que pide e introduce las puntuaciones para el
        #jugador A
        jugadorA[i]=introducirPuntuaciones()
        #Imprimimos que son las puntuaciones del jugador A
        print("\n-- Puntuaciones del jugador B --")
        #Llamamos a la función que pide e introduce las puntuaciones para el
        #jugador B
        jugadorB[i]=introducirPuntuaciones()

    #Guardamos en una variable el resultado de las partidas ganadas por cada
    #jugador y los empates e imprimimos los resultados
    partidasGanadasJugadores=calculaPartidasJugador(jugadorA, jugadorB)
    print("El jugador A ha ganado %s partida(s)." % partidasGanadasJugadores[0])
    print("El jugador B ha ganado %s partida(s)." % partidasGanadasJugadores[1])
    print("Han empatado %s partida(s)." % partidasGanadasJugadores[2])

main()

