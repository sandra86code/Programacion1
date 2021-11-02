def repite_sinretorno(caracter="-", repite=3):
    print(caracter*repite)

repite_sinretorno()


#Función con retorno
def leer(cadena):
    num1=int(input(cadena))
    while num1 < 10 or num1>100:
        num1=int(input(cadena))
     
    return num1
 
# cant= 0
# num1 = leer("Introduce el primer número: ")
# cant += num1
#  
# num2 = leer("Introduce el segundo número: ")
# cant += num2
#  
# num3 = leer("Introduce el tercer número: ")
# cant += num3
#  
# print(cant/3)
 
# #Función sin retorno
# def leer2(cadena):
#     num1=int(input(cadena))
#     while num1 < 10 or num1>100:
#         num1=int(input(cadena))
#      
#     print(num1)
#     
# numero=leer("Introduce un número:")
# numero2 = leer2("Introdddd")
# 
# print(numero) #numero vale lo que vale el num1 del return de la función.
# print(numero2) #En este caso, al no asignársele valor en la función, la variable numero2 no tiene valor (None)


def areaTriangulo(base, altura):
    area=base*altura/2
    return area

num1=leer("Introduce la base: ")
num2=leer("Introduce la altura: ")
area = areaTriangulo(num1, num2)
print(area)


#Tramos (no sabemos cuántos argumentos le vamos a pasar a la función)

def suma(*numeros):
    resultado=0
    for pepito in numeros:
        resultado+=pepito

    return resultado

print(suma(1))
print(suma(1,2,3,4,5))
print(suma(1,2,3,4,5,6,7,8,9,10,11,12))


def calculaDescuento(cant, descuento=5):
    return cant*descuento/100

print(calculaDescuento(100)) #En este caso descuento vale 5
print(calculaDescuento(100, 10)) #En este caso descuento vale 10