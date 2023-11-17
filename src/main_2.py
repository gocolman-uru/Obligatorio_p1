from entities.DirectorEquipo import DirectorEquipo
from entities.Mecanico import Mecanico
from entities.Piloto import Piloto
from entities.Equipo import Equipo
from entities.Auto import Auto
from Carrera import Carrera

from excepciones.DatosInvalidos import DatosInvalidos
from excepciones.YaExiste import YaExiste



def main_menu():
    ''' Esta función contiene el menú principal de la aplicación, se le solicita al usuario que ingrese un número en base a lo que quiera realizar.
    Toma ese número y llama a la función que el usuario quiere utilizar.
    '''
    apagar = False
    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")
        try:
            opcion = int(input("Ingrese la opción deseada: "))
        except:
            print('Ingrese una opcion válida')
        if opcion == 1:
            empleado = alta_empleado()
            if empleado == None:
                pass
            else:
                empleados_main.append(empleado)
        elif opcion == 2:
            alta_auto()
        elif opcion == 3: 
            alta_equipo()
        elif opcion == 4:
            simular_carrera()
        elif opcion == 5:
            apagar = realizar_consultas()
            if apagar:
                break
        elif opcion == 6:
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def es_vacio(lista):
    ''' Chequea si una lista u objeto es vacío, en caso de serlo, devuelve True.
    '''
    if lista is None:
        return True
    return False   

def alta_empleado():
    ''' Esta función le solicita al usuario la información necesaria para crear un empleado. 
    En base a las opciones que ingresa se determina si ese empleado es un Piloto (titular o reserva), Director de Equipo o Jefe.
    Luego de crear el objeto, lo agrega a la lista de empleados.
    '''
    id_empleado = input("Ingrese cedula: ")
    try: 
        if not id_empleado.isdigit():
            raise DatosInvalidos()
        if len(id_empleado) >= 8:
            raise DatosInvalidos()
        if buscar_empleado_bool(id_empleado):
            raise YaExiste()
        id_empleado = int(id_empleado)
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None
    except YaExiste as mensaje:
        print(mensaje)
        return None
    
    try:
        nombre = input("Ingrese nombre: ")
        if not nombre.isalpha():
            raise DatosInvalidos()
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None

    try:
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        if len(fecha_nacimiento.split("/")) != 3:
            raise DatosInvalidos()
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None
    try:
        nacionalidad = input("Ingrese nacionalidad: ")
        if not nacionalidad.isalpha():
            raise DatosInvalidos()
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None
    
    try:
        salario = input("Ingrese salario: ")
        if salario.isalpha():
            raise DatosInvalidos()
        else:
            salario = float(salario)
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None
    
    try:
        cargo = int(input("Ingrese cargo (1 Piloto, 2 Piloto de reserva, 3 Mecánico, 4 Jefe de equipo): "))
        if cargo > 4:
            raise DatosInvalidos()
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None

    if cargo == 1 or cargo == 2:  # Piloto o Piloto de reserva
        try:
            score = input("Ingrese score: ")
            if score.isalpha():
                raise DatosInvalidos()
            else:
                score = int(score)
                if score > 99 or score<1:
                    DatosInvalidos()
        except DatosInvalidos as mensaje:
            print(mensaje)
            return None

        try:
            numero_auto = input("Ingrese número de auto: ")
            if numero_auto.isalpha():
                raise DatosInvalidos()
            else:
                numero_auto = int(numero_auto)
        except DatosInvalidos as mensaje:
            print(mensaje)
            return None

        if cargo == 1:
            empleado = Piloto(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento, score, numero_auto, reserva=False)
        else:
            empleado = Piloto(id_empleado, nombre, nacionalidad, salario, 
                                fecha_nacimiento, score, numero_auto, reserva=True)
    elif cargo == 3:  # Mecánico

        try:
            score = input("Ingrese score: ")
            if score.isalpha():
                raise DatosInvalidos()
            else:
                score = int(score)
        except DatosInvalidos as mensaje:
            print(mensaje)
            return None
        empleado = Mecanico(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento, score)
    elif cargo == 4:  # Jefe de equipo
        empleado = DirectorEquipo(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento)     
    return empleado

