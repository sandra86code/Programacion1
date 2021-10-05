'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 19
 @enunciado: 
 Pedir al usuario 10 números y después decir cuántos son negativos y cuántos son positivos.

'''

positivo = 0
negativo = 0

for i in range(10):
    num = int(input("Introduzca un número: "))
    if num>=0:
        positivo += 1
    else:
        negativo += 1
        
print("Ha introducido "+ str(positivo) + " números positivos y " + str(negativo) + " números negativos.")