'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 21
 @enunciado: 
 Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad de
números primos que queremos mostrar.
'''

#Petición y comprobación de datos
cantidadNumPrimos=int(input("¿Cuántos números primos quieres mostrar? "))
while cantidadNumPrimos<=0:
    cantidadNumPrimos=int(input("Error. ¿Cuántos números primos quieres mostrar? "))
    
num=1000
primos=[]

while len(primos)!=cantidadNumPrimos:
    divisor=0
    for i in range(2, num):
        for j in range (2, num//2+1):
            if i%j==0:
                 divisor+=1
        if divisor in {1,2}:
            primos.append(i)
    
print(primos)