numero = 6 
suma = 0
while numero <=10:
    suma += numero
    numero = numero+1
    print(numero)
print("la suma es", suma)


# largestNumber = -999999999
# number = int(input("Introdusca un numero o escriba -1 para detener: "))
# while number != -1:
#     if number > largestNumber:
#         largestNumber = number
#     number = int(input("Introdusca un numero o escriba -1 para detener: " ))
# print("El numero mas grande es:", largestNumber)


for i in range(20,40): #Donde inicia, y donde finaliza, intervalo
    print(i)
    
print()
    
for i in range(20,40,5): #Donde inicia, y donde finaliza, intervalo
    print(i)

print()

cantidad=int(input("Cuantos saludos quiere?"))
for i in range(cantidad): #Donde inicia, y donde finaliza, intervalo
    print(i, "hola")

print()

cantidad=int(input("Cuantos saludos quiere 2?"))
for i in cantidad: #Donde inicia, y donde finaliza, intervalo
    print(i, "hola")

print()

nombre=input("Cual es u nombre: ")
for i in nombre: #Donde inicia, y donde finaliza, intervalo
    print(i)
    
print()
    
nombre=input("Quien va  ha ser el presidente: ")
for i in nombre: #Donde inicia, y donde finaliza, intervalo
    print(i)
print("Que dice")
print(nombre, "Presidente")

