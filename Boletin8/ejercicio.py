'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 26 nov 2021
 @nombre: Notas Alumnos
 @enunciado: 
 Vamos a escribir un ejercicio para que un profesor almacene las notas de las asignaturas de los
alumnos, para ello vamos a crear un menú con las siguientes opciones:
    1. Dar de alta un alumno/a
    2. Dar de alta una asignatura de un alumno/a
    3. Añadir una nota de una asignatura de un alumno/a
    4. Ver las notas que un alumno/a tienen en una asignatura.
    5. Ver la nota que un alumno/a tendría en una asignatura suponiéndole la nota máxima
    6. Ver la nota que un alumno/a tendría en una asignatura suponiéndole la nota media.
    7. Ver todas las notas de una asignatura de un alumno/a
    8. Ver todas las notas de todas las asignaturas de un alumno/a
    9. Ver todas las notas de todas las asignaturas de todos los alumnos/a
    10. Salir

Para realizar el programa vamos a tener un array o lista de alumnos, un array o lista de listas de
asignaturas y un array o listas de listas de notas de asignaturas es decir sería algo como:

Lista de alumnos/as:
0                            |  1                                    | 2                        | 3
Inma                         |  Juan                                 | Pepe                     | Pablo

Lista de asignaturas de los alumnos/as:
Lengua     Mates     Infor   |  Infor.   Mates     Inglés   Lengua   | Ciencias                 | Inglés     Francés
0          1         2       |  0        1         2        3        | 0                        | 0          1

Lista de notas de las asignaturas de los alumnos/as
[10, 9]   [10,9,8]   [10]    |  [8]     [5,6,2,4]  [5]      [8]      | [4,5]                    | [7]        [1,4]

