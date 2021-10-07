'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 16
 @enunciado: 
 Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente.
'''

#Petición y comprobación de datos
num=int(input("Introduce un número entre 1 y 12: "))
while num<1 or num>12:
    num=int(input("Error. Introduce un número entre 1 y 12: "))

#Creación de una lista con los nombres de los meses
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", 
       "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

#Creación de una lista con los días que tiene cada mes
diasEnMeses=["31", "28 o 29", "31", "30", "31", "30", "31", "31", "30", 
             "31", "30", "31"]

#Salida del resultado por consola
print("El mes %s, que corresponde con %s, tiene %s días." 
      %(num, meses[num-1], diasEnMeses[num-1]))