"""
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 3
 @enunciado: 
Design a program that asks how many numbers the user wants to introduce. 
Then, the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. 
If the user inputs 0 or a negative number, it is not valid, and the system should 
ask for another number. 
The messages are the following:
"How many numbers do you want input?" to ask for the number of numbers.
"Enter one number greater than 0:" to ask for a number.
"The number is not valid, it should be greater than 0" to inform that the number is not
valid.
"The number XX is odd"
"The number XX is even"

 """

#Petición de cantidad de números que el usuario quiere introducir 
cantidadNumeros=int(input("¿Cuántos números quieres introducir? "))
#Compruebo que el dato sea positivo, si es negativo o 0, vuelvo a preguntar
while cantidadNumeros<=0:
    cantidadNumeros=int(input("Error. ¿Cuántos números quieres introducir? "))
    
#Bucle for cuyo rango es la cantidad de números que el usuario ha introducido
for i in range (cantidadNumeros):
    #Pido el número
    num=int(input("Introduce un número mayor que 0: "))
    #Bucle while para mostrar mensaje de error y volver a pedir el número si el introducido es menor o igual que 0
    while num<=0:
        print("El número no es válido, debería ser mayor que 0.")
        num=int(input("Introduce un número mayor que 0: "))
    #Estructura lógica en la que imprime si el número es par o impar
    if num%2==0:
        print("El número %s es par." % (num))
    else:
        print("El número %s es impar." % (num))