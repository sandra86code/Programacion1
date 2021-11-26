'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 6
 @enunciado: 
 Crea un programa que calcule cuántos números negativos hay en un array de
enteros.
'''

#===============================================================================
# Esta función calcula cuántos números negativos hay en un array de enteros
# Recibe: una lista de enteros
# Devuelve: la cantidad de enteros negativos en la lista
#===============================================================================
def calculaNegativosDeLista(lista):
    cantidadNegativos=0
    for i in lista:
        if i<0:
            cantidadNegativos+=1
            
    return cantidadNegativos


assert(calculaNegativosDeLista([1,2,3,4,5])==0)
assert(calculaNegativosDeLista([-1,2,3,4,-5,0])==2)
assert(calculaNegativosDeLista([-1,2,-3,-4,-5,0])==4)