"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 2 - Ejercicio 11 (propuesto en clase
 @enunciado: 
 Haz un programa que pida 3 números comprendidos entre el 10 y el 100 
 y nos escriba la media de esos tres números. 
 Si da un valor que no esté entre 10 y 100, tiene que volver a preguntar el dato.
 """

#Creo la variable sumatoria para calcular la suma de los 3 números
suma=0
#Creo un bucle que tenga 3 iteraciones
for i in range (3):
    #Pido el número
    num=int(input("Dime un número comprendido entre 10 y 100: "))
    #Si el número no es correcto, lo vuelvo a pedir
    while num<10 or num>100:
        print("Datos incorrectos. Vuelve a intentarlo")
        num=int(input("Dime un número comprendido entre 10 y 100: "))
    #En cada iteración sumo el número
    suma+=num

#Una vez hechas las 3 iteraciones, calculo la media
media=suma/3

#Muestro por consola el resultado
print("La media de los números es %s" %(media))