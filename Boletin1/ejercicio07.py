'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 7 
 @enunciado: 
 Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?

#La raíz cúbica se puede expresar con potencias: x**1/3
'''

#Importar la función de raíz cuadrada
from math import sqrt

#Pedir datos
num=int(input("Dime un número: "))

#Comprobación de positivos
if num>=0:
    #Calcular la raíz cuadrada
    raizCuadrada=sqrt(num)
    print("La raíz cuadrada de %s es %s" %(num, round(raizCuadrada,3)))
    #Calcular la raíz cúbica
    raizCubica=num**(1/3)
    print("La raíz cúbica de %s es %s" %(num, round(raizCubica,3)))
else:
    print("Error. Debe introducir un número mayor o igual que 0")