'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 25 nov 2021
 @nombre: Cuadrado de números
 @enunciado: 
 Cuadrado de números:
Crea un programa que lea del teclado un número y genere un mitadSuperior con el patrón siguiente
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

#===============================================================================
# Esta función convierte una lista de números de x posiciones en un cuadrado de 
# formato string
# de x filas
# Recibe: una lista de números
# Devuelve: el cuadrado en formato string
#===============================================================================
def convierteCuadrado(lista):
    
    cuadrado=""
    #Recorro la lista para acceder a cada una de las sublistas
    for fila in range (len(lista)):
        fila=lista[fila]
        #Recorro cada una de las sublistas hasta la posición -1 por
        #el tema del espacio
        for j in range (len(fila)-1):
            #Acumulo el número en formato string en la fila del cuadrado
            #y le añado un espacio detrás
            cuadrado+=str(fila[j])
            cuadrado+=" "
        #Añado el último elemento
        cuadrado+=str(fila[-1])
        #Hago el salto de línea
        cuadrado+="\n"

    return cuadrado


#===============================================================================
# Esta función inserta los números enteros en el cuadrado vacío (lista con sublistas)
# Recibe: un número de tipo entero y el cuadrado, que es una lista con sublistas anidadas
# vacías
# Devuelve: la lista con las sublistas anidadas pero con números enteros dentro 
#===============================================================================
def insertaEnCuadrado(num, cuadrado):
    #Un bucle que va desde 0 hasta el número-1
    for i in range (num):
        #Calculo la cantidad de veces que se repite el mismo número (que va decreciendo)
        #en cada fila. Dicha cantidad también decrece en 1.
        cantidad=2*(num-i)-1
        #Este bucle va a llenar los números entre el inicio de la lista y los números que se
        #repiten. Aumenta en 1 con cada iteración y los números tb decrecen en 1.
        for j in range(i):
            cuadrado[i].append(num-j)
        #Este bucle llena la cantidad central de números repetidos en la fila, la cantidad de
        #veces de la variable de arriba. Va decreciendo en 2 por fila
        for k in range(cantidad):
            cuadrado[i].append(num-i)
        #Este bucle va a llenar los números entre el inicio de la lista y los números que se
        #repiten. Aumenta en 1 con cada iteración y los números aumentan en 1.
        for l in range(i):
            cuadrado[i].append(num-i+l+1)
    
    #Hasta aquí he llenado la mitad del cuadrado (las listas)+1, por lo que ahora necesito llenar
    #la otra mitad, por lo que recorro el cuadrado hasta su mitad-1 (resultado de la división entera)
    #y cada fila del principio +1 será la fila del final -1
    for n in range (len(cuadrado)//2):
        #Como empieza en 0 la iteración y necesito que la primera por el final sea la -1, pues le resto
        #-1 a -n
        cuadrado[-n-1]=cuadrado[n]

    return cuadrado

#===============================================================================
# Esta función crea el cuadrado con listas llena de sublistas, una por cada fila
# del cuadrado
# Recibe: un número entero
# Devuelve: la lista con sus sublistas vacías
#===============================================================================
def creaCuadrado(numero):
    #Calculo el número de filas que siempre será el doble del número -1
    numFilas=numero+(numero-1)
    cuadradoVacio=[]
    #Añado una lista por cada fila
    for i in range (numFilas):
        cuadradoVacio.append([])
        
    return cuadradoVacio


#Pido y compruebo datos
num=int(input("Introduce un número entero positivo: "))
while num<=0:
    print("El número debe ser un entero positivo (mayor que 0).")
    num=int(input("Introduce un número entero positivo: "))

#Imprimo los resultados llamado a las funciones creadas con los datos proporcionados 
# por el usuario
print("\n"+convierteCuadrado(insertaEnCuadrado(num, creaCuadrado(num))))

