from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, goles, tarjetas, pierna):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetas
        self._piernaHabil = pierna
        self._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setGolesMarcados(self, goles):
        self._golesMarcados = goles
    
    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas
    
    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna
    
    def getListaFutbolistas(self):
        return self._listaFutbolistas
    
    def setListaFutbolistas(self, lista):
        self._listaFutbolistas = lista

    def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"
