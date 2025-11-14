from guerrero import ador
from personajes import persona

class Coliseo:

    dic_camp = {"P1":ador, "P2":persona}

    print("Bienvenidos Aventureros al COLISEO!!! ")
    print("El llamado a las armas es ahora!")
    print("Seleccion de Campeones!")
    
    print(f"Campeon : {dic_camp['P1'].get_Nombre}     Lvl: {dic_camp['P1'].get_Nivel}")
    print(f"Campeon : {dic_camp['P2'].get_Nombre}     Lvl: {dic_camp['P2'].get_Nivel}")
