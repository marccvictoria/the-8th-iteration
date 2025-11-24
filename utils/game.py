import random, os, platform, json
from colorama import init, Fore, Back, Style
from utils import training, fight, open_shop, ascii

def train(mc):
    os.system("cls" if platform.system()=="Windows" else "clear")
    print(ascii.train_menu)
    while True:
        choice = input("  Choice: ")
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
        elif choice == "0":
            return mc
        else:
            print("  Invalid Input. Try again.")
        
def rest(mc):
    os.system("cls" if platform.system()=="Windows" else "clear")
    print("  This option lets you replenish HP to the maxHP (Consumes 1 day).\n")
    print(ascii.sleeping)
    while True:
        choice = input("  Continue? [1] Yes [2] No: ")
        if choice == "1":
            hp_gained = mc["maxHP"] - mc["HP"]
            mc["HP"] += hp_gained
            print("  Gained +" + str(hp_gained) + "HP")
            return mc
        elif choice == "2":
            return mc
        else:
            print("  Invalid input. Please try again.")

def explore(mc):
    os.system("cls" if platform.system()=="Windows" else "clear")
    monster = {}

    tis = mc["maxHP"] + mc["ATK"] + mc["DEF"] + mc["SPD"]
    if tis < 100:
        tis_weighted = ["decr"] * 85 + ["obliv"] * 10 + ["morph"] * 5
        monster_choice = random.choice(tis_weighted)
    elif tis < 150:
        tis_weighted = ["decr"] * 45 + ["obliv"] * 45 + ["morph"] * 10
        monster_choice = random.choice(tis_weighted)
    else:
        tis_weighted = ["decr"] * 35 + ["obliv"] * 35 + ["morph"] * 30
        monster_choice = random.choice(tis_weighted)

    if monster_choice == "decr":
        monster["Name"] = "DecryptixV1"
        monster["HP"] = 50
        monster["ATK"] = 8
        monster["DEF"] = 8
        monster["SPD"] = 8
        monster["Gold Drop"] = 50
    elif monster_choice == "obliv":
        monster["Name"] = "Obliviator22"
        monster["HP"] = 100
        monster["ATK"] = 20
        monster["DEF"] = 20
        monster["SPD"] = 20
        monster["Gold Drop"] = 50
    elif monster_choice == "morph":
        monster["Name"] = "MorpheusR3"
        monster["HP"] = 200
        monster["ATK"] = 50
        monster["DEF"] = 50
        monster["SPD"] = 50
        monster["Gold Drop"] = 500

    old_gold = mc["Gold"]
    curr_gold = mc["Gold"] + fight.fight_monster(mc, monster) # fight the monster
    print("Old Gold: " + str(old_gold))
    print("Current Gold: " + str(curr_gold))
    return curr_gold

def shop(mc):
    mc = open_shop.buy(mc)
    return mc

def save(mc, current_day):
    os.system("cls" if platform.system()=="Windows" else "clear")
    save_data = {
        "MC": mc,
        "day": current_day
    }
    save_path = os.path.join("data", "game.save")
    with open(save_path, "w") as f:
        json.dump(save_data, f, indent=4) # json.dump converts save_data dictionary into json format and writes it to the file

    print("\n  📁 Progress saved successfully!")
    # input("\nPress Enter to continue...")

def status(mc):
    print("\n===== STATUS =====")
    print(f"|| Name: {mc['Name']}")
    print(f"|| HP: {mc['HP']} / {mc['maxHP']}")
    print(f"|| ATK: {mc['ATK']}")
    print(f"|| DEF: {mc['DEF']}")
    print(f"|| SPD: {mc['SPD']}")
    print(f"|| Gold: {mc['Gold']}")
    print("|| Potions:")
    for potion, count in mc["Potion"].items():
        print(f"||  {potion}: {count}")
    print("==================\n")


def exit():
    return

def game(mc, day):
    # print(day)
    while True:
        # boss fight
        if day == 20:
            os.system("cls" if platform.system()=="Windows" else "clear")
            fb = {"Name": "Argus",
                          "HP": 200,
                          "ATK": 75,
                          "DEF": 75,
                          "SPD": 75}
            fight.final_boss(mc, fb)
            # win or lose, reset
            break

        input("\n  Press Enter to continue...")
        os.system("cls" if platform.system()=="Windows" else "clear")
        print(ascii.game_display_menu)
        print("\t" + Fore.GREEN + Back.BLACK + "Day " + str(day))
        choice = input(("\n\tChoice: "))

        if choice == "1": # train
            mc = train(mc)
            day += 1
        elif choice == "2": # rest
            mc = rest(mc)
            day += 1
        elif choice == "3": # explore
            mc["Gold"] = explore(mc)
            day += 1
        elif choice == "4": # shop
            mc = shop(mc)
        elif choice == "5": # save
            save(mc, day)
        elif choice == "6": # status
            os.system("cls" if platform.system()=="Windows" else "clear")
            status(mc)
        elif choice == "7": # exit
            break # proceeds to start menu, will not save the game
        else:
            print("Invalid input. Try again.")

        