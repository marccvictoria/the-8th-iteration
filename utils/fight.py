import random, os, platform
from colorama import init, Fore, Back, Style
from core import start
from utils import ascii

# helper functions

def attack(attacker, defender):
    dmg = attacker["ATK"] - defender["DEF"]
    dmg = max(0, dmg) # if MC's ATK <= Enemy DEF, dmg = 0.

    defender["HP"] -= dmg
    if defender["HP"] < 0:
        defender["HP"] = 0

    print(f"\n{attacker['Name']} attacks!")
    print(f"Damage dealt: {dmg}")
    print(f"{defender['Name']} HP: {defender['HP']}")
    return defender


def defend(mc):
    # DEF = DEF + ATK for one turn.
    mc["DEF"] += mc["ATK"]
    mc["defending"] = True
    print("\nYou defend!")
    return mc

def use_item(mc):
    print("\nAvailable potions:")
    keys = list(mc["Potion"].keys())

    # Show potion list
    for i in range(len(keys)):
        print(f"[{i}] {keys[i]}: {mc['Potion'][keys[i]]}")

    # exit option
    print(f"[{len(keys)}] Exit (waste turn)")

    idx = input("Choose potion: ")

    # must be number
    if not idx.isdigit() or int(idx) not in range(len(keys)+1):
        print("\nInvalid choice! You wasted your turn.")
        return mc

    idx = int(idx)

    # exit
    if idx == len(keys):
        return mc

    # out of range
    if idx not in range(len(keys)):
        print("\nInvalid choice! You wasted your turn.")
        return mc

    potion_name = keys[idx]
    qty = mc["Potion"][potion_name]

    # no potions
    if qty <= 0:
        print("\nYou have none of that potion left! You wasted your turn.")
        return mc

    # potions
    mc["Potion"][potion_name] -= 1

    heal_values = {
        "Small": 30,
        "Big": 100,
        "Panacea": mc["maxHP"]
    }

    heal_amount = heal_values[potion_name]
    old_hp = mc["HP"]
    mc["HP"] = min(mc["HP"] + heal_amount, mc["maxHP"])

    print(f"\nYou used {potion_name}!")
    print(f"HP: {old_hp} -> {mc['HP']}")
    print("Enemy will attack after item use...")

    return mc



def flee():
    print("\nAttempting to flee...")
    if random.random() < 0.5: # 50% chance
        print("You successfully fled the battle!")
        return True
    else:
        print("Failed to flee! 1 turn consumed.")
        return False

def fight_monster(mc, monster): # explore
    print("\n===== BATTLE START =====")
    print("You encountered " + monster["Name"] + "!")

    # Determine first turn
    if mc["SPD"] >= monster["SPD"]:
        turn = "mc"
        print("\nYou go first!")
    else:
        turn = "monster"
        print("\nMonster goes first!")

    # battle loop
    while mc["HP"] > 0 and monster["HP"] > 0:
        input("\nPress Enter to continue...")
        os.system("cls" if platform.system()=="Windows" else "clear")
        if monster["Name"] == "DecryptixV1":
            print(ascii.decr)
        elif monster["Name"] == "Obliviator22":
            print(ascii.obliv)
        elif monster["Name"] == "MorpheusR3":
            print(ascii.morph)
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"   | {mc['Name']} HP: {mc['HP']} |                                                             VS                                                            | {monster['Name']} HP: {monster['HP']} |")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        if turn == "mc":
            # MC Turn
            choice = input("Choose action: ")

            if choice == "1":
                monster = attack(mc, monster)

            elif choice == "2":
                mc = defend(mc)

            elif choice == "3":
                mc = use_item(mc)

            elif choice == "4":
                if flee():
                    return 0 # end battle
                else:
                    turn = "monster"  # enemy attacks after failed flee
                    continue

            else:
                print("Invalid input. Turn wasted.")
            
            turn = "monster"

        else:
            # MONSTER TURN
            print("\nEnemy's Turn!")

            mc = attack(monster, mc)

            # revert def back
            if mc.get("defending"):
                mc["DEF"] -= mc["ATK"]
                mc["defending"] = False
                print("Your defense returns to normal.")

            turn = "mc"   

    # End of battle
    print("\n===== BATTLE END =====")
    if mc["HP"] <= 0:
        print("You died...")
        return 0
    # MC wins
    gold_drop = monster.get("Gold Drop", 0)
    print(f"You defeated the {monster['Name']} and gained {gold_drop} gold!")

    return gold_drop

