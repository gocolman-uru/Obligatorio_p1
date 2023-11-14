

class Equipo():
    def __init__(self, nombre_equipo, piloto, director_de_equipo, mecanico, auto):
        self._nombre_equipo = nombre_equipo
        self._pilotos = piloto
        self._director_de_equipos = director_de_equipo
        self._mecanicos = mecanico
        self._auto = auto

    @property
    def get_nombre_equipo(self):
        return self._nombre_equipo
    
    @property
    def get_piloto(self):
        return self._piloto
    
    @property
    def get_director_de_equipo(self):
        return self._director_de_equipo
    
    @property
    def get_mecanico(self):
        return self._mecanico

