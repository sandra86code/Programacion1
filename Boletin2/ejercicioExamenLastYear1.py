'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Examen año 2020/2021 - Ejercicio 1
 @enunciado: 
 En el gimnasio Jacafitness tienen el siguiente horario:
 - Los lunes, miércoles y jueves imparten Spinning de 12 a 14, Yoga de 16 a 20 y
 Body Combat de 20 a 22.
 - Los martes y viernes las sesiones de Spinning y Yoga se intercambian.
 
 Elabora un programa que dé la bienvenida al gimnasio Jacafitness y, tras
 preguntar por la hora y el día de la semana, te indique la actividad que puedes
 realizar.
'''
#Muestro por consola el mensaje de bienvenida
print("Bienvenid@ al gimansio Jacafitness.")

#Pido datos y, si no son correctos, los vuelvo a pedir
hora=int(input("Introduzca una hora (12, 16 o 20): "))
while hora not in {12, 16, 20}:
    print("Error. Han introducido datos erróneos. Vuelva a intentarlo.")
    hora=int(input("Introduzca una hora (12, 16 o 20): "))
dia=input("Introduzca un día de la semana (L/M/X/J/V): ")
while dia not in {"L", "M", "X", "J", "V"}:
    print("Error. Han introducido datos erróneos. Vuelva a intentarlo.")
    dia=input("Introduzca un día de la semana (L/M/X/J/V): ")

#Estructura lógica por horas y luego por días    
if hora==20:
    mensaje="Puede asistir a Body Combat de 20 a 22."
elif hora==12:
    if dia in {"L", "X", "J"}:
        mensaje="Puede asistir a Spinning de 12 a 14."
    else:
        mensaje="Puede asistir a Yoga de 12 a 14."
else:
    if dia in {"L", "X", "J"}:
        mensaje="Puede asistir a Yoga de 16 a 20."
    else:
        mensaje="Puede asistir a Spinning de 16 a 20."

#Imprimo mensaje por consola
print(mensaje)
