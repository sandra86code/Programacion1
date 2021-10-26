'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 5, 2021
 @nombre: Boletin 2 - Ejercicio Extra 5
 @enunciado: 
 Realizar un programa que solicite la coordenada x e y de un punto e informe si se encuentre
en el primer, segundo, tercer o cuarto cuadrante.
'''

#Pido datos
x=int(input("Introduce la coordenada x del punto: "))
y=int(input("Introduce la coordenada y del punto: "))

#(+x,+y)
if x>0 and y>0:
    mensaje="El punto se encuentra en el cuadrante 1." 
#(-x,+y)
elif x<0 and y>0:
    mensaje="El punto se encuentra en el cuadrante 2." 
#(-x,-y)
elif x<0 and y<0:
    mensaje="El punto se encuentra en el cuadrante 3." 
#(+x,-y)
elif x>0 and y<0:
    mensaje="El punto se encuentra en el cuadrante 4." 
elif x==0:
    #(0,0)
    if y==0:
        mensaje="El punto se encuentra en el origen de coordenadas."
    #(0, !0)
    else:
        mensaje="El punto se encuentra en el eje x."
#(!0, 0)
else:
    mensaje="El punto se encuentra en el eje y."

#Muestro resultado por consola
print(mensaje)