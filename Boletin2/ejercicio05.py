"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 5
 @enunciado: 
Design a program that asks for numbers until the user inputs a negative one. 
When this happens, the program will show how many positive numbers have been
introduced by the user. 
The messages are the following:
"Enter a number (negative to finish):"
"You have entered XX positive numbers."
 """

#Inicializo la variable número asignándole un valor positivo para que entre en el bucle while posterior 
num=1
#Inicializo la variable contador a 0 para en el bucle while
contador=0

#Bucle while en el que se entra con números positivos y el 0. Para con negativos
while num>=0:
    #Pido los datos
    num=int(input("Introduce un número (negativo para finalizar): "))
    #Si el número es positivo se incrementa, con 0 no
    if num>0:
        contador+=1

#Muestro resultado por consola
print("Has introducido %s números positivos." %(contador))