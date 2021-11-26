'''
# coding: utf-8 
 @autor: Sandra Ruiz Jimenez
 @fecha: 26 nov 2021
 @nombre: Notas Alumnos
 @enunciado: 
 Vamos a escribir un ejercicio para que un profesor almacene las notas de las asignaturas de los
alumnos, para ello vamos a crear un men� con las siguientes opciones:
    1. Dar de alta un alumno/a
    2. Dar de alta una asignatura de un alumno/a
    3. A�adir una nota de una asignatura de un alumno/a
    4. Ver las notas que un alumno/a tienen en una asignatura.
    5. Ver la nota que un alumno/a tendr�a en una asignatura suponi�ndole la nota m�xima
    6. Ver la nota que un alumno/a tendr�a en una asignatura suponi�ndole la nota media.
    7. Ver todas las notas de una asignatura de un alumno/a
    8. Ver todas las notas de todas las asignaturas de un alumno/a
    9. Ver todas las notas de todas las asignaturas de todos los alumnos/a
    10. Salir

Para realizar el programa vamos a tener un array o lista de alumnos, un array o lista de listas de
asignaturas y un array o listas de listas de notas de asignaturas es decir ser�a algo como:

Lista de alumnos/as:
0                            |  1                                    | 2                        | 3
Inma                         |  Juan                                 | Pepe                     | Pablo

Lista de asignaturas de los alumnos/as:
Lengua     Mates     Infor   |  Infor.   Mates     Ingl�s   Lengua   | Ciencias                 | Ingl�s     Franc�s
0          1         2       |  0        1         2        3        | 0                        | 0          1

Lista de notas de las asignaturas de los alumnos/as
[10, 9]   [10,9,8]   [10]    |  [8]     [5,6,2,4]  [5]      [8]      | [4,5]                    | [7]        [1,4]

'''



def annadirAlumno(nombre):
    listaAlumnos.append(nombre)
    listaAsignaturas.append([])
    listaNotas.append([])
    

def annadirAsignaturaAlumno(nombreAlumno, nombreAsignatura):
    if nombreAlumno in listaAlumnos:
        pos = listaAlumnos.index(nombreAlumno)
        listaAsignaturas[pos].append(nombreAsignatura)
        listaNotas[pos].append([])
        return True
    else:
        return False
    
listaAlumnos=[]
listaAsignaturas=[]
listaNotas=[]

nombre = input("Introduce un alumno")
annadirAlumno(nombre)
nombre = input("Introduce un alumno")
annadirAlumno(nombre)
print(listaAlumnos)
print(listaAsignaturas)
print(listaNotas)

for i in range(5):
    nombreAlum = input("Introduce un alumno que quieres matricular")
    nombreAsig = input("Introduce la asignatura")
    if annadirAsignaturaAlumno(nombreAlum, nombreAsig) == False:
        print("Alumno no matriculado")
    


print(listaAlumnos)
print(listaAsignaturas)
print(listaNotas)

for i in range(len(listaAlumnos)):
    print(listaAlumnos[i], "se encuentra matriculado en las siguientes asignaturas:")
    listaAigAlumno = listaAsignaturas[i]
    for asign in listaAigAlumno:
        print(asign)
        











# print(listaAlumnos)
# print(listaAsignaturas)