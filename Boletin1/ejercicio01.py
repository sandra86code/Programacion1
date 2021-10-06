'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 1
 @enunciado: 
 Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''

from math import sqrt

#Pedir datos y comprobación de que sean mayor de 0
cateto1=int(input("Introduce el primer cateto: "))
while cateto1<=0:
    cateto1=int(input("Error. Introduce el primer cateto: "))
    
cateto2=int(input("Error. Introduce el segundo cateto: "))
while cateto2<=0:
    cateto2=int(input("Error. Introduce el segundo cateto: "))

    
#Cálculo de la hipotenusa
'''Teorema de Pitágonas:
hipotenusa**2 = (cateto1**2) + (cateto2**2)
'''
hipotenusa = sqrt(cateto1**2 + cateto2**2)

#Mostrar resultado por consola
print("La hipotenusa es de " + str(hipotenusa) + " cm.")
