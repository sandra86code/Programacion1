'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Ejercicios del año pasado - Ejercicio 1
 @enunciado: 
 Encriptar un mensaje usando el método de “la cifra del cesar”, que consiste en desplazar cada letra,
considerando la posición de cada una en el alfabeto, una determinada cantidad de lugares. Por
ejemplo: si el desplazamiento es de 2 lugares, la palabra “HOLA” se transforma en “JQNC”.
Si el alfabeto termina antes de poder desplazar la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra ‘a’.
Nota: considerar el alfabeto en castellano de 27 letras.
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
        #Si es "Ñ", lo convierto en "ñ"
        elif ord(i)==209:
            cadenaConvertida+=chr(241)
        #Si i es mayúsculas, lo convierto a minúsculas usando ord() y luego como esto es
        #un ordinal y yo necesito el string, uso chr() y lo acumulo en la cadena convertida
        else:
            cadenaConvertida+=chr(ord(i)+32)
  
    return cadenaConvertida


assert(convertirAMinusculas('La ONU es internacional')=='la onu es internacional')
assert(convertirAMinusculas('CadeNA')=='cadena')
assert(convertirAMinusculas('Eres la caÑa')=='eres la caña')


#===============================================================================
# Esta función devuelve una cadena convertida a mayúsculas (funcion cadena.upper())
# Recibe una cadena
# Devuelve: la cadena en mayúsculas
#===============================================================================
def convertirAMayusculas(cadena):
    cadenaConvertida=''
    for i in cadena:
        #Si i es minúsculas, lo convierto a mayúsculas usando ord() y luego como esto es
        #un ordinal y yo necesito el string, uso chr() y lo acumulo en la cadena convertida
        if ord(i)>=97 and ord(i)<=122:
            cadenaConvertida+=chr(ord(i)-32)
        #Si es 'ñ' lo convierto en 'Ñ'
        elif ord(i)==241:
            cadenaConvertida+=chr(209)
        #En el resto de casos, lo concateno
        else:
            cadenaConvertida+=i
        
    return cadenaConvertida

assert(convertirAMayusculas('La ONU es internacional')=='LA ONU ES INTERNACIONAL')
assert(convertirAMayusculas('CadeNA')=='CADENA')
assert(convertirAMayusculas('Niño')=='NIÑO')


def creaAlfabeto():
    alfabeto=[]
    for i in range(27):
        if i<14:
            alfabeto.append(chr(97+i))
        elif i>14:
            alfabeto.append(chr(97+i-1))
        else:
            alfabeto.append(chr(241))

    return alfabeto


def desplazaCaracteresDeString(cadena, desplazamiento):
    alfabeto=creaAlfabeto()
    cadenaDesplazada=""
    for i in range (len(cadena)):
        for j in range (len(alfabeto)):
            if cadena[i]==alfabeto[j]:
                if desplazamiento>0:
                    toTheEnd=len(alfabeto)-1-j
                else:
                    toTheEnd=j
                while desplazamiento>toTheEnd:
                    desplazamiento-=len()
                    
                cadenaDesplazada+=alfabeto[j+desplazamiento]
                
            elif convertirAMinusculas(cadena[i])==alfabeto[j]:
                cadenaDesplazada+=convertirAMayusculas(alfabeto[j+desplazamiento])
    # print(cadenaDesplazada)
    
    return cadenaDesplazada       
            


assert(desplazaCaracteresDeString("HOLA", 2)=="JQNC")
assert(desplazaCaracteresDeString("hola", 2)=="jqnc")


    
