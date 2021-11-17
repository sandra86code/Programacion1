'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 1
 @enunciado: 
 Design a function called charactersInString that has a character string and a character as
input parameters and returns how many times that character appears in the string. 
It should do if the string and character are lower case or upper case characters.
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
# Esta función calcula el número de coincidencias de un caracter en una cadena
# Recibe una cadena y un caracter
# Devuelve:
# El número de coincidencias de un caracter en una cadena
#===============================================================================
def charactersInString(cadena, caracter):
    resultado=0
    #Estructura condicional en que si el resultado de la llamada a la otra función es True 
    #(caracter es minúsculas, se le quitan -32 para que coincide con el mismo caracter en
    #mayúsculas
    if isMinusculas(caracter):
        suma = -32          
    #De lo contrario (el caracter no es minúsculas, se le suman 32.
    else:
        suma = 32
    
    #Recorro cadena y compruebo que el codigo ASCII de cada letra de la cadena es igual a
    #código ASCII del caracter o que es igual a la suma (-32 o 32).
    for i in cadena:
        if ord(i)==ord(caracter) or ord(i)==ord(caracter)+suma:
            resultado+=1
            
    return resultado

assert(charactersInString('Stranger Things', 'u')==0)
assert(charactersInString('Stranger Things', 'a')==1)
assert(charactersInString('Stranger Things', 's')==2)
assert(charactersInString('Stranger Things', 'H')==1)


'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 2
 @enunciado: 
 Diseña una función que reciba una cadena y la devuelva en minúsculas y otra función 
 que la devuelva en mayúsculas:
'''


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
        else:
            cadenaConvertida+=i
        
  
    return cadenaConvertida

assert(convertirAMayusculas('La ONU es internacional')=='LA ONU ES INTERNACIONAL')
assert(convertirAMayusculas('CadeNA')=='CADENA')


'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 2
 @enunciado: 
 Design a function called lowCaseInString that has a string of characters as parameter, the
method should return how many of those characters are lowcase letters.
#CÓDIGO ASCII: a-z es [97-122], 
ñ = 241
estos números se sacan con ord('A')
'''


#===============================================================================
# Esta función calcula cuántas letras en minúscula hay en una cadena (no controla tildes ni ñ)
# Recibe una cadena (variable string)
# Devuelve: el número de letras en minúscula de la cadena (sin contar letras con tildes o ñ)
#===============================================================================
def lowCaseInString(cadena):
    resultado=0
    for i in cadena:
        if isMinusculas(i) or i==chr(241):
            resultado+=1
    return resultado

assert(lowCaseInString("clase de programacion")==19)
assert(lowCaseInString("Hola")==3)
assert(lowCaseInString("ONU")==0)
assert(lowCaseInString("Guiso de ñame")==10)




'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 3
 @enunciado: 
 Design a function called upperCaseInString that has a string of characters as parameter, the
method should return how many of those characters are upper case letters.
#CÓDIGO ASCII: A-Z es [65 a 90]
Ñ= 209
estos números se sacan con ord('A')
'''


#===============================================================================
# Esta función calcula cuántas letras en mayúscula hay en una cadena (no controla tildes ni ñ)
# Recibe una cadena (variable string)
# Devuelve: el número de letras en mayúscula de la cadena (sin contar letras con tildes o ñ)
#===============================================================================
def upperCaseInString(cadena):
    resultado=0
    for i in cadena:
        #No me vale usar la funcion isMinusculas() pq no controla que para el False sean solo
        #los caracteres correspondientes a las mayúsculas
        if (i>=chr(65) and i<=chr(90)) or i==chr(209):
            resultado+=1
    return resultado


assert(upperCaseInString("clase de programacion")==0)
assert(upperCaseInString("Hola")==1)
assert(upperCaseInString("ONU")==3)
assert(upperCaseInString("Sandra Ñantes")==2)


'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 4
 @enunciado: 
 Design a function called numberInString that has a string of characters as parameter, the
method should return how many of those characters are numbers.
#CÓDIGO ASCII: 0-9 es [48-57]
'''


#===============================================================================
# Esta función calcula cuántos caracteres numéricos hay en una cadena
# Recibe una cadena
# Devuelve:
# El número de caracteres numéricos que hay en una cadena
#===============================================================================
def numberInString(cadena):
    resultado=0 
    for i in cadena:
        if i>=chr(48) and i<=chr(57):
            resultado+=1
            
    return resultado

assert(numberInString('Los 40 principales')==2)
assert(numberInString('kdi2335kik213')==7)
assert(numberInString('clase de programacion')==0)

'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 5
 @enunciado: 
 Design a function called palindrome that has a string of characters as parameter, and return
