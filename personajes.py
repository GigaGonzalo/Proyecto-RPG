class Personaje:

    vida = 0
    energia = 0
    ataque = 0
    armadura = 0
    escudoM = 0

    def __init__(self, vida, energia, ataque, armadura, escudoM):
        self.vida = vida
        self.energia = energia
        self.ataque = ataque
        self.armadura = armadura
        self.escudoM = escudoM


    def curar_Vida(self, cura_mas):
        self.vida += cura_mas
        return self.vida
    
    def incrementar_Armadura(self, arma_mas):
        self.armadura += arma_mas
        return self.armadura
    
    def crear_EscudoM(self, escudo_mas):
        self.escudoM += escudo_mas
        return self.escudoM
    
    def restaurar_Energia(self, energia_mas):
        self.energia += energia_mas

    def aplicar_Defensa(self, daño_puro):
        daño_mitigado = daño_puro - (self.armadura + self.escudoM)
        return daño_mitigado

    def recibir_Ataque(self, daño_recibido):
        self.vida -= daño_recibido

    def causar_Daño(self, mod_daño):
        self.ataque += mod_daño
        return self.ataque

    def movimiento(self,costo):
        self.energia -= costo


persona = Personaje(10,10,10,10,10)
print(f"La persona tiene de vida :{persona.vida}")
print(f"La persona tiene de energia :{persona.energia}")
print(f"La persona tiene de ataque :{persona.ataque}")
print(f"La persona tiene de armadura :{persona.armadura}")
print(f"La persona tiene de escudo magico :{persona.escudoM}")
persona.recibir_Ataque(5)
persona.movimiento(3)
print(f"La persona se tropezo y ahora tiene {persona.vida} de vida "
      + f"tambien termino con {persona.energia} de energia")