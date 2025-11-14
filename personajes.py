class Personaje:

    vida = 0
    energia = 0
    ataque = 0
    armadura = 0
    escudoM = 0

    def __init__(self, vida : float, energia : float, ataque : float, armadura : float,
                  escudo_mag : float, costo_mov : float,nombre : str, nivel : int ,clase = "Humano"):
        self.nombre = nombre
        self.nivel = nivel
        self.clase = clase
        self.vida = vida
        self.energia = energia
        self.ataque = ataque
        self.armadura = armadura
        self.escudo_mag = escudo_mag
        self.costo_mov = costo_mov


    def curar_Vida(self, cura_mas : float):
        self.vida += cura_mas
        return self.vida

    def crear_EscudoM(self, escudo_mas : float):
        self.escudoM += escudo_mas
        return self.escudoM
    
    def restaurar_Energia(self, energia_mas : float):
        self.energia += energia_mas

    def aplicar_Defensa(self, daño_puro : float, bonificacion : float):
        daño_mitigado = daño_puro - (self.armadura + self.escudoM + bonificacion)
        return daño_mitigado

    def recibir_Ataque(self, daño_recibido : float):
        self.vida -= daño_recibido

    def causar_Daño(self, mod_daño : float):
        self.ataque += mod_daño
        return self.ataque

    def movimiento(self, penalizacion : float):
        self.energia -= self.costo_mov + penalizacion

    def set_Nombre(self, set_nombre : str):
        self.nombre = set_nombre

    @property
    def get_Nombre(self):
        return self.nombre
    
    def set_Nivel(self, set_nivel : int):
        self.nivel = set_nivel

    @property
    def get_Nivel(self):
        return self.nivel
    
    def set_Clase(self, set_clase : str):
        self.clase = set_clase

    @property
    def get_Clase(self):
        return self.clase

    def set_Vida(self,set_vida : float):
        self.vida = set_vida

    @property
    def get_Vida(self):
        return self.vida

    def set_Energia(self, set_energia : float):
        self.energia = set_energia

    @property
    def get_Energia(self):
        return self.energia

    def set_Ataque(self, set_ataque : float):
        self.ataque = set_ataque

    @property   
    def get_Ataque(self):
        return self.ataque

    def set_Armadura(self, set_armadura : float):
        self.armadura = set_armadura

    @property
    def get_Armadura(self):
        return self.armadura

    def set_EscudoMag(self, set_escudoMag : float):
        self.escudo_mag = set_escudoMag
        
    @property
    def get_EscudoMag(self):
        return self.escudo_mag

    def set_CostoMov(self, set_costo_mov : float):
        self.costo_mov = set_costo_mov

    @property
    def get_CostoMov(self):
        return self.costo_mov

persona = Personaje(10,10,10,10,10, 1,"Pedro", 1,)
print(f"La {persona.get_Nombre} tiene de vida :{persona.get_Vida}")
print(f"La {persona.get_Nombre} esta en el nivel :{persona.get_Nivel}")
print(f"La {persona.get_Nombre} es de clase :{persona.get_Clase}")
print(f"La {persona.get_Nombre} tiene de energia :{persona.get_Energia}")
print(f"La {persona.get_Nombre} tiene de ataque :{persona.get_Ataque}")
print(f"La {persona.get_Nombre} tiene de armadura :{persona.get_Armadura}")
print(f"La {persona.get_Nombre} tiene de escudo magico :{persona.get_EscudoMag}")
persona.recibir_Ataque(5)
persona.movimiento(2)
print(f"{persona.get_Nombre} se tropezo y ahora tiene {persona.get_Vida} de vida "
      + f",tambien termino con {persona.get_Energia} de energia")
