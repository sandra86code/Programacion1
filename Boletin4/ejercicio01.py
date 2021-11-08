'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 1
 @enunciado: 
 Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el
primero es múltiplo del segundo.
'''

numA=int(input("Dame un número entero: "))
numB=int(input("Dame otro número entero: "))

def esMultiplo(numA,numB):
    
    return numA%numB==0

print(esMultiplo(numA, numB))