'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Ejercicios del año pasado - Ejercicio 4
 @enunciado: 
Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
 Muestra el máximo de los números guardado en la lista, muestra los números pares.
'''
#===============================================================================
# Esta función comprueba qué números de una lista de números son pares y los mete
# en otra lista
# Recibe: una lista de números
# Devuelve: una lista con los números pares de la lista original
# 
#===============================================================================
def listaPares (lista):
    pares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
            
    return pares


#===============================================================================
# Esta función calcula el número mayor de los números de una lista
# Recibe: una lista de números
# Devuelve: el número mayor
# 
#===============================================================================
def numMayor(lista):
    #Inicializo la variable a 0 porque va a ser siempre menor que cualquier número de
    #la lista, que son todos números positivos
    numMayor=0
    for i in lista:
        if i>numMayor:
            numMayor=i
            
    return numMayor


#===============================================================================
# Esta función es la parte principal del programa
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
# 1. Pregunta un número y si este no es negativo, lo mete en una lista. Si el número
# es negativo, el programa para.
# 2. Imprime el número mayor de la lista
# 3. Muestra una lista solo con los números pares
#===============================================================================
def leeNumeros():
    num=int(input("Introduce un número: "))
    listaNumeros=[]
    while num>0:
        listaNumeros.append(num)
        num=int(input("Introduce un número: "))
    #En el caso de que la lista esté vacía, porque el primer número introducido sea
    #un negativo, no muestra nada. De lo contrario, imprime los resultados
    if len(listaNumeros)!=0:
        print("El número mayor introducido es: %s" % numMayor(listaNumeros))
        print("Los números pares introducidos son: %s" % listaPares(listaNumeros))

#Llamada a la función, ya que no tiene return        
leeNumeros()