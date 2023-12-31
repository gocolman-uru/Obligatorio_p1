from entities.Empleado import Empleado

class DirectorEquipo(Empleado):

    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento):
        super().__init__(id, nombre, nacionalidad, salario, fecha_nacimiento)   
        self._id=id
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self._salario = salario
        self._fecha_nacimiento = fecha_nacimiento


    @property
    def id(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def nacionalidad(self):
        return self._nacionalidad
    @property
    def salario(self):
        return self._salario
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    


        