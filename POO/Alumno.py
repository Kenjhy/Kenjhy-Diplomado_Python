class Alumno:
    
    #Constructos o inicializador, crea instancia de clase y define que todas las fguciones hagan parte de la clase
    def __init__(self, nombre, apellido):
        self.nombre = nombre #Atributos
        self.apellido = apellido #Atributos
    #pass
    #Funciones o metodos (argumentos) selft = es una referencia a la intancia de la clase
    def saludar(self):
        print("Saludar Hola, profesor")
        print(f"saludar selft, {self.nombre}!")
        print("saludar format{}, {}".format(self.nombre, self.apellido))
        print()
    
    def despertarse(self):
        print("despertarse")
        print("despedirse format{}".format(self.nombre))
        print()

#Objetos
estudiante_a_objeto = Alumno("argumento_daniel", "pamplona") #Instanciacion
estudiante_b_objeto = Alumno("argumento_pepito", "pamplona") #Instanciacion
#alumno_parametro_objeto = Alumno() #Instanciacion

#Llamar o usar las funciones
estudiante_a_objeto.saludar()
estudiante_a_objeto.despertarse()

estudiante_b_objeto.saludar()
estudiante_b_objeto.despertarse()


