'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 10, 2021
 @nombre: Examen 10 Diciembre - Ejercicio 3
 @enunciado: 
 Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las palabras de
más de cinco letras a sólo cinco letras (e indicando que una palabra fue cortada con el
agregado de una arroba). Además también elimina todos los espacios en blanco de más.

Por ejemplo, al texto » Llego mañana alrededor del mediodía » se transcribe como «Llego
mañan@ alred@ del medio@».

Por otro lado cobra un valor para las palabras cortas y otro valor para las palabras largas
(que deben ser cortadas).
Escribir una función que reciba un texto, la longitud máxima de las palabras (en el caso
anterior eran 5 letras) y devuelva como resultado el texto del telegrama.

Extra:
Escribir una segunda función que devuelva el costo del texto. Esta función deberá recibir
como argumento el costo de cada palabra corta, el costo de cada palabra larga y el texto del
telegrama, es decir, el texto ya cifrado.
'''

#===============================================================================
# Esta función calcula el costo de enviar el texto en función de lo que cuesta cada
# palabra corta (las no modificadas), cada palabra larga (las cortadas) y el texto
# en formato de lista (para un mejor acceso a cada elemento).
# Recibe: el costo de la palabra corta (float), costo de la palabra larga (float) y
# una lista de palabras
# Devuelve: el costo total del mensaje redondeado a 2 caracteres
# 
#===============================================================================
def calcularCostoTexto(costoPalabraCorta, costoPalabraLarga,lista):
    
    coincidencia=0
    #recorro la lista
    for i in range (len(lista)):
        #Recorro cada elemento de la lista
        for j in range (len(lista[i])):
            #Si el caracter del item contiene una @ es que ha sido cortada, así que
            #añado 1 en la coincidencia
            if lista[i][j]=="@":
                coincidencia+=1
    
    costoTotalLargas=coincidencia*costoPalabraLarga
    costoTotalCortas=(len(lista)-coincidencia)*costoPalabraCorta
    
    
    return round((costoTotalLargas+costoTotalCortas),2)



#===============================================================================
# Esta función pasar una lista de string a cadena de caracteres. Cada item está separado
# del siguiente con un espacio, salvo antes del primer item y después del último item.
# Recibe: una lista de palabras (lista de string)
# Devuelve: una cadena de caracteres (string) con los items separados por espacios.
#===============================================================================
def pasarDeArrayACadena(lista):
    
    cadena=""
    
    for i in range (len(lista)-1):
        cadena+=lista[i]+" "
    
    cadena+=lista[-1]
       
    return cadena


assert(pasarDeArrayACadena(["Lleg@", "maña@", "alre@", "del", "medi@"])=="Lleg@ maña@ alre@ del medi@")


#===============================================================================
# Esta función recibe una lista de palabras y devuelve la lista con las palabras
# cortadas y una @ a partir del corte, según la longitud que recibe por parámetro.
# Recibe: una lista de palabras (lista de string) y una longitud (entero positivo)
# Devuelve: la lista con las cortadas a partir de la longitud, siempre que la longitud
#sea menor que el len de la palabra.
#===============================================================================
def cortaPalabras(lista,longitud):
    
    for i in range(len(lista)):
        #Si la longitud de la palabra es mayor que la longitud, creo la variable palabra,
        #itero sobre la palabra y añado el número de caracteres de la longitud y luego una
        #arroba y asigno a la lista[i] la variable palabra
        if len(lista[i])>longitud:
            palabra=""
            for j in range (longitud):
                palabra+=lista[i][j]
            palabra+="@"
            lista[i]=palabra
                
    return lista

assert(cortaPalabras(["Llego", "mañana", "alrededor", "del", "mediodía"],5)==["Llego", "mañan@", "alred@", "del", "medio@"])
assert(cortaPalabras(["Llego", "mañana", "alrededor", "del", "mediodía"],4)==["Lleg@", "maña@", "alre@", "del", "medi@"])


#===============================================================================
# Esta función pasa una cadena de caracteres (frase con palabras que estar separadas
# por espacios) a una lista de palabras. Tiene en cuenta los dobles espacios y los
# espacios al final y al principio de la frase, es decir, los corta y deja la lista
# sin espacios.
# Recibe: una cadena de caracteres
# Devuelve: la lista de palabras
# 
#===============================================================================
def pasarDeCadenaAArray(cadena):
    lista=[]
    palabra=""
    for i in range (len(cadena)):
        if cadena[i]!=" ":
            palabra+=cadena[i]
        elif cadena[i]==" " and palabra!="":
            lista.append(palabra)
            palabra=""
    #Por si no hay espacios al final y no ha añadido la última palabra en el bucle.
    if palabra!="":
        lista.append(palabra)
 
        
    return lista


assert(pasarDeCadenaAArray(" Llego mañana alrededor del mediodía ")==["Llego", "mañana", "alrededor", "del", "mediodía"])
assert(pasarDeCadenaAArray(" Llego   mañana alrededor  del mediodía  ")==["Llego", "mañana", "alrededor", "del", "mediodía"])
assert(pasarDeCadenaAArray(" Llego mañana alrededor del mediodía")==["Llego", "mañana", "alrededor", "del", "mediodía"])


def main():
    
    #Pido datos
    texto=input("Introduce el texto que quieras enviar: ")
    longitud=int(input("Introduce la longitud máxima de las palabras a partir del cual se cortarán: "))
    #Valido longitud
    while longitud<=0:
        print("Datos erróneos. Debe ser un número mayor que 0.")
        longitud=int(input("Introduce la longitud máxima de las palabras a partir del cual se cortarán: "))
    
    textoConvertido=pasarDeCadenaAArray(texto)
    #Muestro texto resultante
    print("\nEl texto resultante es:\n%s" % pasarDeArrayACadena(cortaPalabras(textoConvertido, longitud)))
    
    #Creo constantes para los precios, así se pueden cambiar fácilmente
    COSTO_PALABRA_CORTA=0.20
    COSTO_PALABRA_LARGA=0.30
    
    #Muestro coste total
    print("El coste total de su mensaje es de: %s €" % calcularCostoTexto(COSTO_PALABRA_CORTA, COSTO_PALABRA_LARGA, textoConvertido))
    
    
main()




    
    