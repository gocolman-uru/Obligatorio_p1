from entities.Empleado import Empleado

class Piloto(Empleado):

    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento,score, numero_auto, puntaje_campeonato=0, lesion=False):
        super().__init__(id, nombre, nacionalidad, salario, fecha_nacimiento)
        self._score = score ##Setter    
        self._lesion = lesion ##Setter
        self._numero_auto = numero_auto
        self._puntaje_campeonato = puntaje_campeonato


    #Getters
    @property
    def score(self):
        return self._score
    
    @property
    def lesion(self):
        return self._lesion
    
    @property
    def modelo_auto(self):
        return self._modelo_auto
    
    @property
    def puntaje_campeonato(self):
        return self._puntaje_campeonato
    
    
