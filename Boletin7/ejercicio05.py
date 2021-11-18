'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Ejercicios del año pasado - Ejercicio 5
 @enunciado: 
Realizar un función que reciba una lista y devuelva una nueva lista cuyo 
contenido sea igual a la original pero invertida. 
Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver 
[‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]. 
Llamar a dicha función
'''

#===============================================================================
# Esta función devuelve una lista pero con el orden inverso de sus elementos
# Recibe: una lista
# Devuelve: la lista en orden invertida
#===============================================================================
def listaALaInversa(lista):
    listaInversa=[]
    for i in range (1, len(lista)+1):
        listaInversa.append(lista[-i])

    return listaInversa


assert(listaALaInversa(['Di', 'buen', 'dia', 'a', 'papa'])==['papa', 'a', 'dia', 'buen', 'Di'])
        