def alta_auto():
    ''' Esta función le solicita la usuario la información necesaria para crear el objeto Auto.
    Luego crea el objeto auto y lo agrega a la lista de autos ya existentes.
    '''
    modelo = input("Ingrese modelo: ")
    try:
        anio = input("Ingrese año: ")
        if anio.isalpha():
            raise DatosInvalidos()
        else:
            anio = int(anio)
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None
    try:
        score = input("Ingrese score: ")
        if score.isalpha():
            raise DatosInvalidos()
        else:
            score = int(score)
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None
    auto = Auto(modelo, anio, score)
    autos_main.append(auto)
    print('Tarea completada con éxito!\n')


def buscar_auto(modelo_auto):
    '''Esta función recibe el modelo de una auto y lo compara con todos los autos creados.
    Si encuentra coincidencia, devuelve el objeto auto encontrado, caso contrario devuelve None.'''
    for auto in autos_main:
        if auto.modelo == modelo_auto:
            return auto
        else:
            return None

def buscar_empleado(cedula): 
    '''Esta función recibe una cedula y la compara con todos los empleados creados.
    Si encuentra coincidencia, devuelve el objeto empleado encontrado, caso contrario devuelve None.
    '''
    for empleado in empleados_main:
        if empleado.id == cedula:
            return empleado
        else: 
            return None
        
def buscar_empleado_bool(cedula): 
    ''' Esta función recibe una cedula y la compara con todos los empleados creados.
    Si encuentra coincidencia, devuelve True, caso contrario devuelve False.
    '''
    for empleado in empleados_main:
        if empleado.id == cedula:
            return True
        else: 
            return False
    

def alta_equipo(): 
    ''' Función recibe listas de pilotos, director de equipo, mecanicos y se le solicita al usuario el modelo de auto
    para crear un equipo nuevo '''

    pilotos = []
    director_equipo = []
    mecanicos = []
    piloto_titular = 0
    piloto_reserva = 0
    i=1
    nombre_equipo = input('Ingrese nombre del equipo: ')
    modelo_auto = input('Ingrese modelo de auto:  ')
    auto = buscar_auto(modelo_auto)

    try:
        if es_vacio(auto):
            raise DatosInvalidos()
    except DatosInvalidos as mensaje:
        print(mensaje)
        return None

    while i <=12:
        cedula = input('Ingrese cedula del empleado: ')
        try:
            if cedula.isalpha():
                raise DatosInvalidos()
            else:
                cedula = int(cedula)
        except DatosInvalidos as mensaje:
            print(mensaje)
            return None
        empleado = buscar_empleado(cedula)
        try:
            if not es_vacio(empleado):
                if isinstance(empleado,Piloto): 
                    if empleado.reserva and piloto_reserva<1:
                        pilotos.append(empleado)
                        piloto_reserva+=1
                    elif piloto_titular<2:
                        pilotos.append(empleado) 
                        piloto_titular+=1
                    else:
                        raise DatosInvalidos()
                if isinstance(empleado,DirectorEquipo):
                    if len(director_equipo)<2:
                        director_equipo.append(empleado)
                    else:
                        raise DatosInvalidos()
                if isinstance(empleado,Mecanico):
                    if len(mecanicos)<8:
                        mecanicos.append(empleado)
                    else:
                        raise DatosInvalidos()
            else:
                raise DatosInvalidos()
        except DatosInvalidos as mensaje:
            print(mensaje)
            return None
        i+=1
    
    equipo = Equipo(nombre_equipo, pilotos, director_equipo, mecanicos, auto)
    equipos_main.append(equipo)
    print('Tarea completada con éxito!\n')
    
    

def lista_desde_str(cadena):
    ''' Función auxiliar que crea una lista a partir de un string, utilizando ',' como separador.
    '''
    if len(cadena.strip()) == 0:
        lista_final = []
    else:
        lista_aux = cadena.split(',')
        lista_final = [x.strip() for x in lista_aux]
    return lista_final


