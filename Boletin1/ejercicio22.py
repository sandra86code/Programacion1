"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 25, 2021
 @nombre: Boletin 1 - Ejercicio 22 (propuesto en clase) 
 @enunciado: 
 Realiza un programa que solicita números enteros al usuario.
 El programa debe terminar cuando el usuario introduzca -1.
 Al final se nos informará de la suma de los números introducidos
 por el usario, sin incluir el -1 que nos servirá para salir, y de
 si hay algún número par o no entre los introducidos.
"""
 
#Pido el número (Fuera del bucle para que si al principio mete -1, no entre en el bucle while posterior
num=int(input("Introduce un número (-1 para parar): "))
#Creo la variable sumatoria y la igualo a 0
suma=0
#Creo la bandera a false, ya que en un principio no hemos introducido ningún n.º par
par=False
#Creo el bucle cuya condición de entrada es que el número no sea igual a -1.
while num!=-1:
    #Voy sumando los números a la variable sumatoria
    suma+=num
    #Si el número es par, cambio la bandera. Si no entra por aquí, la bandera sigue valiendo False
    if num%2==0:
        par=True
    #Vuelvo a pedir el número
    num=int(input("Introduce un número (-1 para parar): "))

#Imprimo el resultado de la suma    
print("La suma de los números introducidos es %s." % (suma))
#Imprimo el resultado de la bandera
if par==False:
    print("No se han introducido números pares.")
else:
    print("Se ha introducido, al menos, algún número par.")
    