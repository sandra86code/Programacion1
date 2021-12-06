'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 18 Diciembre 2020 - Ejercicio 3
 @enunciado: 
Realizar una función que dada una fecha en formato 12 horas nos devuelva la fecha en formato 24
horas.
La función recibirá una cadena con el siguiente formato hh:mm:ssAM u hh:mm:ssPM y deberá
devolver el formato de fecho hh:mm:ss con 24 horas.
Si la fecha que recibe no tiene el formato adecuado deberá devolver una cadena vacía.

Ejemplos:
convierteFecha(“12:02:04AM”) → “”
convierteFecha(“12:02:04PM”) → “”
convierteFecha(“11:02:04AM”) → “11:02:04”
convierteFecha(“11:02:04PM”) → “23:02:04”
convierteFecha(“14:89:04AM”) → “”
convierteFecha(“12:02:04AP”) → “”
'''

#===============================================================================
# Esta función convierte una fecha (variable de tipo string) en una lista con mezcla
# de enteros y string
# Recibe: una fecha (cadena de caracteres)
# Devuelve: una lista con enteros y string
#===============================================================================
def pasaFechaALista(fecha):
    
    lista=[]
    #Creo una estructura condicional para que, si la longitud de la lista no es 10
    #(los únicos datos correctos), me devuelva una cadena vacía
    if len(fecha)==10:        
        #Creo una variable donde voy a ir agregando los números (de las horas,
        #de los minutos y de los segundos) en cada vuelta y luego agregando cada
        #uno de ellos a la lista
        var=""
        #Creo una variable para el formato, independiente de la variable porque quiero
        #usarla fuera del bucle y por la separación de los segundos y el formato sin los
        #dos puntos
        formato=""
        #Recorro la cadena
        for i in range (len(fecha)):
            #Si el caracter no son los dos puntos
            if fecha[i]!=":":
                #Si el caracter es un número (en string) entre 0 y 9, lo añado a la variable var
                if fecha[i]>=chr(48) and fecha[i]<=chr(57):
                    var+=fecha[i]
                #Sino, es que es el formato y lo añado a la variable formato
                else:
                    formato+=fecha[i]
            #Cuando el caracter sean los dos puntos, añado la variable var (convertida a entero)
            #a la lista y reinicializo la variable var a vacía
            else:
                lista.append(int(var))
                var=""
        #Como no toda la separación es por dos puntos, al salir del bucle, si la variable var
        #no está vacía, la añado a la lista
        if var!="":
            lista.append(int(var))
        #Si el formato es PM o AM lo mete en la lista
        if formato in {"PM", "AM"}:
            lista.append(formato)
        #Sino la lista se convierte en vacía, ya que el formato no será correcto
        else:
            lista=[]
            
    return lista



#===============================================================================
# Esta función valida que las horas, los minutos y los segundos almacenados dentro
# de una lista sean correctos
# Recibe 
# Devuelve:
# 
#===============================================================================
def validaFecha(lista):
    #Limito las operaciones a que la lista no esté vacía
    if len(lista)!=0:
        i=0
        bandera=True
        while i<len(lista) and bandera:
            #Si las horas son mayores de 11, cambio la bandera y freno el bucle
            if lista[0]>11:
                bandera=False
            #Si los minutos o los segundos son mayores de 59, cambio la bandera
            #y freno el bucle
            elif lista[1]>59 or lista[2]>59:
                bandera=False
            i+=1
        #Si la bandera es Falsa, es decir, los datos son erróneos, la lista se
        #convierte en una lista vacía
        if bandera==False:
            lista=[]

    return lista


#===============================================================================
# Esta función convierte una fecha (variable string) en formato de 12 horas 
# (hh:mm:ssAM o hh:mm:ssPM) en una fecha en formato string de 24 horas (hh:mm:ss).
# Recibe: una fecha (variable de tipo string) en formato de 12 horas
# Devuelve: la fecha (variable de tipo string) en formato de 24 horas
#===============================================================================
def convierteFecha(fecha):
    
    fecha24horas=""
    #Creo la lista y le asigno el valor de las otras 2 funciones
    lista=validaFecha(pasaFechaALista(fecha))
    
    #Creo una estructura condicional, ya que si la lista no tiene 4 posiciones,
    #me devuelve directamente la cadena vacía
    if len(lista)==4:
        #Si el último elemento es PM (solo puede ser AM o PM), a las horas (primer
        #elemento de la lista) les sumo 12
        if lista[-1]=="PM":
            lista[0]+=12
        #Recorro la lista hasta la penúltima posición (solo horas, minutos y segundos)    
        for i in range (len(lista)-1):
            #Si el elemento no es el penúltimo
            if lista[i]!=lista[-2]:
                #Si el número es menor de 10, me lo va a poner sin el cero delante.
                #Por eso, en ese caso, añado un 0 primero.
                if lista[i]<10:
                    fecha24horas+=("0")
                #Añado el número convertido a string y luego los dos puntos
                fecha24horas+=str(lista[i])+":"
            #Si el elemento es el penúltimo, hago lo mismo, pero no añado los dos puntos al final
            else:
                if lista[i]<10:
                    fecha24horas+=("0")
                fecha24horas+=str(lista[i])
      
    return fecha24horas
    
    

assert(convierteFecha("12:02:04AM")=="")
assert(convierteFecha("12:02:04PM")=="")
assert(convierteFecha("11:02:04AM")=="11:02:04")
assert(convierteFecha("11:02:04PM")=="23:02:04")
assert(convierteFecha("14:89:04AM")=="")
assert(convierteFecha("12:02:04AP")=="")
