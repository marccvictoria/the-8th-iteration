# Marc Tristan A. Victoria
# G-5L
# Final Project: A terminal-based RPG.

# To install the needed libraries: pip install -r requirements.txt
# Before executing the program in terminal: source venv/bin/activate

# References
# https://docs.python.org/3/howto/curses.html
# https://stackoverflow.com/questions/26282222/generating-random-numbers-in-python-with-percentage-function-on-what-selected-va
# https://www.geeksforgeeks.org/python/python-shutil-get_terminal_size-method/

import time, curses, os, platform, shutil

from core import menu, start
from utils import about
from data import load

MIN_ROWS = 41
MIN_COLS = 160

def check_terminal_size():
    os.system("cls" if platform.system()=="Windows" else "clear")
    size = shutil.get_terminal_size()  # returns (columns, lines)
    cols, rows = size.columns, size.lines

    if rows < MIN_ROWS or cols < MIN_COLS:
        print(f"ERROR: Terminal too small!")
        print(f"Current terminal size: {cols}x{rows}")
        print("Resize your terminal and rerun the program.")
        input("\nPress Enter to exit...")
        exit()

    os.system("cls" if platform.system()=="Windows" else "clear")

check_terminal_size()

def main():
    namee = ""
    day = 1
    while True:
        choice, name = menu.main(namee) # tuple unpacking returns list of [choice, name]
        namee = name

        if choice == 0:
            start.start_game(namee, load_data=None)
        elif choice == 1:  # Load game
            data = load.load_data()
            if data is None:
                print("\nNo save file found. Starting new game instead.")
                start.start_game(namee, load_data=None)
            else:
                mc = data["MC"]
                day = data["day"]
                start.start_game(mc["Name"], load_data=data)
        elif choice == 2:
            about.about()
        elif choice == 3:
            os.system("cls" if platform.system()=="Windows" else "clear")
            exit()

main()