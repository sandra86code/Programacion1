'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Boletin 6 - Ejercicio 13
 @enunciado: 
Escribe una función que, dada una lista de nombres y una letra, 
devuelva una lista con todos los nombres que empiezan por dicha letra.
'''

#Importo la función que convierte a minúsculas una cadena
from ejercicio11 import convertirAMinusculas

#===============================================================================
# Esta función crea una lista con las palabras de otra lista que recibe que empiezan
# por un caracter (que puede estar en minúsculas o mayúsculas)
# Recibe: una lista de palabras y un caracter
# Devuelve: la lista con las palabras que empiezan por ese caracter
#===============================================================================

def empiezaPorLetra(lista, caracter):
    listaResultante=[]
    
    # Recorro cada elemento de la lista (palabra) y si la primera letra de la palabra
    # es igual al caracter, lo añado a la lista resultante
    for palabra in lista:
        if convertirAMinusculas(palabra[0])==caracter:
            listaResultante.append(palabra)
    
    return listaResultante


assert(empiezaPorLetra(["Anselmo", "Veronica", "Cristina", "Miguel", "Amalia", "Barbara"], "a")==["Anselmo", "Amalia"])
assert(empiezaPorLetra(["Anselmo", "Veronica", "Cristina", "Miguel", "Amalia", "Barbara"], "d")==[])
assert(empiezaPorLetra(["Anselmo", "Veronica", "Cristina", "Miguel", "Amalia", "Barbara"], "v")==["Veronica"])