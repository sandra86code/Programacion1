'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 16
 @enunciado: 
 Realiza un programa que pregunte una cantidad de minutos y muestre por pantalla 
 a cuantas horas y minutos corresponde.

'''
minutos = int(input("Introduce los minutos: "))
while minutos<=0:
    print("Debe introducir una cantidad positiva.")
    minutos = int(input("Introduce los minutos: "))
    
print(str(minutos) + " minutos corresponden a " + str(minutos//60) + " hora(s) y " + str(minutos%60) + " minuto(s).")

'''
#Solución con bucle

minutos = int(input("Introduce los minutos: "))
while minutos<=0:
    print("Debe introducir una cantidad positiva.")
    minutos = int(input("Introduce los minutos: "))

hora = 0

while minutos>=60:
    minutos -= 60
    hora += 1

print("Son " + str(hora) + " hora(s) y " + str(minutos) + " minuto(s).")

'''