def simular_carrera():
    ''' Esta función le solicita al usuario los datos necesarios para simular la carrera y crea 4 listas con información.
    Luego instancia Carrera y se utiliza el metodo .simular() para iniciar la simulación.
    '''
    pilotos_lesionados = input("Ingrese nro de todos pilotos lesionados (enter si no hay): ")
    pilotos_abandono = input("Ingrese nro de todos pilotos que abandonan (enter si no hay): ")
    pilotos_error_pits = input("Ingrese nro de todos pilotos con error en pits (enter si no hay): ")
    pilotos_penalidad = input("Ingrese nro de todos pilotos con penalidad (enter si no hay): ")
    # Los paso a lista
    lista_pilotos_lesionados = lista_desde_str(pilotos_lesionados)
    lista_pilotos_abandono = lista_desde_str(pilotos_abandono)
    lista_pilotos_error_pits = lista_desde_str(pilotos_error_pits)
    lista_pilotos_penalidad = lista_desde_str(pilotos_penalidad)


    carrera = Carrera(equipos_main, lista_pilotos_lesionados, lista_pilotos_abandono, lista_pilotos_error_pits, lista_pilotos_penalidad)
    simulacion = carrera.simular()

    return simulacion


def buscar_jefe(jefe, equipos_main):
    ''' La función se encarga de chequear si el nombre dado, coincide con un director de equipo,
     devuelve el nombre del equipo en caso de encontrarlo, sino retorna None
    '''
    for equipo in equipos_main:
        if isinstance(equipo, Equipo):
            if equipo.director_de_equipo.nombre == jefe:
                return equipo.nombre_equipo
    return None

def top_diez(empleados_main):
    ''' La función crea una lista de pilotos y los ordena en base al puntaje del campeonato de forma descendente.
    Luego se crea una lista con los primeros 10 y se muestran en pantalla los pilotos ordenados por puntaje.
    '''
    pilotos = [empleado for empleado in empleados_main if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.puntaje_campeonato, reverse=True)
    top_10 = pilotos_ordenados[:10]
    for piloto in top_10:
        print(f"Piloto: {piloto.nombre}, Puntos: {piloto.puntaje_campeonato}")

def resumen_equipos():
    ''' La función despliega el nombre de los equipos.
    '''
    equipo = [equipo for equipo in equipos_main if isinstance(equipo, Equipo)]
    i=1
    for team in equipo:
        print(f"Equipo {i}: {team.nombre_equipo}")
        i+=1

def top_cinco_salarios_pilotos():
    ''' La función crea una lista de pilotos y la ordena en base a su salario de forma descendente.
    Luego crea una lista con los primeros 5 pilotos y se imprimen en pantalla ordenados por salario.
    '''
    pilotos = [empleado for empleado in empleados_main if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.salario, reverse=True)
    top_10 = pilotos_ordenados[:5]
    for piloto in top_10:
        print(f"Piloto: {piloto.nombre}, Salario: {piloto.salario}")

def top_tres_score_pilotos():
    ''' Esta función crea una lista con los pilotos y los ordena por su score de forma descendente.
    Luego se crea una lista con los primeros 3 pilotos y se imprimen en pantalla.
    '''
    pilotos = [empleado for empleado in empleados_main if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.score, reverse=True)
    top_10 = pilotos_ordenados[:3]
    for piloto in top_10:
        print(f"Piloto: {piloto.nombre}, Puntos: {piloto.score}")

def jefes_de_equipo(equipos_main):
    ''' Esta función crea una lista con los Directores de todos los equipos y la ordena alfabéticamente.
    Luego se imprime en pantalla los directores de equipo y el nombre del equipo
    '''
    jefes = [jefe for jefe in empleados_main if isinstance(jefe, DirectorEquipo)]
    jefes_ordenados = sorted(jefes, key=lambda jefe: jefe.nombre, reverse=False)
    for jefe in jefes_ordenados:
        equipo = buscar_jefe(jefe.nombre,equipos_main)
        if equipo is not None:
            print(f"Jefe de Equipo: {jefe.nombre} Equipo: {equipo}")


