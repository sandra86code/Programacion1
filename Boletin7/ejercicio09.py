'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 9
 @enunciado: 
Escribir una función que reciba una lista de números enteros y un entero k. 
Escribir tres funciones:
    - Una que devuelva una lista con los menores de k, 
    - Otra función devueva los mayores y otra los iguales a k. 
    - Por último, otra función que devuelva una lista con aquellos que son múltiplos de k.
'''
#===============================================================================
# Esta función comprueba qué elementos de una lista de números son múltiplos de otro número
# Recibe: una lista de números y un número entero
# Devuelve: una lista con los múltiplos
#===============================================================================
def multiplosDeNum(numeros, num):
    multiplos=[]
    for i in numeros:
        if i!=num and i%num==0:
            multiplos.append(i)
            
    return multiplos


#===============================================================================
# Esta función comprueba qué elementos de una lista de números son mayores o iguales
# que otro número.
# Recibe: una lista de números y un número entero
# Devuelve: una lista con los números mayores o iguales
#===============================================================================
def mayoresIgualesQueNum(numeros, num):
    numMayoresIguales=[]
    for i in numeros:
        if i>=num:
            numMayoresIguales.append(i)
            
    return numMayoresIguales


#===============================================================================
# Esta función comprueba qué elementos de una lista de números son menores
# que otro número.
# Recibe: una lista de números y un número entero
# Devuelve: una lista con los números menores
#===============================================================================
def menoresQNum(numeros, num):
    numMenores=[]
    for i in numeros:
        if i<num:
            numMenores.append(i)
    
    return numMenores


#===============================================================================
# Esta función es la principal del programa
# Recibe: no tiene parámetros
# Devuelve: no tiene return
# 1. Pide números y, mientras que sean diferente de 0, los mete en una lista
# 2. Pide el número para comparar, que tiene que ser diferente de 0.
# 3. Imprime los resultados del resto de funciones
#===============================================================================
def main():
    lista=[]
    num=int(input("Introduce un número en la lista (0 para parar): "))
    while num!=0:
        lista.append(num)
        num=int(input("Introduce un número en la lista (0 para parar): "))
    numK=int(input("Introduce el número para comparar (distinto de 0): "))
    while numK==0:
        print("Datos erróneos. No puede ser 0.")
        numK=int(input("Introduce el número para comparar (distinto de 0): "))
    
    print("Los números menores que %s son: %s" % (numK, menoresQNum(lista, numK)))
    print("Los números mayores o iguales que %s son: %s" % (numK, mayoresIgualesQueNum(lista, numK)))
    print("Los números múltiplos de %s son: %s" % (numK, multiplosDeNum(lista, numK)))

#Llamada a la función, ya que no tiene return
main()

