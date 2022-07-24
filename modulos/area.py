def area_cuadrado():
    lado = float(input("Ingrese el vlor del lado: "))
    return print("El area del cuadrado es: ", lado**2)



def area_rectangulo():
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    return print("El area del rectangulo es", base* altura)



def area_circulo():
    pi = 3.1416
    lado = float(input("Ingrese el valor del radio: "))
    return print("El area del cuadrado es: ", pi * lado ** 2)

if __name__==("__main__"):
    print(__name__)
    print("en este momento soy el archivo principal")
    #Evalue
    area_cuadrado()
    area_rectangulo()
    area_circulo()
else:
    print("me comporto como un modulo area")
    print(__name__)