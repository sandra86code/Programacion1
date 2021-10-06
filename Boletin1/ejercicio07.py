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

#Calcular la raíz cúbica
if num>=0:
    raizCubica=num**(1/3)
else:
    raizCubica=(-num)**(1/3)
    raizCubica=-raizCubica
print("La raíz cúbica de %s es %s" %(num, raizCubica))    

#Calcular la raíz cuadrada
if num>=0:
    raizCuadrada=sqrt(num)
    print("La raíz cuadrada de %s es %s" %(num, round(raizCuadrada,3)))
else:
    print("La raíz cuadrada de un número negativo no tiene solución real.")

    
    
