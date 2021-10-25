"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 22, 2021
 @nombre: Boletin 2 - Ejercicio Extra
 @enunciado: 
 Crea una programa que tenga muestre un mensaje para elegir las siguientes opciones:
0. voltea: Le da la vuelta a un número.
1. esCapicua: Devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario. 
2. siguientePrimo: Devuelve el menor primo que es mayor al número que se pasa como parámetro. 
3. digitos: Cuenta el número de dígitos de un número entero. 
4. digitoN: Devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha. 
5. posicionDeDigito: Da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1. 
6. quitaPorDetras: Le quita a un número n dígitos por detrás (por la derecha). 
7. quitaPorDelante: Le quita a un número n dígitos por delante (por la izquierda). 
8. pegaPorDetras: Añade un dígito a un número por detrás. 
9. pegaPorDelante: Añade un dígito a un número por delante. 
10. trozoDeNumero: Toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente. 
11. juntaNumeros: Pega dos números para formar uno.
 """
 
#Creo el menú y lo guardo en una variable 
menu="Menú de opciones: \n"\
    "0. voltea \n"\
    "1. esCapicua \n"\
    "2. siguientePrimo \n"\
    "3. digitos \n"\
    "4. digitoN \n"\
    "5. posicionDeDigito \n"\
    "6. quitaPorDetras \n"\
    "7. quitaPorDelante \n"\
    "8. pegaPorDetras \n"\
    "9. pegaPorDelante \n"\
    "10. trozoDeNumero \n"\
    "11. juntaNumeros \n"

#Imprimo el menú
print(menu)

#Pido al usuario que elija una opción
opcion=int(input("Elige una de las opciones: "))         

#Compruebo que los datos son correos y sino lo son,
#vuelvo a imprimir menú y a pedir los datos
while opcion<0 or opcion>11:
    print("Opción incorrecta. Vuelve a intentarlo.")
    print(menu)
    opcion=int(input("Elige una de las opciones: "))

#Pido un número, variable que voy a usar en cada opción
num=int(input("Introduce un número: "))                

#Estructura lógica para que haga la opcion seleccionada
#el usuario
if opcion==0:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Creo variable acumuladora vacía del tipo cadena para usarla en el bucle
    numReves=""
    #Creo un bucle para recorrer el número
    for i in range (1, len(num)+1):
        #Voy acumulando cada caracter (dígito) del número 
        #pero en orden inverso con respecto al número
        numReves+=num[-i]
    #Guardo mensaje final en variable mensaje
    mensaje="El número dado la vuelta es %s." %(numReves)

elif opcion==1:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Creo variable acumuladora vacía del tipo cadena para usarla en el bucle
    numReves=""
    #Creo un bucle para recorrer el número
    for i in range (1, len(num)+1):
        #Voy acumulando cada caracter (dígito) del número 
        #pero en orden inverso con respecto al número
        numReves+=num[-i]
    #Compruebo si el num es igual al número en orden inverso.
    #Si es cierto devuelve True, si no, False
    if num==numReves:
        mensaje=True
    else:
        mensaje=False

elif opcion==2:
    #Creo la variable que itera en el bucle while externo y le doy un valor inicial que parta del n.º siguiente 
    #al número que ha introducido el usuario
    i=num+1
    #Creo la bandera que voy a utilizar en el bucle externo y la inicializo a False
    esPrimo=False
    #La condición de entrada en el bucle externo es doble: que la bandera no se haya modificado
    #y que la variable iteradora sea menor o igual que el número + 100 (suficiente para encontrar
    #el siguiente primo)
    while i<=num+100 and esPrimo==False:
        #Creo la variable que itera el bucle while interno y le digo que empiece en 2 porque va a comprobar
        #los divisores de i
        j=2
        #Creo la bandera que voy a utilizar en el bucle interno y la inicializo a True
        esPrimo=True
        #La condición de entrada en el bucle interno es doble: que la bandera no se haya modificado
        #y que la variable iteradora sea menor o igual que la mitad del número (al estar buscando divisores)
        while j<=i//2 and esPrimo==True:
            #Si i es divisible entre j, el número tiene un divisor, por lo que no es primo, así que cambio 
            #la bandera para que no vuelva a entrar en el bucle
            if i%j==0:
                esPrimo=False
            #Si i no es divisible entre j, incrementamos j en 1, para que vuelva a dar otra vuelta al bucle.
            else:
                j+=1
           
        #Si tras salir del bucle while interno la bandera esPrimo ha cambiado a True, guarda un mensaje en una
        #variable y aquí se parará el bucle while externo
        if esPrimo==True:        
            mensaje="%s es el siguiente primo." %(i)
        #Si la bandera esPrimo no ha cambiado, incrementamos la variable iteradora i y será otra iteración del
        #bucle externo while.
        else:
            i+=1

elif opcion==3:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Creo una variable contadora para usarla en el bucle
    contador=0
    #Bucle for que recorre la variable num de tipo string y aumenta la variable contadora con cada iteración.
    for i in num:
        contador+=1
    #En la variable mensaje guardamos el mensaje final
    mensaje="Tiene %s dígitos." % (contador)

elif opcion==4:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos datos
    posicion=int(input("¿El dígito de qué posición quiere saber (0 en adelante)? "))
    #Si la variable es menor que 0 o mayor que la longitud de num (se iria fuera de rango), vuelve a pedir los datos
    while posicion<0 or posicion>len(num):
        print("Posición fuera de rango del número. Inténtalo de nuevo.")
        posicion=int(int("¿El dígito de qué posición quiere saber (0 en adelante)? "))
    #Creamos la variable mensaje donde calculamos la posicion
    mensaje="El dígito que se encuentra en la posición %s es %s." % (posicion, num[posicion])
    
elif opcion==5: 
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos datos
    digito=int(input("¿Qué dígito quiere saber en qué posición se encuentra? "))
    #Comprobación de dato correcto. Si no lo es, se pide de nuevo
    while digito<0:
        print("El dígito debe ser un entero positivo (incluido el 0).")
        digito=int(input("¿Qué dígito quiere saber en qué posición se encuentra? "))
    #Creamos una bandera y la inicializamos a False
    ocurrencia=False
    #Creamos la variable iteradora para usarla en el bucle while
    i=0
    #Establecemos el bucle en el que i va [0, longitud del número) y tiene una bandera
    while i<len(num) and ocurrencia==False:
        #Si el digito (casting para poder comprobar con num que es string) es igual al valor del digito del numero,
        #guardamos mensaje en la variable y cambiamos la bandera, para que pare el bucle
        if str(digito)==num[i]:
            mensaje="La primera ocurrencia del dígito se encuentra en la posición %s." %(i)
            ocurrencia=True
        #Si no ocurre lo anterior, incrementamos el valor de i, para hacer otra iteración del bucle
        else:
            i+=1
    #Si al terminar el bucle la bandera no ha cambiado, la variable mensaje toma valor -1.
    if ocurrencia==False:
        mensaje=-1
    
elif opcion==6:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos datos
    numDigitosDerecha=int(input("¿Cuántos dígitos quiere quitarle al número por la derecha? "))
    #Si los datos son incorrectos (el número de dígitos a quitar es mayor que la longitud de número), 
    #los volvemos a pedir
    while numDigitosDerecha>len(num):
        print("El número introducido no tiene suficientes dígitos para los que quiere quitar.")
        numDigitosDerecha=int(input("¿Cuántos dígitos quiere quitarle al número por la derecha? "))
    #Si los digitos que queremos quitar es igual a la longitud del número, creamos variable mensaje
    #para decir que no nos quedan dígitos en el número
    if numDigitosDerecha==len(num):
        mensaje="El número resultante es 0."
    #De lo contrario, es decir, si nos quedan dígitos:
    else:
        #Creanos una nueva variable de tipo string para guardar el número que nos queda una vez
        #quitemos los dígitos
        numNuevoDerecha=""
        #Recorremos con un buble desde [0, longitud numero-numDigitosDerecha) y acumulamos en la variable vacía
        #definida en la línea anterior
        for i in range (len(num)-numDigitosDerecha):
            numNuevoDerecha+=num[i]
        #El resultado lo guardamos en la variable mensaje
        mensaje="El número resultante es %s." % (numNuevoDerecha)

elif opcion==7:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos datos
    numDigitosIzquierda=int(input("¿Cuántos dígitos quiere quitarle al número por la izquierda? "))
    #Si los datos son incorrectos (el número de dígitos a quitar es mayor que la longitud de número), 
    #los volvemos a pedir
    while numDigitosIzquierda>len(num):
        print("El número introducido no tiene suficientes dígitos para los que quiere quitar.")
        numDigitosIzquierda=int(input("¿Cuántos dígitos quiere quitarle al número por la izquierda? "))
    #Si los digitos que queremos quitar es igual a la longitud del número, creamos variable mensaje
    #para decir que no nos quedan dígitos en el número
    if numDigitosIzquierda==len(num):
        mensaje="Se han eliminado todos los dígitos del número."
    #De lo contrario, es decir, si nos quedan dígitos:
    else:
        #Creanos una nueva variable de tipo string para guardar el número que nos queda una vez
        #quitemos los dígitos
        numNuevoIzquierda=""
        #Recorremos con un buble desde [numeroDigitosIzquierda, longitud numero) y acumulamos en la variable vacía
        #definida en la línea anterior
        for i in range (numDigitosIzquierda, len(num)):
            numNuevoIzquierda+=num[i]
        #El resultado lo guardamos en la variable mensaje
        mensaje="El número resultante es %s." % (numNuevoIzquierda)

elif opcion==8:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos los datos
    digitosDerecha=input("¿Qué dígito quiere añadir al número por la derecha? ")
    #Comprobamos los datos y de ser erróneos, volvemos a pedirlos.
    while digitosDerecha<0:
        print("Error. Debe introducir un número positivo, el 0 incluído.")
        digitosDerecha=input("¿Qué dígito quiere añadir al número por la derecha? ")
    #Creamos una nueva variable en la que concatenamos el número y los digitos a la derecha, sumándolos
    newNum=num+digitosDerecha
    #El resultado lo guardamos en la variable mensaje
    mensaje="El número resultante es %s." % (newNum)
    

elif opcion==9:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos los datos
    digitosIzquierda=input("¿Qué dígito quiere añadir al número por la izquierda? ")
    #Comprobamos los datos y de ser erróneos, volvemos a pedirlos.
    #El 0 es un dato erróneo, ya que no tiene valor a la izquierda.
    while digitosIzquierda<=0:
        print("Error. Debe introducir un número positivo.")
        digitosIzquierda=input("¿Qué dígito quiere añadir al número por la izquierda? ")
    #Creamos una nueva variable en la que concatenamos los digitos a la izquierda y el número, sumándolos
    newNum=digitosIzquierda+num
    #El resultado lo guardamos en la variable mensaje
    mensaje="El número resultante es %s." % (newNum)

elif opcion==10:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos los datos de la posición inicial
    posicionInicial=int(input("Introduzca la posición inicial: "))
    #Comprobamos que los datos no sean erróneos, es decir, que la posición no sea un número negativo
    #o que la posición inicial sea mayor o igual que la longitud del número (salida de rango o que no
    #muestre ningún dígito. Si son incorrectos, los volvemos a pedir
    while posicionInicial<0 or posicionInicial>=len(num):
        print("Datos erróneos. La posición inicial no puede ser menor que cero ni mayor o igual que la longitud del número.")
        posicionInicial=int(input("Introduzca la posición inicial: "))
    #Pedimos los datos de la posición final
    posicionFinal=int(input("Introduzca la posición final: "))
    #Comprobamos que los datos no sean erróneos, es decir, que la posición final no sea mayor o igual
    #que la inicial o que la posición final no sea mayor que la longitud del número.
    #Si son incorrectos, los volvemos a pedir
    while posicionFinal<=posicionInicial or posicionFinal>len(num):
        print("Datos erróneos. La posición final no puede ser menor o igual que la inicial ni mayor que la longitud del número.")
        posicionFinal=int(input("Introduzca la posición final: "))
    #Creamos una variable acumuladora de tipo string donde guardaremos el nuevo número entre posición inicial y final
    newNum=""
    #Recorremos desde [posicion inicial, posicion Final], para que incluya ambos números
    for i in range (posicionInicial, posicionFinal+1):
        #Con cada iteración almacenamos el resultado en la variable acumuladora
        newNum+=num[i]
    #El resultado lo guardamos en la variable mensaje
    mensaje="El trozo comprendido entre la posición inicial %s y la posición final %s, ambas inclusive, es %s." % (posicionInicial, posicionFinal, newNum)

else:
    #Hago un casting del número para que lo lea como string
    num=str(num)
    #Pedimos un segundo número, con una variable de tipo string, para poder sumarla con la primera
    num2=input("Introduce otro número: ")
    #Sumamos ambas variables de tipo string
    newNum=num+num2
    #El resultado lo guardamos en la variable mensaje
    mensaje="El número resultante de juntar ambos números es %s." % (newNum)

#Imprimimos la variable mensaje, común a toda la estructura lógica    
print(mensaje)
