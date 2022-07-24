class Humano():
    #1 Contructor
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    def presentar(self):
        presentacion = ("Hola soy {}, miedad es {} y mi ocupacion es {}")
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))
    
    def contratar(self, puesto):
        self.puesto = puesto
        print("{} ha sido contratado como {} ".format(self.nombre, self.puesto))
        self.ocupacion = puesto

#Objeto
Persona1 = Humano(31, "Lizet", "Desocupado")#Instancia
Persona1.presentar()
Persona1.contratar("Obrero")
Persona1.presentar()

