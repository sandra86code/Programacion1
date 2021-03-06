'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 3, 2021
 @nombre: Simulacro Examen - Ejercicio 1
 @enunciado: 
 Juan recibe un regalo económico de su familia todos sus cumpleaños, de forma que cada año recibe
15€ más que en el anterior.
Elabora un programa que pida una edad y calcule cuánto dinero en total ha recibido Juan en regalos
de cumpleaños hasta esa edad sabiendo que en el primer cumpleaños le regalaron 20€.
Ejemplo 1: 1 año ⇒ 20€ (recibe el 1o año)
Ejemplo 2: 2 años ⇒ 55€ (= 20€ tenía +35€ recibe el 2o año)
Ejemplo 3: 3 años ⇒ 105€ (= 55€ tenía +50€ recibe el 3o año)
Ampliación: modifica el programa anterior para que tanto la cantidad que se incrementa cada año
como el regalo inicial cambien en cada programa.
'''

#===============================================================================
# Esta función calcula el dinero total (numero entero) que ha recibido una persona 
# en su cumpleaños dependiendo de su edad y de un incremento
# Recibe: edad, dinero e incremento, que son 3 variables de tipo entero.
# Devuelve: el dinero total recibido (un entero)
#===============================================================================
def calcularTotalDinero(edad, dinero, incremento):
    
    dineroYear=dinero
    dineroTotal=dineroYear
    for i in range(2, edad+1):
        dineroYear+=incremento
        dineroTotal+=dineroYear
    
    return dineroTotal


#===============================================================================
# Esta función es el menú principal de la función, que pide los datos e imprime
# el resultado
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
#===============================================================================
def main():
    
    edad=int(input("Introduce la edad de Juan: "))
    while edad<0:
        print("Datos erróneos.")
        edad=int(input("Introduce la edad de Juan: "))
    
    dineroInicial=20
    incremento=15
    print("El dinero total que recibe Juan con %s años es %s €." % (edad, calcularTotalDinero(edad, dineroInicial, incremento)))

main()