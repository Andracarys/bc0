class Dino:
    paatas = 4
    noombre = None
    def __init__(self, paatas, noombre):
        self.patas = paatas
        self.nombre = noombre
        print("Hola soy un dino," "me llamo", self.nombre, "y tengo", self.patas)

    def get_patas(self):
        return self.patas

    def get_patas(self, cantidad):
        self.patas = cantidad
    
    def cortar_pata(self):
        self.paatas = self.paatas - 1

pepito = Dino(4,"Pepito")

"""
En el archivo.py crear una clase Persona con atributo nombre, despues instanciar un obejto de tipo persona.
"""

