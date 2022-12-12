class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, cColor):
        if cColor == "rojo":
            self.color = cColor
        elif cColor == "verde":
            self.color = cColor
        elif cColor == "amarillo":
            self.color = cColor
        elif cColor == "negro":
            self.color = cColor
        elif cColor == "blanco":
            self.color = cColor


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,cRegistro):
        self.registro = cRegistro
    
    def asignarTipo(self, cTipo):
        if cTipo == "electrico":
            self.tipo = cTipo
        elif cTipo == "gasolina":
            self.tipo = cTipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados=0):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        cAsientos = list(filter(lambda x: x!=None, self.asientos))
        return len(cAsientos)

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        else:
            cNoNone = list(filter(lambda x: x!=None, self.asientos))
            cAsientos = list(filter(lambda x: x.registro != self.registro, cNoNone))
            if len(cAsientos) != 0:
                return "Las piezas no son originales"
            else:
                return "Auto original"

