'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Boletin 6 - Ejercicio 14
 @enunciado: 
Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga. 
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá 
una cualquiera de ellas.
'''

#===============================================================================
# Esta función dice qué cadena de una lista de cadenas es más larga. Si hay dos iguales
# devuelve la que esté en la posición más adelantada
# Recibe: una lista de cadenas
# Devuelve: la cadena más larga de la lista
#===============================================================================
def cadenaMasLarga(lista):
    #Al principio, la palabra más larga es la primera
    longestString=lista[0]
    
    #Ya no necesito recorrer el lista[0], por lo que inicio el bucle en el 1
    for i in range (1,len(lista)):
        #Si la longitud de la cadena de esa posición de la lista es mayor que la longitud
        #de la cadena guardada en longestString, longestString pasa a ser esa cadena
        if len(lista[i])>len(longestString):
            longestString=lista[i]

    return longestString


assert(cadenaMasLarga(["hola", "fisica cuantica", "codigo"])=="fisica cuantica")
assert(cadenaMasLarga(["hola como estas", "codigo", "fisica cuantica", "codigo"])=="hola como estas")
assert(cadenaMasLarga(["codigo", "fisica", "codigo", "hola como estas"])=="hola como estas")
    
    