'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 7
 @enunciado: 
 
'''

numA = int(input("Dame un n�mero entero: "))
numB = int(input("Dame otro n�mero entero: "))
operacion = input("�Qu� operaci�n desea realizar (+ o -)? ")
while operacion not in {"+","-"}:
    operacion = input("�Qu� operaci�n desea realizar (+ o -)? ")

if operacion=="+":
    print("El resultado de la suma de "+str(numA)+" m�s "+str(numB)+" es "+str(numA+numB))
else:
    print("El resultado de la resta de "+str(numA)+" menos "+str(numB)+" es "+str(numA-numB))