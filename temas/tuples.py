#region 1
#Funciona como una lista
miTupla=(1,10,100,1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])
#endregion
for elem in miTupla:
    print(elem)

print()
t1 = miTupla + (1000,10000) #Concatena
t2=miTupla*3 #Multiplica

print(len(t2))
print(t1)
print(t2)

#region no se puede eliminar, editar, ni agregar
#miTupla.append(10000) 

#del miTupla[0]
#miTupla[1] = -10
#endregion
