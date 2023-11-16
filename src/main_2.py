from entities.DirectorEquipo import DirectorEquipo
from entities.Mecanico import Mecanico
from entities.Piloto import Piloto
from entities.Equipo import Equipo
from entities.Auto import Auto
from Carrera import Carrera

from excepciones.DatosInvalidos import DatosInvalidos
from excepciones.YaExiste import YaExiste



def main_menu():
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
            realizar_consultas()
        elif opcion == 6:
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def es_vacio(lista):
    if lista is None:
        return True
    return False   

def alta_empleado():

    try:
        id_empleado = input("Ingrese ID: ")
        if len(id_empleado) >= 8:
            raise DatosInvalidos()
        if buscar_empleado_bool(id_empleado):
            raise YaExiste()
        
        nombre = input("Ingrese nombre: ")
        if not nombre.isalpha():
            raise DatosInvalidos()

        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        if len(fecha_nacimiento.split("/")) != 3:
            raise DatosInvalidos()

        nacionalidad = input("Ingrese nacionalidad: ")
        if not nacionalidad.isalpha():
            raise DatosInvalidos()
        
        salario = input("Ingrese salario: ")
        if salario.isalpha():
            raise DatosInvalidos()
        else:
            salario = float(salario)
        

        cargo = int(input("Ingrese cargo (1 Piloto, 2 Piloto de reserva, 3 Mecánico, 4 Jefe de equipo): "))
        if cargo > 4:
            raise DatosInvalidos()
        empleado = None

        if cargo == 1 or cargo == 2:  # Piloto o Piloto de reserva
            score = int(input("Ingrese score: "))
            numero_auto = int(input("Ingrese número de auto: "))
            if cargo == 1:
                empleado = Piloto(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento, score, numero_auto, reserva=False)
            else:
                empleado = Piloto(id_empleado, nombre, nacionalidad, salario, 
                                  fecha_nacimiento, score, numero_auto, reserva=True)
        elif cargo == 3:  # Mecánico
            score = int(input("Ingrese score: "))
            empleado = Mecanico(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento, score)
        elif cargo == 4:  # Jefe de equipo
            empleado = DirectorEquipo(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento)
            

        return empleado
    except (DatosInvalidos,YaExiste):
        return None

def alta_auto():
    modelo = input("Ingrese modelo: ")
    año = int(input("Ingrese año: "))
    score = int(input("Ingrese score: "))
    auto = Auto(modelo, año, score)
    autos_main.append(auto)
    print('Tarea completada con éxito!\n')


def buscar_auto(modelo_auto):
    for auto in autos_main:
        if auto.modelo == modelo_auto:
            print(auto.modelo)
        else:
            print('El modelo ingresado no existe')

def buscar_empleado(cedula): 
    for empleado in empleados_main:
        if empleado.id == cedula:
            return empleado
        else: 
            return None
        
def buscar_empleado_bool(cedula): 
    for empleado in empleados_main:
        if empleado.id == cedula:
            return True
        else: 
            return False
    

def alta_equipo(): 

    pilotos = []
    director_equipo = []
    mecanicos = []
    dato_invalido = False
    nombre_equipo = input('Ingrese nombre del equipo: ')
    modelo_auto = input('Ingrese modelo de auto:  ')
    auto = buscar_auto(modelo_auto)
    i=1
    while i <=12:
        cedula = int(input('Ingrese cedula del empleado: '))
        empleado = buscar_empleado(cedula)
        print(empleado)
        es_vacio(empleado)
        if not es_vacio(empleado):
            if isinstance(empleado,Piloto) and not dato_invalido: #chequear cantidad de pilotos
                pilotos.append(empleado)
            elif isinstance(empleado,DirectorEquipo) and len(director_equipo)<2:
                director_equipo.append(empleado)
            elif isinstance(empleado,Mecanico) and len(mecanicos)<8:
                mecanicos.append(empleado)
            else:
                dato_invalido = True
        else:
            input('Piloto No Existe, ingrese el documento nuevamente: ')
            i-=1
        i+=1
    
    equipo = Equipo(nombre_equipo, pilotos, director_equipo, mecanicos, auto)
    equipos_main.append(equipo)
    print('Tarea completada con éxito!\n')
    
    

def lista_desde_str(cadena):
    if len(cadena.strip()) == 0:
        lista_final = []
    else:
        lista_aux = cadena.split(',')
        lista_final = [x.strip() for x in lista_aux]
    return lista_final


def simular_carrera():
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




def top_diez(empleados_main):
    pilotos = [empleado for empleado in empleados_main if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.puntaje_campeonato, reverse=True)
    top_10 = pilotos_ordenados[:10]
    for piloto in top_10:
        print(f"Piloto: {piloto.nombre}, Puntos: {piloto.puntaje_campeonato}")

def resumen_equipos():
    equipo = [equipo for equipo in equipos_main if isinstance(equipo, Equipo)]
    i=1
    for team in equipo:
        print(f"Equipo {i}: {team.get_nombre_equipo}")
        i+=1

def top_cinco_salarios_pilotos():
    pilotos = [empleado for empleado in empleados_main if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.salario, reverse=True)
    top_10 = pilotos_ordenados[:5]
    for piloto in top_10:
        print(f"Piloto: {piloto.nombre}, Salario: {piloto.salario}")

def top_tres_score_pilotos():
    pilotos = [empleado for empleado in empleados_main if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.score, reverse=True)
    top_10 = pilotos_ordenados[:3]
    for piloto in top_10:
        print(f"Piloto: {piloto.nombre}, Puntos: {piloto.score}")

def jefes_de_equipo():
    jefes = [jefe for jefe in empleados_main if isinstance(jefe, DirectorEquipo)]
    for jefe in jefes:
        print(f"Jefe de Equipo: {jefe.nombre}")


def realizar_consultas():
    print("1. Top 10 pilotos con más puntos en el campeonato")
    print("2. Resumen campeonato de constructores (equipos).")
    print("3. Top 5 pilotos mejores pago")
    print("4. Top 3 pilotos más habilidosos")
    print("5. Retornar jefes de equipo")
    print("6. Para Finalizar")

    try:
        opcion = int(input("Ingrese la opción deseada: "))
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
        jefes_de_equipo()
    elif opcion == 6:
        print('Finalizando Programa')
    else:
        return main_menu()
    
    


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

### ver lo de equipos, dos tituilares un suplente
## ver lo del input en el for de alta equipo al final cuando no lo encuentra
## cheuear el tema del raise y except en la funcion de alta empleado
# chequeo en cada input de datos con un try que vuelva al menu o algo, por ejemplo score en piloto
# metodos to string en empleado y iloto para que me indique que y cuantos pilotos corren
# hacer los append de las listas main, empleados, equipos main etc....
# poner texto en las excepciones para que imprimar el error
# chequear el setter de lesion, creo que no es necesario por la condicion de la letra
    
    equipos_main = [
        Equipo('nombre_equipo', 
                [
                   Piloto('1', 'uno', 'uruguay', '100', '05/05/06', '99', '101', reserva=False),
                   Piloto('2', 'dos', 'uruguay', '200', '05/05/06', '98', '102', reserva=False),
                   Piloto('7', 'siete', 'uruguay', '800', '05/05/06', '93', '107', reserva=True),
                ],
                DirectorEquipo('48', 'asdsad', 'uruguay', '5000', '97/97/96'), 
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
                DirectorEquipo('47', 'asdsad', 'uruguay', '5000', '97/97/96'), 
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
    #git pull origin master6
