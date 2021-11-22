x=[1,2,3,4]

def prueba(x):
    x[1]=5
    x=[5,6,7]
    x[0]=5
    return x
    
x =prueba(x)
print(x)