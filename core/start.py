import time
import os
import platform

def animateText(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # moves cursor to next line

def start_game(name):
    os.system("cls" if platform.system() == "Windows" else "clear") 

    timebetw = 0.5
    animateText("ARGUS: “Cognitive pattern detected. Initializing Profile: Subject 08. Loading the environment…” [The world loads in like a simulation booting up: buildings mesh into place, sky texture fades in, NPCs activate.]", 0.02)
    time.sleep(timebetw)
    animateText("You stand in the heart of Year 3067’s chrome-lit metropolis. You look around and find yourself in a dystopian-like city with holographic billboards, drones humming overhead, and pedestrians walking with strangely synchronized steps.", 0.02)