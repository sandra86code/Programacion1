"""
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 19, 2021
 @nombre: Boletin 2 - Ejercicio 10  
 @enunciado: 
Design a program that reads an integer positive number and says the "factorial" of
the number. 
To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= 1 * 2 * 3 * 4 * ... * N

Ejemplo: 5! = 1 * 2 * 3 * 4 * 5 = 120

The messages are the following:
"Enter an integer positive number:"
"The number is not valid, try again."
"The factorial is XX."
 """
 
#Pido los datos
num=int(input("Introduce un número entero positivo: "))
#Si los datos son erróneos, muestro mensaje de error y vuelvo a pedir los datos
while num<0:
    print("El número no es válido, inténtalo de nuevo.")
    num=int(input("Introduce un número entero positivo: "))
    
#Declaro variable para usarla en el bucle for posterior.
#Como la voy a usar en multiplicación, se inicializa a 1.
factorial=1
#Bucle for con rango [1,num]
for i in range(1, num+1):
    #Con cada iteración del bucle, multiplico la i al factorial
    factorial*= i

#Muestro el resultado por consola
print("El factorial es %s." %(factorial))