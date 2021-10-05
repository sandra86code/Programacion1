'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 13
 @enunciado: 
 Haz un programa que haga una tabla de multiplicar del número que el usuario 
 introduzca por consola.

'''

num = int(input("Introduce un número"))
for i in range(11):
    print(str(num) + "*" + str(i) + "=" + str(num*i))