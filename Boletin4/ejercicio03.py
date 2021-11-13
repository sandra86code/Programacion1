'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 3 
 @enunciado: 
 Diseñar una función que calcule el área y el perímetro de una circunferencia. 
 Utiliza dicha función en un programa que lea el radio de una circunferencia 
 y muestre su área y perímetro.
'''

#Importo pi de la librería math
from math import pi

'''
Esta función calcula el área de una circunferencia
Recibe el radio de la circunferencia
Devuelve:
El área de la circunferencia redondeada a 2 decimales
'''
def calculaAreaCircunferencia(radio):

    return round((radio**2)*pi, 2)


'''
Esta función calcula el perímetro de una circunferencia
Recibe el radio de la circunferencia
Devuelve:
El perímetro de la circunferencia redondeada a 2 decimales
'''
def calculaPerimetroCircunferencia(radio):
    
    return round(2*pi*radio, 2)


#Petición y comprobación de datos
radio=int(input("Introduce el lado de la circunferencia: "))
while radio<=0:
    print("Datos incorrectos. Introduce un valor positivo.")
    radio=int(input("Introduce el lado de la circunferencia: "))
    
    
#Imprimo por consola el aŕea y el perímetro llamando a las funciones con el valor de la variable introducida en línea 38
print("Él área de la circunferencia es %s " %(calculaAreaCircunferencia(radio)))
print("Él perímetro de la circunferencia es %s " %(calculaPerimetroCircunferencia(radio)))