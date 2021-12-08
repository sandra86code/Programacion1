'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 3, 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: 
 Vamos a realizar un programa  para una gasolinera que tiene cuatro surtidores y quiere que 
 cuando un coche llegue a nuestra gasolinera se le asigne el surtidor que esté más lleno dentro 
 de su categoría (Diesel o Gasolina). 
 La gasolinera tiene 4 surtidores, dos de gasolina (el 1 y el 2) y dos de diesel, (el 3 y el 4) 
 y deberemos realizar un programa con el siguiente menú:

    1. Llenar surtidor.
    2. Llegada de coche.
    3. Ver puntos.
    4. Comprobar ventas.
    5. Ver surtidores.
    6. Asignar precio de gasolina.
    7. Asignar precio de diesel.
    8. Salir.

Cuando se pulse la opción 1, nos deberá preguntar qué cantidad se va añadir al depósito del surtidor 
y qué surtidor se va a llenar, y añadir la nueva cantidad a la cantidad que tiene el depósito del surtidor. 
No se pueden introducir cantidades negativas porque no se puede vaciar el surtidor.

Con la opción 2 se deberá preguntar la matrícula del coche (se deberá comprobar que es el formato adecuado, 
4 números y 3 letras), si el coche ya ha estado en nuestra gasolinera debemos ver si es diesel o gasolina, 
preguntarle cuánto dinero quiere gastar en gasolina o diesel (Tendrá que ser cómo mínimo 10 euros y cómo 
máximo dos decimales) quiere y asignarle el surtidor adecuado. Se debe asignar el surtido más lleno de los 
dos disponibles. 
Si el coche no ha estado en nuestra gasolinera nunca debemos preguntar si es diesel o gasolina, 
almacenarlo para no tener que preguntarle más veces, preguntar cantidad y asignarle el surtidor. 
En ambos casos se deberá almacenar el dinero gastado ya que vamos a ir dandole puntos según el dinero que 
se ha gastado en la gasolinera.

En la opción 3 se le pedirá la matrícula y se le dirá los puntos que tiene. Se les dará un punto por cada 
10 euros gastados en nuestra gasolinera. Si la matrícula no está registrado se le dirá que no es un cliente 
de nuestra gasolinera.

En la opción 4 se deberá mostrar un listado con todos las matriculas de coches que han respostado en nuestra 
gasolinera junto con el total gastado.

En la opción 5 se deberá mostrar la cantidad de gasolina o diesel que hay en cada surtidor.

La opción 6 y 7 servirá para asignar el precio de la gasolina y el diesel. Por supuesto este precio será 
superior a 1 y podrá tener 3 decimales (las gasolineras son así). Al empezar el programa también se deberán 
pedir los precios para poder trabajar con el programa.

