def perimetro_cuadrado():
    lado = float(input("Ingrese el vlor del lado: "))
    return print("El perimetro del cuadrado es: ", lado**2)



def perimetro_rectangulo():
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    return print("El perimetro del rectangulo es", base* altura)



def perimetro_circulo():
    pi = 3.1416
    lado = float(input("Ingrese el valor del radio: "))
    return print("El perimetro del cuadrado es: ", pi * lado ** 2)

if __name__==("__main__"):
    print(__name__)
    print("en este momento soy el archivo principal per")
    #Evalue
    perimetro_cuadrado()
    perimetro_rectangulo()
    perimetro_circulo()
else:
    print("me comporto como un modulo perimetros")
    print(__name__)