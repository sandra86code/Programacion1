'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 17 
 @enunciado: 
 Pedir la edad a dos personas y decir quién es más joven, 
 la primera, la segunda o si tienen la misma edad.
'''

edadA = int(input("¿Cuántos años tiene la persona A?"))
while edadA<=0:
    print("Datos erróneos.")
    edadA = int(input("¿Cuántos años tiene la persona A?"))
    
edadB = int(input("¿Cuántos años tiene la persona B?"))
while edadB<=0:
    print("Datos erróneos.")
    edadB = int(input("¿Cuántos años tiene la persona B?"))
    
if edadA==edadB:
    print("La persona A y la persona B tienen la misma edad.")
elif edadA<edadB:
    print("La persona A es más joven que la persona B.")
else:
    print("La persona B es más joven que la persona A.")