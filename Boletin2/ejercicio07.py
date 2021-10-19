"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 7
 @enunciado: 
Design a program that asks how many numbers the user wants to write. 
After the user enters all numbers, the program should say the medium of the numbers. 
If the user inputs a wrong number, the program should ask for it again. 
The messages are the following:
"How many numbers do you want input?" to ask for the number of numbers.
"Enter one number greater than 0:" to ask for a number.
"The number is not valid, it should be greater than 0" to inform that the number is not
valid.
"The medium is XX.XX" to show the result.
 """
 
#Petición de cantidad de números que el usuario quiere introducir  
cantidadNumeros=int(input("¿Cuántos números quieres introducir? "))
#Compruebo que el dato sea positivo, si es negativo o 0, vuelvo a preguntar
while cantidadNumeros<=0:
    cantidadNumeros=int(input("Error. ¿Cuántos números quieres introducir? "))

#Inicializo la variable suma a 0 que voy a utilizar en el bucle for posterior
suma=0

#Bucle for cuyo rango es la cantidad de números que el usuario ha introducido
for i in range (cantidadNumeros):
    #Pido los números
    num=int(input("Introduce un número mayor que 0: "))
    #Si el número es negativo, muestro un mensaje de error y vuelvo a pedirlo
    while num<=0:
        print("El número no es válido, debería ser mayor que 0.")
        num=int(input("Introduce un número mayor que 0: "))
    #Con cada iteración del bucle, se suma el número introducido a la variable suma    
    suma+=num

#Creo una variable para calcular la media    
media=suma/cantidadNumeros

#Muestro el resultado por pantalla
print("La media es %s" %(round(media,2)))
