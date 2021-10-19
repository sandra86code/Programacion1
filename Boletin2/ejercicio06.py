"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 6 
 @enunciado: 
Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
"Enter one number:"
"The product is XX."
 """

#Pido los datos 
numA=int(input("Introduce un número: "))
numB=int(input("Introduce otro número: "))

#Inicializo a 0 la variable suma para utilizarla en los bucles for
suma=0

#Si numB es positivo
if numB>0:
    #Bucle for que se repite el valor de numB
    for i in range (numB):
        #En cada iteración sumo numA a la variable suma
        suma+=numA
#Si numB es negativo
else:
    #Convierto numB en positivo para poderlo utilizar como rango en el bucle for
    numB*=-1
    #Bucle for que se repite el valor de numB
    for i in range (numB):
        #En cada iteración sumo numA a la variable suma
        suma+=numA
    #Cambio a signo negativo la variable suma, ya que un número positivo (numA) por un número negativo (numB) tiene un resultado negativo
    suma*=-1

#Muestro el resultado por consola
print("El producto es %s." %(suma))