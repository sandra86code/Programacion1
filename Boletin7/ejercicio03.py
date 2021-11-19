'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Ejercicios del año pasado - Ejercicio 3
 @enunciado: 
Realizar un programa que solicite la fecha como tres datos numéricos 
(día, mes y año). 
Deberá mostrar la fecha en formato largo.
    Introduce el día de la fecha: 15
    Introduce el mes de la fecha: 3
    Introduce el año de la fecha: 2009
    La fecha en formato largo es 15 de Marzo de 2009
Si la fecha introducida es incorrecta se mostrará un mensaje de error: 
“Fecha incorrecta” y el programa terminará. 
El programa terminará cuando se introduzca un día negativo.
'''

#===============================================================================
# Esta función comprueba si un año es bisiesto o no
# Recibe: un año
# Devuelve:
# True si el año es bisiesto, False de lo contrario
#===============================================================================
def isLeapYear(year):
    leapYear=False
    if year%4==0 or (year%100==0 and year%400==0):
        leapYear=True
    
    return leapYear


#===============================================================================
# Esta función comprueba cuántos días tiene un mes, teniendo en cuenta los años bisiestos
# Recibe: un mes y un año
# Devuelve:
# 31 para los meses de 31 días
# 30 para los meses de 30 días
# 28 para febrero de los años no bisiestos
# 29 para febrero de los años bisiestos
#===============================================================================
def daysInMonth(month, year):
    
    if month in {4,6,9,11}:
        days=30
    elif month==2:
        if isLeapYear(year):
            days=29
        else:
            days=28
    else:
        days=31
        
    return days


#===============================================================================
# Esta función comprueba que una fecha (día, mes y año) es correcta o no
# Recibe: un día, un mes y un año
# Devuelve:
# True si la fecha es correcta, False de lo contrario.
#===============================================================================
def compruebaFecha(day,month,year):
    isCorrecta=False
    #Si el día es mayor de 0 y menor o igual de lo que nos devuelva la función daysInMonth
    #y el mes sea mayor de 0 y menor o igual que 12, la fecha es correcta
    if day>0 and day<=daysInMonth(month, year) and month>0 and month<=12:
        isCorrecta=True
        
    return isCorrecta


#===============================================================================
# Esta función convierte la fecha a formato largo (dd de mm de yyyy)
# Recibe: un día, un mes y un año
# Devuelve: la fecha en formato largo
#===============================================================================
def fechaLarga(day, month, year):
    #Creo una lista con los meses del año, para luego acceder a ella por su posición-1
    meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    fecha="%s de %s de %s" % (day, meses[month-1], year) 
    
    return fecha


#===============================================================================
# Esta función es el menú principal del programa 
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
# Si la fecha es correcta, imprime la fecha en formato largo
# Si la fecha es incorrecta, muestra un mensaje de fecha incorrecta.
# El programa se para si el día introducido es -1.
#===============================================================================
def menu():
    dia=int(input("Introduce el día de la fecha: "))
    while dia!=-1:
    
        mes=int(input("Introduce el mes de la fecha: "))
        anyo=int(input("Introduce el año de la fecha: "))
        
        if compruebaFecha(dia,mes,anyo):
            print(fechaLarga(dia, mes, anyo))
        else:
            print("Fecha incorrecta.")
        
        dia=int(input("Introduce el día de la fecha: "))
        
#Llamada a la función, ya que no tiene return    
menu()