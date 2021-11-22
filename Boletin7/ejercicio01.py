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

from ejercicio11 import convertirAMinusculas

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
        #En el resto de casos, lo concateno
        #Si es 'ñ' lo convierto en 'Ñ'
        elif ord(i)==241:
            cadenaConvertida+=chr(ord(209))
        #En el resto de casos, lo concateno
        else:
            cadenaConvertida+=i
        
  
    return cadenaConvertida

assert(convertirAMayusculas('La ONU es internacional')=='LA ONU ES INTERNACIONAL')
assert(convertirAMayusculas('CadeNA')=='CADENA')



def desplazarCaracter(caracter, desplazamiento):
    
    if caracter!="ñ":
        ordinalCaracterDesplazado=ord(caracter)+desplazamiento
    else:
        ordinalCaracterDesplazado=111+desplazamiento
    
    if ordinalCaracterDesplazado<97:
        ordinalCaracterDesplazado+=27
    elif ordinalCaracterDesplazado>122:
        ordinalCaracterDesplazado-=26
    
    if ordinalCaracterDesplazado>=97 and ordinalCaracterDesplazado<=110:
        caracterDesplazado=chr(ordinalCaracterDesplazado)
    elif ordinalCaracterDesplazado==111:
        caracterDesplazado="ñ"
    elif ordinalCaracterDesplazado<=122:
        caracterDesplazado=chr(ordinalCaracterDesplazado)

    print(caracterDesplazado)
    return caracterDesplazado

assert(desplazarCaracter("a", 3)=="d")
assert(desplazarCaracter("l", 2)=="n")
assert(desplazarCaracter("l", 4)=="o")
assert(desplazarCaracter("z", 4)=="d")
assert(desplazarCaracter("z", 20)=="s")
assert(desplazarCaracter("l", 3)=="ñ")
assert(desplazarCaracter("f", 9)=="ñ")
assert(desplazarCaracter("a", -5)=="v")
assert(desplazarCaracter("ñ", 3)=="q")
assert(desplazarCaracter("ñ", -4)=="k")
assert(desplazarCaracter("ñ", 12)=="a")
assert(desplazarCaracter("a", -15)=="m")
assert(desplazarCaracter("o", 2)=="q")




def desplazaCaracteresDeString(cadena, desplazamiento):
    cadenaDesplazada=""
    for i in cadena:
        cadenaDesplazada+=desplazarCaracter(convertirAMinusculas(i), desplazamiento)
    cadenaDesplazada=convertirAMayusculas(cadenaDesplazada)
    print(cadenaDesplazada)
    return cadenaDesplazada


assert(desplazaCaracteresDeString("HOLA", 2)=="JQNC")
assert(desplazaCaracteresDeString("hola", 2)=="jqnc")

    
    