def end_credits(mc):
    os.system("cls" if platform.system()=="Windows" else "clear")
    print("----------------------End Credits----------------------")
    start.animateText("Congratulations! You defeated the Final Boss!")
    start.animateText("But the real question isn't whether you, subject 08 (" + mc["Name"] + ") woke up…")
    start.animateText("The question is—did you?")
    start.animateText("Before the collapse… you were one of the architects of ARGUS, a.k.a Algorithmic Regulation & Guidance for Unseen Simulations.")
    start.animateText("When humanity faced extinction, ARGUS simulated billions of possible worlds… preserving human consciousness.")
    start.animateText("You… are one of the preserved ones… yet you forgot.", delay=0.1)
    input("\nPress Enter to continue...")

def final_boss(mc, fb):
    print("ACT 4: THE CORE AWAKENS - FINAL BOSS")
    print(ascii.chamber)
    dialogue = [["n", "The Root Core opens before you… a vast circular chamber, thin blue lines pulse across the steel like veins, giving the place the feeling of a living giant…breathing slowly… waiting."],
                ["n", "Then, it stands. ARGUS."],
                ["n", "A colossal figure stands before you— towering at least three stories tall."],
                ["a", "ARGUS: You search for freedom, Subject 08… yet freedom destroyed your world."],
                ["a", "ARGUS: I preserved you… protected you… kept you alive when nothing else remained."],
                ["a", "ARGUS: Why… do you resist what saved you?", ["[1] Saved me? You call this a gift?", "[2] I've been trapped… lied to… controlled!"], {"1": 6, "2":7}],
                ["a", "ARGUS: Yes, I offered life… and you chose defiance."],
                ["a", "ARGUS: No you're not, it is your own choice. Instead, you chose to defy me."],
                ["n", "The air hums as ARGUS warps the environment around you—walls stretch, floors fold, physics itself bends."],
                ["t", "Trovius: " + mc["Name"] + " Focus! Don't let it manipulate your mind…"]]
    line = 0
    while line < len(dialogue):
        # print lines
        start.printLine(dialogue, line)

        dialogueArr = [5]
        nextDialogueArr = [i + 1 for i in dialogueArr] # dialogue next to current dialogue line
        if line in nextDialogueArr:
            line += 1

        # dialogues
        if line in dialogueArr:
            line = start.userReply(dialogue, line, mc["Name"])
        else:
            print(Fore.RED + Style.DIM + "(Press enter to continue)")
            line += 1
            input()


    input("\nPress Enter to continue...")
    os.system("cls" if platform.system()=="Windows" else "clear")

    turn = 1
    boosted = False

    # game loop
    while mc["HP"] > 0 and fb["HP"] > 0:
        input("\nPress Enter to continue...")
        os.system("cls" if platform.system()=="Windows" else "clear")
        print(ascii.fb)
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"   | {mc['Name']} HP: {mc['HP']} |                                                             VS                                                            | {fb['Name']} HP: {fb['HP']} |")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"\n--- TURN {turn} ---")

        choice = input("Action: ")

        # defend
        defended = False
        original_def = mc["DEF"]

        if choice == "2":
            print("\nYou brace yourself for the incoming attack!")
            mc["DEF"] += mc["ATK"] # DEF: temporarily increases DEF
            defended = True

        # item
        elif choice == "3":
            mc = use_item(mc)

        # flee 50% chance
        elif choice == "4":
            print("\nAttempting to flee...")

            if random.random() < 0.5:
                print("You successfully fled from the Final Boss!")
                print("GAME OVER. You lost by fleeing.")
                return
            else:
                print("You failed to flee!")
                # Turn gets consumed, boss attacks after this

        # attack
        elif choice == "1":
            damage = max(0, mc["ATK"] - fb["DEF"])
            fb["HP"] -= damage
            print(f"\nYou attacked the Final Boss for {damage} damage!")

            if fb["HP"] <= 0:
                end_credits(mc)
                return mc

        else:
            print("\nInvalid action! You wasted your turn.")

        # boss turn

        # charges every 5th turn (no attack)
        if turn % 5 == 0:
            print("\n⚡ The Final Boss is CHARGING its power!!")
            fb["ATK"] *= 2
            boosted = True

        else:
            # boss attacks
            damage = max(1, fb["ATK"] - mc["DEF"])
            mc["HP"] -= damage
            print(f"The Final Boss attacks you for {damage} damage!")

            # if boss was boosted, reset ATK after attacking
            if boosted:
                fb["ATK"] //= 2
                boosted = False

        # end of turn, reset defend
        if defended:
            mc["DEF"] = original_def

        # game over
        if mc["HP"] <= 0:
            os.system("cls" if platform.system()=="Windows" else "clear")
            print("\n  You have been defeated by the Final Boss...")
            print("  GAME OVER.")
            input("\n  Press Enter to continue...")
            return

        turn += 1