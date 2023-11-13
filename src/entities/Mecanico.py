from entities.Empleado import Empleado


class Mecanico(Empleado):

    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento, score):
        super().__init__(id, nombre, nacionalidad, salario, fecha_nacimiento) 
        self._score = score


    #Getters
    @property
    def score(self):
        return self._score



