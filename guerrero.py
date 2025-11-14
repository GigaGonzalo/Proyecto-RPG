from personajes import Personaje

class Guerrero(Personaje):

    def __init__(self, vida, energia, ataque, armadura, escudo_mag, costo_mov,
                  habilidad_guerrero, bono_armadura, nombre, nivel, clase="Humano"):
        super().__init__(vida, energia, ataque, armadura, escudo_mag, costo_mov, nombre, nivel, clase)
        
        self.habilidad_guerrero = habilidad_guerrero
        self.bono_armadura = bono_armadura

    def habilidad_Guerrero_Ataque(self):
        h_ataque = self.ataque * self.bono_armadura
        return h_ataque
    
    def habilidad_Guerrero_Defensa(self):
        h_defensa = self.bono_armadura * 3
        return h_defensa
    
    def set_HabilidadGuerrero(self, set_habilidadguerrero : int):
        self.habilidad_guerrero = set_habilidadguerrero

    @property
    def get_HabilidadGuerrero(self):
        return self.habilidad_guerrero
    
    def set_bonoArmadura(self, set_bonoarmadura : float):
        self.bono_armadura = set_bonoarmadura

    @property
    def get_bonoArmadura(self):
        return self.bono_armadura

vidaRada = 15
ador = Guerrero(10,10,12,3,0,1,2,1,"Ador", 1, "Guerrero")
print(f"{ador.get_Nombre} tiene de vida :{ador.get_Vida}")
print(f"{ador.get_Nombre} es nivel : {ador.get_Nivel}")
print(f"{ador.get_Nombre} tiene de energia : {ador.get_Energia}")
print(f"{ador.get_Nombre} tiene de ataque : {ador.get_Ataque}")
print(f"{ador.get_Nombre} tiene de armadura : {ador.get_Armadura}")
print(f"{ador.get_Nombre} tiene de escudo magico : {ador.get_EscudoMag}")
print(f"{ador.get_Nombre} tiene de puntos de habilidad : {ador.get_HabilidadGuerrero} ")
print(f"{ador.get_Nombre} tiene una bonificacion de {ador.get_bonoArmadura}")

print(f"El guerrero Ador es atacado por una rata a la que le piso la cola!!")
ador.recibir_Ataque(ador.aplicar_Defensa(5, ador.get_bonoArmadura))
print(f"Ador ahora tiene {ador.get_Vida} puntos de vida y ahora el ataca con su espada")
vidaRada = vidaRada - ador.causar_Daño(0)
if vidaRada <= 0:
    print(f"La rata a muerto a causa del ataque")
    ador.movimiento(0)
    print(f"Ador a perdido {ador.get_CostoMov} de energia, tiene ahora {ador.get_Energia}")
elif vidaRada > 0:
    print(f"La rata furiosa regresa el ataquecon una mordida")
    ador.recibir_Ataque(ador.aplicar_Defensa(5, ador.get_bonoArmadura))
    print(f"Ador ahora tiene {ador.get_Vida} puntos de vida")
