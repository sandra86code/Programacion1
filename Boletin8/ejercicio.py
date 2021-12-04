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

#Defino las listas arriba para que sean globales
listaAlumnos=[]
listaAsignaturas=[]
listaNotas=[]


#===============================================================================
# darAltaAlumno
# Esta función da de alta a un alumno en el sistema, es decir, añade su nombre
# a a lista de alumnos y una lista en la lista de Asignaturas y otra lista en la
# lista de notas.
# Recibe: el nombre de un alumno
# Devuelve: no tiene return, para que lo que hace la función esté disponible globalmente
# 
#===============================================================================
def darAltaAlumno(nombre):

    listaAlumnos.append(nombre)
    listaAsignaturas.append([])
    listaNotas.append([])
    

#===============================================================================
# AltaAsignaturaAlumno
# Esta función da de alta una asignatura a un alumno ya matriculado
# Recibe: el nombre del alumno y el nombre de la asignatura
# Devuelve:
# True si se ha podido matricular al alumno para esa asignatura
# False si el alumno ya estaba matriculado de esa asignatura 
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
# PonerNotas
# Esta función añade una nota en una asignatura a un alumno
# Recibe: el nombre del alumno, el nombre de la asignatura y la nota
# Devuelve:
# True si se ha podido añadir la nota al alumno en esa asignatura
# False si no se ha podido añadir la nota al alumno, bien sea porque el alumno
# no está dado de alta en el sistema o porque, estando dado de alta, no está
# matriculado en esa asignatura
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


#===============================================================================
# getNotas 
# Esta función, partiendo de una parte de una linea de un archivo txt, correspondiente
# a las notas de un alumno en una asignatura, crea una lista de tipo entero con las notas
# Recibe: una linea de caracteres
# Devuelve: una lista de tipo entero con las notas
#===============================================================================
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
        

#===============================================================================
# getAsignatura 
# Esta función, partiendo de una parte de una linea de un archivo txt, obtiene 
# el nombre de una asignatura
# Recibe: una linea de caracteres
# Devuelve: una variable de tipo string con el nombre de la asignatura
#===============================================================================
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


#===============================================================================
# getAlumno
# Esta función, partiendo de una linea de un archivo txt, obtiene 
# el nombre de un alumno
# Recibe: una linea de caracteres
# Devuelve: una variable de tipo string con el nombre del alumno
#===============================================================================
def getAlumno(linea):
    
    alumno=""
    for i in range (len(linea)):
        if linea[i]!="*":
            alumno+=linea[i]
    
    return alumno


#===============================================================================
# Esta función lee un fichero .txt y convierte sus datos a formato cadenas, para
# poder trabajar con ellos en el programa. En concreto, una lista de Alumnos, una
# lista de Asignaturas (relacionadas sus posiciones con la de los alumnos) y una
# lista de notas de las asignaturas (relacionadas sus posiciones con la de los alumnos
# y las de las asignaturas).
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene return
#===============================================================================
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


#===============================================================================
# Esta función, una vez terminado el programa, vuelca en el fichero txt todos los
# cambios que se hayan producido en las listas, en el formato adecuado para ello
# Recibe: no tiene parámetros de entrada.
# Devuelve: no tiene return.
#===============================================================================
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


#===============================================================================
# Esta función extrae la lista de notas de un alumno en una determinada asignatura
# Recibe: nombre del alumno y nombre de la asignatura
# Devuelve: la lista de notas
#===============================================================================
def getNotasAsignatura(alumno, asignatura):
    
    posAlumno=listaAlumnos.index(alumno)
    posAsignatura=listaAsignaturas[posAlumno].index(asignatura)
    notas=listaNotas[posAlumno][posAsignatura]
    
    return notas


#===============================================================================
# Esta función nos dice la posición que tiene una asignatura asociada a un alumno
# dentro de la lista de asignaturas
# Recibe: el nombre del alumno
# Devuelve: la lista de asignaturas asociada a ese alumno
#===============================================================================
def getAsignaturasAlumno(alumno):
    
    posAlumno=listaAlumnos.index(alumno)
    
    return listaAsignaturas[posAlumno]


#===============================================================================
# Esta función recibe un mensaje y lo imprime
# Recibe: un mensaje (cadena de texto)
# Devuelve: no tiene return
#===============================================================================
def mostrarMensaje(mensaje):
    
    print(mensaje)
    
    
#===============================================================================
# Esta función da de alta a un alumno (lo añade a la lista de alumnos, le añade
# una lista vacía en la lista de asignaturas, y le añade una lista vacía dentro 
# de otra lista vacía en la lista de notas) si no está previamente dado de alta.
# Pide el nombre del alumno.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================    
def pedirAlumnoMatricular():
    
    nombreAlumno = input("Nombre del alumno/a que quieres dar de alta: ")
    if nombreAlumno not in listaAlumnos:
        darAltaAlumno(nombreAlumno)
        mostrarMensaje("%s ha sido dado/a de alta." % (nombreAlumno))
    else:
        mostrarMensaje("Error. %s ya estaba dado/a de alta." % (nombreAlumno))
        