La opción 8 termina la ejecución del programa.
'''

#Lista global para guardar el precio del carburante: primero en la lista va el precioGasolina y luego el precioDiesel
precioCarburantes=[0,0]
#Lista global para guardar cuánta cantidad tiene cada depósito. El primer [0] y el segundo depósito [1] son de gasolina y
#el tercero [2] y cuarto [3] son de diésel
surtidores=[0,0,0,0]
#Lista global para guardar las matrículas de los coches que ya son clientes de la gasolinera.
matriculasCoches=[]
#Lista global para guardar el tipo de carburante de cada coche que es cliente de la gasolinera. Se relaciona con las 
#matrículas por la posición en la lista.
tipoCarburanteCoches=[]
#Lista global para guardar el dinero total gastado por cada coche en la gasolinera. Se relaciona con las matrículas y el tipo
#de carburante por la posición en la lista.
totalGastadoCoches=[]


#===============================================================================
# Esta función imprime un mensaje que recibe
# Recibe: un mensaje, cadena de string, variable o lista
# Devuelve: no tiene return
#===============================================================================
def mostrarMensaje(mensaje):
    
    print(mensaje)


#===============================================================================
# Esta función añade una cantidad de carburante a un surtidor.
# Recibe: no tiene parámetros de entrada
# 1. Pregunta al usuario por el número de surtidor y valida los datos. Si no son
# válidos, lo vuelve a preguntar.
# 2. Pregunta al usuario la cantidad que añadir a en ese surtidor. Valida los datos
# y si no son válidos (que sean 0 o negativo), lo vuelve a preguntar.
# 3. Accede a la posición correspondiente en la lista de surtidores y le suma la
# cantidad.
#===============================================================================
def llenarSurtidor():
    
    numeroSurtidor=int(input("¿Qué surtidor desea llenar (1,2,3,4)?: "))
    while numeroSurtidor not in {1,2,3,4}:
        mostrarMensaje("Ese surtidor no existe.")
        numeroSurtidor=int(input("¿Qué surtidor desea llenar (1,2,3,4)?: "))
    
    cantidad=float(input("¿Qué cantidad de litros desea introducir en el surtidor? "))
    while cantidad<=0:
        mostrarMensaje("Error, la cantidad debe ser mayor que 0.")
        cantidad=float(input("¿Qué cantidad de litros desea introducir en el surtidor? "))
    
    surtidores[numeroSurtidor-1]+=cantidad


#===============================================================================
# Esta función comprueba que una matrícula sea válida (formato de 4 números y 3
# letras).
# Recibe: una matrícula (cadena de caracteres alfanuméricos)
# Devuelve:
# True si la matrícula es válida.
# False si la matrícula no es válida.
#===============================================================================
def comprobarValidezMatricula(matricula):
    
    i=0
    matriculaCorrecta=True
    #Si la matrícula tiene 7 caracteres, recorremos la cadena.
    if len(matricula)==7:
        while i<len(matricula) and matriculaCorrecta:
            #Comprobamos si los primero 4 caracteres son números (ASCII). Si no lo son,
            #cambiamos la bandera y se frena el bucle. 
            if i<4:
                if ord(matricula[i])<ord("0") or ord(matricula[i])>ord("9"):
                    matriculaCorrecta=False
            #Comprobamos que los 3 últimos caracteres (del total de 7) son letras mayúsculas
            #(ASCII). Si no lo son, cambiamos la bandera y se frena el bucle.
            elif i<7:
                if ord(matricula[i].upper())>=ord("A") and ord(matricula[i].upper())<=ord("Z"):
                    matriculaCorrecta=True
                else:
                    matriculaCorrecta=False
            i+=1
    #Si no tiene 7 posiciones, directamente devolvemos False.
    else:
        matriculaCorrecta=False
        
    return matriculaCorrecta

#Tests para comprobar que la función funciona correctamente
assert(comprobarValidezMatricula("0349XZA")==True)
assert(comprobarValidezMatricula("1345X2A")==False)
assert(comprobarValidezMatricula("13w4XZA")==False)
assert(comprobarValidezMatricula("13XZA")==False)
assert(comprobarValidezMatricula("13444XZA")==False)


#===============================================================================
# Esta función comprueba qué surtidor (según el tipo de Carburante) está más lleno
# Recibe: el tipo de carburante (string)
# Devuelve: el surtidor (número entero)
#===============================================================================
def comprobarSurtidorMasLleno(tipoCarburante):
    #Compruebo cuál de los surtidores de gasolina [0] o [1] está más lleno
    if tipoCarburante=="gasolina":
        #Controlo también si están igual de llenos, ya que de ser así no devolvería nada
        # al no hacer esta comprobación.
        if surtidores[0]>=surtidores[1]:
            surtidor=1
        elif surtidores[1]>surtidores[0]:
            surtidor=2
    #Compruebo cuál de los surtidores de diésel [2] o [3] está más lleno
    else:
        #Controlo también si están igual de llenos, ya que de ser así no devolvería nada
        # al no hacer esta comprobación.
        if surtidores[2]>=surtidores[3]:
            surtidor=3
        elif surtidores[3]>surtidores[2]:
            surtidor=4
    
    return surtidor


#===============================================================================
# Esta función calcula los litros de carburante que reposta un coche en función
# del dinero repostado y del precio del tipo de carburante por litro.
# Recibe: el dinero repostado (float de 2 decimales) y el tipo de carburante (string)
# Devuelve: los litros de carburante repostado redondeado a 2 decimales
#===============================================================================
def calcularLitros(dinero,tipoCarburante):
    
    if tipoCarburante=="gasolina":
        #El precio del carburante se asigna llamando a una función que accede a la posición
        #de una lista donde se guarda el precio de la gasolina y del diésel.
        precioCarburante=comprobarPrecioGasolina()
    else:
        precioCarburante=comprobarPrecioDiesel()
    
    litros=dinero/precioCarburante
    
    return round(litros, 2)


#===============================================================================
# Esta función:
# 1. Pide una matrícula y comprueba si es válida:
#    - Si no es válida, muestra un mensaje de que no lo es.
#    - Si es válida, comprueba si la matrícula está en la lista de matrículas 
#    (si es cliente o no de la gasolinera):
#        *Si lo es, comprueba la posición de la matrícula en la lista de matrículas
#         y, usando esa posición, comprueba el tipo de carburante del coche en la
#         lista de tipos de carburantes.
#         *Si no lo es:
#            +Añade la matrícula a la lista de matrículas y guarda su posición
#            en una variable (para usarlo más adelante).
#            +Añade un 0 a la lista del total de dinero gastado por el coche.
#            +Pregunta el tipo de carburante, valida el dato y, si no es correcto,
#            lo vuelve a preguntar.
#            +Añade el tipo de carburante a la lista de tipos de carburantes.
#        
#        - Para ambos casos, pregunta el dinero que va a repostar. Valida el dato y,
#        si no es correcto, lo vuelve a preguntar.
#        - Guarda en una variable cuál es el surtidor de ese tipo de carburante más
#        lleno.
#        - Muestra un mensaje para que el coche se dirija a ese surtidor.
#        - Resta a ese surtidor el número de litros repostados por el coche (llamando
#        a la función calcularLitros).
#        - Suma el dinero repostado a la posición correspondiente a ese coche de la 
#        lista del total de dinero gastado por cada coche.       
#===============================================================================
def llegadaCoche():
    
    matricula=input("Introduzca la matrícula de su coche: ")
    if comprobarValidezMatricula(matricula):
        if matricula in matriculasCoches:
            pos=matriculasCoches.index(matricula)
            tipoCarburante=tipoCarburanteCoches[pos]
        else:
            matriculasCoches.append(matricula)
            pos=matriculasCoches.index(matricula)
            totalGastadoCoches.append(0)
            tipoCarburante=input("¿Su coche es gasolina o diesel? ")
            while tipoCarburante not in {"gasolina", "diesel"}:
                mostrarMensaje("Respuesta incorrecta.")
                tipoCarburante=input("¿Su coche es gasolina o diesel? ")
            tipoCarburanteCoches.append(tipoCarburante)
        dinero=float(input("¿Cuánto dinero desea repostar? "))
        while dinero<10 or dinero!=float("{:.2f}".format(dinero)):
            mostrarMensaje("Datos erróneos. Debe ser mayor que 10 y tener 2 decimales.")
            dinero=float(input("¿Cuánto dinero desea repostar? "))
        surtidor=comprobarSurtidorMasLleno(tipoCarburante)
        mostrarMensaje("Diríjase al surtidor %s" % (surtidor))
        surtidores[surtidor-1]-=calcularLitros(dinero, tipoCarburante)
        totalGastadoCoches[pos]+=dinero
           
    else:
        mostrarMensaje("La matrícula no es correcta (4 números y 3 letras).")    
        

#===============================================================================
# Esta función calcula los puntos que tiene un cliente según total gastado en euros,
# a razón de 1 punto cada 10 euros gastados.
# Recibe: no tiene parámetros de entrada.
# Devuelve: no tiene return
#===============================================================================
def verPuntos():
    #Comprobamos que tengamos clientes registrados y sino imprimimos un mensaje que diga
    # que no hay clientes registrados.
    if len(matriculasCoches)!=0:
        #Pedimos la matrícula del coche
        matricula=input("Introduzca la matrícula del coche: ")
        #Si la matrícula está en la lista de matrículas, es decir, si el propietario del coche
        #es cliente, calculamos la posición de la matricula en la lista de matrículas
        if matricula in matriculasCoches:
            posicion=matriculasCoches.index(matricula)
            #Imprimos el mensaje de los puntos totales dividiendo el total de dinero gastado en euros
            #de esa posición en la lista del dinero gastado por cada coche y lo dividimos entre 10
            #(división entera para que el número de puntos sea entero)
            mostrarMensaje("Sus puntos totales son: %s" % (totalGastadoCoches[posicion]//10))
        #Si la matrícula no está en la lista de matrículas, imprimimos el mensaje de que no es cliente.
        else:
            mostrarMensaje("No es cliente de nuestra gasolinera.")
    else:
        mostrarMensaje("Aún no hay clientes registrados.")


#===============================================================================
# Esta función muestra el dinero gastado por cada cliente y en qué tipo de carburante
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
#===============================================================================
def comprobarVentas():
    #Siempre que la lista de matrículas no esté vacía tendremos ventas
    if len(matriculasCoches)!=0:
        #Recorremos la lista de matrículas para mostrar el dinero gastado por cada cliente
        #y en qué tipo de carburante.
        for i in range (len(matriculasCoches)):
            mostrarMensaje("El coche con la matrícula %s ha gastado un total de %s € de %s." % (matriculasCoches[i], totalGastadoCoches[i], tipoCarburanteCoches[i]))
    #Si la lista de matrículas está vacía, imprimimos el mensaje de que aún no hay ventas.
    else:
        mostrarMensaje("Aún no hay ventas por mostrar.")
    

#===============================================================================
# Esta función muestra los litros que tiene cada surtidor y de qué tipo de carburante
#===============================================================================    
def mostrarSurtidores():
    #Como la lista de surtidores tiene iniciada al principio los 4 surtidores a 0, si
    #estuviese vacíos, mostraría que tienen 0 litros 
    for i in range (len(surtidores)):
        if i==0 or i==1:
            mostrarMensaje("El surtidor %s tiene %s litros de gasolina." % (i+1, surtidores[i]))
        else:
            mostrarMensaje("El surtidor %s tiene %s litros de diésel." % (i+1, surtidores[i]))
    

#===============================================================================
# Esta función asigna el precio del diésel y lo modifica en la lista de precios
# de carburantes en la posición 1, correspondiente al precio del diésel.
#===============================================================================
def asignarPrecioDiesel():
    
    precioDiesel=float(input("Introduzca el precio del diésel: "))
    #Validamos datos, que tanto el precio del diésel sea mayor o igual que 1 y que tenga
    #3 decimales, comprobando que la variable con formato de 3 decimales no sea diferente 
    #a la variable introducida por el usuario
    while precioDiesel<=1 or precioDiesel!=float("{:.3f}".format(precioDiesel)):
        mostrarMensaje("Datos erróneos. Debe ser mayor o igual que 1 y tener 3 decimales")
        precioDiesel=float(input("Introduzca el precio del diésel: "))
    #Asignamos el valor a la posición 1 de la lista de Carburantes
    precioCarburantes[1]=precioDiesel
    #Mostramos el mensaje con el nuevo precio    
    mostrarMensaje("El nuevo precio del diésel es %s" % precioCarburantes[1])    


#===============================================================================
# Esta función asigna el precio de la gasolina y lo modifica en la lista de precios
# de carburantes en la posición 0, correspondiente al precio de la gasolina.
#===============================================================================     
def asignarPrecioGasolina():
    
    precioGasolina=float(input("Introduzca el precio de la gasolina: "))
    #Validamos datos, que tanto el precio de la gasolina sea mayor o igual que 1 y que tenga
    #3 decimales, comprobando que la variable con formato de 3 decimales no sea diferente 
    #a la variable introducida por el usuario
    while precioGasolina<=1 or precioGasolina!=float("{:.3f}".format(precioGasolina)):
        mostrarMensaje("Datos erróneos. Debe ser mayor o igual que 1 y tener 3 decimales.")
        precioGasolina=float(input("Introduzca el precio de la gasolina: "))
    #Asignamos el valor a la posición 0 de la lista de Carburantes
    precioCarburantes[0]=precioGasolina
    #Mostramos el mensaje con el nuevo precio    
    mostrarMensaje("El nuevo precio de la gasolina es %s" % precioCarburantes[0])
    
    
#===============================================================================
# Esta función devuelve el precio de la gasolina 
# Devuelve: el precio de la gasolina (float de 3 decimales)
#===============================================================================
def comprobarPrecioGasolina():
    
    return precioCarburantes[0]


#===============================================================================
# Esta función devuelve el precio del diésel 
# Devuelve: el precio del diésel (float de 3 decimales)
#=============================================================================== 
def comprobarPrecioDiesel():
    
    return precioCarburantes[1]

        
#===============================================================================
# Esta función gestiona el menú de opciones, es decir, según la opción, llama a una
# función de las anteriores
# Recibe: una opción (número entero)
#===============================================================================            
def gestionarMenu(opcion):
    
    if opcion==1:
        llenarSurtidor()
    elif opcion==2:
        llegadaCoche()
    elif opcion==3:
        verPuntos()
    elif opcion==4:
        comprobarVentas()
    elif opcion==5:
        mostrarSurtidores()
    elif opcion==6:
        asignarPrecioGasolina()
    elif opcion==7:
        asignarPrecioDiesel()


#===============================================================================
# Esta función muestra el menú de opciones
# Devuelve: la variable con el menú de opciones (string)
#===============================================================================
def mostrarMenu():
    menu="1. Llenar surtidor.\n"\
        "2. Llegada de coche.\n"\
        "3. Ver puntos.\n"\
        "4. Comprobar ventas.\n"\
        "5. Ver surtidores.\n"\
        "6. Asignar precio de gasolina.\n"\
        "7. Asignar precio de diesel.\n"\
        "8. Salir.\n"
    
    return menu


#===============================================================================
# Esta función es la principal del programa.
# 1. Muestra un mensaje de bienvenida
# 2. Pide el precio de la gasolina y del diésel
# 3. Muestra el menú
# 4. Pide la opción y valida datos
# 5. Mientras que la opción esté entre la 1 y la 7, llama a la función que 
#    gestiona el menú de opciones, muestra el mensaje de la opción (en el caso de
#    que lo haya, y vuelve a pedir la opción.
#    Si la opción es la 8 (salida), sale del bucle y muestra un mensaje de despedida.
#===============================================================================
def main():
    
    mostrarMensaje("Bienvenid@ al surtidor Jacarandá.")
    asignarPrecioGasolina()
    asignarPrecioDiesel()
    
    opcion=1
        
    while opcion!=8:
        mostrarMensaje("-----------------------------------------------------------")
        mostrarMensaje(mostrarMenu())
    
        opcion=int(input("Escriba la opción deseada: "))
        while opcion<1 or opcion>8:
            mostrarMensaje("Opción incorrecta.")
            opcion=int(input("Escriba la opción deseada: "))
        
        mostrarMensaje("-----------------------------------------------------------")
         
        if opcion!=8:
            gestionarMenu(opcion)
        
    print("Hasta la próxima.")
    
main()
