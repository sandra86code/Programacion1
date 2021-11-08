'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 29, 2021
 @nombre: Examen 1  - Ejercicio 02
 @enunciado: 
 2.- Seguimos trabajando para un centro de salud y nos piden que digamos cuántos enfermos de los
que han pasado el covid son menores de 30 años, cuántos tienen entre 31 y 49 años (49 incluidos) y
cuántos hay de los que tengan 50 o más años. Para ello van a llamar a todos los pacientes que han
pasado el covid y le van a preguntar la edad, debemos diseñar un programa que vaya pidiendo el
mes y el año de nacimiento de los enfermos, calcule la edad que tienen (piensa que si cumple en
noviembre lo vamos a contar como que ya ha cumplido aunque por ejemplo cumpla a finales de
mes y lo llamen el día 2) y lo contabilice en el tramo correspondiente. El programa terminará
cuando el usuario introduzca un -1 en el mes de nacimiento.
Ten en cuenta que si el usuario introduce un mes en negativo no debe pedirle el año, ya que debe
mostrar los resúmenes y salir.
•
Posible mejora a implementar si sabes, ¿cómo podrías hacer para que fuese fácil cambiar el
mes y el año en el que se ejecuta tu programa? Escribe la respuesta en el mismo fichero de
Python
'''


#Pido datos del mes y lo introduzco en una variable numérica
mes=int(input("Introduce el mes de nacimiento en números: "))
#Si los datos no son correctos (mes menor que 1 o mayor que 12) o si el mes es diferente de -1
#(esto lo hago porque sino es imposible que siga adelante el programa, cuando debería hacerlo
#según lo que dice el programa, no debería ejecutar el bucle y debería decirme que hay 0
#pacientes)
while (mes<1 or mes>12) and mes!=-1:
    print("Datos incorrectos. Vuelve a intentarlo.")
    mes=int(input("Introduce el mes de nacimiento en números (-1 para parar): "))

#Creo las 3 variables contadoras donde voy a ir sumando pacientes según su rango de edad
#Como son sumatorias y al principio tengo 0 pacientes, las inicializo a 0        
pacienteMenos30=0
pacienteMenos50=0
pacienteMas50=0

#Creo el bucle de tipo while (ya que no sé cuántas iteraciones va a tener), cuya condición
#de salida es que el mes introducido sea el -1
while mes!=-1:
    #Pido los datos del año de nacimiento y si la fecha es incorrecto (no se puede nacer en
    #el futuro) los vuelvo a pedir. No pongo límite inferior, aunque podría establecerse en
    #1900, por ejemplo.
    year=int(input("Introduce el año de nacimiento: "))
    while year>2021 or (year==2021 and mes>10):
        print("Datos incorrectos. Vuelve a intentarlo.")
        year=int(input("Introduce el año de nacimiento: "))
    
    #Hago la estructura condicional para comprobar si ha cumplido años o no según el mes.
    #Como estamos en octubre, parto desde ese mes.
    #De esta manera calculo la edad y la almaceno en la variable edad.
    if mes<=10:
        edad=2021-year
    else:
        edad=2021-1-year
    
    #Hago una estructura lógica según la edad del paciente y si entra por la condición,
    #sumo 1 a la variable contadora
    if edad<31: #[0,30]
        pacienteMenos30+=1
    elif edad<50: #[31,50]
        pacienteMenos50+=1
    else: #51 en adelante
        pacienteMas50+=1
    
    #Vuelvo a pedir el mes y comprobar si los datos son incorrectos (los vuelve a pedir)
    #Lo pongo al final para que si se introduce -1, frene el bucle y no me pida el año    
    mes=int(input("Introduce el mes de nacimiento en números (-1 para parar): "))
    while (mes<1 or mes>12) and mes!=-1:
        print("Datos incorrectos. Vuelve a intentarlo.")
        mes=int(input("Introduce el mes de nacimiento en números (-1 para parar): "))
    
#Muestro por consola el resultado de las tres variables contadoras
print("Hay %s enfermos menores de 30 años, %s entre 31 y 49 años y %s con 50 o más años." % (pacienteMenos30, pacienteMenos50, pacienteMas50))


'''
Mejora a implementar:

En este caso, guardaríamos el mes actual en una variable, por ejemplo, MES_ACTUAL, y el año actual en otra variable,
por ejemplo, YEAR_ACTUAL. De esta manera, se convertirían en una constante (aunque realmente no existen en Python).
De esta manera, cambiaríamos los datos de comparación por las constantes y si hubiese que cambiarlas,
sería tan fácil como modificar el valor de la constante.
'''

'''
También puede hacerse con la función date.today() de Python (importadas) para obtener el mes y el año actual.

# from datetime import date
#
# mesActual=date.today().month
# yearActual=date.today().year

'''