def listaALaInversa(lista):
    listaInversa=[]
    for i in range (1, len(lista)+1):
        listaInversa.append(lista[-i])

    return listaInversa

listaNumeros=[]
num=int(input("Introduce un numero (-1 para parar): "))
while num!=-1:
    listaNumeros.append(num)
    num=int(input("Introduce un numero (-1 para parar): "))
    
print(listaALaInversa(listaNumeros))