#Crear la super clase Vehiculo
from statistics import mode


class Vehiculo:
    #Constructor
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    #Mostrar loq ue tiene el objeto
    def __str__(self) -> str:
        return " Color {}, marca {}".format(self.color, self.marca)
    
car = Vehiculo("Chevrolet", "negro")
print(car)

class CarroAntiguo(Vehiculo):
    def __init__(self, marca, color, modelo):
        #super().__init__(marca, color)
        Vehiculo.__init__(self, marca, color)
        self.modelo = modelo 
        
    def __str__(self):
        #super().__init__(marca, color)
        return "Color {}, marca {}, modelo {}".format(self.color, self.marca, self.modelo)
    
carAntiguo = CarroAntiguo("Negro", "BMW", "2000")
print(carAntiguo)


class CarroNuevo(Vehiculo):
    def __init__(self, marca, color, cilindrada): #Datos del carro
        #super().__init__(marca, color)
        Vehiculo.__init__(self, marca, color) #Inicializamos los datos de la superclase
        self.cilindrada = cilindrada #Atributos de intancias
        
    def __str__(self) -> str:
        #return super().__str__()
        return "Color {}, marca, {}, cilindrada {}".format(self.color, self.marca, self.cilindrada)
    #Inicializamos la clase
    #Cramos la intancia de la clase
    #2 objeto con 3 parametros, hereda  marca y color
    
carNuevo= CarroNuevo("Azul","MAZDA", "3200")
print(carNuevo)

class CarroNuevoAltaGama(CarroNuevo):
    def __init__(self, marca, color, cilindrada, costo):
        super().__init__(marca, color, cilindrada)
        #CarroNuevo.__init__(marca, color, cilindrada)
        self.costo = costo
    
    def __str__(self) -> str:
        return super().__str__()
        #return "Color {}, marca {}, cilindrada {}, costo {}".format(self.color, self.marca, self.cilindrada, self.costo)
    
    

carNuevoAltaGama = CarroNuevoAltaGama("audi", "Amarillo", 3600, "$ 400.000.000")
print(carNuevoAltaGama)
print(carNuevoAltaGama.color)
print(carNuevoAltaGama.marca)
print(carNuevoAltaGama.cilindrada)
print(carNuevoAltaGama.costo)
