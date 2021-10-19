"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 9  
 @enunciado: 
Design a program that reads an integer positive number greater than 0 and says if
it's a "perfect number". A number is perfect if it is equal to the sum of all its divisors.
The messages are the following:
"Enter an integer positive number greater than 0:"
"The number is not valid, try again."
"The number is perfect."
"The number is not perfect."
 """

#Pido los datos 
num=int(input("Introduce un número positivo mayor que 0: "))
#Si los datos son erróneos, muestro mensaje de error y vuelvo a pedirlos
while num<=0:
    print("El número no es válido, inténtalo de nuevo.")
    num=int(input("Introduce un número positivo mayor que 0: "))

#Inicializo la variable para sumar los divisores a 0
sumaDivisores=0
#Bucle for que va desde [1, num)
for i in range (1, num):
    #Compruebo que es divisor
    if num%i==0:
        #Sumo i a la variable que suma el total de los divisores del número
        sumaDivisores+=i

#Si el número es igual a la suma de sus divisores "[1,num)" el número es perfecto, sino no
if num==sumaDivisores:
    print("El número es perfecto.")
else:
    print("El número no es perfecto.")
    