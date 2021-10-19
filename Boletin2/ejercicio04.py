"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 4  
 @enunciado: 
Design a program that reads a positive number N greater than 0 and show the result
of the sum of the N numbers between 1 and N. 
If the number N is not valid, the program should ask for it again. 
The messages are the following:
"Enter one number greater than 0:"
"The number is not right, try again."
"The sum of the N first numbers is XX."
 """

#Pedimos los datos 
num=int(input("Introduce un número mayor que 0: "))
#Si los datos no son correctos, los volvemos a pedir
while num<=0:
    print("El número no es correcto, inténtalo de nuevo.")
    num=int(input("Introduce un número mayor que 0: "))

#Declaración de variable sumatoria para usarla en el bucle
suma=0
#Bucle for que con intervalo [1,num]
for i in range(1,num+1):
    #En cada iteración, sumamos el valor de i a la variable suma
    suma+=i

#Mostramos por consola el resultado    
print("La suma de los %s primeros números es %s." %(num, suma))
    