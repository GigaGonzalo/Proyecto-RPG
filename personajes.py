class Personaje:

    vida = 0
    energia = 0
    ataque = 0
    armadura = 0
    escudoM = 0

    def __init__(self, vida, energia, ataque, armadura, escudo_mag, costo_mov):
        self.vida = vida
        self.energia = energia
        self.ataque = ataque
        self.armadura = armadura
        self.escudo_mag = escudo_mag
        self.costo_mov = costo_mov


    def curar_Vida(self, cura_mas):
        self.vida += cura_mas
        return self.vida

    def crear_EscudoM(self, escudo_mas):
        self.escudoM += escudo_mas
        return self.escudoM
    
    def restaurar_Energia(self, energia_mas):
        self.energia += energia_mas

    def aplicar_Defensa(self, daño_puro, bonificacion):
        daño_mitigado = daño_puro - (self.armadura + self.escudoM + bonificacion)
        return daño_mitigado

    def recibir_Ataque(self, daño_recibido):
        self.vida -= daño_recibido

    def causar_Daño(self, mod_daño):
        self.ataque += mod_daño
        return self.ataque

    def movimiento(self, penalizacion):
        self.energia -= self.costo_mov + penalizacion


persona = Personaje(10,10,10,10,10, 1)
print(f"La persona tiene de vida :{persona.vida}")
print(f"La persona tiene de energia :{persona.energia}")
print(f"La persona tiene de ataque :{persona.ataque}")
print(f"La persona tiene de armadura :{persona.armadura}")
print(f"La persona tiene de escudo magico :{persona.escudoM}")
persona.recibir_Ataque(5)
persona.movimiento(2)
print(f"La persona se tropezo y ahora tiene {persona.vida} de vida "
      + f"tambien termino con {persona.energia} de energia")

class Guerrero(Personaje):

    def __init__(self, vida, energia, ataque, armadura, escudo_mag, costo_mov,
                  habilidad_guerrero, bono_armadura):
        super().__init__(vida, energia, ataque, armadura, escudo_mag, costo_mov)
        
        self.habilidad_guerrero = habilidad_guerrero
        self.bono_armadura = bono_armadura

    def habilidad_Guerrero_Ataque(self):
        h_ataque = self.ataque * self.bono_armadura
        return h_ataque
    
    def habilidad_Guerrero_Defensa(self):
        h_defensa = self.bono_armadura * 3
        return h_defensa

vidaRada = 5
ador = Guerrero(10,10,12,3,0,1,2,1)
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