class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon
    def __repr__(self):
        ret = self._nombre +' '+self._salon
        return ret