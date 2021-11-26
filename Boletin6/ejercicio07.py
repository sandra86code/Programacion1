'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Boletin 6 - Ejercicio 7
 @enunciado: 
Escribir una función que indique si dos fichas de dominó encajan o no. 
Las fichas son recibidas en dos cadenas, por ejemplo:[3,4] [2,5].


NOTA: 
En el dominó, encajar dos fichas es colocar una pieza al lado de otra, 
debiendo tener por lo menos un valor en común (ejemplo: 2-5 encaja con 5-6).
'''

#===============================================================================
# Esta función comprueba si dos fichas de dominó encajan 
# Recibe: una lista compuesta por dos listas
# Devuelve:
# Si la lista no está compuesta por dos listas, el mensaje "Error en el número de fichas"
# Si encajan, True
# Si no encjana, False
#===============================================================================
def encajan(fichas):
    if len(fichas)!=2:
        encontrado="Error en el número de fichas"
    else:
        ficha1=fichas[0]
        ficha2=fichas[1]
        
        i=0
        encontrado=False
        while i<len(ficha1) and encontrado==False:
            if ficha1[i] in ficha2:
                encontrado=True
            i+=1

    return encontrado


assert(encajan([[3,4]])=="Error en el número de fichas")
assert(encajan([[3,4], [4,3], [7,8]])=="Error en el número de fichas")
assert(encajan([[3,4], [2,5]])==False)
assert(encajan([[2,4], [2,5]])==True)
assert(encajan([[0,6], [4,0]])==True)
assert(encajan([[0,6], [6,5]])==True)
assert(encajan([[4,3], [1,3]])==True)
