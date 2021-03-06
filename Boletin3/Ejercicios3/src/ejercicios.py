"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 1
 @enunciado: 
 Design a method called factorial that receives a positive integer and returns 
 the factorial. 
 If the number is negative the method should return -1.    
 """


'''
Esta función calcula el factorial de un número 
Recibe un número entero
Devuelve:
-1 si el número es negativo
El factorial si el número es positivo
'''
def factorial(num):
    #Iniciamos la variable resultado a 1 porque vamos a usarla para multiplicar.
    #Además es el resultado del número 0, que no entrará en la estructura condicional posterior
    resultado=1
    #Estructura condicional si el número (parámetro de entrada) es menor o mayor que 0
    if num<0:
        resultado=-1
    elif num>0:
        #Bucle que va [1, num]
        for i in range (1, num+1):
            #Con cada iteración se multiplica i al resultado
            resultado*=i
     
    return resultado


"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 2
 @enunciado: 
 Design a method called leapYear that returns 1 if the number that receives the 
 method is a leap year. In other case, the method returns -1. 
 A year is a leap year if it is multiple of 4 but the year is not multiple of 100 
 and not multiple of 400.
 """

'''
Esta función calcula si un año es bisiesto o no.
Recibe un año. 
Devuelve:
1 si el año es bisiesto
-1 si el año no es bisiesto o es el año 0
'''
def leapYear(year):
    #Estructura lógica si el año es bisiesto y diferente de 0
    if (year%4==0 or (year%100==0 and year%400==0)) and year!=0:
        resultado=1
    #Años no bisiestos y año==0
    else:
        resultado=-1
     
    return resultado



"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 3
 @enunciado: 
 Design a method called daysInMonth that returns the integer number of days 
 in the month and year that received as arguments. 
 You can use the method leapYear. 
 If the arguments are not valid the method should return -1.
 """

'''
Esta función calcula cuántos días hay en un mes.
Recibe un mes y un año
Devuelve:
31 si el mes tiene 31 días
30 si el mes tiene 30 días
28 si el mes es febrero y el año no es bisiesto
29 si el mes es febrero y el año es bisiesto
-1 si los datos no son correctos
'''
def daysInMonth(month, year):
    #Iniciamos la variable en -1 que nos servirá para argumentos incorrectos,
    #ya que no entrarán en la estructura condicional
    days=-1
    #Años positivos
    if year>0:
        #Meses de 31 días
        if month in {1,3,5,7,8,10,12}:
            days=31
        #Meses de 30 días
        elif month in {4,6,9,11}:
            days=30
        #Elif para que entre solo en febrero, al no haber control de meses mayores de 13
        #o menores de 0
        elif month==2:
            #Uso la función del año bisiesto con el parámetro year y cuando el resultado era 1 (año bisiesto)
            if leapYear(year)==1:
                days=29
            #Años no bisiestos
            else:
                days=28
                
    return days



"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 4
 @enunciado: 
 Design a method called dayOfWeek that receives three integer parameters: 
 day, month and year. 
 The method should return a number between 0 and 6 that is the day in the 
 week for that date. You have to know the next algorithm:
 
        a = (14 - month) / 12 
       y = year – a 
       m = month + 12 * a – 2 
       d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
       
       If the variable d is zero was Sunday, 1 Monday……………... 6 Saturday. 
 """

