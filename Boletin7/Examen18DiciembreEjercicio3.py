'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 17 nov 2021
 @nombre: Examen 18 Diciembre 2020 - Ejercicio 3
 @enunciado: 
Realizar una función que dada una fecha en formato 12 horas nos devuelva la fecha en formato 24
horas.
La función recibirá una cadena con el siguiente formato hh:mm:ssAM u hh:mm:ssPM y deberá
devolver el formato de fecho hh:mm:ss con 24 horas.
Si la fecha que recibe no tiene el formato adecuado deberá devolver una cadena vacía.

Ejemplos:
convierteFecha(“12:02:04AM”) → “”
convierteFecha(“12:02:04PM”) → “”
convierteFecha(“11:02:04AM”) → “11:02:04”
convierteFecha(“11:02:04PM”) → “23:02:04”
convierteFecha(“14:89:04AM”) → “”
convierteFecha(“12:02:04AP”) → “”
'''

def pasaFechaALista(fecha):
    
    lista=[]

    if len(fecha)==10:        
        var=""
        formato=""
        for i in range (len(fecha)):
            if fecha[i]!=":":
                if fecha[i]>=chr(48) and fecha[i]<=chr(57):
                    var+=fecha[i]
                else:
                    formato+=fecha[i]
            else:
                lista.append(int(var))
                var=""
        if var!="":
            lista.append(int(var))
        if formato in {"PM", "AM"}:
            lista.append(formato)
        else:
            lista=[]
            
    return lista


def compruebaFecha(lista):
    
    if len(lista)!=0:
        i=0
        bandera=True
        while i<len(lista) and bandera:
            if lista[0]>11:
                bandera=False
            elif lista[1]>59 or lista[2]>59:
                bandera=False
        if bandera==False:
            lista=[]
    print(lista)
    return lista


def convierteFecha(fecha):
    
    fecha24horas=""
    lista=compruebaFecha(pasaFechaALista(fecha))
    print(lista)
    if len(lista)==4:
        if lista[-1]=="PM":
            lista[0]+=12
        for i in range (len(lista)-1):
            if lista[i]==lista[-2]:
                fecha24horas+=str(lista[i])
            else:
                fecha24horas+=str(lista[i])+":"
    print(fecha24horas)       
    return fecha24horas
    
    

# assert(convierteFecha("12:02:04AM")=="")
# assert(convierteFecha("12:02:04PM")=="")
assert(convierteFecha("11:02:04AM")=="11:02:04")
assert(convierteFecha("11:02:04PM")=="23:02:04")
# assert(convierteFecha("14:89:04AM")=="")
# assert(convierteFecha("12:02:04AP")=="")
