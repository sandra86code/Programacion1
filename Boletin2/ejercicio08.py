"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 8 
 @enunciado: 
Design a program that asks for a set of numbers. 
After inputting each number, the program should ask:
"Do you want to enter more numbers (Y/N)?". 
If the answer is "Y" the program asks for other numbers. 
When the user finishes to enter all the numbers,
the program should say which one is the smallest. 
The messages are the following:
"Enter one number:"
"Do you want to enter more number (Y/N)?"
"The smallest number is XX"
 """
 
#Inicializo variable de tipo String para que entre en el bucle al principio
respuesta="S"
#Inicializo variable de tipo numérico con un número muy grande, que lo será más que el primer número que introduzca el usuario
smallestNum=99999999999

#Bucle while cuya condición de entrada es que la variable respuesta sea "S", con otra respuesta para
while respuesta=="S":
    #Pido datos al usuario
    num=int(input("Introduce un número: "))
    #Si el num introducido es menor que la variable smallestNum, el smallestNum pasa a ser el num. Sino, smallestNum no cambia.
    #Así obtengo siempre el más pequeño
    if num<smallestNum:
        smallestNum=num
    
    #Pido datos al usuario    
    respuesta=input("¿Quiere introducir más números (S/N)? ")
    #Mientras la respuesta no sea correcta, vuelvo a preguntar.
    #Esto hace que la condición de salida del bucle solo pueda ser "N"
    while respuesta not in {"S", "N"}:
        print("Datos erróneos.")
        respuesta=input("¿Quiere introducir más números (S/N)? ")

#Muestro el resultado por consola      
print("El número más pequeño es %s." %(smallestNum))