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

precioCarburantes=[]
surtidores=[0,0,0,0]
matriculasCoches=[]
tipoCarburanteCoches=[]
totalGastadoCoches=[]



def mostrarMensaje(mensaje):
    
    print(mensaje)



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



def comprobarValidezMatricula(matricula):
    
    i=0
    matriculaCorrecta=True
    if len(matricula)==7:
        while i<len(matricula) and matriculaCorrecta:
            if i<4:
                if ord(matricula[i])>=ord("0") and ord(matricula[i])<=ord("9"):
                    matriculaCorrecta=True
                else:
                    matriculaCorrecta=False
            elif i<7:
                if ord(matricula[i].upper())>=ord("A") and ord(matricula[i].upper())<=ord("Z"):
                    matriculaCorrecta=True
                else:
                    matriculaCorrecta=False
            else:
                matriculaCorrecta=False
            i+=1
    else:
        matriculaCorrecta=False
        
    return matriculaCorrecta

assert(comprobarValidezMatricula("0349XZA")==True)
assert(comprobarValidezMatricula("1345X2A")==False)
assert(comprobarValidezMatricula("13w4XZA")==False)
assert(comprobarValidezMatricula("13XZA")==False)
assert(comprobarValidezMatricula("13444XZA")==False)



def comprobarSurtidorMasLleno(tipoCarburante):
    
    if tipoCarburante=="gasolina":
        if surtidores[0]>surtidores[1]:
            surtidor=1
        elif surtidores[1]>surtidores[0]:
            surtidor=2
    else:
        if surtidores[2]>surtidores[3]:
            surtidor=3
        elif surtidores[3]>surtidores[2]:
            surtidor=4
    
    return surtidor


def calcularLitros(dinero,tipoCarburante):
    if tipoCarburante=="gasolina":
        precioCarburante=comprobarPrecioGasolina()
    else:
        precioCarburante=comprobarPrecioDiesel()
    
    litros=dinero/precioCarburante
    
    return round(litros, 2)


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
        


def verPuntos():
    
    if len(matriculasCoches)!=0:
        matricula=input("Introduzca la matrícula del coche: ")
        if matricula in matriculasCoches:
            posicion=matriculasCoches.index(matricula)
            mostrarMensaje("Sus puntos totales son: %s" % (totalGastadoCoches[posicion]/10))
        else:
            mostrarMensaje("No es cliente de nuestra gasolinera.")
    else:
        mostrarMensaje("Aún no hay clientes registrados.")


def comprobarVentas():
    if len(matriculasCoches)!=0:
        for i in range (len(matriculasCoches)):
            mostrarMensaje("El coche con la matrícula %s ha gastado un total de %s € de %s." % (matriculasCoches[i], totalGastadoCoches[i], tipoCarburanteCoches[i]))
    else:
        mostrarMensaje("Aún no hay ventas por mostrar.")
    
    
def mostrarSurtidores():
    
    for i in range (len(surtidores)):
        if i==0 or i==1:
            mostrarMensaje("El surtidor %s tiene %s litros de gasolina." % (i+1, surtidores[i]))
        else:
            mostrarMensaje("El surtidor %s tiene %s litros de diésel." % (i+1, surtidores[i]))
    


def asignarPrecioGasoil():
    
    precioGasoil=float(input("Introduzca el precio de la gasoil: "))
    while precioGasoil<=1 or precioGasoil!=float("{:.3f}".format(precioGasoil)):
        mostrarMensaje("Datos erróneos. Debe ser mayor o igual que 1 y tener 3 decimales")
        precioGasoil=float(input("Introduzca el precio de la gasoil: "))
    precioCarburantes[1]=precioGasoil
        
    mostrarMensaje("El nuevo precio del diésel es %s" % precioCarburantes[1])    

     
def asignarPrecioGasolina():
    
    precioGasolina=float(input("Introduzca el precio de la gasolina: "))
    while precioGasolina<=1 or precioGasolina!=float("{:.3f}".format(precioGasolina)):
        mostrarMensaje("Datos erróneos. Debe ser mayor o igual que 1 y tener 3 decimales.")
        precioGasolina=float(input("Introduzca el precio de la gasolina: "))
    precioCarburantes[0]=precioGasolina

    mostrarMensaje("El nuevo precio del diésel es %s" % precioCarburantes[0])
    
    

def comprobarPrecioGasolina():
    
    return precioCarburantes[0]

    
def comprobarPrecioDiesel():
    
    return precioCarburantes[1]


def asignarPrecioCarburantes():
    
    if len(precioCarburantes)==0:
        precioGasolina=float(input("Introduzca el precio de la gasolina: "))
        while precioGasolina<=1 or precioGasolina!=float("{:.3f}".format(precioGasolina)):
            mostrarMensaje("Datos erróneos. Debe ser mayor o igual que 1 y tener 3 decimales.")
            precioGasolina=float(input("Introduzca el precio de la gasolina: "))
        precioCarburantes.append(precioGasolina)
        precioGasoil=float(input("Introduzca el precio de la gasoil: "))
        while precioGasoil<=1 or precioGasoil!=float("{:.3f}".format(precioGasoil)):
            mostrarMensaje("Datos erróneos. Debe ser mayor o igual que 1 y tener 3 decimales.")
            precioGasoil=float(input("Introduzca el precio de la gasoil: "))
        precioCarburantes.append(precioGasoil)
        
            
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
        asignarPrecioGasoil()


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



def main():
    
    mostrarMensaje("Bienvenid@ al surtidor Jacarandá.")
    asignarPrecioCarburantes()
    
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
