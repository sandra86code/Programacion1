'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 5
 @enunciado: 
Crea un programa que solicite 20 números y luego los muestre en el orden inverso al
que se introdujeron.
'''

#===============================================================================
# Esta función invierte el orden de los elementos de una lista
# Recibe: una lista
# Devuelve: la lista invertida
#===============================================================================
def invertirLista(lista):
    listaInvertida=[]
    for i in range (1, len(lista)+1):
        listaInvertida.append(lista[-i])
        
    return listaInvertida

assert(invertirLista([1,2,3,4,5])==[5,4,3,2,1])



#===============================================================================
# Esta función es el programa principal que solicita los 20 números y los introduce
# en una lista. Luego imprime la lista de los números en el orden inverso al introducido
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
# 
#===============================================================================
def solicitaNumeros():
    numeros=[]
    for i in range (20):
        num=int(input("Introduce un número: "))
        numeros.append(num)
    
    print(invertirLista(numeros))

solicitaNumeros()
    