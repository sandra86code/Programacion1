"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 26, 2021
 @nombre: Boletin 2 - Ejercicio Extra 2
 @enunciado: 
 Diseñar un programa que calcule el perímetro de una figura geométrica. 
 Para ello debemos preguntar “¿Cuántos lados tiene la figura?”. 
 Luego debemos pedir la longitud de cada uno de los lados y mostrar el 
 perímetro. 
 Se debe garantizar que los datos son correctos.
 """

#Pido datos 
numLados=int(input("¿Cuántos lados tiene la figura? "))
#Si los datos son erróneos, vuelvo a pedir datos
while numLados<=0:
    print("Datos erróneos, debe dar un entero positivo.")
    numLados=int(input("¿Cuántos lados tiene la figura? "))

#Creo variable sumatoria para guardar el perímetro sumando los lados en el bucle
perimetro=0
#Creo el bucle con el número de iteraciones introducido por el usuario
for i in range (numLados):
    #Pido el lado en cada iteración
    lado=int(input("Introduce la dimensión del lado %s: " %(i+1)))
    #Si los datos son erróneos, vuelvo a pedirlos
    while lado<=0:
        print("Datos erróneos, debe dar un entero positivo.")
        lado=int(input("Introduce la dimensión del lado: "))
    #Con cada iteración sumo el lado al perímetro
    perimetro+=lado

#Muestro por consola el resultado del cálculo del perímetro    
print("El perímetro de la figura es %s" %(perimetro))