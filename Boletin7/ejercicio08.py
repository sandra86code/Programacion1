'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 8
 @enunciado: 
 Crea un programa que cree 60 números aleatorios de 0 a 100 (usa una constante
para fijar este número).
Muestra:
    ● La media de los números leídos.
    ● El dígito en el que más números terminan.
    ● En qué dígitos no ha terminado ningún número.
    ● Cuántos números terminan en cada uno de los dígitos (0 .. 9).
'''
#Importo la funcion randint de la libreria random
from random import randint

#===============================================================================
# Esta función nos dice cuáles son las posiciones de una lista en la que el valor
# es 0
# Recibe: una lista de enteros
# Devuelve: 
# Una lista con las posiciones en las que el valor es 0
# Si la lista está vacía, un mensaje "Ninguno"
#===============================================================================
def valorCeroEnLista(lista):
    listaPosicionCero=[]
    for i in range(len(lista)):
        if lista[i]==0:
            listaPosicionCero.append(i)
    
    if len(listaPosicionCero)==0:
        listaPosicionCero="Ninguno"
        
    return listaPosicionCero


assert(valorCeroEnLista([7,0,3,7,9,3,2,8,0,1])==[1,8])
assert(valorCeroEnLista([7,10,3,7,9,3,2,8,2,1])=="Ninguno")



#===============================================================================
# Esta función calcula cuál es la posición (o posiciones) del valor mayor de una lista
# de enteros
# Recibe: una lista de enteros
# Devuelve: una lista con la posición (o posiciones cuando los valores mayores coincidan
# en varias posiciones) del valor mayor de la lista
#===============================================================================
def posicionDelMayor(lista):
    mayor=lista[0]
    posicionesMayores=[]
    for i in range (len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    
    for j in range (len(lista)):
        if lista[j]==mayor:
            posicionesMayores.append(j)
    
    return posicionesMayores


#===============================================================================
# Esta función acumula en una lista la cantidad de números de una lista que acaban 
# en cada dígito [0-9]
# Recibe: una lista de enteros 
# Devuelve: una lista correspondiente a cada dígito [0-9] con la cantidad de
# números de la lista que recibe que acaban en ese dígito.
#===============================================================================
def digitoFinalNumeros(lista):
    #Creo la lista de dígitos finales y la inicializo a 0 en las 10 posiciones posibles
    listaDigitosFinales=[0,0,0,0,0,0,0,0,0,0]
    #Creo una lista de dígitos pero de tipo String, ya que voy a comprobar el dígito
    #final de cada número, conviertiendo este a String. De esta manera la comparación
    #es más sencilla
    listaDigitos=["0","1","2","3","4","5","6","7","8","9"]
    #Recorro la lista de números recibida
    for numero in lista:
        #Convierto cada número a string), para comparar su dígito final
        numero=str(numero)
        #Recorro la lista de Dígitos (de tipo string)
        for i in range (len(listaDigitos)):
            #Si el dígito final del número coincide con el valor de la posicion en la 
            #lista de dígitos, esa misma posición en la lista de Digitos finales la aumento
            #en 1
            if numero[-1]==listaDigitos[i]:
                listaDigitosFinales[i]+=1
    #Devuelvo la lista de dígitos finales
    return listaDigitosFinales
        

#===============================================================================
# Esta función calcula la media de los números redondeada a 2 decimales
# Recibe: una lista de números enteros
# Devuelve: la media de los números con un redonde a 2 decimales
#===============================================================================
def calcularMedia(lista):
    suma=0
    for i in lista:
        suma+=i
    
    media=round(suma / len(lista),2)
    
    return media

#===============================================================================
# Esta función genera una lista de x números aleatorios (que recibe como constante)
# Recibe: una constante con la cantidad de números que incluirá la lista
# Devuelve: la lista de números aleatorios
#===============================================================================
def generaListaAleatorios(CANTIDAD_ALEATORIOS):
    listaAleatorios=[]
    for i in range (CANTIDAD_ALEATORIOS):
        aleatorio=randint(0,100)
        listaAleatorios.append(aleatorio)

    return listaAleatorios


#===============================================================================
# Esta función es la principal del programa
# Recibe: no tiene parámetros
# Devuelve: no tiene return
# 1. Guarda la lista de aleatorios en una variable
# 2. Imprime la media
# 3. Imprime el dígito en el que más numeros terminan
# 4. Imprime el/los dígitos en el que no termina ningún numero. Ninguno en el caso
# de que no lo haya.
# 5. Imprime la cantidad de números que acaban en 0, en 1, en 2, en 3, ... en 9.
#===============================================================================
def main():
    CANTIDAD_ALEATORIOS=60
    lista=generaListaAleatorios(CANTIDAD_ALEATORIOS)
    
    print("La media de los números es: %s" % calcularMedia(lista))
    print("El dígito en el que más números terminan es: %s" % (posicionDelMayor(digitoFinalNumeros(lista))))
    print("Los dígitos en los que no termina ningún número son: %s" % (valorCeroEnLista(digitoFinalNumeros(lista))))
    print("Números que terminan en 0: %s números" % (digitoFinalNumeros(lista)[0]))
    print("Números que terminan en 1: %s números" % (digitoFinalNumeros(lista)[1]))
    print("Números que terminan en 2: %s números" % (digitoFinalNumeros(lista)[2]))
    print("Números que terminan en 3: %s números" % (digitoFinalNumeros(lista)[3]))
    print("Números que terminan en 4: %s números" % (digitoFinalNumeros(lista)[4]))
    print("Números que terminan en 5: %s números" % (digitoFinalNumeros(lista)[5]))
    print("Números que terminan en 6: %s números" % (digitoFinalNumeros(lista)[6]))
    print("Números que terminan en 7: %s números" % (digitoFinalNumeros(lista)[7]))
    print("Números que terminan en 8: %s números" % (digitoFinalNumeros(lista)[8]))
    print("Números que terminan en 9: %s números" % (digitoFinalNumeros(lista)[9]))

main()
