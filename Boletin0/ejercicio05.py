'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 5 
 @enunciado: 
 Vamos a hacer un programa que nos pregunte la edad:
 - Si la edad es menor de 25 años, nos debe pintar una flecha de color rojo.
 - Si la edad es menor de 50, nos debe pintar una flecha de color azul.
 - Para los demás datos, debe pintar una fleja de color verde.
 
'''

from turtle import *

turtle = Turtle()

edad = int(input("How old are you?"))
while edad<0:
    edad = int(input("How old are you?"))

if edad<25:
    turtle.color(255, 0, 0)
elif edad<50:
    turtle.color(0, 255, 0)
else:
    turtle.color(0, 0, 255)
    
turtle.forward(edad)