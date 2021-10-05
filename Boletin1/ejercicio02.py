'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 2
 @enunciado: 
 Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
'''

#Pedir datos
fahrenheit=int(input("Dime los grados Fahrenheit: "))

#Cálculo de Fahrenheit a Celcius
celcius=(fahrenheit-30)/2

#Mostrar resultado por consola
print("%s F son %s ºC" %(fahrenheit, celcius))