'''

listaAlumnos=[]
listaAsignaturas=[]
listaNotas=[]




#===============================================================================
# darAltaAlumno
# Esta función da de alta a un alumno en el sistema
# Recibe 
# Devuelve:
# 
#===============================================================================
def darAltaAlumno(nombre):

    listaAlumnos.append(nombre)
    listaAsignaturas.append([])
    listaNotas.append([])
    
    print(listaAlumnos)
    print(listaAsignaturas)
    print(listaNotas)

#===============================================================================
# AltaAsignaturaAlumno
# Esta función da de alta una asignatura en un alumno matriculado
# Recibe
# Devuelve:
# 
#===============================================================================
def matricularAlumno(alumno, asignatura):

    pos = listaAlumnos.index(alumno)
    if asignatura in listaAsignaturas[pos]:
        estaMatriculado=False
    else:   
        listaAsignaturas[pos].append(asignatura)
        estaMatriculado=True
    
    return estaMatriculado



#===============================================================================
# AltaAsignaturaAlumno
# Esta función da de alta una asignatura en un alumno matriculado
# Recibe
# Devuelve:
# 
#===============================================================================
def ponerNotas(alumno, asignatura, nota):
    pos = listaAlumnos.index(alumno)
    if alumno in listaAlumnos and asignatura in listaAsignaturas:
        listaNotas[pos].append(nota)
        estaMatriculado=True
    else:
        estaMatriculado=False
        
    return estaMatriculado




def getNotas(linea):
    notas=[]
    i=0
    while i<len(linea) and linea[i]!=",":
        i+=1
    
    i+=1
    
    nota=""
    while i<len(linea):
        if linea==",":
            notas.append(int(nota))
            nota=""
        else:
            nota+=i
        i+=1

    
    return notas
        

def getAsignatura(linea):
    asignatura=""
    i=0
    bandera=False
    while i<len(linea) and bandera==False:
        if linea[i]!=",":
            asignatura+=linea[i]
        else:
            bandera=True
    
    return asignatura



def getAlumno(linea):
    
    alumno=""
    for i in range (len(linea)):
        if linea[i]!="*":
            alumno+=linea[i]
    
    return alumno



def leerFichero():

    f = open ('alumnos.txt','r')
    mensaje = f.read()
    f.close()
    
    linea=""
    for i in mensaje:
        if i=="\n":
            if linea[0]=="*":
                alumno=getAlumno(linea)
                darAltaAlumno(alumno)
            else:
                asignatura=getAsignatura(linea)
                matricularAlumno(alumno,asignatura)
                listaNotas=getNotas(linea)
                for nota in listaNotas:
                    ponerNotas(alumno,asignatura,nota)
            linea=""
        else:
            linea+=i
    
    if linea[0]=="*":
        alumno=getAlumno(linea)
        darAltaAlumno(alumno)
    else:
        asignatura=getAsignatura(linea)
        matricularAlumno(alumno,asignatura)
        listaNotas=getNotas(linea)
        for nota in listaNotas:
            ponerNotas(alumno,asignatura,nota)
    

leerFichero()


#===============================================================================
# Esta función 
# Recibe 
# Devuelve:
# 
#===============================================================================
def menuSecundario(opcion, listaAlumnos, listaAsignaturas, listaNotas):
    
    if opcion==1:
        nombreAlumno = input("Introduce el nombre del alumno/a que quieres matricular: ")
        if nombreAlumno not in listaAlumnos:
            listaAlumnos=darAltaAlumno(nombreAlumno)
            mensaje="El/La alumno/a %s ha sido dado de alta en el sistema." % (nombreAlumno)
        else:
            mensaje="Error. El/La alumno/a %s ya está dado de alta en el sistema." % (nombreAlumno)
    elif opcion==2:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:    
            nombreAsignatura=int(input("¿De qué asignatura quiere matricular al alumno/a %s" %nombreAlumno))
            if matricularAlumno(nombreAlumno, nombreAsignatura):
                mensaje="La asignatura %s ha sido dado de alta para el/la alumno/a %s." % (nombreAsignatura, nombreAlumno)
            else:
                mensaje="Error. La asignatura %s ya está dada de alta para el/la alumno/a %s." % (nombreAsignatura, nombreAlumno)
   
    elif opcion==3:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        
    # elif opcion==4:
    #
    # elif opcion==5:
    #
    # elif opcion==6:
    #
    # elif opcion==7:
    #
    # elif opcion==8:
    #
    # else:
        
    return mensaje


def menuPrincipal():
    
    menu="1. Dar de alta un alumno/a.\n"\
        "2. Dar de alta una asignatura de un alumno/a.\n"\
        "3. Añadir una nota de una asignatura de un alumno/a.\n"\
        "4. Ver las notas que un alumno/a tienen en una asignatura..\n"\
        "5. Ver la nota que un alumno/a tendría en una asignatura suponiéndole la nota máxima.\n"\
        "6. Ver la nota que un alumno/a tendría en una asignatura suponiéndole la nota media.\n"\
        "7. Ver todas las notas de una asignatura de un alumno/a.\n"\
        "8. Ver todas las notas de todas las asignaturas de un alumno/a.\n"\
        "9. Ver todas las notas de todas las asignaturas de todos los alumnos/a.\n"\
        "10. Salir.\n"\

    return menu



def main():
    

    
    linea="\n-----------------------------------------------------------------------------\n"
    bienvenida="Bienvenido/a al menú principal del sistema de registro del alumnado del IES Jacarandá."
    
    opcion=1
    
    while opcion!=10:
        print(linea)
        print(bienvenida)
        print(menuPrincipal())
    
        opcion=int(input("¿Qué opción desea? "))
        while opcion<1 or opcion>10:
            print("Opción incorrecta. Vuelve a intentarlo.")
            opcion=int(input("¿Qué opción desea? "))
        
        print(linea)
        
        if opcion!=10:
            print(menuSecundario(opcion, listaAlumnos, listaAsignaturas, listaNotas))
            print(listaAlumnos)
            print(listaAsignaturas)
            print(listaNotas)
            
    print("Hasta la próxima.")


    
main()





