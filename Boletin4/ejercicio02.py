'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 2
 @enunciado: 
 Crear una función que calcule la temperatura media de un día a partir de la temperatura
máxima y mínima. 
Crear un programa, que utilizando la función anterior, vaya pidiendo la temperatura 
máxima y mínima de cada día y vaya mostrando la media. 
El programa pedirá el número de días que se van a introducir.
'''

'''
Esta función calcula la temperatura media 
Recibe la temperatura máxima y la temperatura mínima (dos números de tipo float)
Devuelve:
La temperatura media con un redondeo de 2 decimales
'''
def calculaTMedia(tMin, tMax):
    tMedia=(tMin+tMax)/2
    
    return round(tMedia,2)

'''
Esta función pregunta la temperatura mínima y la temperatura máxima, calcula e imprime la media de ambas
el número de veces del parámetro de entrada
Recibe un número de días (entero positivo)
Devuelve:
No devuelve nada
'''
def pideTemperatura(numDias):
    for i in range (numDias):
        tMin=float(input("Introduce la temperatura mínima del día: "))
        tMax=float(input("Introduce la temperatura máxima del día: "))
        print("La temperatura media del día ha sido %s" %(calculaTMedia(tMin,tMax)))
        
#Petición y comprobación de datos        
numDias=int(input("¿Cuántos días quieres introducir? "))
while numDias<=0:
    print("Datos incorrectos. Vuelve a intentarlo.")
    numDias=int(input("¿Cuántos días quieres introducir? "))
  
        
#Llamada a la función con los datos que hemos pedido
pideTemperatura(numDias) 