'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen Recuperación Python Junio 2021 - Ejercicio 3
 @enunciado: 
 Realizar una función que reciba un array de números y devuelva un array con los números que
están sólo una vez en el array que recibe como argumento.
Entrega las llamadas a la función que has hecho para comprobar que el funcionamiento es el
adecuado.
'''

#===============================================================================
# Esta función comprueba los números que no se repiten en una lista de números y
# devuelve una lista con ellos.
# Recibe: una lista de números
# Devuelve: una lista con los números que no se repiten en la lista que recibe
#===============================================================================
def compruebaNumerosSinRepetir(numeros):
    numerosSinRepetir=[]
    for i in numeros:
        #Si los números no están ya en la lista nueva, los añado, así evito que se
        #repitan
        if i not in numerosSinRepetir:
            numerosSinRepetir.append(i)
                    
    return numerosSinRepetir


assert(compruebaNumerosSinRepetir([1,254,1,26,47,8633,-1,254])==[1,254,26,47,8633,-1])
assert(compruebaNumerosSinRepetir([4,4,4,4])==[4])
assert(compruebaNumerosSinRepetir([1,2,3,4,5,6,7,8,9,10,11,12])==[1,2,3,4,5,6,7,8,9,10,11,12])
