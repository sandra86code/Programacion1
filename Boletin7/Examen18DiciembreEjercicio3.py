'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 18 Diciembre 2020 - Ejercicio 23
 @enunciado: 
Realizar una función que dada una fecha en formato 12 horas nos devuelva la fecha en formato 24
horas.
La función recibirá una cadena con el siguiente formato hh:mm:ssAM u hh:mm:ssPM y deberá
devolver el formato de fecho hh:mm:ss con 24 horas.
Si la fecha que recibe no tiene el formato adecuado deberá devolver una cadena vacía.

Ejemplos:
convierteFecha(“12:02:04AM”) → “”
convierteFecha(“12:02:04PM”) → “”
convierteFecha(“11:02:04AM”) → “11:02:04”
convierteFecha(“11:02:04PM”) → “23:02:04”
convierteFecha(“14:89:04AM”) → “”
convierteFecha(“12:02:04AP”) → “”
'''