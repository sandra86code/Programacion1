'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 21
 @enunciado: 
 Realizar un programa que solicite números al usuario. 
 El programa terminará cuando el usuario introduzca un 0 
 y al final debe decir cuántos números pares y cuántos 
 números impares se han introducido.

'''

num = int(input("Introduce un número (0 para parar): "))

impar = 0
par = 0

while num!=0:
    if num%2==0:
        par += 1
    else:
        impar += 1
    num = int(input("Introduce un número (0 para parar): "))

print("Ha introducido " + str(par) + " números pares y " + str(impar) + " números impares.")
