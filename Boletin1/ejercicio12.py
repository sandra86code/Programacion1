'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 12
 @enunciado: 
 La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. 
Cuando se realiza la venta del producto, esta es de un solo tipo y tamaño, se requiere determinar 
cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: 
- si es de tipo A,se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; 
y 30 céntimos si es de tamaño 2. 
- Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. 
Realice un algoritmo para determinar la ganancia obtenida.
'''

#Petición y comprobación de datos de entrada
tipo=input("¿Qué tipo de uva vende (A/B)? " )
while tipo not in {"A", "B"}:
    tipo=input("Error. ¿Qué tipo de uva vende (A/B)? " )
    
size=input("¿Qué tamaño tiene la uva (1/2)? ")
while size not in {"1", "2"}:
    size=input("Error. ¿Qué tamaño tiene la uva (1/2)? ")

numKg=float(input("Introduzca el número de kilos: "))
while numKg<=0:
    numKg=float(input("Error. Introduzca el número de kilos: "))
    
#Cálculo de la ganancia por kilo    
if tipo=="A":
    if size=="1":
        gananciaKg=0.2
    else:
        gananciaKg=0.3
else:
    if size=="1":
        gananciaKg=-0.3
    else:
        gananciaKg=-0.5

#Cálculo de la ganancia total
gananciaTotal=gananciaKg*numKg

#Impresión de datos por consola
print("La ganancia total es de %s €." %(gananciaTotal))
