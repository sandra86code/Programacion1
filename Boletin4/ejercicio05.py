'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 5
 @enunciado: 
 Crear una función que calcule el MCD de dos número por el método de Euclides. 
 El método de Euclides es el siguiente:
• Se divide el número mayor entre el menor.
• Si la división es exacta, el divisor es el MCD.
• Si la división no es exacta, dividimos el divisor entre el resto obtenido y se
continúa de esta forma hasta obtener una división exacta, siendo el último
divisor el MCD.
Crea un programa que lea dos números enteros y muestre el MCD.
'''

#===============================================================================
# Esta función calcula el máximo común divisor usuando el Teorema de Euclides
# Recibe dos números enteros
# Devuelve: 
# El máximo común divisor de ambos números
#===============================================================================
def calculaMcd(numA, numB):

    #Estructura condicional para ver cuál es el número mayor, que se convierte en dividendo
    #y el número mayor que se convierte en divisor
    if numA>numB:
        dividendo=numA
        divisor=numB
    else:
        dividendo=numB
        divisor=numA
    
    #Creo la variable resto que es el resto del dividendo entre el divisor
    resto=dividendo%divisor

    #Çreo un bucle que frena cuando el resto sea 0
    while resto!=0:
        #El divisor se convierte en el dividendo
        dividendo=divisor
        #El resto se convierte en el divisor
        divisor=resto
        #El nuevo resto es el nuevo dividendo entre el nuevo divisor
        resto=dividendo%divisor
        
    #El divisor es el mcd
    return divisor

#Pido datos y compruebo si son correctos. De no serlo, los vuelvo a pedir
numA=int(input("Introduce un número entero positivo: "))
while numA<=0:
    print("Datos incorrectos. Vuelve a intentarlo")
    numA=int(input("Introduce un número entero positivo: "))
numB=int(input("Introduce otro número entero positivo: "))
while numB<=0:
    print("Datos incorrectos. Vuelve a intentarlo")
    numB=int(input("Introduce otro número entero positivo: "))

#Imprimo por consola el mensaje con el mcd
print("El máximo común divisor (MCD) de %s y %s es %s" %(numA, numB, calculaMcd(numA, numB)))
