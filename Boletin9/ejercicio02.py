'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 3, 2021
 @nombre: Simulacro Examen - Ejercicio 2 
 @enunciado: 
 El índice de masa corporal o IMC es una medida que se utiliza para evaluar el riesgo de enfermedad
cardiovascular. 
Para su cálculo se divide el peso en kilogramos por la altura en metros elevados al cuadrado, de forma 
que un peso normal o normopeso estaría situado en un valor de IMC entre 18,5 y 24,9.
Crea un programa que pida la altura, peso y edad de una persona y calcule e informe del valor y tipo
de IMC obtenido atendiendo al siguiente criterio:
<18,5
18,5-24,9
25-29,9
30-39,9
>40
Peso insuficiente
Normopeso
Sobrepeso
Obesidad
Obesidad mórbida
Además de facilitar el IMD, debe proporcionar un mensaje de recomendación sanitaria si la edad de
la persona es superior a 45 y excede el normopeso (IMC >25), o bien, si ésta tiene obesidad (IMC
>30). Por ejemplo:
Para un peso de 90 kilogramos y una talla de 1.80 metros, su IMC es: 27.78
Usted se encuentra en el grupo: Sobrepeso.
Caso 1 - Dada su edad e IMC es recomendable que cuide su salud cardiovascular
Caso 2 - Dado su IMC es muy recomendable que cuide su salud cardiovascular
Este programa debe validar la información proporcionada y terminar cuando se introduzca un valor
negativo en cualquier medida (edad, peso o tamaño).
'''

def calculoRecomendaciones(edad, altura, peso):
    
    imc=calcularIMC(peso, altura)
    
    mensaje="Usted se encuentra en el grupo: "
    if imc<18.5:
        mensaje+="Peso insuficiente."
    elif imc<25:
        mensaje+="Normopeso"
    elif imc<30:
        mensaje+="Sobrepeso"
        if edad>45:
            mensaje+="\nDada su edad e IMC es recomendable que cuide su salud cardiovascular"
    elif imc<40:
        mensaje+="Obesidad"
        if edad>45:
            mensaje+="\nDada su edad e IMC es recomendable que cuide su salud cardiovascular"
        else:
            mensaje+="\nDado su IMC es recomendable que cuide su salud cardiovascular"
    else:
        mensaje+="Obesidad mórbida"
        if edad>45:
            mensaje+="\nDada su edad e IMC es recomendable que cuide su salud cardiovascular"
        else:
            mensaje+="\nDado su IMC es recomendable que cuide su salud cardiovascular"

    return mensaje




def calcularIMC(peso,altura):
    
    return round(peso/(altura**2),1)
    
    

def pedirDatos():
    edad=int(input("Introduce la edad: "))
    while edad<0:
        print("Datos erróneos.")
        edad=int(input("Introduce la edad: "))
    altura=float(input("Introduce la altura (en m): "))
    while altura<0:
        print("Datos erróneos.")
        altura=float(input("Introduce la altura (en m): "))
    peso=float(input("Introduce el peso (en kg): "))
    while peso<0:
        print("Datos erróneos.")
        peso=float(input("Introduce el peso (en kg): "))
    
    
    
    while altura>0 and edad>0 and peso>0:
        calculoRecomendaciones(edad, altura, peso)
        
        edad=int(input("Introduce la edad: "))
        altura=float(input("Introduce la altura (en m): "))
        peso=float(input("Introduce el peso (en kg): "))
        
    mensaje="Programa finalizado."
        
pedirDatos()
