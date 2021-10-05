'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 11
 @enunciado: 
 Haz un programa que pregunte al usuario el número de cuadrados que quiere dibujar, 
 luego que introduzca la anchura del lado y que los dibuje con un patrón concéntrico 
 en el que cada cuadrado sea 10 cm más grande que el anterior.

'''

from turtle import *

turtle = Turtle()

numCuadrados = int(input("¿Cuántos cuadrados quieres dibujar? "))
while numCuadrados<=0:
    numCuadrados = int(input("¿Cuántos cuadrados quieres dibujar? "))

lado = int(input("Introduce la anchura del cuadrado:"))
while lado<=0:
    lado = int(input("Introduce la anchura del cuadrado:"))
    
for i in range(0, numCuadrados):
    for h in range(4):
        turtle.forward(lado+(i*10))
        turtle.left(90)
    turtle.penup()
    turtle.goto((-5*(i+1), -5*(i+1)))
    turtle.pendown()