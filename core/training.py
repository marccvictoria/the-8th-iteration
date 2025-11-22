import random

def stamina(maxHP):
    additional = random.randint(5, 20)
    maxHP += additional
    return maxHP

def strength(atk):
    additional = random.randint(5, 20)
    atk += additional
    return atk

def resilience(defen):
    additional = random.randint(5, 20)
    defen += additional
    return defen

def dexterity(spd):
    additional = random.randint(5, 20)
    spd += additional
    return spd

def guts(mc):
    exclude = ["Name", "HP", "Gold", "Potion"]
    for stat in mc:
        additional = random.randint(5, 15)
        if stat not in exclude:
            mc[stat] += additional
    return mc