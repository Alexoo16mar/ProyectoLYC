class Token:
    def __init__(self, dato, tipo):
        self.dato = dato
        self.tipo = tipo

    def set_dato(self, nuevo_dato):
        self.dato = nuevo_dato

    def get_dato(self):
        return self.dato

    def set_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo

    def get_tipo(self):
        return self.tipo