def realizar_consultas():
    ''' Esta función despliega el menú para realizar 5 consultas de  estadísticas.
    Se le solicita al usuario que ingrese una opción y en base a su elección se llaman distintas funciones.
    '''
    print("1. Top 10 pilotos con más puntos en el campeonato")
    print("2. Resumen campeonato de constructores (equipos).")
    print("3. Top 5 pilotos mejores pago")
    print("4. Top 3 pilotos más habilidosos")
    print("5. Retornar jefes de equipo")
    print("6. Para Finalizar")

    try:

        opcion = input("Ingrese la opción deseada: ")
        if opcion.isalpha():
            raise DatosInvalidos()
        else:
            opcion = int(opcion)
    except:
        print('Ingrese una opcion válida')

    if opcion == 1:
        top_diez(empleados_main)
    elif opcion == 2:
        resumen_equipos()
    elif opcion == 3: 
        top_cinco_salarios_pilotos()
    elif opcion == 4:
        top_tres_score_pilotos()
    elif opcion == 5:
        jefes_de_equipo(equipos_main)
    elif opcion == 6:
        print('Finalizando Programa')
    else:
        return True
    
    


if __name__=='__main__':
    empleados_main = [
        #titulares
        Piloto('1', 'uno', 'uruguay', '100', '05/05/06', '99', '101', reserva=False),
        Piloto('2', 'dos', 'uruguay', '200', '05/05/06', '98', '102', reserva=False),
        Piloto('3', 'tres', 'uruguay', '300', '05/05/06', '97', '103', reserva=False),
        Piloto('4', 'cuatro', 'uruguay', '400', '05/05/06', '96', '104', reserva=False),
        Piloto('5', 'cinco', 'uruguay', '600', '05/05/06', '95', '105', reserva=False),
        Piloto('6', 'seis', 'uruguay', '700', '05/05/06', '94', '106', reserva=False),
        #reserva
        Piloto('7', 'siete', 'uruguay', '800', '05/05/06', '93', '107', reserva=True),
        Piloto('8', 'ocho', 'uruguay', '900', '05/05/06', '92', '108', reserva=True),
        Piloto('9', 'nueve', 'uruguay', '1000', '05/05/06', '91', '109', reserva=True),
        Piloto('10', 'diez', 'uruguay', '11000', '05/05/06', '90', '110', reserva=True),
        Piloto('11', 'once', 'uruguay', '12000', '05/05/06', '89', '111', reserva=True),
        #mecanicos
        Mecanico('12', 'doce', 'uruguay', '5000', '97/97/96', '99'),
        Mecanico('13', 'trece', 'uruguay', '5000', '97/97/96', '98'),
        Mecanico('14', 'catorce', 'uruguay', '5000', '97/97/96' ,'97'),
        Mecanico('15', 'quince', 'uruguay', '5000', '97/97/96' ,'96'),
        Mecanico('16', 'diensisces', 'uruguay', '5000', '97/97/96' ,'95'),
        Mecanico('17', 'desicisite', 'uruguay', '5000', '97/97/96', '94'),
        Mecanico('18', 'disciocho', 'uruguay', '5000', '97/97/96', '93'),
        Mecanico('19', 'discinueve', 'uruguay', '5000', '97/97/96' ,'92'),
        Mecanico('20', 'veinte', 'uruguay', '5000', '97/97/96' ,'91'),
        Mecanico('21', 'vteintino', 'uruguay', '5000', '97/97/96' ,'90'),
        Mecanico('22', 'vvdos', 'uruguay', '5000', '97/97/96' ,'89'),
        Mecanico('23', 'vvtres', 'uruguay', '5000', '97/97/96' ,'88'),
        Mecanico('24', 'vvcuadtro', 'uruguay', '5000', '97/97/96' ,'87'),
        Mecanico('25', 'asd', 'uruguay', '5000', '97/97/96', '86'),
        Mecanico('26', 'asd', 'uruguay', '5000', '97/97/96', '85'),
        Mecanico('27', 'asd', 'uruguay', '5000', '97/97/96' ,'84'),
        Mecanico('28', 'as', 'uruguay', '5000', '97/97/96' ,'83'),
        Mecanico('29', 'ad', 'uruguay', '5000', '97/97/96' ,'82'),
        Mecanico('30', 'agd', 'uruguay', '5000', '97/97/96' ,'81'),
        Mecanico('31', 'as', 'uruguay', '5000', '97/97/96', '80'),
        Mecanico('32', 'ag', 'uruguay', '5000', '97/97/96', '79'),
        Mecanico('33', 'ah', 'uruguay', '5000', '97/97/96' ,'78'),
        Mecanico('34', 'aer', 'uruguay', '5000', '97/97/96' ,'77'),
        Mecanico('35', 'asd', 'uruguay', '5000', '97/97/96', '76'),
        Mecanico('36', 'bvd', 'uruguay', '5000', '97/97/96', '75'),
        Mecanico('37', 'cvbcxv', 'uruguay', '5000', '97/97/96', '74'),
        Mecanico('38', 'sdfds', 'uruguay', '5000', '97/97/96' ,'73'),
        Mecanico('39', 'sdfdsf', 'uruguay', '5000', '97/97/96', '72'),
        Mecanico('40', '', 'uruguay', '5000', '97/97/96', '71'),
        #directores
        DirectorEquipo('41', 'sadas', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('42', 'asds', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('43', 'asdsa', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('44', 'asd', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('45', 'asdsa', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('46', 'asdas', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('47', 'asdsad', 'uruguay', '5000', '97/97/96'),
        DirectorEquipo('48', 'asdsad', 'uruguay', '5000', '97/97/96')
        ]

    equipos_main = [
        Equipo('nombre_equipo', 
                [
                   Piloto('1', 'uno', 'uruguay', '100', '05/05/06', '99', '101', reserva=False),
                   Piloto('2', 'dos', 'uruguay', '200', '05/05/06', '98', '102', reserva=False),
                   Piloto('7', 'siete', 'uruguay', '800', '05/05/06', '93', '107', reserva=True),
                ],
                [DirectorEquipo('48', 'asdsad', 'uruguay', '5000', '97/97/96')], 
                [
                   Mecanico('12', 'doce', 'uruguay', '5000', '97/97/96', '99'),
                   Mecanico('13', 'trece', 'uruguay', '5000', '97/97/96' ,'98'),
                   Mecanico('14', 'catorce', 'uruguay', '5000', '97/97/96' ,'97'),
                   Mecanico('15', 'quince', 'uruguay', '5000', '97/97/96' ,'96'),
                   Mecanico('16', 'diensisces', 'uruguay', '5000', '97/97/96' ,'95'),
                   Mecanico('17', 'desicisite', 'uruguay', '5000', '97/97/96' ,'94'),
                   Mecanico('18', 'disciocho', 'uruguay', '5000', '97/97/96' ,'93'),
                   Mecanico('19', 'discinueve', 'uruguay', '5000', '97/97/96' ,'92'),
                ],
                Auto('ferrari', '2023', '99')),
        Equipo('nombre_equipo', 
                [
                   Piloto('3', 'tres', 'uruguay', '300', '05/05/06', '97', '103', reserva=False),
                   Piloto('4', 'cuatro', 'uruguay', '400', '05/05/06', '96', '104', reserva=False),
                   Piloto('8', 'ocho', 'uruguay', '900', '05/05/06', '92', '108', reserva=True),
                ],
                [DirectorEquipo('47', 'asdsad', 'uruguay', '5000', '97/97/96')], 
                [
                   Mecanico('27', 'asd', 'uruguay', '5000', '97/97/96' ,'84'),
                   Mecanico('28', 'as', 'uruguay', '5000', '97/97/96' ,'83'),
                   Mecanico('29', 'ad', 'uruguay', '5000', '97/97/96' ,'82'),
                   Mecanico('30', 'agd', 'uruguay', '5000', '97/97/96', '81'),
                   Mecanico('31', 'as', 'uruguay', '5000', '97/97/96' ,'80'),
                   Mecanico('32', 'ag', 'uruguay', '5000', '97/97/96' ,'79'),
                   Mecanico('33', 'ah', 'uruguay', '5000', '97/97/96' ,'78'),
                   Mecanico('34', 'aer', 'uruguay', '5000', '97/97/96', '77'),
                ],
                Auto('mustang', '2023', '97')),

    ] 

    autos_main = [
        Auto('ferrari', '2023', '99'),
        Auto('mercedes', '2023', '98'),
        Auto('mustang', '2023', '97'),
        Auto('bmw', '2023', '96'),
        Auto('renault', '2023', '95'),
        Auto('fiat', '2023', '94'),

    ]
    carrera = []





    main_menu()

    #git commit --no-verify
    #git pull origin master
