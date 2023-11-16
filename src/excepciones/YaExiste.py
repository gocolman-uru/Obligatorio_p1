class YaExiste(Exception):
    
    def __init__(self, mensaje = 'Ya existe un registro asociado al dato ingresado'):
        self.message = mensaje
        super().__init__(self.message)

