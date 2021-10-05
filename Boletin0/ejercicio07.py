'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 7
 @enunciado: 
 Vamos a hacer un programa que nos pregunte dos números y si queremos restar o sumar y nos
muestre el resultado de la suma o la resta.

'''

numA = int(input("Dame un ncmero entero: "))
numB = int(input("Dame otro número entero: "))
operacion = input("¿Qué operación desea realizar (+ o -)? ")
while operacion not in {"+","-"}:
    operacion = input("¿Qué operación desea realizar (+ o -)? ")

if operacion=="+":
    print("El resultado de la suma de "+str(numA)+" más "+str(numB)+" es "+str(numA+numB))
else:
    print("El resultado de la resta de "+str(numA)+" menos "+str(numB)+" es "+str(numA-numB))
    

'''
#Solución propuesta por Inma:

resultado = 0
numA = int(input("Introduzca un número: "))
numB = int(input("Introduzca otro número: "))

if (numA>0 and numB>0)  or (numA<0 and numB<0):
    signo = "Positivo"
else:
    signo = "Negativo"
    
if numA<0:
    numA = -numA
if numB<0:
    numB = -numB
    
for i in range(numA):
    resultado += numB
    
if signo=="Negativo":
    resultado = -resultado
    
print("El resultado es " + str(resultado))
'''