'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Examen año 2020/2021 - Ejercicio 2
 @enunciado: 
 En el gimnasio Jacafitness, para el que ya hemos trabajado,nos piden
 que realicemos un programa para determinar si deberías acuidr al médico
 para que te haga una revisión, para ello debemos hacer las siguientes
 preguntas:
 - ¿Peso?
 - ¿Edad?
 - ¿Tipo de vida? (Sedentaria/Activa/Muy activa)
 
 El programa terminará si se introduce un peso negativo.
 Se deben comprobar que los datos son correctos y si no lo son, se deben
 volver a preguntar.
 
 Las recomendaciones para ir al médico son:
 - Si tienes más de 70 años y llevas una vida Sedentaria.
 - Si pesa más de 100 kg, sea cual sea la edad.
 - Si pesa más de 74,4 kg y tiene más de 50 años.
 
 En cualquier otro caso se mostrará "No es urgente que acuda al médico si
 no tiene problemas de salud".
'''

#Pido los datos y, si no son correctos, los vuelvo a pedir
peso=float(input("Introduce tu peso en kilos: "))
while peso<=0:
    print("Datos incorrectos. Vuelve a intentarlo.")
    peso=float(input("Introduce tu peso en kilos: "))
    
edad=int(input("Introduce tu edad: "))
while edad<=0:
    print("Datos incorrectos. Vuelve a intentarlo.")
    edad=int(input("Introduce tu edad: "))
    
tipoVida=input("¿Tipo de vida? (Sedentaria/Activa/Muy activa): ")
while tipoVida not in {"Sedentaria", "Activa", "Muy activa"}:
    print("Datos incorrectos. Vuelve a intentarlo.")
    tipoVida=input("¿Tipo de vida? (Sedentaria/Activa/Muy activa): ")

#Creo una estructura en la que de darse alguna de las 3 condiciones del if,
#se guarda un mensaje. En todos los demás casos, se guarda el otro mensaje.    
if peso>100 or (edad>70 and tipoVida=="Sedentaria") or (peso>74.4 and edad>50):
    mensaje="Debería acudir al médico a una revisión."
else: 
    mensaje="No es urgente que acuda al médico si no tiene problemas de salud."

#Imprimo la variable mensaje
print(mensaje)
