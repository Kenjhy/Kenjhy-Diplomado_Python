import math
from math import sin, cos, tan, pi, ceil, floor, hypot, sqrt
from math import *
import math as m
from platform import platform
from platform import machine
from platform import processor
from platform import system
from platform import version
from platform import python_implementation, python_version_tuple

x=1.4
y=2.6
ad=90

def sin_(x):
    if 2*x==pi_:
        return 0.99999999
    else:
        return None
    
pi_ = 3.14

print(sin_(pi_/2))
print(math.sin(math.pi/2))
print(sin(pi/2))
print(m.sin(m.pi/2))

print()

print(pi)
print(sin(pi/2))
print(cos(ad))
print(tan(ad))
print(floor(x), floor(y)) 
print(ceil(x),ceil(y))
print(hypot(x,y))
print(sqrt(144))

print()

print(platform())
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
print(python_version_tuple())
