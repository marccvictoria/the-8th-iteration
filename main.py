# Marc Tristan A. Victoria
# G-5L
# Final Project

# To install the needed libraries, run: pip install -r requirements.txt
# Do source venv/bin/activate before executing the program in terminal

# References
# https://docs.python.org/3/howto/curses.html
# https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/introduction/

import rich
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