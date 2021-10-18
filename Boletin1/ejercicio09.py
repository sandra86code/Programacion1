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

'''
#Petición de datos
base=int(input("Introduce la base: "))
exponente=int(input("Introduce el exponente: "))
 
#Expresión lógica para calcular la potencia dependiendo del exponente
if exponente==0:
    potencia = 1
elif exponente<0:
    potencia = 1 / (base**abs(exponente))
else:
    potencia = base**exponente
 
#Mostrar resultado por consola
print("El resultado de la potencia es %s" %(round(potencia, 2)))
'''


#Solución con bucles
base=int(input("Introduce la base: "))
exponente=int(input("Introduce el exponente: "))

potencia=1
if exponente<0:
    for i in range (abs(exponente)):
        potencia*=base
    potencia=1/potencia
elif exponente>0:
    for i in range (exponente):
        potencia*=base
    
print("El resultado de la potencia es %s" %(round(potencia, 2)))
