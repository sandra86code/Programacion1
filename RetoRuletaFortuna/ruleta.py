'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 19 nov 2021
 @nombre: Reto Ruleta de la Fortuna
 @enunciado: La ruleta de la fortuna

Vamos a hacer la ruleta de la suerte, para ellos vamos a pensar que hay tres jugadores, en principio 
le pediremos el nombre y tendremos que irle dando el turno de forma secuencial empezando por el primero. 
Es decir, sería preguntar el nombre de los tres concursantes, por ejemplo:

Dime tu nombre: "Inma"
Dime tu nombre: "Juan"
Dime tu nombre: "Pepe"

Todos los jugadores, que empezarán con cero puntos, consiguen 50 puntos por cada consonante acertada (tantas como 
haya) y para comprar vocal tienen que tener 50 puntos que será lo que cueste la vocal.

Lo que tendremos que hacer es mostrar una refran oculta y darle el turno al primer jugador, en nuestro caso sería:
    Inma es tu turno , ¿vocal o consonante?

Si dice vocal tendremos que ver si tienen dinero suficiente, si no lo tiene suficiente hay que mostrarle un mensaje 
de error y pedirle una consonante.

En ambos casos se deberá informar si la consonante o vocal dicha esté y mostrar de nuevo la refran con las nuevas 
vocales o consonantes descubiertas y volver a preguntar.

Si no está la vocal o consonante, deberá pasar el turno al siguiente jugador, así hasta que termine el juego.


Puedes hacer este reto como quieras, pero para ayudarte te dejo aquí un fichero con algunas funciones o métodos 
que te recomiendo y una que te dice cómo leer las frases de un fichero (La refran puede contener mayúsculas, 
minúsculas, espacios en blanco, comas, puntos, punto y coma y el usuario podría dar las vocales en minúsculas y 
en mayúsculas). 

