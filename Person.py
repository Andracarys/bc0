"""
#this is a test
print ("chau world")
print ("chauuuuuu")
print ("E´a")
print ("y bueno")
"""

class Persona:
    
    nombre = None
    edad = None
    sexo = None

    def __init__ (self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        print("Hola soy ",self.nombre,", tengo ",self.edad," anhos, y soy ",self.sexo, ".")

    def getnombre(self):
        return self.nombre
    
    def getedad(self):
        return self.edad

    def getsexo(self):
        return self.sexo

Andrea = Persona("Andrea", 28, "mujer")

print(Andrea.edad)

