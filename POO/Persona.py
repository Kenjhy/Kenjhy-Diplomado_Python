class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape
    
    #Imprimir el parametro objeto y no la hubicacion en memoria
    def __str__(self): #str = hace que con un solo parametro self, se retorna los prametros de la clase persona
        cadena = self.nombre + ", " + self.apellido
        return cadena
        
persona1 = Persona("Jose", "Rodriguez")
print(persona1)

persona2 = Persona("Daniel", "Vargas")
print(persona2)