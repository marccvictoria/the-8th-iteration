import curses
# (row, column) => (y, x)

def start(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)  # Green text
    curses.init_pair(2, curses.COLOR_CYAN, -1)   # Cyan text

    stdscr.clear()

    # ASCII title
    title = """                                                                                   █▒░════════════════════════════════░▒█
                                                                                   ║                                    ║
                  ████████╗██╗  ██╗███████╗     █████╗ ████████╗██╗  ██╗           ║                                    ║
                  ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗╚══██╔══╝██║  ██║           ║          Welcome, player!          ║
                     ██║   ███████║█████╗      ╚█████╔╝   ██║   ███████║           ║                                    ║
                     ██║   ██╔══██║██╔══╝      ██╔══██╗   ██║   ██╔══██║           ║            [ 1 ] START             ║
                     ██║   ██║  ██║███████╗    ╚█████╔╝   ██║   ██║  ██║           ║                                    ║
                     ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚════╝    ╚═╝   ╚═╝  ╚═╝           ║            [ 2 ] LOAD              ║
                                                                                   ║                                    ║
           ██╗████████╗███████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗     ║            [ 3 ] ABOUT             ║
           ██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║     ║                                    ║
           ██║   ██║   █████╗  ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║     ║            [ 4 ] EXIT              ║
           █1║   █0║   ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║0█║   ██║██║╚██╗█0║     ║                                    ║
           █00   0█║   ██0███0╗██║  ██║██║  0█║   1█0   █0║╚██10█0╔╝█0║ ╚0██0║     ║                                    ║
           0 1   0═1   ╚0═000═╝╚0╝  0═00═╝  ╚1╝   101   10╝ 10═0═0╝ ╚0╝  10═0╝     ║                                    ║
         10 1     01   01  01    1    0      0   10  0 1  0  1 0 0   1   1 0  01   ║                                    ║
                                                                                   ║                                    ║
                                                                                   █▒░════════════════════════════════░▒█"""

    stdscr.addstr(0, 0, title, curses.color_pair(1))

    stdscr.addstr(20, 0, ">" * 130, curses.color_pair(1))
    stdscr.addstr(22, 0, "<" * 130, curses.color_pair(1))

    stdscr.addstr(21, 0, ">>>>> Identify yourself (Nickname): ", curses.color_pair(2)) # 36 char
    stdscr.refresh()

    curses.echo()

    name = stdscr.getstr(21, 36).decode("utf-8")

    # Welcome message
    stdscr.addstr(3, 103, " " * 7, curses.color_pair(1))
    stdscr.addstr(3, 103, name + "!", curses.color_pair(1))
    stdscr.refresh()

    stdscr.addstr(21, 0, "")

    # Arrow keys
    curses.curs_set(0)  # Hide cursor
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)   # normal green
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)  # highlight
    
    menu = ["START NEW MISSION", "LOAD SESSION", "ABOUT", "EXIT"]
    current_row = 0

    while True:
        stdscr.clear()
        # ASCII header
        stdscr.addstr(0, 0, "███ W E L C O M E ███\n▒▓░░ PLAYER INITIATE ░░▓▒", curses.color_pair(1))
        
        # Draw menu
        for idx, row in enumerate(menu):
            if idx == current_row:
                stdscr.addstr(5 + idx, 0, f"> {row}", curses.color_pair(2))  # highlight
            else:
                stdscr.addstr(5 + idx, 0, f"  {row}", curses.color_pair(1))
        
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key in [10, 13]:  # Enter key code 10 or 13
            stdscr.clear()
            stdscr.addstr(0, 0, f"You selected: {menu[current_row]}", curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()
            break

curses.wrapper(start)
