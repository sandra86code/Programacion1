'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 14
 @enunciado: 
 La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que esta dura, de tal forma que:
- los primeros cinco minutos cuestan 1 euro,
- los siguientes tres, 80 céntimos,
- los siguientes dos minutos, 70 céntimos, 
- y a partir del décimo minuto, 50 céntimos. 
Además, se carga un impuesto de:
- 3 % cuando es domingo, 
- y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
'''

#Petición y comprobación de datos
duracionLlamada=int(input("¿Cuántos minutos ha durado la llamada? "))
while duracionLlamada<=0:
    duracionLlamada=int(input("Error. ¿Cuántos minutos ha durado la llamada? "))

dia=input("Introduce el día de la semana en el que ha realizado la llamada (L,M,X,J,V,S,D): ")
while dia not in {"L", "M", "X", "J", "V", "S", "D"}:
    dia=input("Error. Introduce el día de la semana en el que ha realizado la llamada (L,M,X,J,V,S,D): ")

turno=input("Introduce el turno en el que se ha realizado la llamada (mañana/tarde): ")
while turno not in {"mañana", "tarde"}:
    turno=input("Error. Introduce el turno en el que se ha realizado la llamada (mañana/tarde): ")



#Cálculo del importe de la llamada por tiempo

#Declaro lista de precios de minutos 
precioPorMinuto=[1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 0.8, 0.8, 0.7, 0.7]

importeTotal=0
if duracionLlamada<=10:
    #Bucle para asociar minutos a la lista de precios por posición
    for i in range(duracionLlamada):
        importeTotal+=precioPorMinuto[i]
else:
    #Calculo la suma total de los 10 primeros minutos
    sumaPrimerosMinutos=0
    for i in range(len(precioPorMinuto)):
        sumaPrimerosMinutos+=precioPorMinuto[i]
    #Calculo minutos que tienen asociados un precio invariable de 0.5
    minutosRestantes=duracionLlamada-10
    #Cálculo de precio total
    importeTotal=round(sumaPrimerosMinutos,2) + (minutosRestantes*0.5)

#Cálculo del impuesto por días
if dia=="D":
    impuesto=importeTotal*0.03
else:
    #Cálculo del impuesto por turnos
    if turno=="mañana":
        impuesto=importeTotal*0.15
    else:
        impuesto=importeTotal*0.10

#Mostrar resultados por consola
print("La llamada tiene un coste de %s € con un impuesto de %s €, lo que hace un total de %s €." 
      %(round(importeTotal,2), round(impuesto,2), round(importeTotal+impuesto, 2)))