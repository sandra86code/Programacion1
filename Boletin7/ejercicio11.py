'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Ejercicios del año pasado - Ejercicio 11
 @enunciado: 
Escribe una función que reciba dos listas y devuelva una lista con los 
elementos comunes a ambas, sin repetir ninguno.
'''

def listarElementosComunes(lista1, lista2):
    listaComunes=[]
    if lista1>lista2:
        listaMayor=lista1
        listaMenor=lista2
    else:
        listaMayor=lista2
        listaMenor=lista1
        
    for i in listaMenor:
        j=0
        itemFound=False
        while j<len(listaMayor) and itemFound==False:
            if listaMenor[i]==listaMayor[j]:
                listaComunes.append(listaMenor[i])
                itemFound==True
            
            else:
                j+=1
    
    return listaComunes

assert(listarElementosComunes([], [])==[])