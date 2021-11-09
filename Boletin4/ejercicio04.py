'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: 
 Crear una funcion llamada “Login”, que recibe un nombre de usuario y una contraseña y te
devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
Crear un programa donde se pida un nombre de usuario y una contraseña y se intente hacer
login, solamente tenemos tres oportunidades para intentarlo.
'''

'''
Esta función calcula si el login de un usuario es correcto o no
Recibe el nombre y la contraseña del usuario (dos variables de tipo cadena)
Devuelve:
True si el login es correcto (nombre="usuario1" y password="asdasd").
False si el login no es correcto.
'''
def login (nombre, password):
    if nombre=="usuario1" and password=="asdasd":
        respuesta=True
    else:
        respuesta=False
    
    return respuesta


'''
Esta función pide los datos del nombre y la contraseña al usuario.
Recibe: No recibe parámetros
Devuelve: No tiene return
Imprime "Login correcto" si el nombre y la contraseña son correctas.
Imprime "Login incorrecto" si el nombre y/o la contraseña son incorrectas. 
En este caso, permite 3 intentos. Si ningún intento es correcto, imprime
el mensaje "Has agotado tus 3 intentos".

'''
def pideDatos():
    #Variable iteradora
    i=0
    #Bandera si el login no es correcto
    loguear=False
    #Bucle while que se puede repetir hasta 3 veces, siempre que la bandera no cambie
    while i<3 and loguear==False:
        #Pedir datos
        nombre=input("Introduce tu nombre de usuario: ")
        password=input("Introduce tu contraseña: ")
        #Si el login es correcto (llamada a la otra función), cambio bandera (freno bucle)
        #e imprimo mensaje de login correcto
        if login(nombre, password)==True:
            loguear=True
            print("Login correcto.")
        #De lo contrario, aumento el valor de i para la siguiente iteración e imprimo
        #login incorrecto.
        else:
            i+=1
            print("Login incorrecto.")
    #Si al terminar el bucle while, la bandera no ha cambiado, imprime mensaje de
    #que se han agotado los intentos posibles de logueo.        
    if loguear==False:
        print("Has agotado tus 3 intentos.")

#Llamada de la función, ya que no tiene return.        
pideDatos()