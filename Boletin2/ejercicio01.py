"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 1  
 @enunciado: 
Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.
 """

#Bucle for porque con límites de intervalo abierto (1, 100) 
for i in range (2, 100):
    #Estructura lógica de lo más restrictivo a lo menos restrictivo
    if i%7==0 and i%13==0:
        print("%s es múltiplo de 7 y de 13" % (i))
    elif i%7==0:
        print("%s es múltiplo de 7" % (i))
    elif i%13==0:
        print("%s es múltiplo de 13" % (i))
    else:
        print(i)