'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 4
 @enunciado: 
 Vamos a hacer un programa que nos pregunte el nombre y la edad y 
 nos diga Hola seguido de nuestro nombre y una línea que será mayor 
 o menor en función de la edad que tengamos.

'''

from turtle import *

turtle = Turtle()

nombre = input("What's your name?")
edad = int(input("How old are you?"))

while edad<0:
    edad = int(input("How old are you?"))
    
print("Hola, " + nombre)

turtle.forward(edad)