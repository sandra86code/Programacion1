'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 2 - Ejercicio Extra 3
 @enunciado: 
 Diseñar un programa que lea números hasta que el usuario introduzca el 0. 
 Debe informar de la media de los números leídos (sin tener en cuenta el 0) 
 y el valor máximo y mínimo
introducido.
'''
#Como no quiero que el 0 sea controlado en el bucle, pido la variable fuera
#del bucle. Si es 0, no entra en el bucle.
num=int(input("Introduce un número (0 para parar): "))
#Variable que cuenta el número de iteraciones del bucle para dividir entre
#la suma y calcular la media
cantidad=0
#Variable sumatoria en la que sumo el valor de los números, para luego
#poder calcular la media
suma=0
#Establezco el mínimo como un número muy grande, de manera que en la primera
#iteración del bucle, el número va a convertirse en el mínimo
minimo=9999999
#Establezco el máximo como un número muy pequeño, de manera que en la primera
#iteración del bucle, el número va a convertirse en el máximo
maximo=-9999999

#Se entra en el bucle con cualquier número salvo 0
while num!=0:
    #Con cada iteración del bucle, aumenta en 1
    cantidad+=1
    #Con cada iteración del bucle, sumo cada número
    suma+=num
    #Comparo el número con el mínimo, si es más pequeño, el número pasa a ser
    #el mínimo, sino, sigue igual
    if num<minimo:
        minimo=num
    #Comparo el número con el máximo, si es más grande, el número pasa a ser
    #el máximo, sino, sigue igual
    if num>maximo:
        maximo=num
    #Vuelvo a pedir el número. Si es 0 para, para cualquier otro número,
    #hay otra iteración en el bucle
    num=int(input("Introduce un número (0 para parar): "))

#Muestro resultados por consola.
#La media la calculo dividiendo la suma total de los números entre la cantidad de vueltas del bucle
print("Media: %s \nValor máximo: %s \nValor mínimo: %s" % ((suma/cantidad), maximo, minimo))
    
    
