'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 8
 @enunciado: 
 Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
'''

from math import trunc

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
    
#Calcular total
totalEuros=(monedasDosEuros*2) + monedasEuro + (monedas50Cent*0.5) + (monedas20Cent*0.2) + (monedas10Cent*0.1)

#Mostramos los resultados por consola
parteEntera=trunc(totalEuros)
totalCentimos=(totalEuros-parteEntera)*100
print("La cantidad introducida corresponde con %s € y %s céntimos." %(trunc(parteEntera), trunc(totalCentimos)))
      
      
'''

#Solución con listas
 
#Declaración listas
listaMonedas=["2 €", "1 €", "50 céntimos", "20 céntimos", "10 céntimos"]
 
valorEnEuros=[2,1,0.5,0.2,0.1]
 
#Recorremos listas con bucle y declaramos variable contadora de la suma
valorTotal=0
for i in range (len(listaMonedas)):
    cantidadMoneda=int(input("Indroduce la cantidad de monedas de "+ str(listaMonedas[i]) + ": "))
    #Comprobamos datos
    while cantidadMoneda<0:
        cantidadMoneda=int(input("Error. Indroduce la cantidad de monedas de "+ str(listaMonedas[i]) + ": "))
     
    valorTotal+=cantidadMoneda*valorEnEuros[i]
     
 
#Mostramos los resultados por consola
print("La cantidad introducida corresponde con %s €" %(round(valorTotal,2)))

'''