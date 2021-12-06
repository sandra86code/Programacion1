'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 2 Diciembre 2020 - Ejercicio 1 
 @enunciado: 
 La primitiva es un tipo de sorteo bisemanal en el que se puede elegir 
combinaciones de 6 números del 1 al 49. 
Un boleto resulta ganador si esos 6 números coinciden con la combinación 
extraída al azar de un bombo con todas las bolas. 
También existen premios menores a partir de los 3 aciertos.

1. Diseña una función que reciba como entrada dos listas de números que hagan 
referencia a la combinación ganadora y a la apuesta y devuelva como resultado el 
número de aciertos que tiene la apuesta. 


2. Realiza un programa que solicite la apuesta de la primitiva y usando la función 
anterior escriba un mensaje con el número de aciertos. Si ha adivinado los 6 números 
deberá escribir. “ENHORABUENA. TIENES EL PLENO”. Valida los datos  de la apuesta de 
forma adecuada.

Si sabes, debes generar de forma aleatoria la combinación ganadora, si no sabes, 
utiliza la combinación ganadora que quieras.
'''

from random import randint

#===============================================================================
# Esta función calcula el número de coincidencias entre dos listas de números 
# Recibe: dos listas de números
# Devuelve: el número de coincidencias (aciertos) entre ambas
#===============================================================================
def calcularAciertosPrimitiva(ganadora,apuesta):
    aciertos=0
    for i in range (len(ganadora)):
        for j in range (len(apuesta)):
            if ganadora[i]==apuesta[j]:
                aciertos+=1
    
    return aciertos

#===============================================================================
# Esta función crea una lista de 6 números aleatorios entre 1 y 49 sin repetir
# ninguno 
# Devuelve: la lista con los 6 números
#===============================================================================
def crearCombinacionAleatoria():
    combinacion=[]
    for i in range (6):
        num=randint(1,49)
        #Si el número ya está en la lista, vuelvo a generar el número
        while num in combinacion:
            num=randint(1,49)
        combinacion.append(num)
    
    return combinacion


#===============================================================================
# Esta función crea una lista de 6 números enteros entre 1 y 49, sin repetir,
# a partir de los números que introduce el usuario
# Devuelve: la lista con los 6 números
#===============================================================================
def crearApuesta():
    apuesta=[]
    for i in range(6):
        num=int(input("Elige un número de 1 al 49: "))
        #Valido datos (número [1-49] y que no haya sido introducido previamente
        #en la lista
        while num<1 or num>49 or num in apuesta:
            print("Número incorrecto o repetido. Vuelve a intentarlo.") 
            num=int(input("Elige un número de 1 al 49: "))
        apuesta.append(num)
       
    return apuesta

#===============================================================================
# Esta función es la principal del programa.
# 1. Asigna a la variable de tipo lista "combinacionGanadora" el resultado de la 
# función que la crea.
# 2. Asigna a la variable de tipo lista "apuesta" el resultado de la función que 
# la crea.
# 3. Asigna a la variable de tipo int "aciertos" el resultado de la función que 
# calcula las coincidencias entre las listas anteriores.
# 4. Crea la estructura condicional que imprime un mensaje u otro en función de
# los aciertos.
#===============================================================================
def main():
    
    combinacionGanadora=crearCombinacionAleatoria()
    apuesta=crearApuesta()
    aciertos=calcularAciertosPrimitiva(combinacionGanadora, apuesta)
    
    if aciertos==6:
        print("Enhorabuena, ¡HAS GANADO!")
    elif aciertos>3:
        print("Enhorabuena, tienes %s aciertos, por lo que has ganado un premio." % aciertos)
    else:
        print("Tu número de aciertos es: %s" % aciertos)
        
main()