'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 2
 @enunciado: 
 Implementar la función primerosN que reciba un entero positivo n como único argumento. 
 Luego la función debe imprimir los primeros n cuadrados perfectos que no sean números pares. 
 Por ejemplo, si n=2, debería imprimir los cuadrados perfectos 1 y 9.

NOTA: los cuadrados perfectos son los números que poseen raíces cuadradas exactas.
Por ejemplo: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169,... 
'''
#Importo la raíz cuadrada de la biblioteca math
from math import sqrt

#===============================================================================
# Esta función nos devuelve la cantidad de cuadrados perfectos que no sean números 
# pares que le hayamos introducido
# Recibe: la cantidad de pares
# Devuelve: una lista con los n cuadrados perfectos pares
#===============================================================================
def primerosN(cantidad):
    
    cuadradosPerfectos=[]
    i=0
    bandera=False
    #Pongo el límite en un número grande, aunque puede quedarse pequeño si la cantidad
    #es muy alta
    while i<10000000 and bandera==False:
        #Si el número es par y el resto de su raíz cuadrada entre 1 es 0 (es decir, es
        #un número entero y no con decimales, me lo mete en la lista de perfectos
        if i%2!=0 and sqrt(i)%1==0:
            cuadradosPerfectos.append(i)
        #Si la cantidad de elementos en la lista es igual a la cantidad, cambia la bandera
        #y frena el bucle
        if len(cuadradosPerfectos)==cantidad:
            bandera=True
        i+=1
            
    return cuadradosPerfectos

#Pido los datos y compruebo que sean correctos
n=int(input("Dime la cantidad de cuadrados perfectos que quieres imprimir: "))
while n<=0:
    print("Debe ser un entero positivo. Inténtalo de nuevo.")
    n=int(input("Dime la cantidad de cuadrados perfectos que quieres imprimir: "))

#Imprimo el resultado    
print(primerosN(n))