'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Boletin 6 - Ejercicio 6
 @enunciado: 
 Realizar una función que reciba una lista y devuelva si está ordenada o no. 
 Llamar a dicha función.
'''

#===============================================================================
# Esta función devuelve si una lista (de enteros o de cadenas) está ordenada o no
# Recibe: una lista de enteros o de string
# Devuelve:
# True si la lista está ordenada
# False si la lista no está ordenada
#===============================================================================

#RECORRIENDO LISTA HACIA ATRÁS
def esOrdenada(lista):
    #Como quiero recorrer la cadena al revés (-1,-2,-3, etc.), inicio i a 1
    i=1
    #Bandera
    ordenada=True
    #Recorro el bucle mientras que i [1,len(lista)) y la bandera no cambie
    while i<len(lista) and ordenada==True:
        #Si el item es menor que el item anterior, cambia la bandera, pues
        #la lista no está ordenada
        if lista[-i]<lista[-i-1]:
            ordenada=False
        #Aumento i para otra iteración del bucle
        i+=1

    return ordenada

'''
#RECORRIENDO LISTA HACIA ADELANTE
def esOrdenada(lista):
    i=0
    #Bandera
    ordenada=True
    #Recorro el bucle mientras que i [1,len(lista)) y la bandera no cambie
    while i<len(lista)-1 and ordenada==True:
        #Si el item es mayor que el item posterior, cambia la bandera, pues
        #la lista no está ordenada
        if lista[i]>lista[i+1]:
            ordenada=False
        #Aumento i para otra iteración del bucle
        i+=1
        
    return ordenada
'''

#El 10 como string va antes que el 2, pq compara dígito a dígito
assert(esOrdenada([10,2,3,4,5,6,7])==False)
assert(esOrdenada(["10","2","3","4","5","6","7"])==True)
assert(esOrdenada([1,2,3,4,5,6,7])==True)
assert(esOrdenada([1,2,3,4,5,7,6])==False)
assert(esOrdenada(["a", "e", "i", "o", "u"])==True)
assert(esOrdenada(["amado", "almendra", "izar", "oro", "ulular"])==False)
assert(esOrdenada(["1","4","8","10", "a", "e", "i", "o", "u"])==False)

