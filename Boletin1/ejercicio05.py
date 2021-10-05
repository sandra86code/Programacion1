'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 5
 @enunciado: 
 Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo).
'''
from _operator import abs

#Petición de datos
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el primer número: "))

#Cálculo y salida de datos por consola
print("El valor absoluto de la diferencia entre %s y %s es %s." %(num1, num2, abs(num1-num2)))