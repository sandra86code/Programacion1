'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 11
 @enunciado: 
Escribe una función que reciba dos listas y devuelva una lista con los 
elementos comunes a ambas, sin repetir ninguno.
'''

#===============================================================================
# Esta función calcula si un caracter es minúsculas
# Recibe un caracter
# Devuelve:
# True si el caracter está en minúsculas (usando la función ord() y el número en el código ASCII)
# False si el caracter no está en minúsculas
#===============================================================================
def isMinusculas(caracter):
        
    return ord(caracter)>=97 and ord(caracter)<=122


#===============================================================================
# Esta función devuelve una cadena convertida a minúsculas (funcion cadena.lower())
# Recibe una cadena
# Devuelve: la cadena en minúsculas
#===============================================================================
def convertirAMinusculas(cadena):
    cadenaConvertida=''
    #Recorro la cadena
    for i in cadena:
        #si i es minúsculas o es un espacio, lo acumulo en la cadena convertida
        if isMinusculas(i)==True or i==' ':
            cadenaConvertida+=i
        #Si i es mayúsculas, lo convierto a minúsculas usando ord() y luego como esto es
        #un ordinal y yo necesito el string, uso chr() y lo acumulo en la cadena convertida
        else:
            cadenaConvertida+=chr(ord(i)+32)
  
    return cadenaConvertida


assert(convertirAMinusculas('La ONU es internacional')=='la onu es internacional')
assert(convertirAMinusculas('CadeNA')=='cadena')


#===============================================================================
# Esta función devuelve una lista con las palabras comunes de dos listas, sin
# repetir ningún elemento
# Recibe: dos listras de tipo string
# Devuelve: una lista de tipo string con las palabras comunes
#===============================================================================
def listarElementosComunes(lista1, lista2):
    listaComunes=[]
    #Bucle externo que recorre la lista1
    i=0
    while i<len(lista1):
        j=0
        itemFound=False
        #Bucle interno que se frena, con una bandera, en cuanto hay una coincidencia 
        #para así no repetir palabra
        while j<len(lista2) and itemFound==False:
            #Si la palabra de la lista1 es igual a la palabra de la lista2 y no está en 
            #la listaComunes, la introduzco en la misma, cambio la bandera y aumento la i.
            if convertirAMinusculas(lista1[i])==convertirAMinusculas(lista2[j]):
                if lista1[i] not in listaComunes:
                    listaComunes.append(lista1[i])
                    itemFound=True
                    i+=1
                #Si coincide pero ya está en listaComunes, aumento la j
                else:
                    j+=1
            #Si las palabras no coinciden, aumento la j
            else:
                j+=1
        #Si no ha encontrado coincidencia en la palabra al recorrer la lista2, aumento la i
        i+=1

    return listaComunes

assert(listarElementosComunes(["perro", "sala", "perro", "zapato", "bidon", "almohada"], ["evidencia", "perro", "ruido", "rima", "almohada", "cenutrio"])==["perro", "almohada"])
assert(listarElementosComunes(["perro", "sala", "perro", "zapato", "bidon", "almohada"], ["evidencia", "ruido", "rima", "raudo", "cenutrio"])==[])