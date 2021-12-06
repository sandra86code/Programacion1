'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 2 Diciembre 2020 - Ejercicio 3
 @enunciado: 
 Realizar un programa que nos sirva para crear el id de usuario que nuestros empleados utilizarán
para conectarse a nuestras aplicaciones. 
El programa debe preguntarle al usuario su nombre y sus apellidos, separando los datos por coma. 
Es decir si me preguntan a mi yo debo poner JoséManuel,Sevillano,Armenta (puedes suponer que nos 
van a dar los valores bien). 
Luego debe preguntar el dni, debe comprobar que se trata de un dni válido, si no es válido volver 
a preguntarlo hasta que nos dé un dni válido. 
Por último debe llamar a una función que devuelva el id.
Para calcular el id le pasaremos la cadena con el nombre y apellidos y creará el id con los tres 
primeros caracteres del nombre, los tres últimos del primer apellido, los tres primeros del segundo 
apellido y los tres primeros números del dni.
'''

from Examen02DiciembreEjercicio2 import validaDni

#===============================================================================
# Esta función calcula el id a partir del nombre y apellidos y del dni
# Recibe: dni (cadena de caracteres), nombre (cadena de caracteres)
# Devuelve: el id (cadena de caracteres)
#===============================================================================
def calculaId(dni, nombre):
   
    id=""
    #Separo nombre y apellidos en una lista
    listaNombre=separarCadenaEnLista(nombre)
    #Bucle para los 3 primeros caracteres del nombre, que está en la posicion 0 de
    #la lista que he creado
    for i in range (3):
        id+=listaNombre[0][i]
    #Bucle para los 3 últimos caracteres del primer apellido, que está en la posición 1
    #de la lista que he creado.
    #La i toma los valores 3,2,1, para así luego poder acceder a la posición -3,-2,-1 del item
    for i in range (3,0,-1):
        id+=listaNombre[1][-i]
    #Bucle para los 3 primeros caracteres del dni
    for i in range (3):
        id+=listaNombre[2][i]
    for i in range (3):
        id+=dni[i]
        
    return id


#===============================================================================
# Esta función toma una cadena de caracteres y separa sus elementos en una lista
# cuando se encuentra una coma (,)
# Recibe: una cadena de caracteres
# Devuelve: una lista con las palabras separadas
#===============================================================================
def separarCadenaEnLista(cadena):
    lista=[]
    palabra=""
    for i in cadena:
        if i!=",":
            palabra+=i
        else:
            lista.append(palabra)
            palabra=""
    if palabra!="":
        lista.append(palabra)
    
    return lista


#===============================================================================
# Esta función es la principal del programa.
# 1. Pregunta al usuario su nombre y apellidos.
# 2. Pregunta al usuario su dni y lo valida utilizando la función adecuada que está
# importada del otro ejercicio.
# 3. Imprime el resultado de la función calcularId.
#===============================================================================
def main():
    
    nombre=input("Introduce tu nombre (sin espacios) y tus apellidos, separando los datos por coma: ")
    
    dni=input("Introduce tu dni (sin letra): ")
    while validaDni(dni)==False:
        print("Datos incorrectos.")
        dni=input("Introduce tu dni (sin letra): ")
    
    print("Su id es %s" % (calculaId(dni, nombre)))


main()
    