'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 6 
 @enunciado: 
 Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos.

#Usamos el teorema de Pitágoras con la siguiente fórmula:
distancia=sqrt((x2-x1)**2+(y2-y1)**2))
'''
#Importamos la funcion de la raiz cuadrada
from math import sqrt

#Petición de datos
x1=int(input("Introduce la coordenada x del primer punto: "))
y1=int(input("Introduce la coordenada y del primer punto: "))
x2=int(input("Introduce la coordenada x del segundo punto: "))
y2=int(input("Introduce la coordenada y del segundo punto: "))

#Calcular la distancia entre los dos puntos
distancia=sqrt((x2-x1)**2 + (y2-y1)**2)

#Mostramos el mensaje por consola
print("La distancia entre los puntos es %s" %(distancia))
