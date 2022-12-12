from zooAnimales.animal import Animal
class Zona():
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, animal):
        if isinstance(animal, Animal):
            self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def setNombre(self, nombre):
        self._nombre = nombre
    def setZoo(self, zoologico):
        self._zoo = zoologico
