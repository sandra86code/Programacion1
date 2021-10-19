"""
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 2
 @enunciado: 
Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10". 
If the number is out of the boundaries, the program should show
the message "The number is out of the boundaries". 
If the number is valid, it should show the times table following the next format:
7*0=0
7*1=7
.....
7*10=70
 """
 
#Pido datos
num=int(input("Introduce un número entre 0 y 10: "))
#Estructura lógica con if para parte fuera de rango y else para dentro de rango
if num<=0 or num>=10:
    print("El número está fuera de rango.")
else:
    #Bucle for repetido 11 veces, desde el [0, 10]
    for i in range (11):
        print("%s*%s=%s" %(num, i, num*i))
    
