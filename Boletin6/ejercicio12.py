'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 12
 @enunciado: 
Escribe una función que reciba dos listas y devuelva los elementos que 
pertenecen a una o a otra, pero sin repetir ninguno (unión de conjuntos).
'''

#Importo la función del ejercicio 11 que convierte una cadena a minúsculas
from ejercicio11 import convertirAMinusculas

#===============================================================================
# Esta función une dos listas sin repetir los elementos comunes si los hay
# Recibe: dos listas de tipo string
# Devuelve: una lista con la unión de las que recibe, sin repetir elementos comunes
#===============================================================================
def unirListas(lista1, lista2):
    listaUnida=[]
    for i in lista1:
        #Si el item en minúsculas de la lista1 no está en la listaUnida,
        #lo introduzco en la listaUnida (convertido a minúsculas)
        if convertirAMinusculas(i) not in listaUnida:
            listaUnida.append(convertirAMinusculas(i))
            
    for j in lista2:
        #Si el item en minúsculas de la lista2 no está en la listaUnida,
        #lo introduzco en la listaUnida (convertido a minúsculas)
        if convertirAMinusculas(j) not in listaUnida:
            listaUnida.append(convertirAMinusculas(j))
    
    return listaUnida


assert(unirListas(["perro", "sala", "perro", "zapato"], ["evidencia", "Perro", "ruido", "rima", "zapato"])==["perro", "sala", "zapato", "evidencia", "ruido", "rima"])
