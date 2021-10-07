'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 13
 @enunciado: 
 El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. 
La forma de cobrar es la siguiente: 
- si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
- de 50 a 99 alumnos, el costo es de 70 euros, 
- de 30 a 49, de 95 euros,
- y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. 
Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje.
'''

#Petición y comprobación de datos de entrada
numAlumnos=int(input("Introduce el número de alumnos: "))
while numAlumnos<=0:
    numAlumnos=int(input("Error. Introduce el número de alumnos: "))
    
#Calcular coste total y coste por alumno
if numAlumnos<30:
    costeTotal=4000
    costeAlumno=costeTotal/numAlumnos
elif numAlumnos<50:
    costeAlumno=95
    costeTotal=numAlumnos*costeAlumno
elif numAlumnos<100:
    costeAlumno=70
    costeTotal=numAlumnos*costeAlumno
else:
    costeAlumno=65
    costeTotal=numAlumnos*costeAlumno

#Mostrar resultados por consola
print("Pago total: %s €.\nPago de cada alumno: %s €." %(costeTotal,costeAlumno))
    