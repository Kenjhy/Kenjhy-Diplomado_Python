# import areas
# import areas as a
#from Devnet.perimetros import perimetro_cuadrado
#sto hace que se cree el archivo _pyacahe y sus archivos por dentro_
from areas import area_circulo,area_cuadrado,area_rectangulo
from perimetros import *
#from areas import *
#from ..Devnet.modulos import perimetro
#import "./Devnet/modulos/perimetro"
#areas.area_cuadrado()

from sys import path
from modulos.area import area_circulo,area_cuadrado,area_rectangulo
from modulos.perimetro import *

path.append('..\\modulos')
area_cuadrado()
perimetro_circulo()
#perimetro.perimetro_cuadrado()

def calculo():
    print("$"*40)
    print("Calculo de figuras")
    print("$"*30)
    
    figura = input("Ingrese el nombre de la figura: ")
    
    if figura == "cuadrado":
        area_cuadrado()
        perimetro_cuadrado()
    elif figura == "circulo":
        area_circulo()
        perimetro_circulo()
    elif figura == "rectangulo":
        area_rectangulo()
        perimetro_rectangulo()
    else:
        print("figura no contemplada")

#EntryPoint
if __name__==("__main__"):
    calculo()
    
        
    