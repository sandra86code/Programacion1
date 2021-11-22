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


Puedes hacer este reto como quieras, pero para ayudarte te dejo aquí un fichero con algunas funciones o métodos 
que te recomiendo y una que te dice cómo leer las frases de un fichero (La frase puede contener mayúsculas, 
minúsculas, espacios en blanco, comas, puntos, punto y coma y el usuario podría dar las vocales en minúsculas y 
en mayúsculas). 

Por otro lado te recomiendo crear una lista para los nombres de los jugadores y otra lista para la puntuación de 
los jugadores.
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


#===============================================================================
# Esta función comprueba si los caracteres de una frase (sin contar espacios) 
# coinciden con un caracter o están en una lista de caracteres y los copia 
# en una nueva frase, manteniendo su misma posición
# Si son un espacio, también lo copia tal cual en la nueva frase, en la misma posición. 
# Todos los demás caracteres diferentes al caracter, los sustituye por '-' en la
# nueva frase
# Recibe: una variable string (frase), otra variable string (un caracter, que puede
# ser una vocal o una consonante), una lista de caracteres que ya se han usando.
# Devuelve: la frase resultante, que es una variable de tipo string 
#===============================================================================
def ocultaYDesocultaFrase(frase, caracter, descubiertas):
    fraseResultante=""
    for i in range (len(frase)):
        if frase[i]!=" ":
            if convertirAMinusculas(frase[i])==caracter or convertirAMinusculas(frase[i]) in descubiertas:
                fraseResultante+=frase[i]
            else:
                fraseResultante+="-"
        else:
            fraseResultante+=" "

    return fraseResultante


#===============================================================================
# Esta función comprueba si un caracter está en una frase
# Si lo está, imprime que se encuentra, y si no lo esa, imprime lo contrario.
# Luego descubre usa la función ocultaYDesoculta para mostrarla por el panel con
# las coincidencias acertadas.
# Recibe: un caracter (vocal o consonante), una frase (tipo string) y una lista 
# de caracteres (vocales y consonantes)
# Devuelve: la frase descubierta
#===============================================================================
def jugada(caracter, frase, descubiertas):
    
    if caracter in frase:
        print("La frase incluye la '%s'\n" % caracter)
    else:
        print("La '%s' no está en la frase.\n" % caracter)
    
    fraseDescubierta=ocultaYDesocultaFrase(frase, caracter, descubiertas)
    print("FRASE EN PANEL:\n%s\n" % fraseDescubierta)
    
    return fraseDescubierta


#===============================================================================
# Esta función 
# Recibe: un jugador, la frase ya descubierta, la frase que tenemos que descubrir
# (3 variables de tipo string), los puntos del jugador (variable de tipo int) y
# una lista con los caracteres ya dichos (lista de string)
# Devuelve: una lista con: la frase descubierta (string) tras el turno, los puntos 
# del jugador (int) tras el turno y la lista de caracteres ya dichos (lista de string)
# tras el turno
#===============================================================================      
def turno(jugador, fraseDescubierta, fraseADescubrir, puntos, descubiertas):
    #Bandera que frena el bucle
    sigueTurno=True
    #Creo la variable tipo lista vacía donde voy a acumular los resultados para devolverlos
    resultado=[]
    #Creo un bucle, que mientras tenga la bandera a True y las frases sean diferentes
    #(se acabaría el juego) itera
    while sigueTurno==True and fraseDescubierta!=fraseADescubrir:
        #Si los puntos son menos de 50, no se puede comprar vocal, por lo que
        #la variable turno solo puede ser una consonante
        if puntos<50: 
            print("%s es tu turno, aún no tienes dinero para comprar vocal." %jugador)
            turno="consonante"
        #Si los puntos son mayor o igual que 50, doy la opción al jugador de elegir
        #vocal o consonante
        else:
            turno=input("%s es tu turno, ¿vocal o consonante? " %jugador)
            #Compruebo datos y, si son erróneos vuelvo a preguntarlos
            while turno not in {"vocal", "consonante"}:
                print("Respuesta errónea.")
                turno=input("%s es tu turno, ¿vocal o consonante? " %jugador)
            
        #Si el jugador ha elegido vocal, pregunto por la vocal    
        if turno=="vocal":
            vocal=input("Dime una vocal: ")
            #Si no se recibe una vocal, vuelvo a preguntar
            while vocal not in {"a", "e", "i", "o", "u"}:
                print("La '%s' no es una vocal. Vuelve a intentarlo." % vocal)
                vocal=input("Dime una vocal: ")
            #Compruebo que la vocal no se haya dicho anteriormente, bien sea
            #porque ha sido acierto o error, viendo si está en la lista que acumula
            #los caracteres ya dichos.
            #Si ya se ha dicho, vuelvo a preguntarla
            while vocal in descubiertas:
                print("La '%s' ya se ha dicho. Vuelve a intentarlo." % vocal)
                vocal=input("Dime una vocal: ")
            #Acumulo la vocal en la lista de caracteres ya dichos
            descubiertas.append(vocal)
            #Si la fraseDescubierta ha sufrido modificaciones tras pasar por 
            #la función jugada (es decir, ha habido acierto), la fraseDescubierta 
            #se convierte en lo que devuelve dicha función y sigue el turno (bandera
            #a True)
            if fraseDescubierta!=jugada(vocal, fraseADescubrir, descubiertas):
                fraseDescubierta=jugada(vocal, fraseADescubrir, descubiertas)
                sigueTurno=True
            #Sino, cambio la bandera
            else:
                sigueTurno=False
            #Resto 50 puntos a los puntos del jugador, que es lo que vale comprar
            #vocal
            puntos-=50
        #Si el jugador elige consonante (o no tiene puntos para comprar vocal), pido
        #la consonante    
        else:
            consonante=input("Dime una consonante: ")
            #Compruebo que no sea ni vocal ni espacio y que su tamaño no sea de más de un
            #caracter (de esta manera no descarto otros símbolos, como puntos, puntos y
            #coma, números, etc.). Si los datos son incorrectos, vuelvo a pedir la consonante
            while consonante in {" ", "a", "e", "i", "o", "u"} or len(consonante)!=1:
                print("La '%s' no es una consonante. Vuelve a intentarlo." % consonante)
                consonante=input("Dime una consonante: ")
            #Compruebo que la consonante no se haya dicho anteriormente, bien sea
            #porque ha sido acierto o error, viendo si está en la lista que acumula
            #los caracteres ya dichos.
            #Si ya se ha dicho, vuelvo a preguntarla
            while consonante in descubiertas:
                print("La '%s' ya se ha dicho. Vuelve a intentarlo." % consonante)
                consonante=input("Dime una consonante: ")
            #Acumulo la vocal en la lista de caracteres ya dichos
            descubiertas.append(consonante)
            #Si la fraseDescubierta ha sufrido modificaciones tras pasar por 
            #la función jugada (es decir, ha habido acierto), la fraseDescubierta 
            #se convierte en lo que devuelve dicha función, sigue el turno (bandera
            #a True) y sumo 50 puntos a los puntos del jugador
            if fraseDescubierta!=jugada(consonante, fraseADescubrir, descubiertas):
                fraseDescubierta=jugada(consonante, fraseADescubrir, descubiertas)
                sigueTurno=True
                puntos+=50
            #De lo contrario, cambio la bandera
            else:
                sigueTurno=False

    #Añado en la lista la fraseDescubierta, los puntos del jugador y la lista 
    #de caracteres ya dichos    
    # resultado.append(fraseDescubierta)
    # resultado.append(puntos)    
    # resultado.append(descubiertas)
    
    return [fraseDescubierta,puntos,descubiertas]



