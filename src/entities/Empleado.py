from abc import ABC


class Empleado(ABC):

    total_empleados = 0


    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento):
        super().__init__()
        self.total_empleados += 1
        self._id = id
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self._salario = salario
        self._fecha_nacimiento = fecha_nacimiento

    #Getters
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
    

    def __str__(self):
          return f'[Empleado {self._id}, edad {self._nombre}, sexo {self._nacionalidad}, salario {self._fecha_nacimiento}, fecha de nacimiento {self._fecha_nacimiento}]'







