'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 4
 @enunciado: 
 Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra.
'''

#Petición de datos y comprobación
totalCompra=float(input("Introduzca el total de su compra: "))
while totalCompra<=0:
    totalCompra=float(input("Error. Introduzca el total de su compra: "))
    
#Declaración de la constante del descuento
DESCUENTO = 0.85

#Cálculo del total una vez aplicado el descuento + salida de datos por consola
print("El precio total una vez aplicado el descuento es " + str(totalCompra*DESCUENTO) + " €")