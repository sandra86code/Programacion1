'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen Recuperación Python Junio 2021 - Ejercicio 2
 @enunciado: 
 Realizar una función que reciba una cadena de caracteres en el que puede haber números y
cadenas y un valor numérico que podrá ser 0 o 1. La función debe devolver el resultado de la suma
de todos los números pares que aparecen en la cadena si el segundo parámetro que se le pasa es un
0, y la suma de todos los números impares que aparecen en la cadena si el segundo parámetro es un
1.

Ej: “22abc53”, 1 → 8

Entrega las llamadas a la función que has hecho para comprobar que el funcionamiento es el
adecuado.
'''

#===============================================================================
# Esta función suma los números de una cadena teniendo en cuenta un número que se
# da. Si el número es 0, suma los pares, si el número es 1, suma los impares.
# Recibe: una cadena de caracteres y un número entero (0 o 1)
# Devuelve:
# False si no hay números en la cadena, da igual qué número sea
# Si el número es 0, la suma de los números pares de la cadena.
# Si el número es 1, la suma de los números pares de la cadena.
#===============================================================================
def sumaNumerosDeCadena (cadena, numero):
    suma=0
    coincidencias=0
    if numero in {0,1}:
        for i in cadena:
            #Compruebo que el caracter de la cadena corresponda con un número ["0","9"]
            #del código ASCII.
            if i>=chr(48) and i<=chr(57):
                #El resultado del resto para pares coincide con el número que se introduce
                if int(i)%2==numero:
                    suma+=int(i)
                elif int(i)%2==numero:
                    suma+=int(i)
                coincidencias+=1
    #Controlo si el número no es un entero que sea 0 o 1. En ese caso devuelvo False
    else:
        suma=False
    #Si no hay coincidencias, es que no hay números en la cadena, por lo que devuelvo False
    if coincidencias==0:
        suma=False 

    return suma



assert(sumaNumerosDeCadena("22abc53", 1)==8)
assert(sumaNumerosDeCadena("22abc53", 0)==4)
assert(sumaNumerosDeCadena("22abc68", 1)==0)
assert(sumaNumerosDeCadena("31abc53", 0)==0)
assert(sumaNumerosDeCadena("deabc", 0)==False)
assert(sumaNumerosDeCadena("deabc", 1)==False)
assert(sumaNumerosDeCadena("22abc53", 2)==False)
assert(sumaNumerosDeCadena("22abc53", "w")==False)
