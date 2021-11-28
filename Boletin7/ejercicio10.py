'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 25 nov 2021
 @nombre: Cuadrado de números
 @enunciado: 
 Cuadrado de números:
Crea un programa que lea del teclado un número y genere un cuadrado con el patrón siguiente
donde cada elemento está separado por un espacio.

Resultados de ejemplo:

Número 2:
2 2 2
2 1 2
2 2 2
________________________

Número 4:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
________________________

Número 5:
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
________________________

Número 7:
7 7 7 7 7 7 7 7 7 7 7 7 7
7 6 6 6 6 6 6 6 6 6 6 6 7
7 6 5 5 5 5 5 5 5 5 5 6 7
7 6 5 4 4 4 4 4 4 4 5 6 7
7 6 5 4 3 3 3 3 3 4 5 6 7
7 6 5 4 3 2 2 2 3 4 5 6 7
7 6 5 4 3 2 1 2 3 4 5 6 7
7 6 5 4 3 2 2 2 3 4 5 6 7
7 6 5 4 3 3 3 3 3 4 5 6 7
7 6 5 4 4 4 4 4 4 4 5 6 7
7 6 5 5 5 5 5 5 5 5 5 6 7
7 6 6 6 6 6 6 6 6 6 6 6 7
7 7 7 7 7 7 7 7 7 7 7 7 7
'''

def convierteCuadrado(lista):
    cuadrado=""
    for fila in range (len(lista)):
        fila=lista[fila]
        for j in range (len(fila)-1):
            cuadrado+=str(fila[j])
            cuadrado+=" "
        cuadrado+=str(fila[-1])
        cuadrado+="\n"
    
    return cuadrado
           
    

def insertaEnCuadrado(numero, cuadrado):
    fila=0
    while fila<len(cuadrado):
        columna=0
        while columna<len(cuadrado[fila]):
            cuadrado[0+columna][0+columna]=numero-columna


            
            # if fila-columna==0:
            #     numero-=1
            #     cuadrado[fila][columna]=numero
            columna+=1
        fila+=1
            
    return cuadrado


def creaCuadrado(numero):
    numFilas=numero+(numero-1)
    numColumnas=numFilas
    cuadrado=[]
    for i in range (numFilas):
        cuadrado.append([])
        for j in range (numColumnas):
            cuadrado[i].append([])
        
    return cuadrado


num=int(input("Introduce un número entero positivo: "))
while num<=0:
    print("El número debe ser un entero positivo (mayor que 0).")
    num=int(input("Introduce un número entero positivo: "))
    
print(convierteCuadrado(insertaEnCuadrado(num, creaCuadrado(num))))

