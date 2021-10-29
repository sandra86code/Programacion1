'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 29, 2021
 @nombre: Examen 1  - Ejercicio 03
 @enunciado: 
 3.- Vamos a escribir un programa para codificar una clave que el usuario deberá introducir por
teclado, así, cuando sepamos escribir en ficheros, en vez de guardar la clave guardaremos la
codificación, aunque por ahora lo que haremos es escribirla por pantalla.
La generación de la clave se hará en función de la seguridad que quiera el usuario por lo que lo
primero que debemos hacer es pedirle cuántos números quiere introducir para generar la clave. A
continuación se le deberán preguntar los números y la clave se generará sumando el resto de dividirlos 
números entre 5, siempre y cuando los números sean impares. Aunque se introduzcan números
negativos se debe sumar el resto nunca restar.

'''

#Pido la cantidad de números a introducir por el usuario y, si los datos son incorrectos
#(cantidad negativa o 0), los vuelvo a pedir
cantidadNum=int(input("¿Cuántos números quiere introducir? "))
while cantidadNum<=0:
    print("Datos incorrectos.")
    cantidadNum=int(input("¿Cuántos números quiere introducir? "))

#Creo la variable sumatoria clave, por lo que la inicializo a 0
clave=0

#Creo un bucle para iterar el número de veces que el usuario haya introducido
for i in range (cantidadNum):
    #Pido los datos del número
    num=int(input("Introduce el número %s: " %(i+1)))
    #Si el número es negativo, le cambio el signo
    if num<0:
        num*=-1
    #Calculo el resto del dividir el número (ya siempre positivo, sea porque lo hemos introducido
    #así o al negativo lo hayamos cambiado de signo) entre 5 y lo guardo en la variable resto
    resto=num%5
    #Si el resto es impar y es diferente de 0, sumo el resto a la variable sumatoria clave
    if resto%2!=0 and resto!=0:
        clave+=resto

#Muestro por consola la clave
print("El resultado de la clave es %s" %(clave))