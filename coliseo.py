from guerrero import ador
from personajes import persona
class Coliseo:

    dic_camp = {"P1":ador, "P2":persona}

    print("Bienvenidos Aventureros al COLISEO!!! ")
    print("El llamado a las armas es ahora!")
    print("Seleccione su Campeon!")
    
    print(f"Campeon : {dic_camp['P1'].nombre}     Lvl: {dic_camp['P1'].nivel}")
    print(f"Campeon : {dic_camp['P2'].nombre}     Lvl: {dic_camp['P2'].nivel}")