x=[1,2,3,4]
print(id(x))

def prueba(x):
    x[0]=9
    x=[5,6,7]
    x[1]=8
    print(x)
    print(id(x))
        
    return x

x=prueba(x)

print(x)
print(id(x))