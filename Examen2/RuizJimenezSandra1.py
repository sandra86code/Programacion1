'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 10, 2021
 @nombre: Examen 10 Diciembre - Ejercicio 1
 @enunciado: 
 Crear función que reciba una cadena como parámetro y que devuelva si es una contraseña
FUERTE (True) o DÉBIL (False). Se considera que una contraseña es fuerte si contiene 8 o
más caracteres, y entre ellos al menos hay una mayúscula, una minúscula y un dígito.
'''

#===============================================================================
# Esta función comprueba la solidez de una contraseña que le pasamos por parámetro
# Recibe: password, que es una variable de tipo string
# Devuelve:
# True si la contraseña es fuerte (tiene 8 o más caracteres y contiene al menos
# una mayúscula, una minúscula y un dígito).
# False si la contraseña es débil (no tiene 8 o más caracteres o no contiene al menos
# una mayúscula, una minúscula y un dígito).
#===============================================================================
def comprobarSolidezPassword(password):

    esSolida=False
    if len(password)>=8:
        i=0
        #Estas tres variables actuan como bandera, ya que al cambiar las tres a 1
        # indica que la contraseña es fuerte, por lo que se cambia la bandera que
        #frena el bucle.
        mayuscula=0
        minuscula=0
        digito=0

        while i<len(password) and esSolida==False:
            #Código asci para letras en mayúscula
            if password[i]>=chr(65) and password[i]<=chr(90):
                mayuscula=1
            #Código asci para letras en minúscula
            elif password[i]>=chr(97) and password[i]<=chr(122):
                minuscula=1
            #Código asci para números, por eso no uso else, pq sino entraría cualquier
            #otro caracter, no solo los números
            elif password[i]>=chr(48) and password[i]<=chr(57):
                digito=1

            #Si las tres banderas han cambiado, se cambia la bandera
            #y se frena el bucle
            if mayuscula==1 and minuscula==1 and digito==1:
                esSolida=True

            i+=1


    return esSolida


assert(comprobarSolidezPassword("1abdFk.")==False)
assert(comprobarSolidezPassword("1abdFk2.")==True)
assert(comprobarSolidezPassword("abcdeFGGD")==False)
assert(comprobarSolidezPassword("123abde.")==False)
assert(comprobarSolidezPassword("123ABE.H")==False)



'''
CORRECCIÓN DEL EJERCICIO CON UNA SEGUNDA FUNCIÓN PARA COMPROBAR EL CÓDIGO ASCII:

def esTipoCaracter(caracter, valorInicial, valorFinal):
    
    return caracter>=chr(valorInicial) and caracter<=chr(valorFinal)



def comprobarSolidezPassword(password):
    
    esSolida=False
    if len(password)>=8:
        i=0
        mayuscula=0
        minuscula=0
        digito=0
        
        while i<len(password) and esSolida==False:
            if esTipoCaracter(password[i], 65, 90):
                mayuscula=1
            else:
                esSolida=False
            
            if esTipoCaracter(password[i], 97, 122):
                minuscula=1
            else:
                esSolida=False
            
            if esTipoCaracter(password[i], 48, 57):
                digito=1
            else:
                esSolida=False
            #Si las tres banderas han cambiado, se cambia la bandera
            #y se frena el bucle
            if mayuscula==1 and minuscula==1 and digito==1:
                esSolida=True
                mensaje="La contraseña es fuerte."
            else:
                mensaje="La contraseña es débil."
            
            i+=1
    else:
        mensaje="La contraseña es débil."     
    
    
    return mensaje


assert(comprobarSolidezPassword("1abdFk.")=="La contraseña es débil.")
assert(comprobarSolidezPassword("1abdFk2.")=="La contraseña es fuerte.")
assert(comprobarSolidezPassword("abcdeFGGD")=="La contraseña es débil.")
assert(comprobarSolidezPassword("123abde2")=="La contraseña es débil.")
assert(comprobarSolidezPassword("123ABE.H")=="La contraseña es débil.")

'''