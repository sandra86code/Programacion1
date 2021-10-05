'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 0
 @enunciado: Primer programa que pregunta el nombre del usuario 
y lo saluda.
Luego mostrará el mensaje al nombre pidiéndole dos 
números y los sumará y los restará.
'''


nombre = input("Dime tu nombre: ")

#print("Hola %s" %(nombre))
print("Hola " + nombre)

num1 = int(input(nombre + ", dime un número: "))
num2 = int(input(nombre + ", dime otro número: "))

suma=num1+num2
resta=num1-num2

print("La suma de %s + %s es %s y la resta, %s." %(num1, num2, suma, resta))