'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 0 - Ejercicio 18
 @enunciado: 
 Pedir dos números 'nota' y 'edad', y un caracter 'sexo' y mostramos el mensaje 'ACEPTADA' 
 si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es 'F'. 
 En caso de que se cumpla lo mismo, pero el sexo sea 'M', mostramos 'POSIBLE'. 
 Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
'''

edad = int(input("Introduce la edad: "))
while edad<=0 and edad>80:
    print("DATOS ERRÓNEOS")
    edad = int(input("Introduce la edad: "))
    
nota = int(input("Introduce la nota: "))
while nota<0 or nota>10:
    print("DATOS ERRÓNEOS")
    nota = int(input("Introduce la nota: "))
    
sexo = input("Introduce el sexo (F/M): ")
while sexo not in {"F", "f", "M", "m"}:
    print("DATOS ERRÓNEOS")
    sexo = input("Introduce el sexo (F/M): ")
    
if edad>=18 and nota>=5:
    if sexo in {"F", "f"} :
        print("ACEPTADA")
    else:
        print("POSIBLE")
else:
    print("NO ACEPTADA")