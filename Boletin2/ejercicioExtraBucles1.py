"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 26, 2021
 @nombre: Boletin 2 - Ejercicio Extra Bucles 1
 @enunciado: 
 Diseñar un programa que calcule el perímetro de una figura geométrica. 
 Para ello debemos preguntar “¿Cuántos lados tiene la figura?”. 
 Luego debemos pedir la longitud de cada uno de los lados y mostrar el 
 perímetro. 
 Se debe garantizar que los datos son correctos.
 """

 
numLados=int(input("¿Cuántos lados tiene la figura? "))
while numLados<=0:
    print("Datos erróneos, debe dar un entero positivo.")
    numLados=int(input("¿Cuántos lados tiene la figura? "))

perimetro=0
for i in range (numLados):
    lado=int(input("Introduce la dimensión del lado %s: " %(i+1)))
    while lado<=0:
        print("Datos erróneos, debe dar un entero positivo.")
        lado=int(input("Introduce la dimensión del lado: "))
    perimetro+=lado
    
print("El perímetro de la figura es %s" %(perimetro))