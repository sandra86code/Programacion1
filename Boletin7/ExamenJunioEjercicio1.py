'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen Recuperación Python Junio 2021 - Ejercicio 1
 @enunciado: 
 Una institución financiera proporciona servicios profesionales a los bancos y factura a sus
clientes por un precio fijo por trabajo, por lo que le interesa que sus empleados finalicen las tareas
lo antes posible. 
La empresa ha establecido un plan para motivar y recompensar al personal para
que intenten terminar lo antes posible mediante una bonificación por cada día que terminen antes de
la fecha objetivo del trabajo.
El esquema de bonificación es el siguiente:

Días terminados antes de fecha                 Bonificación
0 a 32 días antes                              5 euros por cada día
33 a 40 días antes                             10 euros por cada día
41 a 49 días antes                             20 euros por cada día
Más de 49 días antes                           30 euros por cada día

Hay que tener en cuenta que el pago de incentivos se calcula progresivamente. Por ejemplo, si
un empleado finaliza 45 días antes, su pago de incentivo se calcula de la siguiente manera:

32*5 + 8*10 + 5*20 = 340 euros

Realizar un programa que solicite el nombre del empleado y el número de días que ha terminado
antes y muestre el siguiente mensaje:
"El empleado <nombre del empleado> debe recibir <bonificacion> euros, por <días>
trabajados de menos en el proyecto"
'''

def calcularBonificacion(dias):
    diasRestantes=dias
    bonificacion=0
    if dias>=50:
        diasRestantes=dias-50
        bonificacion+=diasRestantes*30
    if dias>=41:
        diasRestantes-=8
        bonificacion+=diasRestantes*20
    if dias>=33:
        
        bonificacion+=diasRestantes*10
    if dias>=1:
        diasRestantes-=32
        bonificacion+=dias*5


    
        
    return bonificacion


def main():
    empleado=input("Introduce el nombre del empleado: ")
    dias=int(input("Introduce el número de días terminados antes de fecha: "))
    while dias<0:
        print("Datos incorrectos. Debe introducir un valor mayor o igual que 0.")
        dias=int(input("Introduce el número de días terminados antes de fecha: "))
        
    bonificacion=calcularBonificacion(dias)
    print("El empleado %s debe recibir %s euros, por %s días trabajados de menos en el proyecto." % (empleado, bonificacion, dias))
    

main()