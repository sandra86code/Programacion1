'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 21
 @enunciado: 
 Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad de
números primos que queremos mostrar.
'''

'''
#Petición y comprobación de datos
cantidadNumPrimos=int(input("¿Cuántos números primos quieres mostrar? "))
while cantidadNumPrimos<=0:
    cantidadNumPrimos=int(input("Error. ¿Cuántos números primos quieres mostrar? "))
     
#Declaramos lista vacía que va a acumular los números primos
primos=[]
#Declaramos un número que será el límite superior del bucle for externo
num=1000
#Declaramos variable contadora de los divisores de un número
divisors=0

#Bucle externo que va desde el 2 hasta 1000
for i in range(2, num):
    #Variable que es la dimensión de la lista
    sizeLista=len(primos) 
    #Condición de que cuando la cantidad de primos introducida sea igual a la dimensión de la lista pare el bucle
    if cantidadNumPrimos==sizeLista:    
        i=num
    #Bucle interno que va desde 2 hasta la mitad de i + 1, para así ver los divisores de i
    for j in range (2, (i//2)+1):
        #Comprobación de divisores de i en intervalo abierto
        if i%j==0:
            divisors=1
    #Cuando los divisores sean 0, es decir, el número sea primo, lo añade a la lista
    if divisors==0:
        primos.append(i)
    #Reiniciamos la variable para el siguiente número del bucle interno
    divisors=0
    
#Mostramos el resultado por consola        
print("Los %s primeros números primos son:\n%s" %(cantidadNumPrimos, primos))
'''

#Solución propuesta en clase con bucle while que es más eficiente porque sale del bucle en cuanto encuentra un divisor

    
#Petición y comprobación de datos
cantidadNumPrimos=int(input("¿Cuántos números primos quieres mostrar? "))
while cantidadNumPrimos<=0:
    cantidadNumPrimos=int(input("Error. ¿Cuántos números primos quieres mostrar? "))
     
#Declaramos lista vacía que va a acumular los números primos
primos=[]
#Declaramos un número que será el límite superior del bucle for externo
num=1000    


#Bucle externo que va desde el 2 hasta 1000
for i in range(2, num):
    #Variable que es la dimensión de la lista
    sizeLista=len(primos) 
    #Condición de que cuando la cantidad de primos introducida sea igual a la dimensión de la lista pare el bucle
    if cantidadNumPrimos==sizeLista:    
        i=num
    #Bucle interno que va desde 2 hasta la mitad de i + 1, para así ver los divisores de i
    esPrimo = True
    j = 2
    while j <= i//2 and esPrimo==True:
        if i%j==0:
            esPrimo = False
    #Cuando los divisores sean 0, es decir, el número sea primo, lo añade a la lista
    if esPrimo==True:
        primos.append(i)
    #Reiniciamos la variable para el siguiente número del bucle interno
    esPrimo=True
    
#Mostramos el resultado por consola        
print("Los %s primeros números primos son:\n%s" %(cantidadNumPrimos, primos))
    