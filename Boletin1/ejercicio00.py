"""
 @autor: Sandra Ruiz Jim�nez
 @fecha: Oct 5, 2021
 @nombre: Ejercicio 0
 @enunciado: Primer programa que pregunta el nombre del usuario 
y lo saluda.
Luego mostrar� el mensaje al nombre pidi�ndole dos 
n�meros y los sumar� y los restar�.
 """


nombre = input("Dime tu nombre: ")

#print("Hola %s" %(nombre))
print("Hola " + nombre)

num1 = int(input(nombre + ", dime un n�mero: "))
num2 = int(input(nombre + ", dime otro n�mero: "))

suma=num1+num2
resta=num1-num2

print("La suma de %s + %s es %s y la resta, %s." %(num1, num2, suma, resta))