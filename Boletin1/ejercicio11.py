'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 11
 @enunciado: 
 Escribir un programa que lea un año e indique si es bisiesto. 
 Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400.
'''

#Petición de datos
year=int(input("Introduzca un año: "))

#Calcular si es bisiesto o no
if year%4==0 or (year%100==0 and year%400==0):
    print("El año %s es bisiesto." %(year))
else:
    print("El año %s no es bisiesto." %(year))
