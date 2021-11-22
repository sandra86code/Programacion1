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

# # Importo la librería para generar un número aleatorio
# from random import uniform
#
#
# # Método que devuelve el refrán o frase que se va a usar para que los jugadores
# # la acierten.
#
# def refran():
#     f = open ('ruleta.txt','r')
#     mensaje = f.read()
#     f.close()
#     # ahora mismo lo que tenemos en mensaje es una cadena con todo 
#     # el fichero. Las líneas estarán separadas por \n
#
#     # Pasar el mensaje a un array o lista en el que cada elemento sea una
#     # linea o frase
#
#
#
#     # Generar un número aleatorio entre 0 y uno menos de la longitud de la lista
#
#
#     # Devolver ese elemento
#     return refran
#
# # Oculta el refrán. Método que recibe una cadena y devuelve la cadena cambiando 
# # las letras por guion medio, ten encuenta que los espacio, las comas, los puntos y los
# # punto y coma no los debe cambiar. (sólo se admiten esos carácteres de separción)
# def oculta(refran):
#
#
# # Comprobar letra: Método o función que recibe una cadena oculta, otra cadena completa y un carácter
# # Deberá comprobar si el carácter está en la cadena completa y si es así, ponerlo en la posición de 
# # la cadena oculta para que se vea.
# def comprobar(oculto, refran, letra):
#
#
#
# # iguales refran: método que recibe dos cadenas y comprueba si son siguales o no.
# def iguales(cad1, cad2):

