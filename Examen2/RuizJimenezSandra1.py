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
            if password[i]>=chr(65) and password[i]<=chr(90):
                mayuscula=1
            elif password[i]>=chr(97) and password[i]<=chr(122):
                minuscula=1
            elif password[i]>=chr(48) and password[i]<=chr(57):
                digito=1
            
            if mayuscula==1 and minuscula==1 and digito==1:
                esSolida=True
            
            i+=1
         
    
    return esSolida


assert(comprobarSolidezPassword("1abdFk.")==False)
assert(comprobarSolidezPassword("1abdFk2.")==True)
assert(comprobarSolidezPassword("abcdeFGGD")==False)
assert(comprobarSolidezPassword("123abde.")==False)
assert(comprobarSolidezPassword("123ABE.H")==False)

