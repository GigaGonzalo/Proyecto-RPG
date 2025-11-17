class Aventura:

    def __init__(self, personaje : object):

        self.protagonista = personaje
        self.nivel_dificultad = self.protagonista.get_Nivel + 2
