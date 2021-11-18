'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Ejercicios del año pasado - Ejercicio 8
 @enunciado: 
Realizar un programa que pida números enteros hasta que se introduzca un número negativo. 
Escribir una función que:
    1.    Devuelva una lista con todos los que sean primos.
    2.    Devuelva la sumatoria y el promedio de los valores.
    3.    Devuelva una lista con el factorial de cada uno de esos números.
'''

#===============================================================================
# Esta función calcula el factorial de un número 
# Recibe un número entero
# Devuelve: su factorial
#===============================================================================
def factorial(num):
    factorial=1
    for i in range (1, num+1):
        factorial*=i
        
    return factorial


#===============================================================================
# Esta función calcula el factorial de cada uno de los números de una lista (haciendo
# uso de la función factorial(num) y los introduce en una nueva lista 
# Recibe: una lista de enteros
# Devuelve: la lista de factoriales de cada uno de los números de la lista
# 
#===============================================================================
def listarFactorial(lista):
    listaFactorial=[]
    for i in lista:
        listaFactorial.append(factorial(i))
    
    return listaFactorial
        

#===============================================================================
# Esta función suma los números de una lista 
# Recibe: una lista de enteros
# Devuelve: la suma de los números 
#===============================================================================       
def sumarNumeros(lista):
    suma=0
    for i in lista:
        suma+=i
        
    return suma


#===============================================================================
# Esta función devuelve si un número es primo o no
# Recibe: un número entero positivo
# Devuelve:
# True si es primo
# False si no es primo
#===============================================================================
def isPrimo(num):
    i=2
    esPrimo=True
    #Excluyo el 1 porque no es considera número primo y al no entrar por el bucle
    #while, esPrimo sería True, cosa que es errónea.
    if num==1:
        esPrimo=False
    #Recorro los números entre 2 y la mitad del número y si tiene algún divisor
    #cambio la bandera a False para que se frene el bucle
    while i<=(num//2) and esPrimo==True:
        if num%i==0:
            esPrimo=False
        else:
            i+=1
            
    return esPrimo


#===============================================================================
# Esta función comprueba si los números de una lista son primos o no (usando la
# función isPrimo(num) y, de serlo, los mete en una lista 
# Recibe: una lista de números
# Devuelve: la lista con los números primos
#===============================================================================
def primos(lista):
    primos=[]
    for i in lista:
        if isPrimo(i):
            primos.append(i)
           
    return primos

#===============================================================================
# Esta función es la principal del programa
# Recibe: no tiene parámetros
# Devuelve: no tiene return
# 1. Pide números enteros bucle (0 o negativo para parar) y, si son positivos,
# los mete en una lista
# 2. Si la lista no está vacía, lleva a cabo las operaciones de mostrar la lista
# de números primos, sumar los números, hacer la media de los números y mostrar una
# lista con el factorial de cada uno de los números originales.
#===============================================================================
def main():
    numeros=[]
    num=int(input("Introduce un número entero (0 o negativo para parar): "))
    while num>0:
        numeros.append(num)
        num=int(input("Introduce un número entero (0 o negativo para parar): "))
    
    if len(numeros)!=0:
        print("Los números primos introducidos son: %s" % primos(numeros))
        print("La suma de los números introducidos es: %s" % sumarNumeros(numeros))
        print("La suma de los números introducidos es: %s" % round(sumarNumeros(numeros) / len(numeros), 2))
        print("El factorial de cada número es: %s" % listarFactorial(numeros))

#Llamada a la función principal, ya que no tiene return
main()