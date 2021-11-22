'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Boletin 6 - Ejercicio 1
 @enunciado: 
Crea un programa que genere 1OO números de forma aleatoria y que posteriormente 
ofrezca al usuario la posibilidad de:
    1.    Conocer el mayor de los números
    2.    Conocer el menor de los números
    3.    Obtener la suma de todos los números
    4.    Obtener la media de los números
    5.    Sustituir el valor de un elemento por otro número introducido por teclado.
    6.    Mostrar todos los números.

Realiza las opciones con funciones.
'''
#Importo la librería random para crear los números aleatorios
import random

#===============================================================================
# Esta función sustituye el valor de un elemento de una lista de números por otro
# número
# Recibe: lista de números, un número entero y otro número entero que representa
# una posición de la lista
# Devuelve: la lista con el número sustituído
#===============================================================================
def sustituirNumero(lista, num, posicion):
    #Recorro la lista y cuando i (posición en la lista) coincida con la posición
    #recibida, el elemento de esa posición se convierte en el número recibido
    for i in range (len(lista)):
        if i==posicion:
            lista[i]=num
    
    return lista


#===============================================================================
# Esta función calcula la media de los números de una lista de números
# Recibe: una lista de números
# Devuelve: la media de los números (usando la función de sumar números entre el
# número de items de la lista) y redondea esa media a 2 decimales.
#===============================================================================
def mediaNumeros(lista):
    
    return (round(sumaNumeros(lista)/100, 2))


#===============================================================================
# Esta función suma los números de una lista
# Recibe: una lista de números
# Devuelve: la suma de dichos números
#===============================================================================
def sumaNumeros(lista):
    suma=0
    for i in lista:
        suma+=i
    
    return suma


#===============================================================================
# Esta función calcula el número menor de una lista de números
# Recibe: una lista de números
# Devuelve: el número menor de la lista
#===============================================================================
def esNumMenor(lista):
    #Creo una variable y le asigno un número mayor a cualquiera de los items de
    #la lista (en este caso el random está a 1000, por eso es el 1001).
    #De esta manera, cualquier item va a ser menor que esta variable.
    numMenor=1001
    #Recorro los elementos de la lista
    for i in lista:
        #Si el elemento (número) es menor que el número almacenado en numMenor,
        #el nuevo numMenor es dicho número
        if i<numMenor:
            numMenor=i
   
    return numMenor


#===============================================================================
# Esta función calcula el número mayor de una lista de números
# Recibe: una lista de números
# Devuelve:el número menor de la lista
#===============================================================================
def esNumMayor(lista):
    #Creo una variable y le asigno un número menor a cualquiera de los items de
    #la lista (en este caso el random está a -1000, por eso es el -1001).
    #De esta manera, cualquier item va a ser mayor que esta variable.
    numMayor=-1001
    #Recorro los elementos de la lista
    for i in lista:
        #Si el elemento (número) es mayor que el número almacenado en numMayor,
        #el nuevo numMayor es dicho número
        if i>numMayor:
            numMayor=i
   
    return numMayor


#===============================================================================
# Esta función crea una lista de 100 números aleatorios (entre -1000 y 1000)
# Recibe: no tiene parámetros de entrada
# Devuelve: la lista de 100 números
# 
#===============================================================================
def listaNumerosAleatorios():
    numerosAleatorios=[]
    for i in range(100):
        num=random.randint(-1000, 1000)
        numerosAleatorios.append(num)
    
    return numerosAleatorios


#===============================================================================
# Esta función representa el menú secundario del programa (menú de opciones)
# Recibe una opción y una lista de números 
# Devuelve: no tiene return, sino que imprime un mensaje para cada una de las opciones
#===============================================================================
def menuOpciones(opcion, lista):
   
    if opcion==1:
        mensaje="El número mayor es: %s \n" % esNumMayor(lista)
    elif opcion==2:
        mensaje="El número menor es: %s \n" % esNumMenor(lista)
    elif opcion==3:
        mensaje="La suma de los números es: %s \n" % sumaNumeros(lista)
    elif opcion==4:
        mensaje="La media de los números es: %s \n" % mediaNumeros(lista)
    elif opcion==5:
        #Pido los nuevos datos
        nuevoNum=int(input("Dime el nuevo número: "))
        posicion=int(input("En qué posición quieres sustituirlo (0-99): "))
        #Comprobación de datos
        while posicion<0 or posicion>99:
            print("Posición errónea. Tiene que estar entre 0 y 99. Vuelve a intentarlo.")
            posicion=int(input("En qué posición quieres sustituirlo (0-99): "))
        mensaje="La nueva lista es: %s \n" % sustituirNumero(lista, nuevoNum, posicion)
    else:
        mensaje="Los números son: %s \n" % lista
    
    #Imprimo el mensaje
    print(mensaje)
    #Llamo al menú principal, para que se vuelva a ejecutar el programa en bucle
    menu()
    

#===============================================================================
# Esta función representa el menú principal del programa
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene parámetros de salida
# 1. Muestra el menú
# 2. Pregunta la opción
# 3. Muestra el resultado
#===============================================================================    
def menu():
    menu="Menú de opciones:\n"\
        "1. Conocer el mayor de los números.\n"\
        "2. Conocer el menor de los números.\n"\
        "3. Obtener la suma de todos los números.\n"\
        "4. Obtener la media de los números.\n"\
        "5. Sustituir el valor de un elemento por otro número.\n"\
        "6. Mostrar todos los números.\n"\
        "7. Salir"
        
    print(menu)
    
    opcion=int(input("Elige una opción: "))
    while opcion<1 and opcion>7:
        print("Opción incorrecta. Vuelve a intentarlo")
        opcion=int(input("Elige una opción: "))
    #Mientras que la opción sea diferente a 7, llama a la función del menú de opciones
    if opcion!=7:    
        menuOpciones(opcion, lista)
    #Si la opción es la 7, muestra un mensaje de despedida
    else:
        print("Hasta la próxima.")

#Creo una lista de números aleatorios fuera del menú principal, para que para cualquier
#opción use la misma lista de números y no la reinicialice cada vez        
lista=listaNumerosAleatorios()

#Llamada a la función, ya que no tiene return
menu()