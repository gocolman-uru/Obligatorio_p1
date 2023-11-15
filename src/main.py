from entities.DirectorEquipo import DirectorEquipo
from entities.Mecanico import Mecanico
from entities.Piloto import Piloto
from entities.Auto import Auto

from Carrera import Carrera
from excepciones.DatosInvalidos import DatosInvalidos
from excepciones.YaExiste import YaExiste


equipos = {} 
empleados = []
autos = []

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
            empleado = Mecanico(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score)
        elif cargo == 4:  # Jefe de equipo
            empleado = DirectorEquipo(id_empleado, nombre, fecha_nacimiento, salario, nacionalidad)

        
        print('Tarea completada con éxito!\n')
        empleados.append(empleado)

        return empleado
    except DatosInvalidos():
        main_menu()

def alta_auto():
    modelo = input("Ingrese modelo: ")
    año = int(input("Ingrese año: "))
    score = int(input("Ingrese score: "))
    auto = Auto(modelo, año, score)
    autos.append(auto)
    return auto

def buscar_auto():
    modelo = input("Ingrese Matricula: ")
    for auto in autos:
        if auto.modelo == modelo:
            print(auto.modelo)
        else:
            print('El modelo ingresado no existe')

def alta_equipo():
    pass


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

    print(lista_pilotos_lesionados)


    carrera = Carrera(equipos, lista_pilotos_lesionados, lista_pilotos_abandono, lista_pilotos_error_pits, lista_pilotos_penalidad)
    simulacion = carrera.simular()

    return simulacion



def realizar_consultas():
    pass


def main_menu():
    print('**** MENÚ PRINCIPAL ****')
    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == '1':
            alta_empleado()
        elif opcion == '2':
            alta_auto()
        elif opcion == '3': 
            alta_equipo()
        elif opcion == '4':
            simular_carrera()
        elif opcion == '5':
            realizar_consultas()
        elif opcion == '6':
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__=='__main__':
    
    main_menu()

    print('Equipos:', equipos)
    print('Empleados:', empleados)
    print('Autos:', autos)
