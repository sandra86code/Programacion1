'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 3
 @enunciado: 
 Dada una cadena S y un carácter C, devolver un array de enteros representando la distancia más
corta desde cada carácter en la cadena hasta la posición del carácter C.

Ejemplo 1:
Entrada: "algoritmo", 'o'
Salida: [3, 2, 1, 0, 1, 2, 2, 1, 0]

Ejemplo 2:
Entrada: "abcdefga", 'a'
Salida: [0, 1, 2, 3, 3, 2, 1, 0]

Precondiciones:
- La longitud de S está en [1, 10000].
- C es un único carácter.
- C se encuentra en S.
- Todas las letras en S y C son minúsculas.
'''


def posicionCercanaDePosicion(cadena,posicion):
    listaPosiciones=[]
    for i in range(len(cadena)):
        listaPosiciones.append(posicion-i)

    return listaPosiciones


def posicionMasCercana(cadena, caracter):
    listaPosicionesCaracter=[]
    for i in range (len(cadena)):
        if cadena[i]==caracter:
            listaPosicionesCaracter.append(i)
    
    for i in range (len(listaPosicionesCaracter)):
        listaPosiciones=posicionCercanaDePosicion(cadena, listaPosicionesCaracter[i])
        
    return listaPosicionesCaracter


#Pido los datos de la cadena
cadena=input("Introduce una frase o palabra (en minúsculas): ")
#Compruebo que la precondición de la longitud de la cadena sea correcta y sino
#vuelvo a pedir los datos
while len(cadena)<0 or len(cadena)>10000:
    print("Error. La cadena debe tener una longitud entre 1 y 10000.")
    cadena=input("Introduce una frase o palabra (en minúsculas): ")

#Pido los datos del caracter
caracter=input("Introduce un caracter para hacer la comprobacion: ")
#Compruebo que el caracter sea una sola letra y que esté en la cadena. 
#En caso contrario, vuelvo a pedirlo.
while len(caracter)!=1 or caracter not in cadena:
    print("Error. El caracter debe ser una única letra y encontrarse en la cadena.")
    caracter=input("Introduce un caracter para hacer la comprobacion: ")

#Convierto la cadena y el caracter a minúsculas
cadena=cadena.lower()
caracter=caracter.lower()

#Imprimo el resultado
print(posicionMasCercana(cadena, caracter))



# assert(posicionMasCercana("algoritmo", "o")==[3, 2, 1, 0, 1, 2, 2, 1, 0])
# assert(posicionMasCercana("abcdefga", "a")==[0, 1, 2, 3, 3, 2, 1, 0])

