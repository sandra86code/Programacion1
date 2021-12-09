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
# Esta función 
# Recibe 
# Devuelve:
# 
#===============================================================================
def sumaNumerosDeCadena (cadena, numero):
    suma=0
    coincidencias=0
    for i in cadena:
        if i>=chr(48) and i<=chr(57):
            if numero==0 and int(i)%2==0:
                suma+=int(i)
            elif numero==1 and int(i)%2==1:
                suma+=int(i)
            coincidencias+=1
    if coincidencias==0:
        suma=False 

    return suma

assert(sumaNumerosDeCadena("22abc53", 1)==8)
assert(sumaNumerosDeCadena("22abc53", 0)==4)
assert(sumaNumerosDeCadena("22abc68", 1)==0)
assert(sumaNumerosDeCadena("31abc53", 0)==0)
assert(sumaNumerosDeCadena("deabc", 0)==False)
assert(sumaNumerosDeCadena("deabc", 1)==False)
