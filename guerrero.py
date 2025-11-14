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

vidaRada = 5
ador = Guerrero(10,10,12,3,0,1,2,1,"Ador", 1, "Guerrero")
print(f"ADOR tiene de vida :{ador.vida}")
print(f"ADOR tiene de energia :{ador.energia}")
print(f"ADOR tiene de ataque :{ador.ataque}")
print(f"ADOR tiene de armadura :{ador.armadura}")
print(f"ADOR tiene de escudo magico :{ador.escudoM}")
print(f"ADOR tiene de puntos de habilidad : {ador.habilidad_guerrero} ")
print(f"ADOR tiene una bonificacion de {ador.bono_armadura}")

print(f"El guerrero Ador es atacado por una rata a la que le piso la cola!!")
ador.recibir_Ataque(ador.aplicar_Defensa(5, ador.bono_armadura))
print(f"Ador ahora tiene {ador.vida} puntos de vida y ahora el ataca con su espada")
vidaRada = vidaRada - ador.causar_Daño(0)
if vidaRada <= 0:
    print(f"La rata a muerto a causa del ataque")
    ador.movimiento(0)
    print(f"Ador a perdido {ador.costo_mov} de energia, tiene ahora {ador.energia}")
elif vidaRada > 0:
    print(f"La rata furiosa regresa el ataquecon una mordida")
    ador.recibir_Ataque(ador.aplicar_Defensa(5, ador.bono_armadura))
    print(f"Ador ahora tiene {ador.vida} puntos de vida")