true if it is a palindrome or false in other case. 
A word is a palindrome, if it is reads the same from left to right as from right to left, 
ignoring whites,. For example: "anilina" or "el abad le dio arroz al zorro".
To simplify the problem, you can assume that simple characters are used, that is, without 
tildes or diresis.
'''


#===============================================================================
# Esta función comprueba si una palabra o frase es palíndroma (se lee igual al derecho que al revés)
# Recibe una cadena de texto que puede ser una palabra o una frase
# Devuelve:
# True si la palabra o frase es palíndroma (no tiene en cuenta espacios)
# False si la palabra o frase no es palíndroma
#===============================================================================
def palindrome(cadena):
    #Creo una variable para almacenar la cadena sin espacios
    cadenaSinEspacios=''
    #Recorro la cadena y si el caracter no es un espacio, lo acumulo en la
    #variable nueva
    for i in cadena:
        if i!=' ':
            cadenaSinEspacios+=i
    #Creo otra variable en la que voy acumular la cadena al reveś
    cadenaReves=''
    #Recorro la cadena sin espacios, pero como necesito que el marcador empiece
    #en -1,-2,etc. por eso pongo el límite inferior en 1.
    for i in range (1, len(cadenaSinEspacios)+1):
        cadenaReves+=cadenaSinEspacios[-i]
    
    return cadenaSinEspacios==cadenaReves


assert(palindrome('Ave')==False)
assert(palindrome('lavan esa base naval')==True)
assert(palindrome('el abad le dio arroz al zorro')==False)



'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 6
 @enunciado: 
 Realizar una función que busque una palabra escondida dentro de un texto. 
 Por ejemplo, si la cadena es "shybaoxlna" y la palabra que queremos buscar 
 es "hola", entonces si se encontrará y deberá devolver True, en caso 
 contrario deberá devolver False.
'''

#===============================================================================
# Esta función elimina un caracter contenido en una cadena. Si hay coincidencias, 
# solo quita el primer caracter, no los sucesivos.
# Recibe dos variables de tipo String, una cadena de texto y un caracter
# Devuelve: la cadena sin el caracter (primera coincidencia)
#===============================================================================
def quitarCaracter(cadena, caracter):
    resultado=''
    encontrado=False
    cadena=convertirAMinusculas(cadena)
    caracter=convertirAMinusculas(caracter)
    for i in cadena:
        if i==caracter and encontrado==False:
            encontrado=True
        else:
            resultado+=i
    return resultado
    
    
assert(quitarCaracter("ohalla","h")=="oalla")
assert(quitarCaracter("ohalla","a")=="ohlla")
assert(quitarCaracter("ohalla","A")=="ohlla")
assert(quitarCaracter("ohalla","l")=="ohala")
assert(quitarCaracter("Ohalla","o")=="halla")



#===============================================================================
# Esta función busca si hay una palabra contenida en un texto (usando la función quitarCaracter().
# Recibe dos variables tipo cadena, un texto y una palabra
# Devuelve:
# True si la palabra está contenida en el texto
# False si la palabra no está contenida en el texto
#===============================================================================
def encontrar(cadena,escondida):
    #Recorrer cada una de las letras de escondida
    isFound = True
    for i in escondida:
        #Para cada una de las letras de escondidas intento quitarla de cadena
        #Si la puedo quitar es que está, por lo que paso a la siguiente
        #Si no la puedo quitar, no está con lo cual me salgo y devuelve False
        
        #Función que me devuelve la cadena que recibe como argumento
        #sin la primera ocurrencia que se encuentre de i
        cadenaAux = quitarCaracter(cadena, i)
        if cadenaAux == cadena:
            isFound = False
        cadena = cadenaAux
    return isFound

assert(encontrar("shybaoxlna", "hola")==True)
assert(encontrar("shybaoxlna", "z")==False)
assert(encontrar("shybaoxlna", "Z")==False)
assert(encontrar("sybaoxln", "holaa")==False)
assert(encontrar("sybaoxlna", "hola")==False)
assert(encontrar("mkeigunydo", "mundo")==True)
assert(encontrar("odmnu", "mundo")==True)
assert(encontrar("shyb aoxlna", "hola")==True)
assert(encontrar("", "hola")==False)
assert(encontrar("odmnu", "")==True)


'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 7
 @enunciado: 
 Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
