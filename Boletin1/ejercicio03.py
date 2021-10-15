'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 3 
 @enunciado: 
 Calcular la media de tres números pedidos por teclado
'''

#Petición de datos con un bucle para no tener que introducir 3 variables
suma=0
cantidadNumeros=3
for i in range(cantidadNumeros):
    num=int(input("Introduce el número " + str(i+1) + ": "))
    suma+=num

#Cálculo de la media dentro de la salida de datos por consola
#media=round(suma/cantidadNumeros,2)
print("La media de los números introducidos es " + str(round(suma/cantidadNumeros,2)))