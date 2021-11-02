"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 1
 @enunciado: 
 Design a method called factorial that receives a positive integer and returns 
 the factorial. If the number is negative the method should return -1.    
 """
 
def factorial(num):
    resultado=1
    if num<0:
        resultado=-1
    elif num>0:
        for i in range (1, num+1):
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
 
def leapYear(year):
    if (year%4==0 or (year%100==0 and year%400==0)) and year!=0:
        resultado=1
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
 If the arguments are not valid the method should return -1
 """

def daysInMonth(month, year):
    if year>0:
        if month in {1,3,5,7,8,10,12}:
            days=31
        elif month in {4,6,9,11}:
            days=30
        elif month==2:
            if leapYear==1:
                days=29
            else:
                days=28
        else:
            days=-1
    else:
        days=-1
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
 
def daysOfWeek(day, month, year):
     
    a = (14-month)/12
    y = year-a
    m = month+12 * a-2
    d = (day + y + y/4 - y/100 + y/400 + 31*m/12) % 7
     
    return round(d)
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 5
 @enunciado: 
 Design a method called myPower that receives one integer and one integer 
 positive numbers as parameters and the method calculates the power of the 
 first parameter raised the second number. You only can use the multiplication. 
 If the parameters are not right (the second parameter is negative) the method 
 should return -1. Remember that any number raised 0 is 1.
 """
 
def myPower(numA, numB):
    potencia=0
    if numB>0:
        for i in range (numB):
            potencia+=numA
    elif numB<0:
        numB*=-1
        for i in range (numB):
            potencia+=numA
        potencia*=-1   
    return potencia
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 6
 @enunciado: 
 Design a method called numberOfNumbers that receives one integer positive number 
 as parameter. The method should return the number of digits of the number that 
 received by parameter. If the parameter is not valid the method should return -1.
 """




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
 
 
 
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 8
 @enunciado: 
 Design a method called secondOrder that receives three integer positive number 
 as parameters. This parameters are the coefficients of the an equation of a 
 second order (ax2+bx+c=0) and the method returns the numbers of the solutions. 
 If the parameters are not valid the method should return -1
 """
 
 
 
 
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 8
 @enunciado: 
 Design a method called numberDivisorPrime that receives a positive number as 
 a parameter. 
 The method should return the number of prime divisors of the parameter. 
 If the parameter is not valid the method should return -1.
 """
 
 
 
 
"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Nov 2, 2021
 @nombre: Boletin 3 - Ejercicio 8
 @enunciado: 
 Design a method called friend that receives two positive number as parameters. 
 The method should return true if the number are friends and false in other case. 
 Two numbers are friends if the addition of all the divisors less the same number 
 of the one number is equal to the second number and in the other case too. 
 If the parameters are not valid the method should return false.
 """
 
