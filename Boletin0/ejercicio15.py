'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 15
 @enunciado: 
 Calcular el perímetro y área de un rectángulo dada su base y su altura 
 que será preguntado al usuario (Si los datos no son válidos mostrar mensaje de error).

'''

from turtle import *

turtle = Turtle()

base = int(input("Dime la base del cuadrado: "))
while base<=0:
    print("Error. Los datos proporcionados deben ser enteros positivos.")
    base = int(input("Dime la base del cuadrado: "))
    
altura = int(input("Dime la altura del cuadrado: "))
while altura<=0:
    print("Error. Los datos proporcionados deben ser enteros positivos.")
    altura = int(input("Dime la altura del cuadrado: "))
    
for i in range(2):
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    
print("El área del rectángulo es "+ str(base*altura) + " cm2")
print("El perímetro del rectángulo es "+ str((2*base)+(2*altura)) + " cm.")