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

from core import start_menu as menu

def main():
    menu.start()
    

main()