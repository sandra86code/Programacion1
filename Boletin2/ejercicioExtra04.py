'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 2 - Ejercicio Extra 4 
 @enunciado: 
 Diseñar un programa que muestre un menú con las siguientes opciones:
    1. Cambio de euros a dólares
    2. Cambio de dólares a euros
    3. Cambio de euros a libras
    4. Cambio de libras a euros.
    5. Cambio de libras a dólares
    6. Cambio de dólares a libras
    7. Salir
El programa debe pedir una opción, luego una cantidad según corresponda y mostrar la
conversión correspondientes. El programa terminará cuando pulse un 7.
'''

#Creo el menú y lo guardo en una variable
menu="Menú de opciones:\n"\
    "1. Cambio de euros a dólares.\n"\
    "2. Cambio de dólares a euros.\n"\
    "3. Cambio de euros a libras.\n"\
    "4. Cambio de libras a euros.\n"\
    "5. Cambio de libras a dólares.\n"\
    "6. Cambio de dólares a libras.\n"\
    "7. Salir."

#Imprimo el menú
print(menu)

#Pido los datos de la opcion
opcion=int(input("Elige una opción: "))
#Si no forman parte del menú, vuelvo a pedirlos
while opcion<1 or opcion>7:
    print("Datos erróneos. Inténtalo de nuevo.")
    opcion=int(input("Elige una opción: "))

#Establezco 3 constantes de la tasa de cambio entre monedas
EURO_DOLAR=1.1618
EURO_LIBRA=0.8419
LIBRA_DOLAR=1.3801

#
while opcion!=7:
    #Pido la cantidad a convertir, que puede ser un número con decimales
    cantidad=float(input("Introduce la cantidad a convertir: "))
    #Si los datos no son correctos, los vuelvo a pedir
    while cantidad<=0:
        print("Datos erróneos. Inténtalo de nuevo.")
        cantidad=float(input("Introduce la cantidad a convertir: "))   
    #Estructura lógica para cada opción [1,6]
    #Dentro de cada una creo una variable mensaje donde muestro la cantidad dada
    #con el símbolo de moneda correspondiente y la cantidad convertida redondeada
    #a 2 decimales con el símbolo de moneda correspondiente
    if opcion==1:
        mensaje="%s € son %s $." % (cantidad, round(cantidad*EURO_DOLAR, 2))
    elif opcion==2:
        mensaje="%s $ son %s €." % (cantidad, round(cantidad/EURO_DOLAR, 2))
    elif opcion==3:
        mensaje="%s € son %s £." % (cantidad, round(cantidad*EURO_LIBRA, 2))
    elif opcion==4:
        mensaje="%s £ son %s €." % (cantidad, round(cantidad/EURO_LIBRA, 2))
    elif opcion==5:
        mensaje="%s £ son %s $." % (cantidad, round(cantidad*LIBRA_DOLAR, 2))
    else:
        mensaje="%s $ son %s £." % (cantidad, round(cantidad/LIBRA_DOLAR, 2))
    #Imprimo el mensaje
    print(mensaje)
    #Vuelvo a pedir una opción. Si es incorrecta, pido los datos.
    #Si es 7 sale del bucle, si es [1,6] hay otra iteración en el bucle 
    opcion=int(input("Elige una opción: "))
    while opcion<1 or opcion>7:
        print("Datos erróneos. Inténtalo de nuevo.")
        opcion=int(input("Elige una opción: "))

#Cuando la opcion marcada es 7, imprimo este mensaje por consola        
print("Gracias por utilizar nuestro servicio.")
    