#===============================================================================
# Esta función da de alta una asignatura a un alumno, siempre y cuando el alumno
# esté ya dado de alta y no esté matriculado previamente en esa asignatura.
# Pide el nombre del alumno y luego el nombre de la asignatura.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================
def pedirAsignaturaMatricular():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta. Debe darlo/a de alta antes de matricularlo en una asignatura." % (nombreAlumno))
    else:    
        nombreAsignatura=input("Nombre de la asignatura: ")
        if matricularAlumno(nombreAlumno, nombreAsignatura):
            mostrarMensaje("La asignatura %s ha sido dado de alta para %s." % (nombreAsignatura, nombreAlumno))
        else:
            mostrarMensaje("Error. %s ya estaba matriculado/a en la asignatura %s." % (nombreAlumno, nombreAsignatura))
  

#===============================================================================
# Esta función añade una nota a un alumno en una asignatura, siempre y cuando
# el alumno esté dado de alta y esté matriculado en la asignatura.
# Pide el nombre del alumno y luego el nombre de la asignatura.
# Luego llama a la función que imprime mensaje correspondiente.
#=============================================================================== 
def pedirAnnadirNota():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta. Debe darlo/a de alta y matricularlo en una asignatura antes de poder añadirle una nota." % (nombreAlumno))
    else:
        nombreAsignatura=input("Nombre de la asignatura: ")
        if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
            nota=int(input("Nota a añadir [1-10]: "))
            ponerNotas(nombreAlumno, nombreAsignatura, nota)
            mostrarMensaje("Nota añadida para %s en la asignatura %s" % (nombreAlumno, nombreAsignatura))
        else:
            mostrarMensaje("Error. %s no está matriculado/a en la asignatura %s, primero debe darlo/a de alta." % (nombreAlumno, nombreAsignatura))
                
    
#===============================================================================
# Esta función muestra las notas de un alumno en una asignatura, siempre y cuando
# el alumno esté dado de alta y esté matriculado en un asignatura.
# Pide el nombre del alumno, luego el nombre de la asignatura y luego la nota
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================               
def mostrarNotasAlumnoEnAsignatura():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta." % (nombreAlumno))
    else:
        nombreAsignatura=input("Nombre de la asignatura: ")
        if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
            notas=getNotasAsignatura(nombreAlumno, nombreAsignatura)
            if len(notas)>0:
                mostrarMensaje("Notas de %s en %s: " %(nombreAlumno,nombreAsignatura))
                for i in range (len(notas)):
                    mostrarMensaje(str(notas[i]))
            else:
                mostrarMensaje("%s aún no tiene notas en la asignatura %s." %(nombreAlumno, nombreAsignatura))
        else:
            mostrarMensaje("Error. %s no está matriculado/a en la asignatura %s." % (nombreAlumno, nombreAsignatura))
     

#===============================================================================
# Esta función muestra la nota máxima de un alumno en una asignatura, siempre y 
# cuando el alumno esté dado de alta y esté matriculado en un asignatura.
# Pide el nombre del alumno y luego el nombre de la asignatura.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================     
def getNotaMaximaAlumno():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta." % (nombreAlumno))
    else:
        nombreAsignatura=input("Nombre de la asignatura: ")
        if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
            notas=getNotasAsignatura(nombreAlumno, nombreAsignatura)
            notaMayor=notas[0]
            for i in notas:
                if i>notaMayor:
                    notaMayor=i
            mostrarMensaje("La nota máxima de %s en la asignatura %s es un %s." %(nombreAlumno, nombreAsignatura, notaMayor))
        else:
            mostrarMensaje("Error. %s no está matriculado/a en la asignatura %s." % (nombreAlumno, nombreAsignatura))
    
    
#===============================================================================
# Esta función muestra la nota media de un alumno en una asignatura, siempre y 
# cuando el alumno esté dado de alta y esté matriculado en un asignatura.
# Pide el nombre del alumno y luego el nombre de la asignatura.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================     
def getNotaMedia():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta." % (nombreAlumno))
    else:
        nombreAsignatura=input("Nombre de la asignatura: ")
        if matricularAlumno(nombreAlumno, nombreAsignatura)==False:
            notas=getNotasAsignatura(nombreAlumno, nombreAsignatura)
            sumaNotas=0
            for i in notas:
                sumaNotas+=i
            mostrarMensaje("La nota media de %s en la asignatura %s es un %s." %(nombreAlumno, nombreAsignatura, (sumaNotas/len(notas))))
        else:
            mostrarMensaje("Error. %s no está matriculado/a en la asignatura %s." % (nombreAlumno, nombreAsignatura))
        

#===============================================================================
# Esta función muestra las asignaturas en las que está matriculado un alumno, 
# siempre y cuando el alumno esté dado de alta.
# Pide el nombre del alumno.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================      
def mostrarAsignaturasAlumno():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta." % (nombreAlumno))
    else:
        asignaturas=getAsignaturasAlumno(nombreAlumno)
        if len(asignaturas)>0:
            mostrarMensaje("%s está matriculado/a en: " % (nombreAlumno))
            for i in range (len(asignaturas)):
                mostrarMensaje(asignaturas[i])
        else:
            mostrarMensaje("%s no está matriculado/a en ninguna asignatura." % (nombreAlumno))
            

