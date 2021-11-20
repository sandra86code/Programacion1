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



def mostrarFraseOculta(frase): #Funcionando
    fraseOculta=""
    for i in frase:
        if i!=" ":
            fraseOculta+="-"
        else:
            fraseOculta+=" "
    
    return fraseOculta

#assert(mostrarFraseOculta("El perro de San Roque no tiene rabo")=="-- ----- -- --- ----- -- ----- ----")


def acierto(frase, caracter): #Funcionando
    fraseDescubriendose=""

    for i in frase:
        if i!=" ":
            if convertirAMinusculas(i)==caracter:
                fraseDescubriendose+=i
            else:
                fraseDescubriendose+="-"
        else:
            fraseDescubriendose+=" "

    return fraseDescubriendose

#assert(acierto("El perro de San Roque no tiene rabo", "e")=="E- -e--- -e --- ----e -- --e-e ----")




def mostrarFraseOculta(fraseADescubrir):
        
    fraseOculta=mostrarFraseOculta(fraseADescubrir)
    
    return fraseOculta    



def turnoVocal(frase, vocal):
    
    fraseADescubrir=descubriendoFrase()
    fraseDescubierta=
    vocal=input("Dime una vocal: ")
    while vocal not in {"a", "e", "i", "o", "u"}:
        print("No me has dado una vocal. Vuelve a intentarlo.")
        vocal=input("Dime una vocal: ")
    while vocal in mostrarFraseOculta(fraseADescubrir):
        print("Esa vocal ya está descubierta.")
        vocal=input("Dime una vocal: ")
    if vocal in fraseADescubrir:
        print("La frase incluye la %s" % vocal)
        fraseADescubrir=acierto(fraseADescubrir, vocal)
        print("FRASE EN PANEL:\n%s" % mostrarFraseOculta(fraseADescubrir))
        sigueTurno=True
    else:
        print("La vocal no está en la frase.")
        sigueTurno=False
    
    resultadosTurnoVocal=[sigueTurno, fraseDescubierta]
    
    return resultadosTurnoVocal




        
def turno(jugador, puntos):
    
    sigueTurno=True

    while sigueTurno==True:
        turno=input("%s es tu turno, ¿vocal o consonante? " %jugador)
        while turno not in {"vocal", "consonante"}:
            print("Respuesta errónea.")
            turno=input("%s es tu turno, ¿vocal o consonante? " %jugador)
        
        while turno=="vocal" and puntos>50:
            print("No tiene puntos para comprar una vocal")
        #    turnoConsonante(turno)
        #     if sigueTurno[0]==False:
        #         main()
        #     else:
        #         puntos+=50
            
        if turno=="vocal":
            turnoVocal(mostrarFraseOculta(fraseADescubrir), turno)
            if turnoVocal(frase, vocal)[0]==False:
                main()
            else:
                puntos+=-50
        # else:
        #     turnoConsonante(turno)
        #     if sigueTurno==False:
        #         main()
        #     else:
        #         puntos+=50


    return puntos

def main(jugadores):
    
    fraseEnProceso=mostrarFraseOculta(fraseADescubrir)
    # print(fraseEnProceso)
    while fraseADescubrir!=fraseEnProceso:
        for i in range (len(jugadores)):
            puntos[i]=puntos[i]+turno(jugadores[i], puntos[i])
    
    
    ganador=0
    for i in range (len(puntos)):
        if puntos[i]>ganador:
            ganador=jugadores[i]
    
    print("Felicidades, %s, ha ganado el juego." %jugadores[i])
    
#Creo la frase a descubrir
fraseADescubrir="El perro"


#Creo los jugadores
jugadores=[]
for i in range(3):
    nombre=input("Nombre del jugador %s: " %(i+1))
    jugadores.append(nombre)

#Creo los puntos
puntos=[0,0,0]

main(jugadores)