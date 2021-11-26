'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 7
 @enunciado: 
 Crea un programa que pregunte cuántos elementos tendremos en un array de
enteros. Posteriormente se preguntarán tantos números como haya indicado el
usuario. Posteriormente, mostraremos por pantalla el mayor, el menor y la media. 
Si el número mayor o menor están repetidos, deberá indicarse cuántas veces se repite.

Por ejemplo:
    Introduzca las posiciones que tendrá el array: 5
    Introduzca el número 1: 4
    Introduzca el número 2: -1
    Introduzca el número 3: 9
    Introduzca el número 4: 5
    Introduzca el número 5: 9
    El mayor número introducido es 9 (se repite 2 veces)
    El menor número introducido es -1
    La media de los números introducidos es: 5.2
'''

#===============================================================================
# Esta función calcula la media de una lista de números usando la suma de los mismos
# entre el número de elementos de la lista
# Recibe: una lista de números
# Devuelve: la media de los números con un redondeo a 2 decimales
#===============================================================================
def calculaMedia(lista):
    suma=0
    for i in lista:
        suma+=i
    
    media=round(suma/len(lista),2)
    
    
    return media

#===============================================================================
# Esta función devuelve el número menor de una lista de números y cuántas veces se
# repite dicho número menor en la lista
# Recibe: una lista de números
# Devuelve: el menor de los números de la lista y el número de repeticiones
#===============================================================================
def calculaMenor(lista):
    menor=lista[0]
    repeticion=0
    for i in range(1, len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    
    for i in range(len(lista)):
        if lista[i]==menor:
            repeticion+=1
            
    return [menor, repeticion]

assert(calculaMenor([27,8,-3,80,27,80])==[-3, 1])
assert(calculaMenor([27,8,-3,-80,27,-80])==[-80, 2])

#===============================================================================
# Esta función calcula el número mayor de una lista de números y cuántas veces se
# repite el número mayor en la lista
# Recibe: una lista de números
# Devuelve: el mayor de los números de la lista y el número de repeticiones
# 
#===============================================================================
def calculaMayor(lista):
    mayor=lista[0]
    repeticion=0
    for i in range (1,len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    
    for i in range(len(lista)):
        if lista[i]==mayor:
            repeticion+=1
    
    return [mayor, repeticion]
    
assert(calculaMayor([27,8,-3,80,27,80])==[80, 2])
assert(calculaMayor([27,8,-3,8,27,80])==[80, 1])



#===============================================================================
# Esta función es el programa principal
# Recibe 
# Devuelve:
# 1. Pide cantidad de números a introducir
# 2. Pide esa cantidad de números y los introduce en una lista
# 3. Imprime los resultados del número mayor, el número menor y la media
#===============================================================================
def main():
    cantidadNumeros=int(input("¿Cuántos números quieres introducir? "))
    listaNumeros=[]
    for i in range (cantidadNumeros):
        num=int(input("Introduce el número %s: " %(i+1)))
        listaNumeros.append(num)


    print("El mayor número introducido es %s (se repite %s veces)" % (calculaMayor(listaNumeros)[0], calculaMayor(listaNumeros)[1]))
    print("El menor número introducido es %s (se repite %s veces)" % (calculaMenor(listaNumeros)[0], calculaMenor(listaNumeros)[1]))
    print("La media de los números introducidos es: %s" % (calculaMedia(listaNumeros)))
    
    
main()