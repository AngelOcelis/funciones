#1. Diseñe una aplicación que, dada una lista de 10 elementos, realice las siguientes acciones:
#a. Recorrer la lista y mostrar el contenido de la lista.
def listanew():
    lista=[]
    for i in range(10):
        valor=input(":: Ingrese Un Elemento:  ::")
        lista.append(valor)  
    return lista
#b. Hacer una función que recorra la lista y devuelva una cadena con los valores de la lista.
"""La función map aplica la función str a todos los elementos de la lista, y devuelve un objeto map iterable.
"".join() itera todos los elementos en el objeto map y devuelve los elementos concatenados como una cadena"""
def devolverlista(lista):
        print(",".join(map(str,lista)))       
def ordenarlista(lista):
    print(sorted(lista))
#c. Ordenarla de mayor a menor
#reverse por otra parte, tiene un valor booleano de True o False    
def revertlista(lista):
    lista.sort(reverse=True)
    print(lista)
#d. Buscar un elemento que el usuario pida por teclado
#e. Mostrar su tamaño o longitud
def elemento(lista):
    if valor in lista:
        lista.index(valor)
        print(f':: La Longitud De La Lista es:   :: ',len(lista))
#Programa Principal
lista=listanew()
print("El Contenido De La lista es : ", lista)    
rango=devolverlista(lista)
ordenarlista(lista)
revertlista(lista)
valor=input(":: Ingrese Un Elemento:  ::")
print(lista.index(valor))
elemento(lista)











