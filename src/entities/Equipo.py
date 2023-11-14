

class Equipo():
    def __init__(self, nombre_equipo, piloto, director_de_equipo, mecanico):
        self._nombre_equipo = nombre_equipo
        self._piloto = piloto
        self._director_de_equipo = director_de_equipo
        self._mecanico = mecanico

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

