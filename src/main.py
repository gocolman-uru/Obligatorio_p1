from entities.DirectorEquipo import DirectorEquipo
from entities.Mecanico import Mecanico
from entities.Piloto import Piloto

from entities.Auto import Auto
from Carrera import Carrera

from exceptions.DatosInvalidos import DatosInvalidos
from exceptions.YaExiste import YaExiste

class Programa:
    def __init__(self):
        self.equipos = {}
        self.empleados = {}

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

            salario = float(input("Ingrese salario: "))
            if not salario.replace('.', '', 1).isdigit():
                raise DatosInvalidos()
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
        return auto

    def buscar_auto():
        pass

    def alta_equipo():
        pass

    def simular_carrera():
        pass

    def realizar_consultas():
        pass


def main_menu():
    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == '1':
            Programa.alta_empleado()
        elif opcion == '2':
            Programa.alta_auto()
        elif opcion == '3': 
            Programa.alta_equipo()
        elif opcion == '4':
            Programa.simular_carrera()
        elif opcion == '5':
            Programa.realizar_consultas()
        elif opcion == '6':
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__=='__main__':
    
    main_menu()