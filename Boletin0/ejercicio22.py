'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 22
 @enunciado: 
 Realizar un juego de ordenador que consistirá en que el ordenador 
 pensará un número del 1 al 500 (hacerlo del 1 al 50 si queréis que 
 sea más fácil de adivinar) y el usuario deberá introducir números 
 para intentar adivinarlo. 
 El programa deberá decir si el número introducido por el usuario 
 es mayor o menor que el que ha pensado el usuario para poder ir 
 dándole pistas.
El programa terminará cuando el usuario acierte el número. 
Propuesta de mejora, cuando acierte el número indique en cuántos 
intentos lo ha realizado.

'''

import random

numRandom = random.randint(0,500)
print(numRandom)

numIntroducido = int(input("Introduce un número entre 0 y 500: "))

contador = 1

while numRandom!=numIntroducido:
    if numRandom>numIntroducido:
        print("El número introducido es menor.")
    else:
        print("El número introducido es mayor.")
    contador += 1
    numIntroducido = int(input("Introduce un número entre 0 y 500: "))
    
print("Enhorabuena, has acertado.")
print("Has realizado " + str(contador) + " intento(s).")
