'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 18
 @enunciado: 
 Escribe un programa que pida el limite inferior y superior de un intervalo. 
 Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo.
'''

#Petición de datos y comprobación de datos
limiteInferior=int(input("Introduce el límite inferior del intervalo (diferente de 0): "))
#Comprobación de que el límite inferior sea diferente de 0
while limiteInferior==0:
    limiteInferior=int(input("Error. Introduce el límite inferior del intervalo (diferente de 0): "))

limiteSuperior=int(input("Introduce el límite superior del intervalo (diferente de 0): "))
#Comrpobación de que el límite superior sea diferente de 0 y mayor que el inferior
while limiteSuperior==0 or limiteSuperior<limiteInferior:
    limiteSuperior=int(input("Error. Introduce el límite superior del intervalo (diferente de 0): "))

#Petición de un número    
num=int(input("Introduce un número (0 para parar): "))
#Creación de variables usadas en el bucle posterior
suma=0
contadorOutIntervalo=0
intervalo="No"
#Creación de bucle cuya condición de salida es el que número introducido sea 0
while num!=0:
    #Condición de suma de números dentro del intervalo abierto
    if num>limiteInferior and num<limiteSuperior:
        suma+=num
    #Condición de si se ha introducido un nº igual al límite superior o inferior.    
    elif num<limiteInferior and num<limiteSuperior:
        contadorOutIntervalo+=1  
    #Condición de cantidad de números fuera del intervalo abierto 
    else:
        intervalo="Sí"
    num=int(input("Introduce un número (0 para parar): "))

#Mostrar resultados por consola    
print("Suma de números dentro del intervalo abierto: %s" %(suma))
print("Cantidad de números fuera del intervalo: %s" %(contadorOutIntervalo))
print("¿Se ha introducido el límite inferior o el superior?: %s" %(intervalo))
    