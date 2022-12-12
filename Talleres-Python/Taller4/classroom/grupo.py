

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        values = kwargs.values()
        self._asignaturas = values

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            self.listadoAlumnos = [alumno]
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __repr__(self):
        ret = "Grupo de estudiantes: "+self._grupo
        return ret
