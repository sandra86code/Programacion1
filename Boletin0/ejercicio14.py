'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 14
 @enunciado: 
 Vamos a hacer un programa que deberá preguntar el ancho del cuadrado 
 que vamos a dibujar y dibujarlo, si el ancho que quiere el usuario es 
 mayor que 500 o menor que 10, se le dirá que no se puede.
'''

from turtle import *

turtle = Turtle()

lado = int(input("¿Cuál es ancho del cuadrado? "))

if lado>=10 and lado<=500:
    turtle.goto(lado, 0)
    turtle.goto(lado, lado)
    turtle.goto(0, lado)
    turtle.goto(0, 0)
else:
    print("No se puede dibujar el cuadrado con las dimensiones proporcionadas")


'''
#Solución 2

from turtle import *

turtle = Turtle()

lado = int(input("¿Cuál es ancho del cuadrado? "))

if lado<10 or lado>500:
    print("No se puede dibujar el cuadrado con las dimensiones proporcionadas")
else:
    turtle.goto(lado, 0)
    turtle.goto(lado, lado)
    turtle.goto(0, lado)
    turtle.goto(0, 0)

'''