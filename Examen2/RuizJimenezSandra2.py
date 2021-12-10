'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 10, 2021
 @nombre: Examen 10 Diciembre - Ejercicio 2
 @enunciado: 
 Un restaurante te ha encargado una aplicación para colocar a los clientes en sus mesas. En
una mesa se pueden sentar de 0 (mesa vacía) a 4 comensales (mesa llena). Cuando llega un
cliente se le pregunta cuántos son (dando un mensaje de error si el número de clientes es
superior a 4). Para el grupo que llega, se busca siempre la primera mesa libre (con 0
personas). Si no quedan mesas libres, se busca donde haya un hueco para todo el grupo, por
ejemplo si el grupo es de dos personas, se podrá colocar donde haya una o dos personas.
Cada vez que se sientan nuevos clientes se debe mostrar la mesa en la que se sientan y el
estado de las mesas (Libre u ocupada con x comensales). Si no hay sitio se deberá mostrar el
mensaje “Restaurante completo” y el estado de las mesas Los grupos no se pueden romper
aunque haya huecos sueltos suficientes. El programa terminará cuando se quiera sentar a -1
comensal. En nuestro restaurante habrá 10 mesas, pero deja preparado el programa para que
se pueda ampliar fácilmente el número de mesas.
'''