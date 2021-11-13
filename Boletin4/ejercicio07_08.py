'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 8, 2021
 @nombre: Boletin 4 - Ejercicio 7
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


'''
Esta función calcula si un año es bisiesto o no 
Recibe un año
Devuelve:
False si no es bisiesto
True si es bisiesto
'''
def esBisiesto(year):
    bisiesto=False
    if year%4==0 or (year%100==0 and year%400==0):
        bisiesto=True

    return bisiesto

'''
Esta función calcula cuántos días hay en un mes, teniendo en cuenta si el año es bisiesto o no 
Recibe un mes y un año (variables de tipo entero)
Devuelve:
Los días que tiene el mes, teniendo en cuenta si el año es bisiesto o no
'''
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

'''
Esta función calcula el día juliano (días transcurridos desde el 1 de enero hasta la fecha) 
Recibe un día, un mes y un año (3 variables de tipo entero)
Devuelve:
El día juliano
'''        
def calcularDiaJuliano (dia,mes,year):
    diaJuliano=0
    for i in range(1, mes):
        diaJuliano+=diasDelMes(i, year)
    
    diaJuliano=diaJuliano+dia
    
    return diaJuliano

'''
Esta función valida si una fecha es correcta, ya sea porque el día, el mes o el año no es correcto. 
Recibe un día, un mes y un año (3 variables de tipo entero)
Devuelve:
True si la fecha es válida
False si la fecha no es válida
'''       
def validaFecha(dia, mes, year):
    
    return dia>0 and dia<=diasDelMes(mes, year) and mes>0 and mes<=12 and year>0


'''
Esta función lee una fecha e imprime el resultado del día juliano de esa fecha
Recibe: no tiene parámetros
Devuelve: no tiene return
'''                
def leerFecha():
    #Pido datos
    dia=int(input("Introduce el día del mes: "))
    mes=int(input("Introduce el mes del año: "))
    year=int(input("Introduce el año: "))
    #Mientras que los datos no sean válidos (llamada a la función que los valida),
    #vuelve a pedirlos
    while validaFecha(dia,mes,year)==False:
        print("Datos incorrectos.")
        dia=int(input("Introduce el día del mes: "))
        mes=int(input("Introduce el mes del año: "))
        year=int(input("Introduce el año: "))
    
    #Imprimo en resultado del año juliano por consola
    print("El día juliano es %s" %(calcularDiaJuliano(dia, mes, year)))

#Llamo a la función principal, ya que no tiene return     
leerFecha()