#===============================================================================
# Esta función es la principal del programa 
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
#===============================================================================
def main():
    #Creo la lista con los puntos inicializados a 0 para los 3 jugadores
    puntos=[0,0,0]
    #Creo la lista vacía de caracteres que ya han sido dichos por los jugadores
    descubiertas=[]
    #Pregunto la frase que tienen que descubrir los jugadores
    fraseADescubrir=input("Presentador, introduce la frase: ")
    #Creo la frase sobre la que vamos a ir haciendo los cambios y le asigno el
    #valor de la frase Real pasada por la funcion de ocultar y desocultar, para
    #que me ponga todas las vocales y consonantes como "-"
    fraseDescubierta=ocultaYDesocultaFrase(fraseADescubrir, "", descubiertas)  
    #Creo la lista de jugadores
    jugadores=[]
    #Recorro la lista de jugadores, pregunto su nombre y los meto en la lista
    for i in range(3):
        nombre=input("Nombre del jugador %s: " %(i+1))
        jugadores.append(nombre)
    
    #Imprimo la frase oculta    
    print("\nFRASE EN PANEL:\n%s\n" % (fraseDescubierta))
    
    #Creo dos banderas para los bucles que van a recorrer la lista de jugadores
    #y las inicializo a falso   
    bandera=False
    frasesIguales=False
    #El bucle externo me ayudará a que si llevamos al jugador 3 y, no se ha descubierto
    #aún toda la frase, volverá al jugador 1 (ya que i vale 0), por eso solo le pongo 
    #la bandera como
    #condición de entrada
    while bandera==False:
        #El bucle interno recorre la lista de jugadores y usa una bandera, por si la
        #frase se descubre, cambia la bandera y acaba el juego
        i=0
        while i<len(jugadores) and frasesIguales==False:
            #La función turno devuelve una lista de valores, por lo que los guardo
            #en una variable de tipo lista
            resultado=turno(jugadores[i], fraseDescubierta, fraseADescubrir, puntos[i], descubiertas)
            #La nueva fraseDescubierta es el primer elemento de la lista
            fraseDescubierta=resultado[0]
            #Los puntos del jugador que tenga el turno son el segundo elemento de la lista
            puntos[i]=resultado[1]
            #La lista de caracteres ya dichos son el tercer elemento de la lista
            descubiertas=resultado[2]
            #Si la frase que tienen ya descubierta es igual a la frase que tienen que
            #descubrir, cambio las dos banderas y se frenan ambos bucles
            if fraseDescubierta==fraseADescubrir:
                frasesIguales=True
                bandera=True
            #Sino, aumento la i
            else:
                i+=1       
    
    #Creo una variable para comparar con los puntos de cada jugador, la inicializo
    #a 0 para que sea más pequeña (podría ser igual, por eso lo controlo más abajo)    
    puntosGanador=0
    #Recorro la lista de puntos y si los puntos del jugador son más que los puntos del ganador
    #los puntos del ganador pasan a ser los puntos de ese jugador y el ganador se convierte
    #en ese jugador. Si no ocurre esto, digo que el ganador es False, ya que no hay.
    for i in range (len(puntos)):
        if puntos[i]>puntosGanador:
            puntosGanador=puntos[i]
            ganador=jugadores[i]
        else:
            ganador=False
    #Si el ganador es distinto de False, imprimo el mensaje con el jugador que ha ganado
    #Si no, digo que no ha habido un ganador
    if ganador!=False:    
        print("Felicidades %s, ha ganado el juego." %ganador)
    else:
        print("No ha habido ganador en este juego.")

#Llamada la función principal, ya que no tiene argumentos
main()
