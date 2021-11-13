'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 9  
 @enunciado: 
 Queremos crear un programa que trabaje con fracciones a/b. 
 Para representar una fracción vamos a utilizar dos enteros: numerador y denominador. 
 Vamos a crear las siguientes funciones para trabajar con funciones:
    1. Leer_fracción: La tarea de esta función es leer por teclado el numerador y el
    denominador. Cuando leas una fracción debes simplificarla.
    2. Escribir_fracción: Esta función escribe en pantalla la fracción. Si el denominador es 1, se
    muestra sólo el numerador.
    3. Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
    4. Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir
    numerador y dominador por el MCD del numerador y denominador.
    5. Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de
    las dos fracciones. La suma de dos fracciones es otra fracción cuyo
    numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción
    resultado.
    6. Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y
    denominador=d1*d2. Se debe simplificar la fracción resultado.
    7. Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para
    ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
    8. Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello
    numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.

Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
    1. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
    2. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
    3. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la
    producto.
    4. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
    5. Salir
'''

'''
Esta función pide al usuario el numerador y el denominador de una función y los devuelve en una lista
Recibe: No tiene parámetros
Devuelve: una lista de 2 elementos, numerador y denominador
'''
def leerFraccion():
    #Pedimos datos
    numerador=int(input("Introduce el numerador de la fracción: "))
    denominador=int(input("Introduce el denominador de la fracción: "))
    #Comprobamos que el denominador no es 0, ya que división entre 0 da error
    while denominador==0:
        print("Datos erróneos. El denominador no puede ser 0. Vuelva a intentarlo.")
        denominador=int(input("Introduce el denominador de la fracción: "))
    
    return [numerador, denominador]

'''
Esta función simplifica una fracción (lista de 2 elementos), usando la función para calcular el mcd
Recibe una lista de 2 elementos
Devuelve: una lista de 2 elementos de enteros, simplificada
'''
def simplificarFraccion(fraccion):
    
    mcd=calcularMcd(fraccion)
    
    return [fraccion[0]//mcd, fraccion[1]//mcd]

'''
Esta función pasa una lista de dos elementos y la escribe como cadena
Recibe una fracción (lista de 2 elementos de enteros)
Devuelve:
Si el denominador es 1, devuelve solo el denominador (entero)
De lo contrario, devuelve la función como string
'''
def escribirFraccion(fraccion):
    if fraccion[1]==1:
        fraccion=fraccion[0]
    else:
        fraccion="%s/%s" %(fraccion[0], fraccion[1])
    return fraccion

'''
Esta función calcula el mcd del numerador y denominador de una fraccion 
Recibe una fraccion (lista de 2 elementos enteros)
Devuelve: el mcd de numerador y denominador
'''
def calcularMcd(fraccion):
    if fraccion[0]>fraccion[1]:
        numMenor=fraccion[1]
        numMayor=fraccion[0]
    else:
        numMenor=fraccion[0]
        numMayor=fraccion[1]
        
    mcd=1
    for i in range(2,numMenor+1):
        if numMayor%i==0:
            mcd=i
    
    return mcd

'''
Esta función suma dos fracciones y simplifica la solución usando la función simplificarFraccion
Recibe dos fracciones, que cada una son una lista de 2 números enteros
Devuelve:
La función resultante simplificada
'''
def sumarFracciones(fraccion1, fraccion2):
    numerador=(fraccion1[0] * fraccion2[1]) + (fraccion2[0] * fraccion1[1])
    denominador=(fraccion2[0] * fraccion2[1])
    fraccionSumada=[numerador, denominador]

    return simplificarFraccion(fraccionSumada)

'''
Esta función resta dos fracciones y simplifica la solución usando la función simplificarFraccion
Recibe dos fracciones, que cada una son una lista de 2 números enteros
Devuelve:
La función resultante simplificada
'''
def restarFracciones(fraccion1, fraccion2):
    numerador=(fraccion1[0] * fraccion2[1]) - (fraccion2[0] * fraccion1[1])
    denominador=(fraccion2[0] * fraccion2[1])
    fraccionRestada=[numerador, denominador]

    return simplificarFraccion(fraccionRestada)

'''
Esta función multiplica dos fracciones y simplifica la solución usando la función simplificarFraccion
Recibe dos fracciones, que cada una son una lista de 2 números enteros
Devuelve:
La función resultante simplificada
'''
def multiplicarFracciones(fraccion1, fraccion2):
    numerador=(fraccion1[0] * fraccion1[1])
    denominador=(fraccion2[0] * fraccion2[1])
    fraccionMultiplicada=[numerador, denominador]

    return simplificarFraccion(fraccionMultiplicada)

'''
Esta función divide dos fracciones y simplifica la solución usando la función simplificarFraccion
Recibe dos fracciones, que cada una son una lista de 2 números enteros
Devuelve:
La función resultante simplificada
'''
def dividirFracciones(fraccion1, fraccion2):
    numerador=(fraccion1[0] * fraccion2[1])
    denominador=(fraccion1[1] * fraccion1[1])
    fraccionDividida=[numerador, denominador]

    return simplificarFraccion(fraccionDividida)

'''
Esta función es el menú secundario de opciones que imprime las soluciones
Recibe una opción del menú principal
Devuelve: no tiene return
'''
def menuOpciones(opcion):
    #Creo las fracciones (fuera de la estructura condicional pq sino repetiría código),
    #las leo y las simplifico.
    fraccion1=leerFraccion()
    fraccion1=simplificarFraccion(fraccion1)
    fraccion2=leerFraccion()
    fraccion2=simplificarFraccion(fraccion2)
    
    #Estructura condicional usando las fracciones
    if opcion==1:
        mensaje="La suma de las dos fracciones es %s \n" %(escribirFraccion(sumarFracciones(fraccion1, fraccion2)))
    elif opcion==2:
        mensaje="La resta de las dos fracciones es %s \n" %(escribirFraccion(restarFracciones(fraccion1, fraccion2)))
    elif opcion==3:
        mensaje="La multiplicación de las dos fracciones es %s \n" %(escribirFraccion(multiplicarFracciones(fraccion1, fraccion2)))
    else:
        mensaje="La división de las dos fracciones es %s \n" %(escribirFraccion(dividirFracciones(fraccion1, fraccion2)))
    #Imprimo el mensaje
    print(mensaje)
    #Llamo a la función del menú principal, para que haga un bucle
    menuPrincipal()
    
'''
Esta función es el menú principal del programa
Recibe: no tiene parámetros de entrada
Devuelve: no tiene return
'''    
def menuPrincipal():
    #Creo la variable menú y la imprimo
    menu="Operando con fracciones:\n"\
        "1. Sumar dos fracciones.\n"\
        "2. Restar dos fracciones.\n"\
        "3. Multiplicar dos fracciones.\n"\
        "4. Dividir dos fracciones.\n"\
        "5. Salir."
    print(menu)
    #Creo la variable opcion y compruebo datos
    opcion=int(input("Introduce una opción de las anteriores: "))
    while opcion<1 or opcion>5:
        print("Datos incorrectos.")
        opcion=int(input("Introduce una opción de las anteriores: "))
    #Si la opción es 1,2,3 o 4 llamo a la función del menú secundario
    if opcion!=5:
        menuOpciones(opcion)
    #Si la opción es la 5, me muestra un mensaje
    else:
        print("Hasta la vista.")

#Llamo a la función principal, ya que no tiene return
menuPrincipal()

