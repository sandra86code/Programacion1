'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: 
 Escribir dos funciones que permitan calcular:
◦ La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
◦ La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa con un menú donde se pueda elegir la opción de convertir a segundos,
convertir a horas,minutos y segundos o salir del programa.
'''

'''
Esta función calcula la cantidad de segundos dada una hora en horas, minutos y segundos
Recibe 3 variables enteras, hora, minuto y segundo
Devuelve:
Cantidad total de segundos
'''
def convertirASegundos(hora, minuto, segundo):
        
    return (hora*360)+(minuto*60)+segundo

'''
Esta función pasa una cantidad de segundos a horas, minutos y segundos 
Recibe una variable de tipo entero, los segundos totales
Devuelve:
Un mensaje con la cantidad de horas, minutos y segundos
'''
def convertirAHMinSeg(segundosTotales):
    
    horas=segundosTotales//360
    minutos=(segundosTotales-(horas*360))//60
    segundos=(segundosTotales-(horas*360)-(minutos*60))
    mensaje="%s hora(s), %s minuto(s) y %s segundo(s)."%(horas,minutos,segundos)
    
    return mensaje


'''
Esta función es el menú secundario del programa, en el que pedimos los datos e imprimos el resultado
Recibe una variable de tipo entero que es la opcion introducida en el menú principal
Devuelve: No devuelve nada
'''
def menuOpciones(opcion):
    #Estructura condicional para opciones 1 y 2
    if opcion==1:
        #Petición de datos y comprobación de si son correctos. Sino vuelven a pedirse.
        segundos=int(input("Introduce la cantidad de segundos a convertir: "))
        while segundos<0:
            print("Datos incorrectos. Vuelve a intentarlo.")
            segundos=int(input("Introduce la cantidad de segundos a convertir: "))
        #Imprimo el resultado llamado a la función que lo calcula con el parámetro introducido
        #por el usuario
        print("%s segundos corresponden a %s \n" % (segundos, convertirAHMinSeg(segundos)))
    elif opcion==2:
        #Petición de datos y comprobación de si son correctos. Sino vuelven a pedirse.
        hora=int(input("Introduce la hora: "))
        while hora<0 or hora>23:
            print("Datos incorrectos. Vuelve a intentarlo.")
            hora=int(input("Introduce la hora: "))
        minuto=int(input("Introduce los minutos: "))
        while minuto<0 or minuto>59:
            print("Datos incorrectos. Vuelve a intentarlo.")
            minuto=int(input("Introduce los minutos: "))
        segundo=int(input("Introduce los segundos: "))
        while segundo<0 or segundo>59:
            print("Datos incorrectos. Vuelve a intentarlo.")
            minuto=int(input("Introduce los segundos: "))
        #Imprimo el resultado llamado a la función que lo calcula con los parámetros introducidos
        #por el usuario
        print("%s horas, %s minutos y %s segundos equivalen a %s segundos \n" % (hora, minuto, segundo, convertirASegundos(hora, minuto, segundo)))
    #Llamo a la función para que vuelva a imprimir el menú y a pedir la opción
    menuPrincipal()

'''
Esta función es el menú principal del programa 
Recibe: no tiene parámetros
Devuelve: No devuelve nada
'''
def menuPrincipal():
    #Creo una variable de tipo cadena con el texto de las opciones
    menu="1. Convertir a segundos.\n"\
        "2. Convertir a horas, minutos y segundos.\n"\
        "3. Salir."
    #Imprimo la variable
    print(menu)
    #Creo una variable de tipo entero para guardar la opcion introducida por el usuario
    opcion=int(input("Introduce la opción: "))
    #Comprobación de datos y, si son incorrectos, se piden de nuevo
    while opcion not in {1,2,3}:
        print("Datos incorrectos. Vuelve a intentarlo.")
        opcion=int(input("Introduce la opción: "))
    
    #Si la opción es 1 o 2, llamo a la función del menú de opciones 
    #(como parámetro la variable opcion introducida por el usuario)
    if opcion!=3:
        menuOpciones(opcion)
    #Si la opcion es la 3, imprimo un mensaje de despedida
    else: 
        print("Hasta la próxima.")

#Llamada a la función, ya que no tiene return
menuPrincipal()