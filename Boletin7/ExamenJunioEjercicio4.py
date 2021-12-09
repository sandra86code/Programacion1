'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen Recuperación Python Junio 2021 - Ejercicio 4
 @enunciado: 
 Realizar una función que reciba como parámetro una cadena y devuelva true si la cadena empieza
con la misma palabra que termina. Obviamente el delimitador de la palabra será el espacio.
Ejemplo:
“Inma siempre llama primero a Inma” → True
“Inma siempre llama primera a inma” → False
“Inma siempre llama primero a Pepe” → False
Entrega las llamadas a la función que has hecho para comprobar que el funcionamiento es el
adecuado.
'''

#===============================================================================
# Esta función pasa cada palabra de una cadena a una lista. Usa de delimitador
# el espacio
# Recibe: una cadena de caracteres
# Devuelve: una lista con las palabras de la cadena
#===============================================================================
def cadenaAArray(cadena):
    listaPalabras=[]
    
    palabra=""
    for i in cadena:
        if i!=" ":
            palabra+=i
        else:
            listaPalabras.append(palabra)
            palabra=""
    
    if palabra!="":
        listaPalabras.append(palabra)
        
        
    return listaPalabras


#===============================================================================
# Esta función comprueba si una frase acaba por la misma palabra que empieza.
# Es case sensitive.
# Recibe: una cadena de caracteres
# Devuelve:
# True si acaba por la misma palabra que empieza
# False si no acaba por la misma palabra que empieza
#===============================================================================
def terminaPorPalabraInicial(cadena):
    #Creo una lista con el resultado de la llamada de la función de arriba    
    cadenaEnLista=cadenaAArray(cadena)
    
    #Compruebo si el primer elemento y el último son exactamente iguales (incluidas
    #mayúsculas y minúsculas)
    return cadenaEnLista[0]==cadenaEnLista[-1]


assert(terminaPorPalabraInicial("Inma siempre llama primero a Inma")==True)
assert(terminaPorPalabraInicial("Inma siempre llama primero a inma")==False)
assert(terminaPorPalabraInicial("Inma siempre llama primero a Pepe")==False)
assert(terminaPorPalabraInicial("Inmac siempre llama primero a Inma")==False)

    