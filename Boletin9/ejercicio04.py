'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 3, 2021
 @nombre: Simulacro Examen - Ejercicio 4
 @enunciado: 
 Realizar un programa que pida números positivos y negativos hasta que se introduzca un 0. 
 Una vez tenemos todos los números se debe llamar a una función que debe devolver una lista de 
 unos o menos uno, segun el número sea mayor que el siguiente (un 1) o un menor (un -1).
'''

#===============================================================================
# Esta función recibe una lista y devuelve otra lista de 1 y -1 según el número
#sea mayor que el siguiente (1) o menor que el siguiente (-1).
# Recibe: una lista de números positivos y negativos
# Devuelve: la lista de -1 y 1.
#===============================================================================
def creaLista(lista):
    listaNueva=[]
    for i in range (len(lista)-1):
        if lista[i]>lista[i+1]:
            listaNueva.append(1)
        elif lista[i]<lista[i+1]:
            listaNueva.append(-1)
        else:
            listaNueva.append(0)
            
    return listaNueva


#===============================================================================
# Esta función es la principal del programa, donde creamos la lista de números e
# imprimimos el resultado de la función que crea la lista de -1 y 1
#===============================================================================
def main():
    
    numeros=[]
    num=1
    while num!=0:
        num=int(input("Introduce un número (0 para parar):"))
        numeros.append(num)
    
    print(creaLista(numeros))
    
main()
