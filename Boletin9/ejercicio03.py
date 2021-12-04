'''
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Dec 3, 2021
 @nombre: Simulacro Examen - Ejercicio 3
 @enunciado: 
 Un juguete tiene tres botones, dos de melodías: A y B (con dos músicas por botón) y otro P de
apagado. 
Cada botón de melodía activa el juguete y al ser pulsado sucesivamente cambia de una a
otra melodía.
Es decir, si se pulsa el botón A una vez suena la melodía A1 y si se vuelve a pulsar, la A2, y de igual
modo sucede con el botón B.
Crea un programa que lea por teclado el botón que se ha pulsado (independientemente de si es
mayúscula o minúscula) y escriba la melodía que suena (melodía A1, ... melodía B2) y se apague
cuando se pulse el botón P.
'''
#Creo la lista de enteros de las melodias de los botones (posicion0 es melodia A,
#posicion1 es melodia B
melodiasBotones=[0,0]

#===============================================================================
# Esta función recibe una melodia (numero entero) y la cambia
# Recibe: una melodia, que es un número entero [0, 2]
# Devuelve:
# Si recibe 0, devuelve 1
# Si recibe 1, devuelve 2
# Si recibe 2, devuelve 1
#===============================================================================
def cambiaMelodia(melodia):
    if melodia==0 or melodia==1:
        melodia+=1
    else:
        melodia-=1
    
    return melodia
    
        
#===============================================================================
# Esta función es la principal del programa.
# Pide los datos, los comprueba (si son incorrectos los vuelve a pedir).
# Devuelve la melodía dependiendo del botón dicho por el usuario.
# El programa termina cuando el botón dicho por el usuario es P o p.
#===============================================================================        
def main():
    
    boton=input("¿Qué botón se ha pulsado (A,B,P)? ")
    while boton not in {"A","a","B","b","P","p"}:
        print("Respuesta incorrecta.")
        boton=input("¿Qué botón se ha pulsado (A,B,P)? ")
       
    while boton not in {"P", "p"}:
        #Si el botón es A o a, la lista de melodias en posición 0
        #llama a la función y luego se imprime el resultado
        if boton=="A" or boton=="a":
            melodiasBotones[0]=cambiaMelodia(melodiasBotones[0])
            print("Suena la melodia A%s" % melodiasBotones[0])
        #Si el botón es B o b, la lista de melodias en posición 1
        #llama a la función y luego se imprime el resultado
        else:
            melodiasBotones[1]=cambiaMelodia(melodiasBotones[1])
            print("Suena la melodia B%s" % melodiasBotones[1])
        
        boton=input("¿Qué botón se ha pulsado (A,B,P)? ")
        while boton not in {"A","a","B","b","P","p"}:
            print("Respuesta incorrecta.")
            boton=input("¿Qué botón se ha pulsado (A,B,P)? ")
    
    print("Juguete apagado.")
    
main()

