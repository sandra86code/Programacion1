'''
# coding: utf-8 
 @autor: Sandra Ruiz Jiménez
 @fecha: Oct 5, 2021
 @nombre: Boletin 1 - Ejercicio 10
 @enunciado: 
 Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.
'''

#Petición y comprobación de datos
ladoA=float(input("Introduce la dimensión del primer lado: "))
while ladoA<=0:
    ladoA=float(input("Error. Introduce la dimensión del primer lado: "))
    
ladoB=float(input("Introduce la dimensión del segundo lado: "))
while ladoB<=0:
    ladoB=float(input("Error. Introduce la dimensión del segundo lado: "))
    
ladoC=float(input("Introduce la dimensión del tercer lado: "))
while ladoC<=0:
    ladoC=float(input("Error. Introduce la dimensión del tercer lado: "))

#Compruebo si es un triángulo y, si lo es, compruebo de qué tipo es
if (ladoA+ladoB)>ladoC and (ladoA+ladoC)>ladoB and ladoB+ladoC>ladoA:   
    #Compuebo si es isósceles, equilátero o escaleno
    if ladoA==ladoB and ladoA==ladoC:
        print("Es un triángulo equilátero")
    elif ladoA!=ladoB and ladoA!=ladoC:
        print("Es un triángulo escaleno")
    else:
        print("Es un triángulo isósceles")
    #Comrpuebo si es rectángulo.
    if ladoA**2 == ladoB**2 + ladoC**2 or ladoB**2 == ladoA**2 + ladoC**2 or ladoC**2 == ladoA**2 + ladoB**2:
        print("Además es rectángulo")
   
else:
    print("No es un triángulo.")