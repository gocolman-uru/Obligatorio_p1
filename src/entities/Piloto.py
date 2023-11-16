from entities.Empleado import Empleado

class Piloto(Empleado):

    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento,score, 
                 numero_auto, reserva):
        super().__init__(id, nombre, nacionalidad, salario, fecha_nacimiento)
        self._score = score ##Setter    
        self._lesion = False ##Setter
        self._numero_auto = numero_auto
        self._puntaje_campeonato = 0
        self._reserva = reserva
    

    #Getters
    @property
    def score(self):
        return self._score
    
    @property
    def numero_auto(self):
        return self._numero_auto
    
    @property
    def lesion(self):
        return self._lesion
    
    @property
    def puntaje_campeonato(self):
        return self._puntaje_campeonato
    
    @property
    def reserva(self):
        return self._reserva
    

    
    @puntaje_campeonato.setter
    def puntaje_campeonato(self,puntaje_campeonato):
        self._puntaje_campeonato = puntaje_campeonato
    
    @lesion.setter
    def lesion(self, lesion):
        self._lesion=lesion
    

    def __str__(self) -> str:
        return f'Piloto: {super().__str__()}, score {self._score}, lesion {self._lesion}, nro de auto {self._numero_auto}, puntaje campeonato {self._puntaje_campeonato}, reserva {self._reserva}]'
    
    
    
