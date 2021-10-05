'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 8
 @enunciado: 
 Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
'''

#Pedir datos y comprobar que sean correctos
monedasDosEuros=int(input("Introduzca la cantidad de monedas de 2€: "))
while monedasDosEuros<0:
    monedasDosEuros=int(input("Introduzca la cantidad de monedas de 2€: "))

monedasEuro=int(input("Introduzca la cantidad de monedas de 1€: "))
while monedasEuro<0:
    monedasEuro=int(input("Introduzca la cantidad de monedas de 1€: "))
    
monedas50Cent=int(input("Introduzca la cantidad de monedas de 50 cent: "))
while monedas50Cent<0:
    monedas50Cent=int(input("Introduzca la cantidad de monedas de 50 cent: "))
    
monedas20Cent=int(input("Introduzca la cantidad de monedas de 20 cent: "))
while monedas20Cent<0:
    monedas20Cent=int(input("Introduzca la cantidad de monedas de 20 cent: "))
    
monedas10Cent=int(input("Introduzca la cantidad de monedas de 10 cent: "))
while monedas10Cent<0:
    monedas10Cent=int(input("Introduzca la cantidad de monedas de 10 cent: "))
    
#Calcular total de céntimos
totalCentimos=(monedasDosEuros*200) + (monedasEuro*100) + (monedas50Cent*50) + (monedas20Cent*20) + (monedas10Cent*10)

#Calculamos los euros y los céntimos
euros=totalCentimos//100
centimos=totalCentimos%100

#Mostramos los resultados por consola
print("La cantidad introducida corresponde con %s € con %s céntimos." %(euros, centimos))
