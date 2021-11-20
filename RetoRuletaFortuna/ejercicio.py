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

Lo que tendremos que hacer es mostrar una frase oculta y darle el turno al primer jugador, en nuestro caso sería:
    Inma es tu turno , ¿vocal o consonante?

Si dice vocal tendremos que ver si tienen dinero suficiente, si no lo tiene suficiente hay que mostrarle un mensaje 
de error y pedirle una consonante.

En ambos casos se deberá informar si la consonante o vocal dicha esté y mostrar de nuevo la frase con las nuevas 
vocales o consonantes descubiertas y volver a preguntar.

Si no está la vocal o consonante, deberá pasar el turno al siguiente jugador, así hasta que termine el juego.
'''
#===============================================================================
# Esta función calcula si un caracter es minúsculas
# Recibe un caracter
# Devuelve:
# True si el caracter está en minúsculas (usando la función ord() y el número en el código ASCII)
# False si el caracter no está en minúsculas
#===============================================================================
def isMinusculas(caracter):
        
    return ord(caracter)>=97 and ord(caracter)<=122


#===============================================================================
# Esta función devuelve una cadena convertida a minúsculas (funcion cadena.lower())
# Recibe una cadena
# Devuelve: la cadena en minúsculas
#===============================================================================
def convertirAMinusculas(cadena):
    cadenaConvertida=''
    #Recorro la cadena
    for i in cadena:
        #si i es minúsculas o es un espacio, lo acumulo en la cadena convertida
        if isMinusculas(i)==True or i==' ':
            cadenaConvertida+=i
        #Si i es mayúsculas, lo convierto a minúsculas usando ord() y luego como esto es
        #un ordinal y yo necesito el string, uso chr() y lo acumulo en la cadena convertida
        else:
            cadenaConvertida+=chr(ord(i)+32)
  
    return cadenaConvertida



def acierto(frase, caracter, descubiertas): #Funcionando
    
    for i in range (len(frase)):
        if frase[i]!=" ":
            if convertirAMinusculas(frase[i])==caracter or convertirAMinusculas(frase[i]) in descubiertas:
                frase[i]=frase[i]
            else:
                frase[i]="-"
        else:
            frase[i]=" "

    return frase

#assert(acierto("El perro de San Roque no tiene rabo", "e")=="E- -e--- -e --- ----e -- --e-e ----")


def ocultarFrase(frase):
    fraseOcultada=[]
    for i in frase:
        if i!=" ":
            fraseOcultada.append("-")
        else:
            fraseOcultada.append(" ")
            
    return fraseOcultada


#Creo la frase a descubrir

fraseAConvertir=["E", "l", " ", "p", "e", "r", "r", "o"]
fraseReal=["E", "l", " ", "p", "e", "r", "r", "o"]
descubiertas=[]
      
def turno(jugador, fraseAConvertir, fraseReal, puntos):
    
    sigueTurno=True
    

    while sigueTurno==True and fraseReal!=fraseAConvertir:
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
                print("%s no es una vocal. Vuelve a intentarlo." % vocal)
                vocal=input("Dime una vocal: ")
            while vocal in descubiertas:
                print("La vocal %s ya se ha dicho. Vuelve a intentarlo." % vocal)
                vocal=input("Dime una vocal: ")
            if vocal in fraseReal:
                print("La frase incluye la %s\n" % vocal)
                descubiertas.append(vocal)
                fraseAConvertir=acierto(fraseReal, vocal, descubiertas)
                print("FRASE EN PANEL:\n%s" % fraseAConvertir)
                sigueTurno=True
                puntos-=50
            else:
                print("La vocal no está en la frase.\n")
                descubiertas.append(vocal)
                fraseAConvertir=acierto(fraseReal, vocal, descubiertas)
                print("FRASE EN PANEL:\n%s" % fraseAConvertir)
                sigueTurno=False
                puntos-=50
        else:
            consonante=input("Dime una consonante: ")
            while consonante in {" ", "a", "e", "i", "o", "u"} and len(consonante)!=1:
                print("%s no es una consonante. Vuelve a intentarlo." % consonante)
                consonante=input("Dime una consonante: ")
            while consonante in descubiertas:
                print("La consonante %s ya se ha dicho. Vuelve a intentarlo." % consonante)
                consonante=input("Dime una consonante: ")
            if consonante in fraseReal:
                print("La frase incluye la %s\n" % consonante)
                descubiertas.append(consonante)
                fraseAConvertir=acierto(fraseReal, consonante, descubiertas)
                print("FRASE EN PANEL:\n%s" % fraseAConvertir)
                sigueTurno=True
                puntos+=50
                
            else:
                print("La consonante no está en la frase.\n")
                descubiertas.append(consonante)
                fraseAConvertir=acierto(fraseReal, consonante, descubiertas)
                print("FRASE EN PANEL:\n%s" % fraseAConvertir)
                sigueTurno=False
                
        fraseReal=["E", "l", " ", "p", "e", "r", "r", "o"]
        

    return puntos


#Creo los puntos

    



def jugadores():
    puntos=[0,0,0]
    
    jugadores=[]
    
    for i in range(3):
        nombre=input("Nombre del jugador %s: " %(i+1))
        jugadores.append(nombre)
    
    fraseAConvertir=ocultarFrase(fraseReal)    
    print("FRASE EN PANEL:\n%s" % (ocultarFrase(fraseReal)))
    
    bandera=False
    frasesIguales=False
    
    while bandera==False:
        i=0
        while i<len(jugadores) and frasesIguales==False:
            puntos[i]=turno(jugadores[i], fraseAConvertir, fraseReal, puntos[i])
            print(puntos[i])
            print("Puntos de %s: %s" %(jugadores[i],puntos[i]))
            if fraseAConvertir==fraseReal and i!=0:
                frasesIguales=True
                bandera=True
            else:
                i+=1       
        
    puntosGanador=0
    for i in range (len(puntos)):
        if puntos[i]>puntosGanador:
            puntosGanador=puntos[i]
            ganador=jugadores[i]
    
    print("Felicidades, %s, ha ganado el juego." %ganador)


jugadores()




