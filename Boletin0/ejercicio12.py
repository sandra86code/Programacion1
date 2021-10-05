'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 12
 @enunciado: 
 Haz un programa que pregunte al usuario el número de triángulos que quiere dibujar, 
 luego que introduzca la anchura del lado y que los dibuje con un patrón concéntrico 
 en el que cada triángulo sea 10 cm más grande que el anterior.

'''

from turtle import *

turtle = Turtle()

numFigura = int(input("¿Cuántas figuras quieres dibujar? "))
while numFigura<=0:
    numFigura = int(input("¿Cuántas figuras quieres dibujar? "))
    
lado = int(input("Introduce la anchura de la figura:"))
while lado<=0:
    lado = int(input("Introduce la anchura de la figura:"))
    
for i in range(0, numFigura):
    turtle.forward(lado+(i*10))
    turtle.left(120)
    turtle.forward(lado+(i*10))
    turtle.left(120)
    turtle.forward(lado+(i*10))
    turtle.left(120)
    turtle.penup()
    turtle.goto((-5*(i+1), -5*(i+1)))
    turtle.pendown()