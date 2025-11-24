import os, platform, json

def load_data():
    os.system("cls" if platform.system()=="Windows" else "clear")
    save_path = os.path.join("data", "game.save")  # path in "data" folder
    if not os.path.exists(save_path):
        print("\n  No save file found.")
        return None, None

    with open(save_path, "r") as f:
        data = json.load(f)

    print("\n  📁 Save file loaded successfully!")
    input("\n  Press Enter to continue...")
    return data