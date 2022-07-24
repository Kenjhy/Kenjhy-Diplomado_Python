
colors = {
    "blue": "azul",
    "red": "rojo",
    "yellou": "amarillo",
    "green": "verde",
    4: "black",
    "otro": True,
    "lista": [4,"3","cuatro"],
    "oter_dictionaries": {
        "a": "a",
        "pera": "manzana"
    },
    dict:{
        "numero": "num",
        "uno": 1
    }
    
}

print(colors)
print(colors["blue"])
print(colors[4])
print(colors["lista"][1])
colors["yellou"]=000
print(colors)
print(colors[dict])

print()
for key in colors:
    print(key)
    print(key, ':', colors[key])

#Trae todas las llaves en lista
dic = colors.keys()
print(dic)
print()
#Trae todos los valores en lista
dic = colors.values()
print(dic)
#Convierte el diccionario en tuplas, quitando consepto llave valor y dejarlo en datos normales
print("item")
dic = colors.items()
print(dic)
print()
#Convierte el diccionario en tuplas, quitando consepto llave valor y dejarlo en datos normales
colors_copia = colors.copy()
print("copia")
print(colors_copia)

print()
vr=colors

print(vr)

print()
d1 = {1:'hola',89:'Python','a':'b','c':27}
print(d1)
print()
#dict permite usar el constructor de esa clase para crear DICIONARIOS
d2 = dict({'uno':1,'dos':2,'tres':3})
print(d2)
print()
#dict tuplapermite usar el constructor de esa clase para crear DICIONARIOS
d3 = dict(uno=1,dos=2,tres=3)
print(d3)
print()
#dict tuplas listas de 2 elementospermite usar el constructor de esa clase para crear DICIONARIOS
d4 = dict([('uno',1),('dos',2),('tres',3)])
print(d4)
print()
#dict tuplas listas en listasde 2 elementospermite usar el constructor de esa clase para crear DICIONARIOS
d41 = dict([('uno',1),('dos',2),('tres',3),[('cuatro',4),('quinto',5)]])
print(d41)
print()
#dict vacio
d5 = dict()
print(d5)