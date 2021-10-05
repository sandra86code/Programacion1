'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 10
 @enunciado: 
 Haz un programa que pregunte el lado de un cuadrado y luego lo dibuje. 
 En el caso de que los datos no sean correctos, debe mostrar un error por consola.

'''

from turtle import *

turtle = Turtle()

lado = int(input("Introduce la anchura del cuadrado:"))

if lado>0:
    turtle.forward(lado)
    turtle.right(90)
    turtle.forward(lado)
    turtle.right(90)
    turtle.forward(lado)
    turtle.right(90)
    turtle.forward(lado)
else:
    print("Tiene que introducir un número positivo")