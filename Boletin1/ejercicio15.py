'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 15
 @enunciado: 
 Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error.
'''

#Petición y comprobación de datos
diaSemana=int(input("Introduce el día de la semana (del 1 al 7): "))
while diaSemana not in {1,2,3,4,5,6,7}:
    diaSemana=int(input("Error. Introduce el día de la semana (del 1 al 7): "))

#Creo lista de nombres de los días de la semana    
nombresDias=["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


print("El día %s de la semana es el %s." %(diaSemana, nombresDias[diaSemana-1]))   