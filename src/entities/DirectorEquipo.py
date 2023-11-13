from entities.Empleado import Empleado

class DirectorEquipo(Empleado):

    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento):
        super().__init__(id, nombre, nacionalidad, salario, fecha_nacimiento)   