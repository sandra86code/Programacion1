'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 10, 2021
 @nombre: Examen 10 Diciembre - Ejercicio 2
 @enunciado: 
 Un restaurante te ha encargado una aplicación para colocar a los clientes en sus mesas. 
 
 En una mesa se pueden sentar de 0 (mesa vacía) a 4 comensales (mesa llena). 
 Cuando llega un cliente se le pregunta cuántos son (dando un mensaje de error si el 
 número de clientes es superior a 4). 
 
 Para el grupo que llega, se busca siempre la primera mesa libre (con 0 personas). 
 Si no quedan mesas libres, se busca donde haya un hueco para todo el grupo, por
ejemplo si el grupo es de dos personas, se podrá colocar donde haya una o dos personas.
Cada vez que se sientan nuevos clientes se debe mostrar la mesa en la que se sientan y el
estado de las mesas (Libre u ocupada con x comensales). Si no hay sitio se deberá mostrar el
mensaje “Restaurante completo” y el estado de las mesas Los grupos no se pueden romper
aunque haya huecos sueltos suficientes. El programa terminará cuando se quiera sentar a -1
comensal. En nuestro restaurante habrá 10 mesas, pero deja preparado el programa para que
se pueda ampliar fácilmente el número de mesas.
'''


#Creo una constante para poder cambiar su valor (número de mesas) fácilmente.    
NUMERO_MESAS=10
#Creo la lista y la lleno con 10 mesas a 0 comensales
mesas=[]
for i in range (NUMERO_MESAS):
    mesas.append(0)


#===============================================================================
# Esta función muestra el estado de las mesas, es decir, imprime cada mesa diciendo
# si está libre o si está ocupada y, en este segundo caso, cuántos comensales tiene
#===============================================================================
def mostrarEstadoMesas():
    
    for i in range(len(mesas)):
        if mesas[i]==0:
            print("Mesa %s libre." % (i+1))
        else:
            print("Mesa %s ocupada con %s comensales." %((i+1), (mesas[i])))
            

        

#===============================================================================
# Esta función asignar mesa a los clientes según el número de comensales.
# Primero busca siempre si hay mesas libres (sin comensales) y, de haberla, le asigna
# esa. Si no hay mesas, libres, asigna la primera mesa que encuentre donde quepan
# el grupo de clientes juntos.
# Recibe: el número de comensales (entero positivo)
# Devuelve:
# 1. Si hay mesas libres, un mensaje con la primera mesa que esté libre.
# 2. Si no hay mesas libres, un mensaje con la primera mesa donde quepa el grupo
# de clientes.
# 3. Si no hay sitio para el grupo de clientes o no hay plazas disponibles, un
# mensaje de restaurante lleno
#===============================================================================        
def asignarMesa(numComensales):
    
    i=0
    #bandera para los bucles
    mesaLibre=False
    #Recorro la lista de mesas y compruebo si hay alguna que esté libre
    while i<len(mesas) and mesaLibre==False:
        #Si hay una mesa libre, escribo el mensaje que devuelve la funcion, 
        # sumo a esa posición de la lista
        #el número de comensales que se le añade y cambio la bandera
        if mesas[i]==0:
            mesa="Siéntense en la mesa: %s" % (i+1)
            mesas[i]+=numComensales
            mesaLibre=True
        i+=1
    
    #Si hemos llegado al final de bucle anterior con la bandera sin cambiar,
    #recorremos otra vez la lista de las mesas
    j=0  
    while j<len(mesas) and mesaLibre==False:
        #Si la suma del valor de la mesa más el número de comensales es menor o igual a 4,
        #escribo el mensaje que se devuelve, sumo a esa posición de la lista el número
        # de comensales que se le añade y cambio la bandera
        if mesas[j]+numComensales<=4:
            mesa="Siéntense en la mesa: %s" % (j+1)
            mesas[j]+=numComensales
            mesaLibre=True
        j+=1
    
    #Si hemos salido de ambos bucles sin cambiar la bandera, es que no hay sitio para
    #los comensales, por lo que devolvemos el mensaje de restaurante completo    
    if mesaLibre==False:
        mesa="Restaurante completo"
        
    return mesa
            


#===============================================================================
# Esta función es la principal del programa
#===============================================================================
def main():
    
    print("Bienvenido al restaurante.")
    
    #Pido el número de comensajes y valido datos
    numComensales=int(input("¿Cuántos comensales son (-1 para parar)? "))
    #Los datos no son correctos si el numero de comensales es mayor de 4,
    #0 o número negativo salvo el -1. En este caso, vuelvo a pedir los datos
    while numComensales==0 or numComensales>4 or numComensales<-1:
        print("Datos erróneos. Debe introducir un número entre 1 y 4, ambos incluidos.")
        numComensales=int(input("¿Cuántos comensales son (-1 para parar)? "))
    
    #Creo el bucle para que siga la ejecución salvo que el número de comensales
    #sea -1
    while numComensales!=-1:
        #Imprimo el mensaje con el resultado de la asignación de la mesa    
        print(asignarMesa(numComensales))    
        #Muestro el estado de todas las mesas
        print("\nEstado del restaurante: ")
        mostrarEstadoMesas()
        
        #Vuelvo a pedir y a validar el número de comensales
        numComensales=int(input("¿Cuántos comensales son? (-1 para parar)? "))
        while numComensales==0 or numComensales>4 or numComensales<-1:
            print("Datos erróneos. Debe introducir un número entre 1 y 4, ambos incluidos.")
            numComensales=int(input("¿Cuántos comensales son? (-1 para parar)? "))
    
    #Mensaje de despedida        
    print("Gracias. Le esperamos pronto.")
            
main()
        