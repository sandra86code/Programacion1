'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 4
 @enunciado: 
 Escribe una función que calcule el combinatorio de dos números.
Combinatorio(n,m) = n! / ( m! * (n-m)!) si n>m
'''

#importo la función ceil que redondea al entero superior
from math import ceil

#===============================================================================
# Esta función calcula el factorial de un número entero positivo
# Recibe: un número entero posiitivo
# Devuelve: su factorial
#===============================================================================
def factorial (num):
    
    factorial=1
    for i in range (1, num+1):
        factorial*=i
    
    return factorial
    
assert(factorial(1)==1)
assert(factorial(2)==2)
assert(factorial(5)==120)


#===============================================================================
# Esta función calcula el combinatorio de dos números entero positivos, siempre
# que el num1 sea mayor que el num2 y que ambos sean mayores que 0
# Recibe: dos números enteros positivos
# Devuelve: su combinatorio
# 
#===============================================================================
def combinatorio (n, m):
    combinatorio="No tiene combinatorio"
    if n>m and n>0 and m>0:
        #Puedo utilizar la función ceil o la round
        combinatorio=ceil(factorial(n) / (factorial(m) * factorial(n-m)))
        # combinatorio=round(factorial(n) / (factorial(m) * factorial(n-m)))

    return combinatorio


assert(combinatorio(10, 9)==10)
assert(combinatorio(21, 3)==1330)
assert(combinatorio(9, 10)=="No tiene combinatorio")
assert(combinatorio(10,-1)=="No tiene combinatorio")
