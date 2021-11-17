'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Reto Censo Electoral
 @enunciado: CENSO ELECTORAL
Acaban de pasar las elecciones generales del 10/11/19. Ha ganado el partido de Kodos. Se ha
filtrado que un grupo de extraterrestres se han infiltrado entre la sociedad y han sido los que han
votado mayoritariamente a Kodos. Como Kodos y Kang quieren someternos a todos, tú y tu grupo
de amigos hackers decidís hacer algo al respecto. Robáis la lista de votos por correo (ya que al ser
verdes y con tentáculos estáis casi seguros que todos habrán votado por correo). Pero la lista está
cifrada y en vez del DNI cada voto se referencia por un número (un hash). Conseguís robar el
algoritmo que se ha usado para el cifrado y ahora está en tus manos el conseguir descifrar esos
números y sacar los DNI’s que tienen los extraterrestres. ¡La humanidad te necesita!

El algoritmo de cifrado se basa en repetir los siguientes 5 pasos (una iteración de cifrado) un
número aleatorio de veces. Veremos los pasos usando como ejemplo de entrada el 13112221:

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

Ahora bien, este es solo una iteración de descifrado. Puede haber más ¿Cuántas más? Todas las
válidas ¿Cuándo una iteración es válida? Supongamos que queremos ejecutar una iteración de
descifrado sobra A, lo cual produce B. Esta iteración será válida si al cifrar B nos da como resultado
A.

-----------------------------------------------------------------------------------------

Mejor vemos esto con un ejemplo. Al recibir como entrada el número 1211, nuestro algoritmo
(después de ejecutar todas las iteraciones de descifrad válidas) tendría que dar como resultado 1 ya
que:

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
d descifrado (1111 → 11) no era válida. Por lo que el resultado de descifrar 41 es 1111 y no 11.

------------------------------------------------------------------------------------------

A continuación mostramos estos datos de ejemplo para que puedas comprobar tu algoritmo:

    Clave              Descifrado
    1211               1
    111321             111
    22                 22
'''