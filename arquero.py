from personajes import Personaje

class Arquero(Personaje):

    def __init__(self, vida, energia, ataque, armadura, escudo_mag, costo_mov,cantidad_flechas,
                  nombre, nivel, clase="Humano"):
        super().__init__(vida, energia, ataque, armadura, escudo_mag, costo_mov, nombre, nivel, clase)
        self.costo_mov = 0.5
        self.cantidad_flechas = cantidad_flechas
    
    def causar_Daño_Distancia(self):
        daño_D = self.ataque * 0.7
        return daño_D
    
    