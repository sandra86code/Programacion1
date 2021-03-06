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


#===============================================================================
# Esta función crea una lista con las letras del alfabeto
# Recibe: no tiene parámetros de entrada
# Devuelve: una lista con las letras del alfabeto ordenadas alfabéticamente, valga la redundancia
#===============================================================================
def creaAlfabeto():
    alfabeto=[]
    for i in range(27):
        #Si la posición es anterior a la 14 (lugar de la ñ), me aumenta el código ASCII desde la a
        if i<14:
            alfabeto.append(chr(97+i))
        #Si la posición es posterior a la 14 (lugar de la ñ), sigue desde o a z
        elif i>14:
            alfabeto.append(chr(97+i-1))
        #Si la posición es la 14, introduce la "ñ"
        else:
            alfabeto.append(chr(241))

    return alfabeto


#===============================================================================
# Esta función desplaza cada caracter de una cadena de caracteres una serie de 
# posiciones en orden alfabético. Si llega al final, vuelve a empezar por la a.
# El desplazamiento puede ser hacia la izquierda (negativo) o hacia la derecha
# (positivo)
# Recibe: una cadena de caracteres y un entero que indica el desplazamiento 
# (negativo hacia la izquierda, positivo hacia la derecha)
# Devuelve: la cadena desplazada
# 
#===============================================================================
def desplazaCaracteresDeString(cadena, desplazamiento):
    #Creo el alfabeto y lo guardo en una variable
    alfabeto=creaAlfabeto()
    #Creo la variable acumuladora para almacenar las letras
    cadenaDesplazada=""
    #Si el desplazamiento es positivo, me desplazamiento final
    #será el resto de la división entera del desplazamiento entre
    #el tamaño del alfabeto (27)
    if desplazamiento>0:
        desplazamiento=desplazamiento%len(alfabeto)
    #Como Python hace el resto de números negativos de una forma peculiar,
    #si el desplazamiento es negativo, el desplazamiento es el valor absoluto
    #del desplazamiento entre el tamaño del alfabeto (27) y luego el resultado
    #de esa operación lo cambio de signo
    else:
        desplazamiento=abs(desplazamiento)%len(alfabeto)
        desplazamiento*=-1
    #Recorro la cadena
    for i in range (len(cadena)):
        #Recorro el alfabeto
        for j in range (len(alfabeto)):
            #Si el caracter de la cadena coincide con el caracter del alfabeto,
            #añado a la cadenaDesplazada la posición del caracter del alfabeto que
            #sean la posición de la coincidencia más el desplazamiento
            if cadena[i]==alfabeto[j]:
                cadenaDesplazada+=alfabeto[j+desplazamiento]
            #Si no hay esa coincidencia, compruebo que no sea porque el caracter
            #de la cadena esté en mayúsculas, así que lo convierto en minúsculas,
            #hago la comparación y luego añado el caracter correspondiente desplazado
            #pero convertido a minúsculas (ya que mi alfabeto está en minúsculas)
            elif convertirAMinusculas(cadena[i])==alfabeto[j]:
                cadenaDesplazada+=convertirAMayusculas(alfabeto[j+desplazamiento])
    
    return cadenaDesplazada       
            


assert(desplazaCaracteresDeString("HOLA", 2)=="JQNC")
assert(desplazaCaracteresDeString("hola", 2)=="jqnc")
assert(desplazaCaracteresDeString("HOLA", 27)=="HOLA")
assert(desplazaCaracteresDeString("hola", 28)=="ipmb")
assert(desplazaCaracteresDeString("HOLA", -5)=="CKGV")
assert(desplazaCaracteresDeString("hola", -28)=="gñkz")


    
