
class Carrera():


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
                if pilotos.numero_auto in self._pilotos_lesionados:
                    pilotos.lesion = True # ver si es necesario
                    equipos_con_lesion.append(equipo)
                else: 
                    if pilotos.reserva == False:
                        pilotos_aptos.append(pilotos) 
        if self.lista_es_nula(equipos_con_lesion):
            pass
        else: 
            for equipo in list(set(equipos_con_lesion)):
                for pilotos in equipo.get_piloto:
                    if pilotos.reserva == True:
                        pilotos_aptos.append(pilotos)

        #Ya con todos los pilotos aptos
        #Genero dict con todos los scores
        tabla_posiciones_dict = {}
        tabla_error_pits = {}
        tabla_penalidades = {}
        tabla_score_pilotos = {}
        tabla_score_mecanicos = {}
        tabla_score_auto = {}

        for piloto in pilotos_aptos:
            tabla_posiciones_dict[piloto.numero_auto] = 0
            tabla_score_pilotos[piloto.numero_auto] = int(piloto.score)

            #cargo errores en pits
            if piloto.numero_auto in self._pilotos_error_pits:
                count_apariciones = self._pilotos_error_pits.count(piloto.numero_auto)
                tabla_error_pits[piloto.numero_auto] = int(count_apariciones)
            else:
                tabla_error_pits[piloto.numero_auto] = 0
            #cargo penalidades
            if piloto.numero_auto in self._pilotos_penalidad:
                count_apariciones = self._pilotos_penalidad.count(piloto.numero_auto)
                tabla_penalidades[piloto.numero_auto] = int(count_apariciones)
            else:
                tabla_penalidades[piloto.numero_auto] = 0

        # Calculo de score del equipo 
        for eq in self._equipos:
            puntaje_mecanicos = 0
            puntaje_auto = int(eq.get_auto.score)
            for meca in eq.get_mecanico:
                puntaje_mecanicos += int(meca.score)
            for pilo in eq.get_piloto:
                tabla_score_mecanicos[pilo.numero_auto] = puntaje_mecanicos
                tabla_score_auto[pilo.numero_auto] = puntaje_auto
        # simulo
        for nro_auto in tabla_posiciones_dict.keys():
            if nro_auto in self._pilotos_abandono:
                tabla_posiciones_dict[nro_auto] = 0
            else:
                tabla_posiciones_dict[nro_auto] = (tabla_score_mecanicos[nro_auto] + tabla_score_auto[nro_auto] + tabla_score_pilotos[nro_auto]) - ((5*tabla_error_pits[nro_auto]) - (8*tabla_penalidades[nro_auto]))
        
        #devolver la lista ordenada
        list_posiciones_ordenadas = sorted(tabla_posiciones_dict, reverse=False)
        dict_final_posiciones_con_puntos = {}
        for i in range(0,len(list_posiciones_ordenadas)):
            dict_final_posiciones_con_puntos[i+1] = list_posiciones_ordenadas[i]

        ## Puntos
        puntajes = [25,18,15,12,10,8,6,4,2,1]
        tabla_final_para_puntos = {}
        contador = 1
        for i in list_posiciones_ordenadas:
            if contador <= 10:
                tabla_final_para_puntos[i] = puntajes[contador-1]
            else:
                tabla_final_para_puntos[i] = 0
            contador += 1

        for pilotos_clase in pilotos_aptos:
            for k,v in tabla_final_para_puntos.items():
                if int(pilotos_clase.numero_auto) == int(k):
                    pilotos_clase.puntaje_campeonato = pilotos_clase.puntaje_campeonato + v
        
        print('*' * 100)
        print('Resultados de la carrera:')
        print()
        for k,v in tabla_posiciones_dict.items():
            print(f'Pos. {k}:', f'Auto nro {v}')
        print()
        print('Puntajes totales de los pilotos:')
        for piloto in pilotos_aptos:
            print(f'Piloto {piloto.id} con auto {piloto.numero_auto}:', f'{piloto.puntaje_campeonato} puntos')
        print('*' * 100)

        return pilotos_aptos

