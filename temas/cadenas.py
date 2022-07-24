from numpy import tile


palabra = 'por'
print(len(palabra))

vacio = ''
print(len(vacio))

yo_soy = 'I\'m'
print(len(yo_soy))

multiLinea = '''Linea #1
Linea #2'''
print(len(multiLinea))

str1 = 'a'
str2 ='b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#Doy el codigo acsii 
ch1 = "@"
ch2 = ' ' # espacio
ch3 = "["

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))

# Doy el numero y me devuelve el codigo acsii
print(chr(64))
print(chr(945))

alpha = "abcdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[::2])
print(alpha[::3])
print(alpha[1::2])

alpfabeto = "abcdefghijklmnñopkrsyuvwxyxz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("l" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)

print(min("aAbByYzZ"))

t = [0,1,2]
print(min(t))

print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

print(list("abcabc"))
print("abcabc".count("b"))
print("abcabc".count("d"))
print("aBcD".capitalize())

#Letras o umeros
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#Solo letras
print("Mooo".isalpha())
print("Mu40".isalpha())

#Solo numeros
print("2018".isdigit())
print("Añp2019".isdigit())
print()
print("Mooo".islower())
print("mooo".islower())
print("___")
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
print("___")
print("Moooo".isupper())
print("moooo".isupper())
print("MOOOO".isupper())
print("___")

print()
print("SiGma=60".lower())

print()
#Cadena metodo argumentos, reemplazar, por reemplazar
print("www.netacad.com".replace("www.netacad.com", "ttt"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print()
print("Hugo     Alexander   Peña".split())

#cREAN UNA NUEVA CADENA
print()
print("Yo sé que no.".swapcase())
print("Yo sé que no.".title())
print("Yo sé que no.".upper())

secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)
