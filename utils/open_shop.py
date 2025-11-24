from utils import ascii
import os, platform

def buy(mc):
    os.system("cls" if platform.system()=="Windows" else "clear")
    shop_items = {
        "1": {"name": "Electro Sword", "stat": "ATK", "value": 10, "cost": 30},
        "2": {"name": "Edge of Annhilation", "stat": "ATK", "value": 25, "cost": 60},
        "3": {"name": "TheAbsolutelyOPSwordofMaxDestructionv3", "stat": "ATK", "value": 50, "cost": 100},
        
        "4": {"name": "Nano Vest", "stat": "DEF", "value": 10, "cost": 30},
        "5": {"name": "Titanium Exosuit", "stat": "DEF", "value": 25, "cost": 60},
        "6": {"name": "Energy Dome", "stat": "DEF", "value": 50, "cost": 100},
        
        "7": {"name": "Deca Sandals", "stat": "SPD", "value": 10, "cost": 30},
        "8": {"name": "Octa Shoes", "stat": "SPD", "value": 25, "cost": 60},
        "9": {"name": "Hexa Striders", "stat": "SPD", "value": 50, "cost": 100},
        
        "10": {"name": "Data Patch Potion", "stat": "Potion", "key": "Small", "value": 1, "cost": 15},
        "11": {"name": "System.Restore Potion", "stat": "Potion", "key": "Big", "value": 1, "cost": 30},
        "12": {"name": "Auto-Repair Robot", "stat": "Potion", "key": "Panacea", "value": 1, "cost": 50}
    }

    while True:
        print("\n  ═════════════════════════════════════════════════════════════════════ SHOP MENU ════════════════════════════════════════════════════════════════════════════")
        print(f"  Gold: {mc['Gold']}")
        print(ascii.shop)

        choice = input("  Choose an item to buy (number): ")

        if choice == "0":
            break
        elif choice in shop_items:
            item = shop_items[choice]

            if mc["Gold"] < item["cost"]:
                print("  Not enough gold!")
                input("\n  Press Enter to continue...")
                os.system("cls" if platform.system()=="Windows" else "clear")
                continue

            mc["Gold"] -= item["cost"]

            if item["stat"] == "Potion":
                mc["Potion"][item["key"]] += item["value"]
                print(f"  Bought {item['name']}. You now have {mc['Potion'][item['key']]} {item['key']} Potion(s).")
            else:
                old_value = mc[item["stat"]]
                mc[item["stat"]] += item["value"]
                print(f"  {item['stat']}: {old_value} -> {mc[item['stat']]}")

        else:
            print("  Invalid choice. Try again.")

        input("\n  Press Enter to continue...")
        os.system("cls" if platform.system()=="Windows" else "clear")

    return mc
