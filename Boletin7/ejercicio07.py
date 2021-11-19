'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 7
 @enunciado: 
Escribir una función que indique si dos fichas de dominó encajan o no. 
Las fichas son recibidas en dos cadenas, por ejemplo:[3,4] [2,5].


NOTA: 
En el dominó, encajar dos fichas es colocar una pieza al lado de otra, 
debiendo tener por lo menos un valor en común (ejemplo: 2-5 encaja con 5-6).
'''

#===============================================================================
# Esta función comprueba si dos fichas de dominó encajan 
# Recibe: dos listas de 2 valores cada una
# Devuelve: 
# Si encajan, el mensaje "Las fichas encajan"
# Si no encjana, el mensaje "Las fichas no encajan"
#===============================================================================
def encajan(ficha1, ficha2):
    if ficha1[0]==ficha2[0] or ficha1[1]==ficha2[0] or ficha1[0]==ficha2[1] or ficha1[1]==ficha2[1]:
        mensaje="Las fichas encajan"
    else:
        mensaje="Las fichas no encajan"

    return mensaje

assert(encajan([3,4], [2,5])=="Las fichas no encajan")
assert(encajan([2,4], [2,5])=="Las fichas encajan")
assert(encajan([0,6], [4,0])=="Las fichas encajan")
assert(encajan([0,6], [6,5])=="Las fichas encajan")
assert(encajan([4,3], [1,3])=="Las fichas encajan")