'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 9
 @enunciado: 
 Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
'''


#Petición de datos
base=int(input("Introduce la base: "))
exponente=int(input("Introduce el exponente: "))

#Cambio exponente negativo a positivo y creación de variable interruptor
signo=""
if exponente<0:
    exponente=-exponente
    signo="negativo"
    
#Calculo potencia
potencia=1
for i in range(exponente):
    potencia*=base
        
#Muestra de resultado por consola
if signo=="negativo":
    potencia=1/potencia

print("La potencia es %s" %(potencia))