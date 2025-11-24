import time, os, platform
from colorama import init, Fore, Back, Style
from utils import ascii, game

init(autoreset=True) # color will automatically reset

# helper functions

def animateText(text, color=Fore.WHITE, delay=0.005):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()  # moves cursor to next line

def printLine(dialogue, line):
    if dialogue[line][0] == "n":
            animateText(dialogue[line][1], Fore.GREEN)
    elif dialogue[line][0] == "t":
        animateText(dialogue[line][1], Style.BRIGHT)
    elif dialogue[line][0] == "a":
        animateText(dialogue[line][1], Fore.BLUE + Style.BRIGHT)

def userReply(dialogue, line, name):
    while True:
        for optns in dialogue[line][2]:
            print(optns)
        choice = input(name + ": ")
        if choice == "1":
            line = dialogue[line][3][choice]
            return line
        elif choice == "2":
            line = dialogue[line][3][choice]
            return line
        else:
            print("Invalid input. Try again.\n")

# scenes

def loading(name):
    os.system("cls" if platform.system() == "Windows" else "clear") 

    animateText("Cognitive pattern detected...", delay=0.02)
    time.sleep(0.2)
    animateText("Initializing Profile: Subject 08 - " + name + ". Loading the environment…", delay=0.02)
    for i in range(1, 11):
        print("   [" + "=" * i * 5 + "] " + str(i/10 * 100) + "%")
        time.sleep(0.03)
    print("Please wait.")
    time.sleep(3)

def act1(name):
    os.system("cls" if platform.system() == "Windows" else "clear")
    print("ACT 1: THE AWAKENING PROTOCOL")
    print("Please wait.")
    time.sleep(3)
    os.system("cls" if platform.system() == "Windows" else "clear")

    dialogue = [["n", "You stand in the heart of Year 3067's chrome-lit metropolis. You look around and find yourself in a dystopian-like city with  drones humming overhead, and pedestrians walking with strangely synchronized steps."],
                ["n", "You started to feel that something isn't right. Everything feels… wrong."],
                ["n", "A mysterious figure approaches you from across the street."],
                ["n", "He doesn't move like the others. His clothes look patched, scavenged, unlike the sleek urban fashion around you."],
                ["t", "Trovius: You feel it, don't you? The cracks in this world… the things that don't make sense.", ["[1] Uhm, what… what is this?", "[2] Who are you?"], {"1":5, "2":6}],
                ["t", "Trovius: You may not understand now, but you will. Follow me… if you want answers."], # 5
                ["t", "Trovius: I'm Trovius… your friend, if you'll allow me. You may not understand now, but you will."]] # 6
    
    line = 0
    while line < len(dialogue):
        # print lines
        if line == 0:
            print(ascii.scn1)
        if line == 1:
            os.system("cls" if platform.system() == "Windows" else "clear")
            print(ascii.scn2)
        if line == 4:
            os.system("cls" if platform.system() == "Windows" else "clear")
            print(ascii.scn3)
        
        printLine(dialogue, line)

        # skip the another choice
        dialogueArr = [4]
        nextDialogueArr = [i + 1 for i in dialogueArr]

        if line in nextDialogueArr:
            line += 1

        # dialogues
        if line in dialogueArr:
            line = userReply(dialogue, line, name)
        else:
            print(Fore.RED + Style.DIM + "(Press enter to continue)")
            line += 1
            input()

def act2(name):
    os.system("cls" if platform.system() == "Windows" else "clear")
    print("ACT 2: CHASE THE GLITCH")
    print("Please wait.")
    time.sleep(3)
    os.system("cls" if platform.system() == "Windows" else "clear")

    dialogue = [["n", "As you venture with Trovius, a street vendor approaches you."],
                ["t", "Street Vendor: Hello! Are you interested in buying my cookies? Hello! Are you interested in buying my k31js/'d(gibberish)?", ["[1] Hell no!", "[2] What… what is wrong with these people?"], {"1":2, "2":3}],
                ["t", "Trovius: Language boy! Well, I mean they're not real anyways."],
                ["t", "Trovius: Yeah, well... they're not real people."],
                ["n", "Trovius gestures for you to look up."],
                ["n", "A bird hangs in the sky—frozen mid-flight, like a paused frame in a broken animation.", ["[1] Why is that bird floating? Am I going crazy?!", "[2] This isn't real, is it?"], {"1":6, "2":7}],
                ["t", "You're not crazy " + name + " but you're about to. So, keep attention to everything I will say."],
                ["t", "Real enought to fool you " + name + ". So, keep attention to everything I will say."],
                ["t", "Trovius: Listen carefully. ARGUS controls every part of this simulation… except one."],
                ["t", """Trovius:
 There's a region where its surveillance weakens. A dead zone.
 A place it cannot fully predict.
""", ["[1] And you're taking me there?", "[2] Let's get this done!"], {"1":10, "2":11}],
["t", "Yes, don't be scared now."],
["t", "That's the spirit " + name + "!"],
["t", """Trovius: It's the only path to reach ARGUS' Root Core. 
       The only path to the truth."""],
       ["a", "ARGUS: Unauthorized thought pattern detected. Subject 08, cease deviation immediately."],
       ["t", "Trovius (whispers, afraid yet determined): It always knows. But here? He just taps the wall…here it knows just a little less.”"],
       ["t", "Brace yourself… they're coming. Remember this… these aren't soldiers… they are real, they are just algorithms. And their only goal… is to repair you. Permanently."]]

    line = 0
    while line < len(dialogue):
        if line == 4:
            os.system("cls" if platform.system() == "Windows" else "clear")
            print(ascii.bird)
        if line == 12:
            os.system("cls" if platform.system() == "Windows" else "clear")
            print(ascii.unsanc_zone)
        # print lines
        printLine(dialogue, line)

        dialogueArr = [1, 5, 9]
        nextDialogueArr = [i + 1 for i in dialogueArr] # dialogue next to current dialogue line
        if line in nextDialogueArr:
            line += 1

        # dialogues
        if line in dialogueArr:
            line = userReply(dialogue, line, name)
        else:
            print(Fore.RED + Style.DIM + "(Press enter to continue)")
            line += 1
            input()

def start_game(name, load_data=None):
    os.system("cls" if platform.system()=="Windows" else "clear")
    if load_data is not None:
        # Restore saved game
        mc = load_data["MC"]
        day = load_data["day"]
    
    else:
        # Create NEW MC
        mc = {"Name": str(name),
          "HP": 20.0,
          "ATK": 5,
          "DEF": 5,
          "SPD": 5,
          "maxHP": 30.0,
          "Gold": 30,
          # inventory
          "Potion": {"Small": 0, 
                     "Big": 0, 
                     "Panacea": 0}}
        day = 1
        # mc = {"Name": str(name),
        #   "HP": 20.0,
        #   "ATK": 300,
        #   "DEF": 1000,
        #   "SPD": 1000,
        #   "maxHP": 100.0,
        #   "Gold": 300,
        #   # inventory
        #   "Potion": {"Small": 10, 
        #              "Big": 10, 
        #              "Panacea": 10}}

    
    if load_data == None:
        loading(name)
        act1(name)
        act2(name)

    game.game(mc, day) # daily activities
