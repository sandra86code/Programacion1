'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Boletin 6 - Ejercicio 2
 @enunciado: 
 Realiza un programa que lea 10 números, debe imprimir los 10 números y después 
 desplazarlos una posición, de tal forma que el último pase a la primera posición, 
 el primero a la segunda, el segundo a la tercera, y así sucesivamente
'''

#===============================================================================
# Esta función desplaza los números una posición a la izquierda, es decir, el
# primer elemento es el último y todos los demás se mueven 1 posición a la izquierda
# Recibe: una lista de números
# Devuelve: otra lista de números
#===============================================================================
def desplazarIzquierda(lista):
    listaDesplazada=[]
    #Recorro la lista desde el item [1] hasta el final y los meto en la nueva lista
    for i in range (1, len(lista)):
        listaDesplazada.append(lista[i])
    #Por último, introduzco el item [0] al final
    listaDesplazada.append(lista[0])
    
    return listaDesplazada


#===============================================================================
# Esta función desplaza los números una posición a la derecha, es decir, el
# último elemento elemento es el primero y todos los demás se mueven 1 posición a la derecha
# Recibe: una lista de números
# Devuelve: otra lista de números
# 
#===============================================================================    
def desplazarDerecha(lista):
    listaDesplazada=[]
    #Primero, introduzco en la nueva lista el último elemento
    listaDesplazada.append(lista[-1])
    #Recorro la lista, item a item, menos el último elemento y los meto en la nueva lista
    for i in range (len(lista)-1):
        listaDesplazada.append(lista[i])
    
    return listaDesplazada


#===============================================================================
# Esta función lee 10 números que el usuario introduce y los mete en una lista
# Recibe: No tiene parámetros de entrada
# Devuelve: No devuelve nada, sino que imprime la lista de números introducidos,
# la lista con los números desplazados una posición a la derecha y la lista con
# los números desplazados a la izquierda
#===============================================================================
def leerNumeros():
    listaNumeros=[]
    for i in range (10):
        num=int(input("Introduce el número %s: " %(i+1)))
        listaNumeros.append(num)
    print("Los números introducidos son: %s" % listaNumeros)
    #Imprimo los resultados de las otras dos funciones
    print("La lista desplazada a la derecha es: %s" % desplazarDerecha(listaNumeros))
    print("La lista desplazada a la izquierda es: %s" % desplazarIzquierda(listaNumeros))

#Llamada a la función, ya que no tiene parámetros    
leerNumeros()