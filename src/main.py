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
        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            alta_empleado()
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
    

def alta_empleado():

    try:
        id_empleado = input("Ingrese ID: ")
        if len(str(id_empleado)) >= 8:
            main_menu()
            raise DatosInvalidos()
            
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
        
        cargo = input("Ingrese cargo (1 Piloto, 2 Piloto de reserva, 3 Mecánico, 4 Jefe de equipo): ")
        if cargo > 4:
            raise DatosInvalidos()
        empleado = None

        if cargo == '1' or cargo == '2':  # Piloto o Piloto de reserva
            score = int(input("Ingrese score: "))
            numero_auto = int(input("Ingrese número de auto: "))
            empleado = Piloto(id_empleado, nombre, nacionalidad, salario, fecha_nacimiento,score, numero_auto)
        elif cargo == '3':  # Mecánico
            score = int(input("Ingrese score: "))
            empleado = Mecanico(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score)
        elif cargo == '4':  # Jefe de equipo
            empleado = DirectorEquipo(id_empleado, nombre, fecha_nacimiento, salario, nacionalidad)
        return empleado
    except DatosInvalidos():
        main_menu()

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
            empleado_ = empleados_main.id
        else:
            print('El modelo ingresado no existe')
        
    return empleado_

    

def alta_equipo(): 

    pilotos = []
    director_equipo = []
    mecanicos = []

    nombre_equipo = input('Ingrese nombre del equipo: ')
    modelo_auto = input('Ingrese modelo de auto:  ')
    auto = buscar_auto(modelo_auto)
    
    for i in range(11):
        cedula = int(input('Ingrese cedula del empleado: '))
        empleado = buscar_empleado(cedula)
        if isinstance(empleado,Piloto) and not dato_invalido: 
            pilotos.append(empleado)
        elif isinstance(empleado,DirectorEquipo) and len(director_equipo)<2:
            director_equipo.append(empleado)
        elif isinstance(empleado,Mecanico) and len(mecanicos)<8:
            mecanicos.append(empleado)
        else:
            dato_invalido = True
    
    equipo = Equipo(nombre_equipo, pilotos, director_equipo, mecanicos, auto)
    equipos_main.append(equipo)
    return equipo



def simular_carrera():
    pass

def realizar_consultas():
    pass





if __name__=='__main__':
    equipos_main = [] 
    empleados_main = []
    autos_main = []
    main_menu()

    #git commit --no-verify
    #git pull origin master