Por otro lado te recomiendo crear una lista para los nombres de los jugadores y otra lista para la puntuación de 
los jugadores.
'''

# Importo la librería para generar un número aleatorio
from random import randint


#===============================================================================
# Método que devuelve el refrán o refran que se va a usar para que los jugadores
# la acierten.
#===============================================================================
def generaRefran():
    f = open ('ruleta.txt','r')
    mensaje = f.read()
    f.close()
    # ahora mismo lo que tenemos en mensaje es una cadena con todo 
    # el fichero. Las líneas estarán separadas por \n

    # Pasar el mensaje a un array o lista en el que cada elemento sea una
    # linea o refran
    cadena=""
    listaRefranes=[]
    for i in mensaje:
        if i!="\n":
            cadena+=i 
        else:
            listaRefranes.append(cadena)
            cadena=""
    if cadena!="":
        listaRefranes.append(cadena)

    # Generar un número aleatorio entre 0 y uno menos de la longitud de la lista
    num=randint(0,3)

    # Devolver ese elemento
    return listaRefranes[num]


#===============================================================================
# Oculta el refrán. 
# Método que recibe una cadena y devuelve la cadena cambiando las letras por guion 
# medio, ten encuenta que los espacios, las comas, los puntos y los punto y coma 
# no los debe cambiar (sólo se admiten esos carácteres de separación).
#===============================================================================
def ocultaRefran(refran):
    refranOculto=""
    for i in range (len(refran)):
        if refran[i] in {" ", ",", ".", ";"}:
            refranOculto+=refran[i]
        else:
            refranOculto+="-"

    return refranOculto


#===============================================================================
# Comprobar letra: 
# Método o función que recibe una cadena oculta, otra cadena completa y un carácter.
# Deberá comprobar si el carácter está en la cadena completa y si es así, ponerlo
# en la posición de la cadena oculta para que se vea.
#===============================================================================
def comprobarLetra(refranOculto, refran, letra):
    numAciertos=0
    refranComprobado=""
    for i in range (len(refran)):
        if refran[i]==letra.lower() or refran[i]==letra.upper():
            refranComprobado+=refran[i]
            numAciertos+=1
        else:
            refranComprobado+=refranOculto[i]
    
    return [refranComprobado, numAciertos]   


#===============================================================================
# Son Refranes Iguales
# Método que recibe dos cadenas y comprueba si son siguales o no.
#===============================================================================
def sonRefranesIguales(cad1, cad2):
    
    return cad1==cad2



#===============================================================================
# Esta función 
# Recibe: un jugador, la refran ya descubierta, la refran que tenemos que descubrir
# (3 variables de tipo string), los puntos del jugador (variable de tipo int) y
# una lista con los caracteres ya dichos (lista de string)
# Devuelve: una lista con: la refran descubierta (string) tras el turno, los puntos 
# del jugador (int) tras el turno y la lista de caracteres ya dichos (lista de string)
# tras el turno
#===============================================================================      
def turno(jugador, refran, refranOculto, puntos):
    sigueTurno=True

    while sigueTurno==True and sonRefranesIguales(refran, refranOculto)==False:
        #Imprimo la refran oculta    
        print("\nFRASE EN PANEL:\n%s\n" % (refranOculto))
        
        if puntos<50: 
            print("%s es tu turno, aún no tienes dinero para comprar vocal." %jugador)
            turno="consonante"
        else:
            turno=input("%s es tu turno, ¿vocal o consonante? " %jugador)
            while turno not in {"vocal", "consonante"}:
                print("Respuesta errónea.")
                turno=input("%s es tu turno, ¿vocal o consonante? " %jugador)
            
        if turno=="vocal":
            vocal=input("Dime una vocal: ")
            while vocal not in {"a", "e", "i", "o", "u"}:
                print("La '%s' no es una vocal. Vuelve a intentarlo." % vocal)
                vocal=input("Dime una vocal: ")
            jugada=comprobarLetra(refranOculto, refran, vocal)
            refranOculto=jugada[0]
            aciertos=jugada[1]
            if aciertos==0:
                print("La '%s' no se encuentra en el refrán." % vocal)
                sigueTurno=False
            else:
                sigueTurno=True
            puntos-=50
             
        else:
            consonante=input("Dime una consonante: ")
            while consonante not in {"b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"}:
                print("La '%s' no es una consonante. Vuelve a intentarlo." % consonante)
                consonante=input("Dime una consonante: ")
            jugada=comprobarLetra(refranOculto, refran, consonante)
            refranOculto=jugada[0]
            aciertos=jugada[1]
            if aciertos==0:
                print("La '%s' no se encuentra en el refrán." % consonante)
                sigueTurno=False
            else:
                sigueTurno=True
                puntos+=(50*aciertos)
    
    return [refranOculto, puntos]



#===============================================================================
# Esta función es la principal del programa 
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
#===============================================================================
def main():
       
    #Creo la variable refran y refran Oculto llamando a las funciones
    refran=generaRefran()
    refranOculto=ocultaRefran(refran)
    #Creo la lista de jugadores
    jugadores=[]
    #Recorro la lista de jugadores, pregunto su nombre y los meto en la lista
    for i in range(3):
        nombre=input("Nombre del jugador %s: " %(i+1))
        jugadores.append(nombre)
    
    #Creo la lista con los puntos inicializados a 0 para los 3 jugadores
    puntos=[0,0,0]
    
    #Creo dos banderas para los bucles que van a recorrer la lista de jugadores
    #y las inicializo a falso   
    bandera=False
    refranesIguales=False
    while bandera==False:
        #El bucle interno recorre la lista de jugadores y usa una bandera, por si el
        #refran se descubre, cambia la bandera y acaba el juego
        i=0
        while i<len(jugadores) and refranesIguales==False:
            turnoJugador=turno(jugadores[i], refran, refranOculto, puntos[i])
            refranOculto=turnoJugador[0]
            puntos[i]=turnoJugador[1]
            if sonRefranesIguales(refran, refranOculto):
                refranesIguales=True
                bandera=True
            else:
                i+=1       
    
    #Creo una variable para comparar con los puntos de cada jugador, la inicializo
    #a 0 para que sea más pequeña (podría ser igual, por eso lo controlo más abajo)    
    puntosGanador=0
    #Recorro la lista de puntos y si los puntos del jugador son más que los puntos del ganador
    #los puntos del ganador pasan a ser los puntos de ese jugador y el ganador se convierte
    #en ese jugador.
    for i in range (len(puntos)):
        if puntos[i]>puntosGanador:
            puntosGanador=puntos[i]
            ganador=jugadores[i]
    
    print("Felicidades %s, ha ganado el juego." %ganador)


main()