tercera.
'''
#===============================================================================
# Esta función convierte una cadena de texto a un array, separando por palabras
# Recibe una variable tipo string, que es una cadena de caracteres
# Devuelve: un array de tipo string con las palabras separadas 
# (sin contar puntos, espacios, comas, signos de admiración y de exclamacion)
#===============================================================================
def textoAArray(texto):
    arrayTexto=[]
    palabra=""
    for i in range (len(texto)):
        if texto[i]==" ":
            if palabra!="":
                arrayTexto.append(palabra)
            palabra=""
        elif (texto[i]>=chr(48) and texto[i]<=chr(57)) or (texto[i]>=chr(65) and texto[i]<=chr(90)) or (texto[i]>=chr(97) and texto[i]<=chr(122)):
            palabra+=texto[i]
    if palabra!="":
        arrayTexto.append(palabra)

    return arrayTexto

assert(textoAArray("Hola me llamo Sandra")==["Hola", "me", "llamo", "Sandra"])       
assert(textoAArray("  Hola   me    llamo   Sandra  ")==["Hola", "me", "llamo", "Sandra"])       


#===============================================================================
# Esta función busca una palabra en el texto y, si la encuentra, la reemplaza por otra palabra
# Recibe 3 variables de tipo string, un texto, una palabra y otra palabra
# Devuelve:
# El texto con la palabra reemplazada si encuentra la palabra buscada
# El mismo texto que se ha introducido si no encuentra la palabra buscada
#===============================================================================
def buscaReemplaza(texto, buscada, reemplazada):
    textoReemplazado=""
    texto=textoAArray(texto)
    for i in texto:
        if convertirAMinusculas(i)==convertirAMinusculas(buscada):
            textoReemplazado+=reemplazada
        else:
            textoReemplazado+=i
        if i!=texto[-1]:
            textoReemplazado+=" "
            
    return textoReemplazado
        
assert(buscaReemplaza("Hola me llamo Sandra", "hola", "Adios")=="Adios me llamo Sandra")
assert(buscaReemplaza("Hola me llamo Sandra", "SANDRA", "Sofia Maria")=="Hola me llamo Sofia Maria")
assert(buscaReemplaza("Hola me llamo Sandra", "Mercedes", "Sofia")=="Hola me llamo Sandra")
# assert(buscaReemplaza("El perro marron tiene hambre", "perro marron", "gato angora de mi prima")=="El gato angora de mi prima tiene hambre")

def searchReplace(texto, buscada, reemplazada):
    if buscada in texto:
        textoReemplazado=""
        texto=textoAArray(texto)
        buscada=textoAArray(buscada)
        
        j=0
        isFound=False
        while j<len(texto) and isFound==False:
            if buscada[0]==texto[j]:
                isFound=True
                posInicial=j
                posFinal=len(buscada)+posInicial
            else:
                j+=1
        if isFound:
            del texto[posInicial:posFinal]
            texto.insert(posInicial, reemplazada)
            for i in texto:
                textoReemplazado+=i
                if i!=texto[-1]:
                    textoReemplazado+=" "
    else:
        textoReemplazado=texto
        
    return textoReemplazado

assert(searchReplace("El perro marron tiene hambre", "perro marron", "gato angora de mi prima")=="El gato angora de mi prima tiene hambre")    

'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 8
 @enunciado: 
 Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena "Abaco", devolverá 2.
'''
#===============================================================================
# Esta función nos dice la cantidad de vocales diferentes que tiene una palabra o frase
# Recibe una variable string, que es una palabra o una frase
# Devuelve: 
# La cantidad de vocales diferentes en la palabra o frase
#===============================================================================
def contarVocalesDiferentes(cadena):
    cantidadVocales=0
    vocales=["a","e","i","o","u"]
    cadena=convertirAMinusculas(cadena)
    for i in range (len(vocales)):
        if vocales[i] in cadena:
            cantidadVocales+=1
    return cantidadVocales

assert(contarVocalesDiferentes("Abaco")==2)
assert(contarVocalesDiferentes("sd kg")==0)
assert(contarVocalesDiferentes("mUrcIelaGO")==5)



'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 9
 @enunciado: 
 Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución será
"crsdprgrmcnuoeoaaio".
'''
#===============================================================================
# Esta función reordena una cadena, colocando delante las consonantes y luego las vocales
# Recibe una variable de tipo cadena, que puede ser una palabra o una frase
# Devuelve:
# La cadena reordenada
#===============================================================================
def reordenarCadena(cadena):
    cadenaReordenada=""
    vocales=["a","e","i","o","u"]
    for i in cadena:
        if convertirAMinusculas(i) not in vocales and i!=' ':
            cadenaReordenada+=i
    for i in cadena:
        if convertirAMinusculas(i) in vocales:
            cadenaReordenada+=i

    return cadenaReordenada


assert(reordenarCadena("curso de programacion")=="crsdprgrmcnuoeoaaio")
assert(reordenarCadena("Nothing Else Matters")=="NthnglsMttrsoiEeae")

'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 5 (String) - Ejercicio 10
 @enunciado: 
 Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es "He estudiado mucho", debe devolver 3.
'''
#===============================================================================
# Esta función cuenta el número de palabras que hay en una cadena
# Recibe una variable de tipo String, una cadena de texto
# Devuelve:
# El número de palabras en una cadena
#===============================================================================
def contarPalabras(cadena):
    numPalabras=0
    cadena=textoAArray(cadena)
    for i in cadena:
        numPalabras+=1
    return numPalabras

assert(contarPalabras("He estudiado mucho")==3)
assert(contarPalabras("  He    estudiado   mucho   ")==3)
