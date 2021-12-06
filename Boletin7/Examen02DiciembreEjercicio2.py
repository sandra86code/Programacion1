'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 2 Diciembre 2020 - Ejercicio 2
 @enunciado: 
 Realizar una función que reciba como parámetro una cadena que contenga un dni y 
devuelva un True si el dni es válido y False en caso contrario. 
Para calcular la letra debemos tomar el número completo de hasta 8 cifras de nuestro 
DNI, lo dividimos entre 23 y nos quedamos con el resto de dicha división.

El resultado anterior es un número entre 0 y 22. A cada uno de estos posibles 
números le corresponde una letra, según la siguiente tabla:

RESTO    0    1    2    3    4    5    6    7    8    9    10    11    12    13    14    15    16    17    18    19    20    21    22
LETRA    T    R    W    A    G    M    Y    F    P    D    C     B     N     J     Z     S     Q     V     H     L     C     K     E

Si el formato no es válido deberá devolver False.

Mejora opcional: Ten en cuenta que hay dni que en vez de 8 números pueden tener 7.
'''
#===============================================================================
# Esta función valida el formato de un dni es correcto (7 o 8 números) 
# Recibe: una cadena de caracteres
# Devuelve:
# True si es válido (7 o 8 números)
# False si no es válido
#===============================================================================
def validaDni(dni):
    esValido=True
    if len(dni)==7 or len(dni)==8:
        for i in range (len(dni)):
            if dni[i]<chr(48) or dni[i]>chr(57):
                esValido=False 
    else:
        esValido=False

    return esValido

assert(validaDni("84759612")==True)
assert(validaDni("8475961")==True)
assert(validaDni("847596121")==False)
assert(validaDni("8w759612")==False)
assert(validaDni("859612z")==False)


#===============================================================================
# Esta función calcula la letra de un dni
# Recibe: una cadena de caracteres
# Devuelve:
# - Si el dni no es válido devuelve False
# - Si el dni es válido (7 u 8 números) devuelve la letra del DNI
#===============================================================================
def calcularLetraDni(dni):
    
    #Si el dni es válido
    if validaDni(dni):
        #Convierto la cadena a entero
        dni=int(dni)
        #Calculo y almaceno el resto del módulo de dni entre 23
        resto=dni%23
        #Creo la lista de letras que asocian el resto a la posición de la letra en la lista
        letras=["T","R","W","A","G","M","Y","F","P","D","C","B","N","J","Z","S","Q","V","H","L","C","K","E"]

        letraDni=letras[resto]
    #Si el dni no es válido devuelvo False
    else:
        letraDni=False
        
    return letraDni
    

assert(calcularLetraDni("15409981")=="G")
assert(calcularLetraDni("75410143")=="C")
assert(calcularLetraDni("8759612")=="Q")
assert(calcularLetraDni("847596121")==False)
assert(calcularLetraDni("8w759612")==False)
assert(calcularLetraDni("859612z")==False)


