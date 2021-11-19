'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Ejercicios del año pasado - Ejercicio 10
 @enunciado: 
Escribe una función para pasar un número de binario a decimal y de decimal a binario.
'''

#===============================================================================
# Esta función convierte un número binario en decimal
# Recibe: un número binario
# Devuelve: el número convertido en decimal
#===============================================================================
def binarioADecimal(num):
    #Convierto el número a string para poderlo recorrer como una cadena
    num=str(num)
    #Variable acumuladora para el exponente de la potencia, ya que 
    #se va incrementando en 1
    exponente=0
    #La base de la potencia siempre vale 2
    base=2
    #Variable sumatoria que coincide con el número en decimal
    numDecimal=0
    #Recorro el número desde -1, -2, -3, etc.
    for i in range (1, len(num)+1):
        #Si el dígito es 1 (recordar que num es string
        if num[-i]=="1":
            #Sumo el resultado de la base por el exponente, que se
            #incrementa en 1, pero como empieza desde 0, e i empieza en 1,
            #de ahí que sea (i-1)
            numDecimal+=base**(exponente+(i-1))
          
    return numDecimal

assert(binarioADecimal(1011101)==93)
assert(binarioADecimal(1110111)==119)
assert(binarioADecimal(10111)==23)
assert(binarioADecimal(1000)==8)
assert(binarioADecimal(101)==5)


#===============================================================================
# Esta función convierte un número decimal a binario
# Recibe: un número decimal
# Devuelve: un número en binario
#===============================================================================
# def decimalABinario(num):
#     #Como voy a hacer un .append, que mete los elementos en orden inverso al que
#     #necesito, pues llamo a la lista numeroReves
#     numeroReves=[]
#     #El dividendo al inicio es el número
#     dividendo=num
#     #Divisor siempre es 2
#     divisor=2
#     #Inicio el cociente a 2 para que entre la primera vez en el bucle
#     cociente=2
#     #El bucle se repite hasta que el cociente sea mayor que 1.
#     while cociente>1:
#         #Calculo el cociente con la división entera
#         cociente=dividendo//divisor
#         #Calculo el resto con el módulo
#         resto=dividendo%divisor
#         #Añado el resto a la lista
#         numeroReves.append(resto)
#         #El nuevo dividendo es el cociente
#         dividendo=cociente
#     #Añado a la lista el cociente final    
#     numeroReves.append(cociente)
#     #Creo una variable acumuladora de tipo string para convertir el número
#     numBinario=""
#     #Recorro la cadena desde [1, numero] porque voy a ir concatenando el valor
#     #de i en negativo, por lo tanto será -1, -2, -3, etc.
#     for i in range (1, len(numeroReves)+1):
#         #Las acumulo en la variable, pero con formato str, ya que los elementos
#         #de la lista son de tipo entero.
#         numBinario+=str(numeroReves[-i])
#     #Por último devuelvo el número, pero convertido de cadena a entero
#     return int(numBinario)
#
#
# assert(decimalABinario(93)==1011101)
# assert(decimalABinario(119)==1110111)
# assert(decimalABinario(23)==10111)
# assert(decimalABinario(8)==1000)
# assert(decimalABinario(5)==101)
