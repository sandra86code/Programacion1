'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 2 Diciembre 2020 - Ejercicio 1 
 @enunciado: 
 Realizar una función que reciba como parámetro una cadena que contenga un dni y 
devuelva un True si el dni es válido y False en caso contrario. Para calcular la letra 
debemos tomar el número completo de hasta 8 cifras de nuestro DNI, lo dividimos entre 23 
y nos quedamos con el resto de dicha división.

El resultado anterior es un número entre 0 y 22. A cada uno de estos posibles 
números le corresponde una letra, según la siguiente tabla:

RESTO    0    1    2    3    4    5    6    7    8    9    10    11    12    13    14    15    16    17    18    19    20    21    22
LETRA    T    R    W    A    G    M    Y    F    P    D    C     B     N     J     Z     S     Q     V     H     L     C     K     E

Si el formato no es válido deberá devolver False.

Mejora opcional: Ten en cuenta que hay dni que en vez de 8 números pueden tener 7.

Entrega las pruebas que has realizado.
'''