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


    






# def convierteCuadrado(lista):
#     cuadrado=""
#     for fila in range (len(lista)):
#         fila=lista[fila]
#         for j in range (len(fila)-1):
#             cuadrado+=str(fila[j])
#             cuadrado+=" "
#         cuadrado+=str(fila[-1])
#         cuadrado+="\n"
#
#     return cuadrado
#
#
#
# def insertaEnCuadrado(numero, cuadrado):
#     i=0
#     while i<len(cuadrado):
#         fila=numero-i
#         columna=2*numero-i
#         cuadrado[fila][columna]
#     #
#     #
#     #
#     #         # if fila-columna==0:
#     #         #     numero-=1
#     #         #     cuadrado[fila][columna]=numero
#     #         columna+=1
#     #     fila+=1
#
#     return cuadrado
#
#
# def creaCuadrado(numero):
#     numFilas=numero+(numero-1)
#     numColumnas=numFilas
#     cuadrado=[]
#     for i in range (numFilas):
#         cuadrado.append([])
#         for j in range (numColumnas):
#             cuadrado[i].append([])
#
#     return cuadrado


num=int(input("Introduce un número entero positivo: "))
while num<=0:
    print("El número debe ser un entero positivo (mayor que 0).")
    num=int(input("Introduce un número entero positivo: "))

numero=num
cuadrado=""
for i in range (num):
    cantidad=2*(num-i)-1
    for j in range(i):
        cuadrado+=str(num-j)
    for k in range(1, cantidad+1):
        cuadrado+=str(num-i)
    for l in range(i):
        cuadrado+=str(numero-i+l+1)
    cuadrado+="\n"
for m in range (2, num+1):
    cantidad=2*m-1
    for n in range(m-2):
        cuadrado+=str(numero-m+n+1)
    for o in range(1, cantidad+1):
        cuadrado+=str(m)
    # for p in range(i):
    #     cuadrado+=str(num-p)
    cuadrado+="\n"
    
print(cuadrado)
# print(convierteCuadrado(insertaEnCuadrado(num, creaCuadrado(num))))

