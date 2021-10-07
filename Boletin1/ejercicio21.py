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
    

primos=[]

divisors=0

while len(primos)!=cantidadNumPrimos:
    
    for i in range(2, 20):
        for j in range (2, i):
            if i%j==0:
                 divisors+=1
        if divisors==0:
            primos.append(i)
    
print(primos)