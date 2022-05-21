#Diseñe un algoritmo que defina una lista vacia y luego le agregue valores a la lista, 
# teniendo en cuenta que su longitud debe ser menor a la digita por el usuario
lista=[]
longi = int(input("Digite el tamaño de la lista: "))
longi = longi-1
i = 0
while i != longi:
    elemento = (input("Digite el valor de la lista: "))
    i += 1
    lista.append(elemento)
print(lista)