'''
Esta función calcula el día de la semana en que cayó una fecha. 
Recibe un día, un mes y un año
Devuelve:
De 0 a 6, dependiendo del día de la semana que sea (0 - domingo, 1 - lunes, etc.)
'''
def dayOfWeek(day, month, year):
    #Uso la función que me han dado, usando división entera (para que no haya decimales o da error)
    #y paréntesis para orden de operaciones
    a = (14-month)//12
    y = year - a
    m = month + 12*a - 2
    d = (day + y + (y//4) - (y//100) + (y//400) + (31*m)//12) % 7
     
    return d
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 5
 @enunciado: 
 Design a method called myPower that receives one integer and one integer 
 positive numbers as parameters and the method calculates the power of the 
 first parameter raised the second number. 
 You only can use the multiplication. 
 If the parameters are not right (the second parameter is negative) the method 
 should return -1. 
 Remember that any number raised 0 is 1.
 """

'''
Esta función calcula la potencia de un número utilizando la multiplicación 
Recibe dos números enteros
Devuelve:
La potencia si el exponente es un número positivo.
1 si el exponente es 0.
-1 si el exponente es un número negativo.

'''
def myPower(numA, numB):
    #Inicio la variable a 1, porque la voy a usar en el bucle para multiplicar.
    #Además será el resultado final cuando numB==0
    potencia=1
    #Si numB es positivo, creo un bucle que multiplique numA el número de veces
    #coincidente con el valor de numB
    if numB>0:
        for i in range (numB):
            potencia*=numA
    #Si el num es negativo, la potencia vale -1
    elif numB<0:
        potencia=-1   
        
    return potencia
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 6
 @enunciado: 
 Design a method called numberOfNumbers that receives one integer positive number 
 as parameter. 
 The method should return the number of digits of the number that received by parameter. 
 If the parameter is not valid the method should return -1.
 """

'''
Esta función calcula los dígitos de un número entero. 
Recibe un número entero.
Devuelve:
-1 si el número introducido es negativo.
El número de dígitos del número si el número introducido es positivo.
'''
def numberOfNumbers(num):
    #Inicializo la variable digits a 1 para la primera decena [1,9], correspondiente al primer dígito
    digits=1
    #Si el número es negativo o 0 (parámetro no válido, digits vale -1
    if num<=0:
        digits=-1
    #Mientras que el número tenga dos dígitos
    while num>9:
        #Quita una decena (un dígito)
        num=num/10
        #Utilizo la variable digits como acumulador y le sumo uno con cada dígito que puedo dividir
        digits+=1
    
    return digits


"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 7
 @enunciado: 
 Design a method called isPrime that receives one integer positive number greater 
 than 0 as parameter. The method should return 1 if the number is prime or 0 
 if the number is not prime. If the parameter is not valid the method should return -1.
 """

'''
Esta función calcula si un número es primo. 
Recibe un número entero.
Devuelve:
-1 si el número es negativo o 0.
0 si el número no es primo.
1 si el número es primo.
'''
def isPrime(num):
    #Si el parámetro no es válido la variable que usaré en el return vale -1
    if num<=1:
        isPrime=-1
    #Aquí opero para parámetros correctos (número positivo)
    else:
        #Variable para el bucle que inicia en 2, ya que es el número desde el que empiezo a contar divisores
        i=2
        #Bandera que inicializo a 1 (número primo), es decir, sin divisores.
        isPrime=1
        #Creo el bucle que va desde 2 hasta la mitad del número (posibles divisores) y cuya bandera vale 1
        while i<=num//2 and isPrime==1:
            #Si el número tiene algún divisor modifico la bandera para que valga 0 (no es primo)
            if num%i==0:
                isPrime=0
            #De lo contrario aumento la variable iteradora del bucle
            else:
                i+=1
        
    return isPrime
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 8
 @enunciado: 
 Design a method called secondOrder that receives three integer positive number 
 as parameters.
 This parameters are the coefficients of the an equation of a 
 second order (ax2+bx+c=0) and the method returns the numbers of the solutions. 
 If the parameters are not valid the method should return -1.
 """

'''
Esta función calcula el número de soluciones de una función de segundo grado 
Recibe 3 números enteros (a, b, c)
Devuelve:
-1 si a (primero número) es 0.
0 si el discriminante es menor que 0.
1 si el discriminante es 0.
2 si el discriminante es mayor que 0.
'''
def secondOrder (a, b, c):
    #Compruebo si es una ecuación de segundo grado
    if a!=0:
        #Creo una variable donde igualo la fórmula de su cálculo
        discriminante=(b**2)-4*a*c
        #Creo la estructura lógica según el valor del discriminante
        if discriminante>0:
            #Hay dos soluciones reales distintas
            numSoluciones=2
        elif discriminante==0:
            #Hay dos soluciones reales iguales, por lo que el resultado es 1
            numSoluciones=1
        else:
            #No hay soluciones reales, sino 2 soluciones complejas distintas.
            numSoluciones=0
    #Si no es una ecuación de segundo grado, no tiene soluciones, por lo que devuelve -1
    else:
        numSoluciones=-1
        
    return numSoluciones
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 9
 @enunciado: 
 Design a method called numberDivisorPrime that receives a positive number as 
 a parameter. 
 The method should return the number of prime divisors of the parameter. 
 If the parameter is not valid the method should return 0.
 """

'''
Esta función calcula el número de divisores primos de un número 
Recibe un número entero positivo
Devuelve:
0 si no tiene divisores primos.
El número de divisores primos del número
''' 
def numberDivisorPrime(num):
    #Inicializo la variable a 0, que vale para parámetros no válidos y como variable 
    #acumuladora del bucle posterior
    divisors=0
    #Si el número es mayor que 0, creo un bucle desde 1 hasta la mitad del número más 1
    if num>0:
        for i in range(1,num//2+1):
            #Si i es divisor del número y además i es un número primo, me acumula en la variable divisors
            if num%i==0 and isPrime(i)==1:
                divisors+=1
    elif num<0:
        divisors=-1  
    
    return divisors
 
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 10
 @enunciado: 
 Design a method called friend that receives two positive number as parameters. 
 The method should return true if the number are friends and false in other case. 
 Two numbers are friends if the addition of all the divisors less the same number 
 of the one number is equal to the second number and in the other case too. 
 If the parameters are not valid the method should return false.
 """

'''
Esta función calcula si dos números enteros positivos son números amigos 
Recibe dos números enteros positivos
Devuelve:
False si no son amigos
True si son amigos
''' 
def friend (numA, numB):
    #Inicio el resultado en False, para parámetros no válidos (numeros menores o igual que 0 o que los
    #números no sean amigos
    resultado=False
    #Si los parámetros son correctos y la suma de los divisores de A es igual a B y la suma de divisores
    #de B es igual a A, los números son amigos.
    #Para la suma de los divisores he creado otra función a la que llamo, para no repetir código con cada
    #número
    if numA>0 and numB>0 and sumaDivisores(numA)==numB and sumaDivisores(numB)==numA:
        resultado=True
    
    return resultado

'''
Esta función calcula la suma de los divisores de un número 
Recibe un número entero positivo
Devuelve:
La suma de los divisores de un número
'''
def sumaDivisores(num):
    #Creo la variable sumatoria de los divisores
    suma=0
    #Creo un bucle desde 1 hasta la mitad del número más 1
    for i in range(1,num//2+1):
        #Si i es divisor del número, me lo suma
        if num%i==0:
            suma+=i
    
    return suma

#Test con dos números amigos
assert(sumaDivisores(220)==284)
assert(sumaDivisores(284)==220)
assert(sumaDivisores(8)==7)

