'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 7
 @enunciado: 
 
'''

numA = int(input("Dame un número entero: "))
numB = int(input("Dame otro número entero: "))
operacion = input("¿Qué operación desea realizar (+ o -)? ")
while operacion not in {"+","-"}:
    operacion = input("¿Qué operación desea realizar (+ o -)? ")

if operacion=="+":
    print("El resultado de la suma de "+str(numA)+" más "+str(numB)+" es "+str(numA+numB))
else:
    print("El resultado de la resta de "+str(numA)+" menos "+str(numB)+" es "+str(numA-numB))