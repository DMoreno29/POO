from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)

    def getNombre(self):
        return super().getNombre()
    def getEdad(self):
        return super().getEdad()
    def getHabitat(self):
        return super().getHabitat()
    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "café glorioso")
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
