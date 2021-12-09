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

#===============================================================================
# Esta función calcula la bonificación que debe recibir un empleado según el número
# de días que ha terminado por adelantado su trabajo
# Recibe: el número de días (entero positivo)
# Devuelve: la bonificación (entero positivo)
# 
#===============================================================================
def calcularBonificacion(dias):
    
    diasRestantes=dias
    
    if dias<33:
        bonificacion = dias*5
    elif dias<41:
        diasRestantes-=32
        bonificacion = 32*5 + diasRestantes*10
    elif dias<50:
        diasRestantes-=40
        bonificacion = 32*5 + 8*10 + diasRestantes*20
    else:
        diasRestantes-=49
        bonificacion = 32*5 + 8*10 + 9*20 + diasRestantes*30

    return bonificacion


#===============================================================================
# Esta función es la principal del programa
# Recibe 
# Devuelve:
# 
#===============================================================================
def main():
    
    #Pido los datos y los valido
    empleado=input("Introduce el nombre del empleado: ")
    dias=int(input("Introduce el número de días terminados antes de fecha: "))
    while dias<0:
        print("Datos incorrectos. Debe introducir un valor mayor o igual que 0.")
        dias=int(input("Introduce el número de días terminados antes de fecha: "))
    
    #Imprimo la bonificación del empleado para ese número de días
    print("El empleado %s debe recibir %s euros, por %s días trabajados de menos en el proyecto." % (empleado, calcularBonificacion(dias), dias))
    

main()