from gestion.zona import Zona
class Zoologico():
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        if isinstance(zona, Zona):
            self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for Zona in self._zonas:
            totalAnimales += Zona.cantidadAnimales()
        return totalAnimales

    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def setNombre(self, nombre):
        self._nombre = nombre
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getZona(self):
        return self._zonas