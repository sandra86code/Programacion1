'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Examen año 2020/2021 - Ejercicio 3
 @enunciado: 
 Realiza un programa para obtener el máximo común divisor de dos números
 que se pedirán por teclado.
 
 El máximo común divisor (mcd) es el mayor número que divide a ambos números
 a la vez.
'''

#Pido datos y si los números introducidos son negativos o 0, vuelvo a pedir los datos.
numA=int(input("Introduce un número entero positivo: "))
while numA<=0:
    numA=int(input("Error. Introduce un número entero positivo: "))
numB=int(input("Introduce otro número entero positivo: "))
while numB<=0:
    numB=int(input("Error. Introduce otro número entero positivo: "))

#Compruebo cuál número es mejor y mayor y los asigno a dos variables
if numA>=numB:
    numMayor=numA
    numMenor=numB
else:
    numMayor=numB
    numMenor=numA

#Creo un bucle que va desde [1, número menor], ya que mayor que este no puede ser el mcd
#y el mcd puede ser el número menor en caso de que el mayor sea múltiplo del menor   
for i in range (1, numMenor+1):
    #Si el divisor de un número puede ser el mismo, es el mcd.
    #Como el mcd es el divisor que se dé último, será el último que se guarde en la variable mcd
    if numMayor%i==0 and numMenor%i==0:
        mcd=i

#Muestro el mcd por consola            
print("El máximo común divisor de %s y %s es %s." %(numA, numB, mcd))
