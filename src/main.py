from entities.DirectorEquipo import DirectorEquipo
from entities.Mecanico import Mecanico
from entities.Piloto import Piloto
from entities.Equipo import Equipo
from entities.Auto import Auto
from Carrera import Carrera

from excepciones.DatosInvalidos import DatosInvalidos
from excepciones.YaExiste import YaExiste



def main_menu(empleados_main,equipos_main,autos_main,carrera):
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
            if empleado is None:
                continue  
            empleados_main.append(alta_empleado())
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
        if len(str(id_empleado)) >= 8:
            main_menu()
            raise DatosInvalidos()
        if buscar_empleado(id_empleado) is not None:
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
            empleado = Piloto(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento,score, numero_auto)
        elif cargo == 3:  # Mecánico
            score = int(input("Ingrese score: "))
            empleado = Mecanico(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score)
        elif cargo == 4:  # Jefe de equipo
            empleado = DirectorEquipo(id_empleado, nombre, fecha_nacimiento, salario, nacionalidad)
        return empleado
    except (DatosInvalidos,YaExiste):
        return None

def alta_auto():
    modelo = input("Ingrese modelo: ")
    año = int(input("Ingrese año: "))
    score = int(input("Ingrese score: "))
    auto = Auto(modelo, año, score)
    autos_main.append(auto)


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
            print('Piloto No Existe, ingrese el documento nuevamente: ')
            i-=1
        i+=1
    
    equipo = Equipo(nombre_equipo, pilotos, director_equipo, mecanicos, auto)
    equipos_main.append(equipo)
    
    

def simular_carrera():
    pass

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
    equipos_main = [] 
    empleados_main = []
    autos_main = []
    carrera = []
    main_menu(empleados_main,equipos_main,autos_main,carrera)

    #git commit --no-verify
    #git pull origin master