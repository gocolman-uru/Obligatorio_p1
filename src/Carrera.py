
class Carrera():

    #Variables de clase
    ## Puntajes restados
    error_pits = 5
    infringir_norma = 8

    ## Dict de puntos
    puntajes = {1: 25,
                2: 18,
                3: 15,
                4: 12,
                5:10,
                6: 8,
                7: 6,
                8: 4,
                9: 2,
                10: 1}


    def __init__(self, equipos, pilotos_lesionados, pilotos_abandono, pilotos_error_pits, pilotos_penalidad):
        self._equipos = equipos
        self._pilotos_lesionados = pilotos_lesionados
        self._pilotos_abandono = pilotos_abandono
        self._pilotos_error_pits = pilotos_error_pits
        self._pilotos_penalidad = pilotos_penalidad
    
    


    def lista_es_nula(self,lista):
        if len(lista) == 0: 
            return True
        return False



    def simular(self):
        pilotos_aptos = []
        equipos_con_lesion = []


        # Configuro el escenario antes
        # piloto lesionado
        for equipo in self._equipos:
             for pilotos in equipo.get_piloto:
                if pilotos.id in self._pilotos_lesionados:
                    pilotos.lesion = True #
                    equipos_con_lesion.append(equipo)
                else: 
                    if pilotos.reserva == False:
                        pilotos_aptos.append(pilotos) 
        print('pilotos aptos al momento: ')
        for i in pilotos_aptos:
            print(str(i))


        if self.lista_es_nula(equipos_con_lesion):
            pass
        else: 
            for equipo in list(set(equipos_con_lesion)):
                for pilotos in equipo.get_piloto:
                    if pilotos.reserva == True:
                        pilotos_aptos.append(pilotos)






        
        #Ya con todos los pilotos aptos
        print("Pilotos aptos al final:")
        for i in pilotos_aptos:
            print("--- Piloto:", str(i))
        print('cantidad de pilotos para correr:', len(pilotos_aptos))

        for i in equipos_con_lesion:
            print('Pilotos de equipos con lesion:', str(i.get_piloto))
        print('cantidad de equipos con lesion:', len(equipos_con_lesion))
        



        # Si el piloto abandona

        # Si no abandona

        # score_final = suma_score_mecanicos + score_auto + score_piloto
        # + 5*cantidad_errores_en_pits - 8*cantidad_penalidad_infringir_norma
