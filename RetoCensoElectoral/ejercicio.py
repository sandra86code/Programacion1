'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Reto Censo Electoral
 @enunciado: CENSO ELECTORAL

Acaban de pasar las elecciones generales del 10/11/19. Ha ganado el partido de Kodos. 

Se ha filtrado que un grupo de extraterrestres se han infiltrado entre la sociedad y 
han sido los que han votado mayoritariamente a Kodos. 

Como Kodos y Kang quieren someternos a todos, tú y tu grupo de amigos hackers decidís 
hacer algo al respecto. Robáis la lista de votos por correo (ya que al ser verdes y 
con tentáculos estáis casi seguros que todos habrán votado por correo). 
Pero la lista está cifrada y en vez del DNI cada voto se referencia por un número 
(un hash). 
Conseguís robar el algoritmo que se ha usado para el cifrado y ahora está en tus manos 
el conseguir descifrar esos números y sacar los DNI’s que tienen los extraterrestres. 
¡La humanidad te necesita!

El algoritmo de cifrado se basa en repetir los siguientes 5 pasos (una iteración de cifrado) un
número aleatorio de veces. 
Veremos los pasos usando como ejemplo de entrada el 13112221:

    1. El primer paso será separar la cadena de números agrupando los números en función de
    números iguales: 1 3 11 222 1
    
    2. Una vez separados en función de los números iguales se cuenta el número de elementos que
    tiene cada subgrupo: Un “1”, un “3”, dos “1”, tres “2”, un “1”.

    3. Se traduce el texto anterior por números: 1 x “1”, 1 x “3”, 2 x “1”, 3 x “2”, 1 x “1”.

    4. Se junta el número de repeticiones con los números para cada subgrupo: 11 13 21 32 11
    
    5. Por último se vuelven a juntar en una misma cadena, de manera que quede 1113213211.

Por lo tanto, después de ejecutar una iteración del cifrado sobre 13112221 el resultado sería
1113213211. Así si se volviese a ejecutar otra iteración de cifrado ahora sobre 1113213211, el
resultado sería 31131211131221.

Pero no quieres cifrar los DNI, sino descifrarlos. Por lo tanto, lo primero que tenemos que ver es
como descifrar cada iteración de cifrado. Aquí podemos ver un ejemplo del caso anterior, es decir,
descifrar 1113213211.

1113213211 → 11 13 21 32 11 → 1 x “1”, 1 x “3”, 2 x “1”, 3 x “2”, 1 x “1” → un “1”, un “3”, dos
“1”, tres “2”, un “1” → 1 3 11 222 1 → 13112221

Ahora bien, este es solo una iteración de descifrado. Puede haber más. ¿Cuántas más? Todas las
válidas. 
¿Cuándo una iteración es válida? Supongamos que queremos ejecutar una iteración de descifrado 
sobre A, lo cual produce B. 
Esta iteración será válida si al cifrar B nos da como resultado A.

-----------------------------------------------------------------------------------------

Mejor vemos esto con un ejemplo. 
Al recibir como entrada el número 1211, nuestro algoritmo (después de ejecutar todas las 
iteraciones de descifrad válidas) tendría que dar como resultado 1 ya que:

1211 → 1 x “2”, 1 x “1” → un “2”, un “1” → 2 1→ 21 (primera iteración de descifrado. Es válida
porque al cifrar 21 nos da 1211).

21 → 2 x “1” → dos “1” → 11 → 11 (segunda iteración de descifrado. Es válida porque al cifrar 11
nos da 21).

11 → 1 x “1” → un “1” → 1 → 1 (tercera iteración de descifrado. Es válida porque al cifrar 1 nos
da 11).

1→ ERROR (no se puede ejecutar una cuarta iteración de descifrado ya que no es posible descifrar
el 1).

Por lo tanto, el resultado de descifrar 1211 es 1.

------------------------------------------------------------------------------------------

Otro ejemplo sería recibiendo como entrada el número 41:

41 → 4 x “1” → cuatro “1” → 1111 → 1111 (válida porque al cifrar 1111 nos da 41).

1111 → 1 x “1”, 1 x “1” → un “1”, un “1” → 1 1 → 11 (esta iteración de descifrado NO es válida
porque al cifrar 11 nos debería dar 21 y no 1111).

