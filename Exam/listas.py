lista = [5,7,8,"hola",True,9,7, [6, "mundo"] ]

print(lista)
print(lista[3]) #indice
print(lista[2:4]) #rango
print(lista[-1]) #
print(lista[7])
print(lista[-1][1])#Se para en el ultimo valor y saca el valor de la lista interna
print(lista[7][1])#Se para en el ultimo valor y saca el valor de la lista interna
print(lista[0:8:2]) #Desde la pocicion hasta la pocicion, cada 2 elementos
print(lista[::-1]) #Imprime la lista al revez, sentido inverso
lista[1] ="andina"
print(lista)
lista[2],lista[4] = lista[4],lista[2] #Cambiar la ubiccion dentro de una lista
print(lista)
print()

lista_a = [4,5,5,7 ]

lista_total = lista + lista_a #Concaternar listas

print(lista_total)

for i in lista_total:
    print(i)
    
print()
for i in lista_total[3:6]:
    print(i)
    
print()
for i in lista_total[::-1]:
    print(i)
    
print()
print(len(lista_total))#Cuenta cantidad de elementos de una lista

print()
lista=[]
print(lista)
print()
lista.append(4)
print(lista)
print()
lista.append(6)
print(lista)
print()
lista.append(6)
print(lista)
print()
lista.append(3.9)
print(lista)
print()
# lista.append("Hola")
# print(lista)
print()
print(lista.count(6)) #Cantidad de ve
print()
print(lista.index(4)) #La posicion donde encuentra por primera vez el dato
print()
lista.sort() #Ordenar menor a mayor
print(lista)
lista.reverse() #al revez
print(lista)
print()
del lista[1] #indice a eleiminar
print(lista)
lista.extend([4,6,8,9]) #Extender, concatenar o agregar nuevos valores
print(lista)
lista.remove(3.9)
print(lista)
lista.pop(0)
print(lista)
lista.clear()
print(lista)
# lista.insert()
# print(lista)

myList=[]
for i in range(5):
    myList.append(i+1)
print(myList)

