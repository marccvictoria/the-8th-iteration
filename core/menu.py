import curses
# (row, column) => (y, x)

def main(namee):
    result = [] # curses doesn't allow returning ...
    def menu(stdscr):
        # colors
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)  # Green text
        curses.init_pair(2, curses.COLOR_CYAN, -1)   # Cyan text
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)  # highlight

        stdscr.clear()

        title = """                                                                 
                                                                            
                     ███████╗██╗  ██╗ ██████╗     █████╗ ██ █████╗██╗  ██╗        
                    ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗╚══██╔══╝██║  ██║        
                       ██║    ██████║█████╗      ╚█████╔╝   ██║    ██████║        
                        █║   ██╔══██║██╔══╝      ██╔══██╗   ██║   ██╔══██║        
                        ██║   ██║  ██║█████ █╗    ╚█████╔╝   ██║   ██║  █ ║        
                        ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚════╝    ╚═╝   ╚═╝  ╚═╝        
                                                                            
            ██╗████████╗███████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗  
            ██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║  
            ██║   ██║   █████╗  ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║  
            █1║   █0║   ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║0█║   ██║██║╚██╗█0║  
            █00   0█║   ██0███0╗██║  ██║██║  0█║   1█0   █0║╚██10█0╔╝█0║ ╚0██0║  
            0 1   0═1   ╚0═000═╝╚0╝  0═00═╝  ╚1╝   101   10╝ 10═0═0╝ ╚0╝  10═0╝  
            10 1     01   01  01    1    0      0   10  0 1  0  1 0 0   1   1 0  01

            """
        # stdscr.addstr(8, 0, title, curses.color_pair(1))
        x_offset = 10
        for i, line in enumerate(title.splitlines()):
            stdscr.addstr(8 + i, x_offset, line, curses.color_pair(1))
            
        # add subwindow
        nrow = 18
        ncol = 38
        begin_y = 8
        begin_x = 100
        sub_win = curses.newwin(nrow, ncol, begin_y, begin_x)
        sub_win.refresh()

        text1 = "Welcome, player!"
        sub_win.addstr(3, ncol//2 - len(text1)//2, text1)
        options_arr = ["[1] START", "[2] LOAD", "[3] ABOUT", "[4] EXIT"]
        sub_win.addstr(5, ncol//2 - len(options_arr[0])//2, options_arr[0])
        sub_win.addstr(7, ncol//2 - len(options_arr[1])//2, options_arr[1])
        sub_win.addstr(9, ncol//2 - len(options_arr[2])//2, options_arr[2])
        sub_win.addstr(11, ncol//2 - len(options_arr[3])//2, options_arr[3])

        # get name
        if namee == "":
            stdscr.addstr(30, 15, ">" * 130, curses.color_pair(1))
            stdscr.addstr(32, 15, "<" * 130, curses.color_pair(1))
            stdscr.addstr(31, 50, ">>>>> Identify yourself (Nickname): ", curses.color_pair(2)) # 36 char
            stdscr.refresh()
            curses.echo() # for input
            name = stdscr.getstr(31, 86).decode("utf-8")

            # clear after
            stdscr.addstr(30, 0, " " * 150)
            stdscr.addstr(31, 0, " " * 150)
            stdscr.addstr(32, 0, " " * 150)
            stdscr.refresh()
        else:
            name = namee

        # update welcome message
        sub_win.addstr(3, ncol//2 - len(text1)//2, " " * 16, curses.color_pair(1)) # clear placeholder
        sub_win.addstr(3, ncol//2 - len(name)//2 - 4, "Welcome, " + name + "!", curses.color_pair(1))
        sub_win.refresh()

        curses.curs_set(0) # Hide cursor
        curses.noecho()
        curses.cbreak()
        sub_win.keypad(True)

        curr_row = 0
    
        while True:
            for i, j in enumerate(options_arr):
                if i == curr_row:
                    sub_win.addstr(2 * i + 5, ncol//2 - len(j)//2, "> " + j, curses.color_pair(3))
                else:
                    sub_win.addstr(2 * i + 5, ncol//2 - len(j)//2, " " * 11)
                    sub_win.addstr(2 * i + 5, ncol//2 - len(j)//2, j)
            sub_win.refresh()
                
            key = sub_win.getch()
            if key == curses.KEY_UP and curr_row > 0:
                curr_row -= 1
            elif key == curses.KEY_DOWN and curr_row < len(options_arr) - 1:
                curr_row += 1
            elif key == 10 or key == 13: # enter key code
                result.append(curr_row)
                result.append(name)
                break

    curses.wrapper(menu)
    return result[0], result[1]