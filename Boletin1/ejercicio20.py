'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 20
 @enunciado: 
 Una persona adquirió un producto para pagar en 20 meses. 
 El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagará después de los 20 meses.
'''

#Creación de variables contadoras usadas en el bucle
precioMes=10
precioTotal=0

#Creamos el bucle con 20 iteraciones (20 meses)
for i in range(20):
    #Mostramos por pantalla el resultado del pago mensual
    print("El mes %s pagó %s €." %(i+1, precioMes))
    #Sumamos el precio mensual por cada iteración
    precioTotal+=precioMes
    #Incremento en 10 del pago mensual por cada iteración
    precioMes*=2
    

#Mostramos por pantalla el precio total a pagar
print("El precio total a pagar en 20 meses es: %s €." %(precioTotal))