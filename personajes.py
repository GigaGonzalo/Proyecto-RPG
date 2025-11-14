class Personaje:

    vida = 0
    energia = 0
    ataque = 0
    armadura = 0
    escudoM = 0

    def __init__(self, vida, energia, ataque, armadura, escudo_mag, costo_mov,nombre, nivel,clase = "Humano"):
        self.nombre = nombre
        self.nivel = nivel
        self.clase = clase
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


persona = Personaje("Pedro", 1,10,10,10,10,10, 1)
print(f"La persona tiene de vida :{persona.nombre}")
print(f"La persona tiene de vida :{persona.nivel}")
print(f"La persona tiene de vida :{persona.vida}")
print(f"La persona tiene de energia :{persona.energia}")
print(f"La persona tiene de ataque :{persona.ataque}")
print(f"La persona tiene de armadura :{persona.armadura}")
print(f"La persona tiene de escudo magico :{persona.escudoM}")
persona.recibir_Ataque(5)
persona.movimiento(2)
print(f"{persona.nombre} se tropezo y ahora tiene {persona.vida} de vida "
      + f",tambien termino con {persona.energia} de energia")
