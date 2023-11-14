from entities.Empleado import Empleado

class Piloto(Empleado):

    def __init__(self, id, nombre, nacionalidad, salario, fecha_nacimiento, score, 
                 numero_auto, reserva):
        super().__init__(id, nombre, nacionalidad, salario, fecha_nacimiento)
        self._score = score ##Setter    
        self._lesion = False ##Setter
        self._numero_auto = numero_auto
        self._puntaje_campeonato = 0 #setter
        self._reserva = reserva #setter


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
    
    
