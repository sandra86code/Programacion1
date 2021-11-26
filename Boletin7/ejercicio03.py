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

#===============================================================================
# Esta función devuelve en un array de enteros la distancia desde cada
# caracter hasta una posicion concreta
# Recibe: una cadena de caracteres y una posicion de lista
# Devuelve: una lista de enteros
#===============================================================================
def calculaPosiciones(cadena, posicion):
    
    resultado=[]
    for i in range (len(cadena)):
        if i==posicion:
            resultado.append(0)
        else:
            #La distancia desde cada caracter a la posicion es la posicion menos
            #el caracter, pero esto vale para los numeros hasta la posicion,
            #para los números tras la posición los pone en negativo, por eso usamos
            #el funcion abs para que nos de su valor absoluto
            resultado.append(abs(posicion-i))

    return resultado


#===============================================================================
# Esta función nos dice en qué posición o posiciones de una cadena se encuentra
# un caracter y los devuelve en una cadena
# Recibe: una cadena de caracteres y un caracter
# Devuelve: una lista de enteros
#===============================================================================
def posicionesCaracterEnCadena(cadena, caracter):
    
    posicionesCaracter=[]
    for i in range (len(cadena)):
        if cadena[i]==caracter:
            posicionesCaracter.append(i)
    
    return posicionesCaracter


assert(posicionesCaracterEnCadena("algoritmo", "o")==[3, 8])
assert(posicionesCaracterEnCadena("abcdefga", "a")==[0, 7])


#===============================================================================
# Esta función compara la distancia menor desde cada caracter hasta un caracter
# que recibe la función
# Recibe: una cadena de caracteres y un caracter
# Devuelve: una lista de enteros con las posiciones menores desde cada caracter de la
# cadena hasta el caracter que recibe la función
#===============================================================================
def comparaPosiciones(cadena, caracter):
    #Creo la lista de posiciones con la llamada a la función correspondiente
    posiciones=posicionesCaracterEnCadena(cadena, caracter)
    #Creo la lista con la que voy a ir comparando
    resultado=[]
    #Creo un bucle que tiene las mismas iteraciones que elementos tenga la lista
    # de posiciones
    for i in range (len(posiciones)):
        #Creo una nueva lista utilizando una de las posiciones usando la funcion
        #correspondiente
        resultadoActual=calculaPosiciones(cadena,posiciones[i])
        #Recorro dicha lista
        for i in range (len(resultadoActual)):
            #En la primera iteración, no podré comparar porque resultado está vacía,
            #por eso compruebo que su longitud sea mayor que 0
            if len(resultado)>0:
                #A partir de la segunda iteración del bucle, si el valor del primer
                #elemento de la lista resultadoActual es menor que el de resultado,
                #cambio el valor de ese elemento de resultado, asignándole el valor
                #de resultadoActual. Sino, no realizo ningún cambio, por eso no hay else.
                if resultadoActual[i]<resultado[i]:
                    resultado[i]=resultadoActual[i]
            #Si está vacía, resultado toma el valor de resultado Actual, para que
            #en la próxima iteración, cuando esta cambie de valor, tenga con que comparar
            #dichos valores
            else:
                resultado=resultadoActual
    
    return resultado


#===============================================================================
# Esta función es la principal del programa
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
# 1. Pide los datos y los comprueba
# 2. Convierte los datos a minúscula
# 3. Imprime el resultado final del programa
#===============================================================================
def main():
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
    
    #Imprimo el resultado final del programa
    print(comparaPosiciones(cadena, caracter))            
        
main()





