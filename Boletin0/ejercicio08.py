'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 8
 @enunciado: 
 Vamos a hacer un programa que nos pregunte dos números y si queremos sumar, restar, 
 multiplicar o dividir y nos muestre el resultado.
'''

numA = int(input("Dame un n�mero entero: "))
numB = int(input("Dame otro n�mero entero: "))
operacion = input("�Qu� operaci�n desea realizar (+, -, *, /)? ")
while operacion not in {"+","-","*","/"}:
    operacion = input("�Qu� operaci�n desea realizar (+, -, *, /)? ")

if operacion=="+":
    print("El resultado de la suma de "+str(numA)+" m�s "+str(numB)+" es "+str(numA+numB))
elif operacion=="-":
    print("El resultado de la resta de "+str(numA)+" menos "+str(numB)+" es "+str(numA-numB))
elif operacion=="*":
    print("El resultado de la multiplicaci�n de "+str(numA)+" por "+str(numB)+" es "+str(numA*numB))
else:
    if numB!=0:
        print("El resultado de la divisi�n de "+str(numA)+" entre "+str(numB)+" es "+str(numA/numB))
    else:
        print("No se puede dividir entre 0, cabezaloca")