class DatosInvalidos(Exception):
    
    def __init__(self, mensaje = 'Los datos ingresados son inválidos'):
        self.message = mensaje
        super().__init__(self.message)

