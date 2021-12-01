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
        listaNotas[pos].append([])
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
    if alumno in listaAlumnos:
        pos = listaAlumnos.index(alumno)
        if asignatura in listaAsignaturas[pos]:
            posAsig=listaAsignaturas[pos].index(asignatura)
            listaNotas[pos][posAsig].append(nota)
            estaMatriculado=True
        else:
            estaMatriculado=False
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
        if linea[i]==",":
            notas.append(int(nota))
            nota=""
        else:
            nota+=linea[i]
        i+=1
    if nota!="":
        notas.append(int(nota))
    
    return notas
        

def getAsignatura(linea):
    asignatura=""
    i=0
    bandera=False
    while i<len(linea) and bandera==False:
        if linea[i]!=",":
            asignatura+=linea[i]
            i+=1
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
                notas=getNotas(linea)
                for nota in notas:
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
        notas=getNotas(linea)
        for nota in notas:
            ponerNotas(alumno,asignatura,nota)
    
leerFichero()



def volcarFichero():
    f = open('alumnos.txt', 'w')
    try:
        for posAlumno in range(len(listaAlumnos)):
            f.write("*"+listaAlumnos[posAlumno])
            if len(listaAsignaturas[posAlumno])>0:
                f.write("\n")
                for posAsignatura in range(len(listaAsignaturas[posAlumno])):
                    linea=(listaAsignaturas[posAlumno])[posAsignatura]
                    for nota in (listaNotas[posAlumno])[posAsignatura]:
                        linea +=","+str(nota)
                    if listaAsignaturas[posAlumno][posAsignatura]==listaAsignaturas[posAlumno][-1] and listaAlumnos[posAlumno]==listaAlumnos[-1]:
                        f.write(linea)
                        
                    else:
                        f.write(linea+"\n")
            elif listaAlumnos[posAlumno]!=listaAlumnos[-1]:
                f.write("\n")
            
    finally:
        f.close()
    
            
volcarFichero()



def getNotasAsignatura(alumno, asignatura):
    posAlumno=listaAlumnos.index(alumno)
    posAsignatura=listaAsignaturas[posAlumno].index(asignatura)
    notas=listaNotas[posAlumno][posAsignatura]
    
    return notas


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
            darAltaAlumno(nombreAlumno)
            mensaje="El/La alumno/a %s ha sido dado de alta en el sistema." % (nombreAlumno)
        else:
            mensaje="Error. El/La alumno/a %s ya está dado de alta en el sistema." % (nombreAlumno)
    elif opcion==2:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:    
            nombreAsignatura=input("¿De qué asignatura quiere matricular al alumno/a %s" %nombreAlumno)
            if matricularAlumno(nombreAlumno, nombreAsignatura):
                mensaje="La asignatura %s ha sido dado de alta para el/la alumno/a %s." % (nombreAsignatura, nombreAlumno)
            else:
                mensaje="Error. La asignatura %s ya está dada de alta para el/la alumno/a %s." % (nombreAsignatura, nombreAlumno)
   
    elif opcion==3:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:
            nombreAsignatura=input("¿De qué asignatura quiere matricular al alumno/a %s" %nombreAlumno)
            if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
                nota=int(input("¿Qué nota (1-10) desea añadir? "))
                ponerNotas(nombreAlumno, nombreAsignatura, nota)
                mensaje="Nota añadida"
            else:
                mensaje="Error. El alumno %s no está matriculado en la asignatura %s." % (nombreAlumno, nombreAsignatura)
    elif opcion==4:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:
            nombreAsignatura=input("¿De qué asignatura quiere matricular al alumno/a %s" %nombreAlumno)
            if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
                mensaje=getNotasAsignatura(nombreAlumno, nombreAsignatura)
            else:
                mensaje="Error. El alumno %s no está matriculado en la asignatura %s." % (nombreAlumno, nombreAsignatura)
    elif opcion==5:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:
            nombreAsignatura=input("¿De qué asignatura quiere matricular al alumno/a %s" %nombreAlumno)
            if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
                notas=getNotasAsignatura(nombreAlumno, nombreAsignatura)
                notaMayor=notas[0]
                for i in notas:
                    if i>notaMayor:
                        notaMayor=i
                mensaje="La nota máxima del alumno %s en la asignatura %s es un %s." %(nombreAlumno, nombreAsignatura, notaMayor)
            else:
                mensaje="Error. El alumno %s no está matriculado en la asignatura %s." % (nombreAlumno, nombreAsignatura)
    elif opcion==6:
        nombreAlumno = input("Introduce el nombre del alumno/a al que quieres darle de alta una asignatura: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:
            nombreAsignatura=input("¿De qué asignatura quiere matricular al alumno/a %s" %nombreAlumno)
            if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
                notas=getNotasAsignatura(nombreAlumno, nombreAsignatura)
                sumaNotas=0
                for i in notas:
                    sumaNotas+=i
                mensaje="La nota media del alumno %s en la asignatura %s es un %s." %(nombreAlumno, nombreAsignatura, (sumaNotas/len(notas)))
            else:
                mensaje="Error. El alumno %s no está matriculado en la asignatura %s." % (nombreAlumno, nombreAsignatura)
    # elif opcion==7:
    #

    elif opcion==8:
        nombreAlumno = input("Introduce el nombre del alumno/a: ")
        if nombreAlumno not in listaAlumnos:
            mensaje="Error. El/La alumno/a %s no está dado de alta en el sistema." % (nombreAlumno)
        else:
            posAlumno=listaAlumnos.index(nombreAlumno)
            mensaje=""
            for i in range (len(listaAsignaturas[posAlumno])):
                mensaje+="Asignatura: %s \n" % listaAsignaturas[posAlumno][i]
                listaNotasAsignatura=listaNotas[posAlumno][i]
                if len(listaNotasAsignatura)>0:
                    for nota in listaNotasAsignatura:
                        mensaje+="    Nota: %s\n" % nota
                else:
                    mensaje+="    No hay notas asignadas a esta asignatura.\n"
    
    else:
        mensaje=""
        for i in range (len(listaAlumnos)):
            mensaje+="\nALUMNO/A: %s\n" % (listaAlumnos[i])
            for j in range (len(listaAsignaturas[i])):
                mensaje+="    Asignatura: %s \n" % listaAsignaturas[i][j]
                listaNotasAsignatura=listaNotas[i][j]
                if len(listaNotasAsignatura)>0:
                    for nota in listaNotasAsignatura:
                        mensaje+="        Nota: %s\n" % nota
                else:
                    mensaje+="        No hay notas asignadas a esta asignatura.\n"
        
    return mensaje


def menuPrincipal():
    
    menu="1. Dar de alta un alumno/a.\n"\
        "2. Dar de alta una asignatura de un alumno/a.\n"\
        "3. Añadir una nota de una asignatura de un alumno/a.\n"\
        "4. Ver las notas que un alumno/a tienen en una asignatura.\n"\
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

    
    volcarFichero()        
    print("Hasta la próxima.")


    
main()





