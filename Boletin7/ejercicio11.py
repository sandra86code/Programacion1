'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
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


def listarElementosComunes(lista1, lista2):
    listaComunes=[]
    if lista1>lista2:
        listaMayor=lista1
        listaMenor=lista2
    else:
        listaMayor=lista2
        listaMenor=lista1
        
    for i in listaMenor:
        j=0
        itemFound=False
        while j<len(listaMayor) and itemFound==False:
            if convertirAMinusculas(listaMenor[i])==convertirAMinusculas(listaMayor[j]):
                listaComunes.append(listaMenor[i])
                itemFound==True
            
            else:
                j+=1
    
    return listaComunes

assert(listarElementosComunes([""], [])==[])