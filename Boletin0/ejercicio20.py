'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 20
 @enunciado: 
 Pedir dos números al usuario y realizar la multiplicación usando solo la suma.
'''

numA = int(input("Introduzca un número: "))
numB = int(input("Introduzca otro número: "))

resultado = 0

if numA<0:
    numA = -numA
    for i in range(numA):
        resultado += numB
    resultado = -resultado
else:
    for i in range(numA):
        resultado += numB
        
print("El resultado es " + str(resultado))