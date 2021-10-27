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

numA=int(input("Introduce un número: "))
numB=int(input("Introduce otro número: "))

if numA>=numB:
    numMayor=numA
    numMenor=numB
else:
    numMayor=numB
    numMenor=numA
    
for i in range (1, numMenor+1):
    if numMayor%i==0 and numMenor%i==0:
        mcd=i
            
print("El máximo común divisor de %s y %s es %s." %(numA, numB, mcd))