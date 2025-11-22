# Marc Tristan A. Victoria
# G-5L
# Final Project

# To install the needed libraries: pip install -r requirements.txt
# Before executing the program in terminal: source venv/bin/activate

# References
# https://docs.python.org/3/howto/curses.html


import time
import curses

from core import menu, start, about, load

def main():
    namee = ""
    while True:
        choice, name = menu.main(namee) # tuple unpacking returns list of [choice, name]
        namee = name

        if choice == 0:
            start.start_game(namee)
        elif choice == 1:
            load()
        elif choice == 2:
            about.about()
        elif choice == 3:
            exit()

main()