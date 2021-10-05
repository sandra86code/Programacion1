'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 9 
 @enunciado: 
 Vamos a hacer un programa que nos pregunte el precio de un producto y el dinero que va a 
 entregar para pagar el producto y nos devuelva la vuelta. Si no nos da suficiente dinero, 
 tendremos que decirle que no puede pagar con eso.

'''

precio = float(input("¿Cuál es el precio del producto? "))
while precio < 0:
    precio = float(input("¿Cuál es el precio del producto? "))

pago = float(input("¿Cuánto dinero entrega? "))
while pago < 0:
    pago = float(input("¿Cuánto dinero entrega? "))

if precio <= pago:
    print("Su vuelta es de "+str(pago-precio)+" €.")
else:
    print("El dinero entregado es inferior al precio del producto")