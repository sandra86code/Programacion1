'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: 
 El día juliano correspondiente a una fecha es un número entero que indica los días que han
transcurrido desde el 1 de enero del año indicado. 
Queremos crear un programa que al introducir una fecha nos diga el día juliano que corresponde. 
Para ello podemos hacer las siguientes funciones:
◦ LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
◦ DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
◦ EsBisiesto: Recibe un año y nos dice si es bisiesto.
◦ Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
'''

'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 8  
 @enunciado: 
 Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. 
 De tal forma que al leer una fecha se asegura que es válida.
'''



def esBisiesto(year):
    bisiesto=False
    if year%4==0 or (year%100==0 and year%400==0):
        bisiesto=True

    return bisiesto

def diasDelMes(mes, year):
    if mes in {1,3,5,7,8,10,12}:
        dias=31
    elif mes in {4,6,9,11}:
        dias=30
    else:
        if esBisiesto(year)==True:
            dias=29
        else:
            dias=28
    
    return dias

        
def calcularDiaJuliano (dia,mes,year):
    diaJuliano=0
    for i in range(1, mes):
        diaJuliano+=diasDelMes(i, year)
    
    diaJuliano=diaJuliano+dia
    
    return diaJuliano

       
def validaFecha(dia, mes, year):
    
    return dia>0 and dia<=diasDelMes(mes, year) and mes>0 and mes<=12 and year>0

                
def leerFecha():
    
    dia=int(input("Introduce el día del mes: "))
    mes=int(input("Introduce el mes del año: "))
    year=int(input("Introduce el año: "))
    
    while validaFecha(dia,mes,year)==False:
        print("Datos incorrectos.")
        dia=int(input("Introduce el día del mes: "))
        mes=int(input("Introduce el mes del año: "))
        year=int(input("Introduce el año: "))
    
    print("El día juliano es %s" %(calcularDiaJuliano(dia, mes, year)))
     
leerFecha()







        
        