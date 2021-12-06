'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 18 Diciembre 2020 - Ejercicio 1 
 @enunciado: 
 Un anagrama es el procedimiento de crear una palabra a partir de otra reordenando 
las letras de la primera palabra, por lo tanto diremos que una palabra es un 
anagrama de otra si la primera palabra se puede formar a partir de las letras 
de la otra y no es la misma palabra.

Realizar una función que reciba como argumento dos palabras y devuelva verdadero 
si dichas palabras son anagramas y falso en caso contrario, por ejemplo “sergio” 
y “riesgo”

Realizar las llamadas necesarias para probar la función anterior de forma que 
se testee que funciona bien la función en todos los posibles casos.

** Considera sólo palabras cuyas letras tengan una sola ocurrencia.
'''

#===============================================================================
# Esta función comprueba si dos palabras son anagramas (con las letras de una
# se puede componer la otra palabra). Solo tiene en cuenta palabras cuyas
# letras tengan una sola ocurrencia.
# Recibe: dos palabras (variables strings)
# Devuelve:
# True si son anagramas
# False si no son anagramas
#===============================================================================
def esAnagrama(palabra1, palabra2):
    
    #Compruebo que la longitud de las dos palabras sean igual
    if len(palabra1)==len(palabra2):
        #Recorro la primera palabra
        for i in range (len(palabra1)):
            j=0
            anagrama=False
            #Recorro la segunda palabra
            while j<len(palabra2) and anagrama==False:
                #Si las letras coinciden, cambio la bandera y freno el bucle
                if palabra1[i]==palabra2[j]:
                    anagrama=True
                j+=1              
    #Si la longitud de las dos palabras no es igual, no pueden ser anagramas.
    else:
        anagrama=False
        
    return anagrama


assert(esAnagrama("riesgo", "sergio")==True)
assert(esAnagrama("riosga", "sergio")==False)
assert(esAnagrama("riosgae", "sergio")==False)
assert(esAnagrama("riosga", "sergioz")==False)