Como hemos visto en el ejemplo anterior el 11 produce 21 y no 1111. Es decir, esta última iteración
de descifrado (1111 → 11) no era válida. Por lo que el resultado de descifrar 41 es 1111 y no 11.

------------------------------------------------------------------------------------------

A continuación mostramos estos datos de ejemplo para que puedas comprobar tu algoritmo:

    Clave              Descifrado
    1211               1
    111321             111
    22                 22
    
'''

#===============================================================================
# Esta función corresponde al algoritmo que cifra un número en formato string
# Recibe: un numero en formato string
# Devuelve: el numero cifrado en formato string
#===============================================================================
def cifra(numeroDescifrado):
    #Creo el número cifrado vacío
    numeroCifrado=""
    #Esta variable es la que va a recoger la cuántas veces se repite un mismo número
    #para luego ponerla en el número cifrado. La inicializo a 1 porque el dígito siempre
    #aparece 1 vez.
    cantidad=1
    #Recorro la cadena de dígitos hasta su longitud -1, ya que voy a comparar con el número posterior
    #y sino se saldría de rango
    for i in range(len(numeroDescifrado)-1):
        #Si el caracter numerico es el mismo que el que le sigue, aumento la cantidad
        if numeroDescifrado[i]==numeroDescifrado[i+1]:
            cantidad+=1
        #Si es diferente añado al numeroCifrado la cantidad convertida a string y ese dígito
        else:
            numeroCifrado+=str(cantidad)+numeroDescifrado[i]
            cantidad=1
    #Al finalizar añado el valor de cantidad y el número de la última posición
    numeroCifrado+=str(cantidad)+numeroDescifrado[-1]
    
    return numeroCifrado

# assert(cifra("1")=="11")
# assert(cifra("1111")=="41")
# assert(cifra("21")=="1211")
# assert(cifra("13112221")=="1113213211")


#===============================================================================
# Esta función 
# Recibe 
# Devuelve:
# 
#===============================================================================
def descifra (numeroCifrado):
    numeroDescifrado=""
    #Si el número es par ejecuto el descifrado
    if len(numeroCifrado)%2==0:
        #Recorro el número cifrado (variable string) dígito a dígito en saltos
        #de 2
        for i in range (0,(len(numeroCifrado)),2):
            #La cantidad es el digito y lo convierto a entero porque lo necesito para
            #otro bucle
            cantidad=int(numeroCifrado[i])
            #El número en sí es el siguiente al que corresponde a la cantidad
            numero=numeroCifrado[i+1]
            #Creo un nuevo bucle cuyo número de iteraciones es la cantidad, para añadir
            #el número la cantidad de veces que valga la variable cantidad
            for j in range (cantidad):
                numeroDescifrado+=numero
    #Si el número es impar, el número descifrado es el mismo que el cifrado
    else:
        numeroDescifrado=numeroCifrado

    return numeroDescifrado

# assert(descifra("41")=="1111")
# assert(descifra("1211")=="21")
# assert(descifra("11")=="1")
# assert(descifra("111")=="111")
# assert(descifra("1")=="1")
# assert(descifra("1111111")=="1111111")


#===============================================================================
# Esta función es la principal del programa, la que interactua con el usuario
# llama a las otras funciones e imprime el valor final
#===============================================================================
def main():

    clave=input("Introduce la clave a desencriptar: ")
    #La clave desencriptada es el valor de descifrar la clave
    claveDesencriptada=descifra(clave)
    #La clave Encriptada es el valor de cifrar la clave desencriptada
    claveEncriptada=cifra(claveDesencriptada)

    #Bucle que se repite siempre que la clave sea igual a la encriptada
    # y que la clave no sea igual que la clave desencriptada
    while clave==claveEncriptada and clave!=claveDesencriptada:
        #En cada iteración, la clave toma el valor de la clave desencriptada
        #de la iteración anterior
        clave=claveDesencriptada
        #Volvemos a desencriptar y encriptar la clave para la siguiente comprobación
        claveDesencriptada=descifra(clave)
        claveEncriptada=cifra(claveDesencriptada)
    
    #Imprimimos el resultado con el valor final de la clave desencriptada
    print("El DNI es %s" % claveDesencriptada)

main()

