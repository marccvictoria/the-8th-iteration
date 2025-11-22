import random
from core import training

def train(mc):
    choice = input("Choice: ")
    if choice == "1":
        mc["maxHP"] = training.stamina(mc["maxHP"])
        return mc
    elif choice == "2":
        mc["ATK"] = training.strength(mc["ATK"])
        return mc
    elif choice == "3":
        mc["DEF"] = training.resilience(mc["DEF"])
        return mc
    elif choice == "4":
        mc["SPD"] = training.dexterity(mc["SPD"])
        return mc
    elif choice == "5":
        mc = training.guts(mc)
        return mc
        
def rest(mc):
    hp_gained = mc["maxHP"] - mc["HP"]
    mc["HP"] += hp_gained
    print("Gained +" + hp_gained + "HP")
    return mc

def explore(mc):
    monster_stat = {}

    tis = mc["maxHP"] + mc["ATK"] + mc["DEF"] + mc["SPD"]
    if tis < 100:
        tis_weighted = ["decr"] * 85 + ["obliv"] * 10 + ["morph"] * 5
        monster = random.choice(tis_weighted)

    if monster == "decr":
        monster_stat["HP"] = 50
        monster_stat["ATK"] = 8
        monster_stat["DEF"] = 8
        monster_stat["SPD"] = 8
        monster_stat["Gold Drop"] = 50
    elif monster == "obliv":
        monster_stat["HP"] = 100
        monster_stat["ATK"] = 20
        monster_stat["DEF"] = 20
        monster_stat["SPD"] = 20
        monster_stat["Gold Drop"] = 50
    elif monster == "morph":
        monster_stat["HP"] = 200
        monster_stat["ATK"] = 50
        monster_stat["DEF"] = 50
        monster_stat["SPD"] = 50
        monster_stat["Gold Drop"] = 500

def shop():
    pass

def save():
    pass

def status():
    pass

def exit():
    pass

def game(name):
    mc = {"Name": name,
          "HP": 20.0,
          "ATK": 5,
          "DEF": 5,
          "SPD": 5,
          "maxHP": 30.0,
          "Gold": 30,
          "Potion": {"Small": 0, 
                     "Big": 0, 
                     "Panacea": 0}}
    day = 1
    
    while True:
        choice = input(("Choice: "))

        if choice == "1":
            mc = train(mc)
            day += 1
        elif choice == "2":
            mc = rest(mc)
            day += 1
        elif choice == "3":
            explore()
        elif choice == "4":
            shop()
        elif choice == "5":
            save()
        elif choice == "6":
            status()
        elif choice == "7":
            exit()
        else:
            print("Invalid input. Try again.")