#===============================================================================
# Esta función muestra las notas de un alumno por asignatura, siempre y cuando
# el alumno esté dado de alta.
# Pide el nombre del alumno.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================
def mostrarNotasAlumno():
    
    nombreAlumno = input("Nombre del alumno/a: ")
    if nombreAlumno not in listaAlumnos:
        mostrarMensaje("Error. %s no está dado/a de alta." % (nombreAlumno))
    else:
        posAlumno=listaAlumnos.index(nombreAlumno)
        if len(listaAsignaturas[posAlumno])>0:
            for i in range (len(listaAsignaturas[posAlumno])):
                mostrarMensaje("Asignatura: %s" % listaAsignaturas[posAlumno][i])
                listaNotasAsignatura=listaNotas[posAlumno][i]
                if len(listaNotasAsignatura)>0:
                    for nota in listaNotasAsignatura:
                        mostrarMensaje("    Nota: %s" % nota)
                else:
                    mostrarMensaje("    No hay notas asignadas a esta asignatura.")
        else:
            mostrarMensaje("%s no está matriculado/a en ninguna asignatura." % (nombreAlumno))


#===============================================================================
# Esta función muestra las notas de cada asignatura de cada uno de los alumnos 
# dados de alta.
# Luego llama a la función que imprime mensaje correspondiente.
#===============================================================================
def mostrarContenidoSistema():
    
    for i in range (len(listaAlumnos)):
        mostrarMensaje("\nALUMNO/A: %s" % (listaAlumnos[i]))
        for j in range (len(listaAsignaturas[i])):
            mostrarMensaje("    Asignatura: %s" % listaAsignaturas[i][j])
            listaNotasAsignatura=listaNotas[i][j]
            if len(listaNotasAsignatura)>0:
                for nota in listaNotasAsignatura:
                    mostrarMensaje("        Nota: %s" % nota)
            else:
                mostrarMensaje("        No hay notas asignadas a esta asignatura.")

                      
#===============================================================================
# Esta función gestiona el menú de opciones del programa.
# Con cada opción, llama a la función correspondiente.
#===============================================================================
def gestionarMenu(opcion):
    
    if opcion==1:
        pedirAlumnoMatricular()
    
    elif opcion==2:
        pedirAsignaturaMatricular()
   
    elif opcion==3:
        pedirAnnadirNota()
    
    elif opcion==4:
        mostrarNotasAlumnoEnAsignatura()
    
    elif opcion==5:
        getNotaMaximaAlumno()
    
    elif opcion==6:
        getNotaMedia()
    
    elif opcion==7:
        mostrarAsignaturasAlumno()

    elif opcion==8:
        mostrarNotasAlumno()
            
    elif opcion==9:
        mostrarContenidoSistema()
        


#===============================================================================
# Esta función es el menú principal del programa, que muestra todas las opciones.
# Recibe: no tiene parámetros de entrada
# Devuelve: la variable menú, de tipo string, con todas las opciones.
#===============================================================================
def menu():
    
    menu="1. Dar de alta un alumno/a.\n"\
        "2. Dar de alta una asignatura de un alumno/a.\n"\
        "3. Añadir una nota de una asignatura de un alumno/a.\n"\
        "4. Ver las notas que un alumno/a tienen en una asignatura.\n"\
        "5. Ver la nota que un alumno/a tendría en una asignatura suponiéndole la nota máxima.\n"\
        "6. Ver la nota que un alumno/a tendría en una asignatura suponiéndole la nota media.\n"\
        "7. Ver todas las asignaturas en las que está matriculado un/a alumno/a.\n"\
        "8. Ver todas las notas de todas las asignaturas de un alumno/a.\n"\
        "9. Ver todas las notas de todas las asignaturas de todos los alumnos/a.\n"\
        "10. Salir.\n"\

    return menu


#===============================================================================
# Esta función es la principal del programa, que interactua con el usuario,
# imprime los resultados de las opciones y si la opción elegida es la de salir,
# guarda los cambios producidos en el programa en el archivo .txt asociado.
# Recibe: no tiene parámetros de entrada
# Devuelve: no tiene parámetros de salida
#===============================================================================
def main():
    
    linea="\n-----------------------------------------------------------------------------\n"
    bienvenida="Bienvenido/a al menú principal del sistema de registro del alumnado del IES Jacarandá."
    
    opcion=1
    
    #Mientras que la opción no sea 10 (salida)
    while opcion!=10:
        print(linea)
        print(bienvenida)
        print(menu())
        
        opcion=int(input("¿Qué opción desea? "))
        while opcion<1 or opcion>10:
            print("Opción incorrecta. Vuelve a intentarlo.")
            opcion=int(input("¿Qué opción desea? "))
        
        print(linea)
        
        #Llamamos a la función que gestiona el menú con cada una de las opciones
        gestionarMenu(opcion)

    #Cuando salgamos del bucle (opcion==10), llamamos a la función que vuelca
    #la información en el fichero e imprimimos un mensaje    
    volcarFichero()        
    print("Hasta la próxima.")


main()

