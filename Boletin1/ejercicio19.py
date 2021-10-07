'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 19
 @enunciado: 
 Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. 
No se puede utilizar el operador de potencia.
'''

#Petición de datos
base=int(input("Introduce la base: "))
exponente=int(input("Introduce el exponente (mayor que 0): "))
while exponente<=0:     #Comprobación de exponente positivo
    exponente=int(input("Error. Introduce el exponente (mayor que 0): "))
    
#Cálculo de la potencia con un bucle for
potencia=1
for i in range(exponente):
    potencia*=base

#Mostrar resultado por consola      
print("La resultado de %s elevado a %s es %s." %(base, exponente, potencia))