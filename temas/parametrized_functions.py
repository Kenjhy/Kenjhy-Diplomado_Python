def message(number):
    print("Enter a number: ", number)
message("sss")

def mesaje(numero):
    print("Ingresa un numero: ", numero)
    
numero = 1234
mesaje(1)
print(numero)

def mesaje(que, numero):
    print("Ingresa ", que, "Numero", numero)

mesaje("telefono", 11)
mesaje("telefono", 5)
mesaje("telefono", "numero")


def sum(a,b,c):
    print(a, "+", b, "+", c, "=", a + b + c)
    
sum(1,2,3)
sum(c = 1, a=2, b=3)
sum(3,c=1,b=2)
# sum(3,a=1,b=2)
sum(4,3,c=2)
# sum(4,d=3,c=2)

def introduction(firstNmae, lastName="Smith"):
    print("Hello, my name is", firstNmae, lastName)

introduction("jOHN", "Doe")
introduction("Jhohn")

valor =None
if valor == None:
    print("Lo sineto, no tienes ningun valor", valor)
    
