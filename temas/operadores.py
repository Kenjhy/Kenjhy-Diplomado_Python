from cmath import e
from contextlib import AbstractAsyncContextManager
from re import A


i = 15
j = 22
bit = i & j #Ampersat
print(bit)

i = 15
j = 22
bit = i and j
print(bit)

i = 15
j = 22
bit = i | j
print(bit)

i = 15
j = 22
bit = i or j
print(bit)

var = 16
varRight = var >> 1 #Desplazamiento binadio a la derecha
varLeft = var << 2 #Desplazamiento binadio a la izquierda
print(var, varLeft, varRight)

x = 4 
y = 1

a = x & y 
b = x | y
c = ~ x #Negado o not
d = x ^ 5 #Or esclusivo , ley de signos, cuando los signos dan un valor cuando dan otros da otr
e = x >> 2
f = x << 2

