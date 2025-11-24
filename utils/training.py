import random

def stamina(maxHP):
    old = maxHP
    additional = random.randint(5, 20)
    maxHP += additional
    print(f"  maxHP: {old} -> {maxHP} (+{additional})")
    return maxHP

def strength(atk):
    old = atk
    additional = random.randint(5, 20)
    atk += additional
    print(f"  ATK: {old} -> {atk} (+{additional})")
    return atk

def resilience(defen):
    old = defen
    additional = random.randint(5, 20)
    defen += additional
    print(f"  DEF: {old} -> {defen} (+{additional})")
    return defen

def dexterity(spd):
    old = spd
    additional = random.randint(5, 20)
    spd += additional
    print(f"  SPD: {old} -> {spd} (+{additional})")
    return spd

def guts(mc):
    exclude = ["Name", "HP", "Gold", "Potion"]
    for stat in mc:
        old = mc[stat]
        additional = random.randint(5, 15)
        if stat not in exclude:
            mc[stat] += additional
            print(f"  {stat}: {old} -> {mc[stat]} (+{additional})")
    return mc