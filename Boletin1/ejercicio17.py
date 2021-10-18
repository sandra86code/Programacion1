'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 17
 @enunciado: 
 Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario
'''

#Petición de datos
numA=int(input("Introduzca un número: "))
numB=int(input("Introduzca otro número "))

#Comprobar cuál es el límite inferior y el límite superior del bucle
if numA<numB:
    #Bucle entre límite interior y superior
    for i in range(numA+1, numB):
        #Cálculo e impresión de números pares
        if i%2==0:
            print(i)
else:
    #Bucle entre límite interior y superior
    for i in range(numA-1, numB, -1):
        #Cálculo e impresión de números pares
        if i%2==0:
            print(i)