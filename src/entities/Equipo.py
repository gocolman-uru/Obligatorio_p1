

class Equipo():
    def __init__(self, nombre_equipo, pilotos, director_de_equipo, mecanico, auto):
        self._nombre_equipo = nombre_equipo
        self._pilotos = pilotos
        self._director_de_equipos = director_de_equipo
        self._mecanicos = mecanico
        self._auto = auto

    @property
    def nombre_equipo(self):
        return self._nombre_equipo
    
    @property
    def pilotos(self):
        return self._pilotos
    
    @property
    def director_de_equipo(self):
        return self._director_de_equipos
    
    @property
    def get_mecanico(self):
        return self._mecanicos
    
    @property
    def get_auto(self):
        return self._auto
    

    def __str__(self) -> str:
        return f'Equipo: {self._nombre_equipo}, pilotos {self._pilotos}, director de equipo {self._director_de_equipos}, mecanicos {self._mecanicos}, auto {self._auto}]'

