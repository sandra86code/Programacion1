'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 29, 2021
 @nombre: Examen 1  - Ejercicio 01
 @enunciado: 
 1.- Realiza un programa que le pida al usuario su edad y que le pregunte si 
 ha pasado el Covid o no, así como si ha recibido la vacuna de Pfizer, Moderna 
 o Astrazeneca. 
 En función de la respuesta se debe informar al usuario si debe 
 volver a vacunarse o no teniendo en cuenta las siguientes condiciones:
• Si ha recibido Astrazeneca, haya pasado el covid o no e independientemente 
de la edad debe volver a vacunarse.
• Si ha recibido Moderna y es mayor de 60 años, sólo debe volver a vacunarse si 
no ha pasado el covid. En otro caso, lo que han recibido Moderna no deben volver 
a vacunarse.
• Si ha recibido Pfizer y no ha pasado el covid, debe volver a vacunarse, y si lo 
ha pasado sólo se vacunará si es mayor de 70 años.
Si el usuario no introduce los valores correctos, se debe mostrar un mensaje de 
error y volver a solicitar los datos hasta que el usuario introduzca los datos 
de forma correcta.
'''

#Pido los datos de la edad y lo guardo en una variable de tipo entero.
#Si los datos son incorrectos (0 o negativo), vuelvo a pedirlos
edad=int(input("Introduce tu edad: "))
while edad<=0:
    print("Datos incorrectos. Vuelve a intentarlo.")
    edad=int(input("Introduce tu edad: "))
#Pido los datos de si ha pasado el covid y lo guardo en una variable de tipo string.  
#Si los datos son incorrectos, vuelvo a pedirlos  
covid=input("¿Has pasado el covid? (S/N): ")
while covid not in {"S", "N"}:
    print("Datos incorrectos. Vuelve a intentarlo.")
    covid=input("¿Ha pasado el covid? (S/N): ")
#Pido los datos de la vacuna y lo guardo en una variable de tipo string.
#Si los datos son incorrectos, vuelvo a pedirl(os
vacuna=input("¿Con qué vacuna te has vacunado? (Pfizer/Moderna/Astrazeneca): ")
while vacuna not in {"Pfizer", "Moderna", "Astrazeneca"}:
    print("Datos incorrectos. Vuelve a intentarlo.")
    vacuna=input("¿Con qué vacuna se ha vacunado? (Pfizer/Moderna/Astrazeneca): ")
    
#Creo la estructura condicional con las condiciones que me indica el programa.
if vacuna=="Astrazeneca":
    mensaje="Debes volver a vacunarte."
elif vacuna=="Moderna" and edad>60 and covid=="N":
    mensaje="Debes volver a vacunarte."
elif vacuna=="Pfizer" and (covid=="N" or (covid=="S" and edad>70)):
    mensaje="Debes volver a vacunarte."
else:
    mensaje="No debes volver a vacunarte."

#Muestro el mensaje por consola    
print(mensaje)

