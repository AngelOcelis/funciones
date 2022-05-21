#a. Ingresar estudiantes
alumnos={}
def entrarnombre():
    for i in range(2):
        codigo_alumno= int(input("Ingrese El Codigo: "))
        nombre=input("Ingrese el nombre: ")
        nota1=float(input("Ingrese la nota 1:  "))
        nota2=float(input("Ingrese la nota 2:  "))
        estudiantes.append(alumnos)
        i=i+1
        alumnos[codigo_alumno]=[nombre, [nota1 , nota2]]
    return alumnos
#b. Listar estudiantes
"""La función map aplica la función str a todos los elementos de la lista, y devuelve un objeto map iterable.
"".join() itera todos los elementos en el objeto map y devuelve los elementos concatenados como una cadena"""
def listarestudiantes():
    print("\n".join(map(str,estudiantes)))
#c. Modificar notas de un estudiante por código
def modificarnota():
    codigo_alumno=int(input("Ingrese El Codigo Del Alumno:  "))
    cambiar_nota=int(input("Que Nota Desea Cambiar:  "))
    nueva_nota=float(input("Ingrese La Nueva Nota:  "))
    alumnos[codigo_alumno][1][cambiar_nota]=nueva_nota
#d. Consultar la nota definitiva de un estudiante por código

    
def Menú():
    print("---------------------------------------------------------------")
    print ("Selecciona una opción...")
    print ("\t1 - Añadir Estudiante y Codigo")
    print ("\t2 - Listar Esudiantes")
    print ("\t3 - Modificar Nota Por Codigo")
    print ("\t4 - Definitiva Por Codigo")
    print ("\n\t0 - Salir")
estudiantes=[]
while True:
    Menú ()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion=-1
    if opcion == 1:
        entrarnombre()
    elif opcion == 2:
        listarestudiantes()
    elif opcion == 3:
        modificarnota()
    elif opcion == 4:
        notadefinitiva()
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")

