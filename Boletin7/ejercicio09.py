'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 9
 @enunciado: 
 Crear un programa que sirva para crear una combinación de números de la lotería
Primitiva. 
Debe crear una combinación de 6 números diferentes entre 1 y 49.
'''

#Importo la funcion randint de la libreria random
from random import randint

#===============================================================================
# Esta función crea una lista de 6 números aleatorios que no se repiten
# Recibe: no tiene parámetros de entrada
# Devuelve: la lista con los 6 números aleatorios sin repetir
#===============================================================================
def combinacionPrimitiva():
    primitiva=[]
    for i in range (6):
        num=randint(1,49)
        #Si el número aleatorio ya está en la lista, lo vuelve a pedir, así evito
        #que haya números repetidos
        while num in primitiva:
            num=randint(1,49)
        #Inserto el número aleatorio en la lista
        primitiva.append(num)
        
    return primitiva

print(combinacionPrimitiva())
