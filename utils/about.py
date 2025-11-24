import curses
import os
import platform

def about():
    os.system("cls" if platform.system() == "Windows" else "clear") # might conflict with other os
    print("""
                                                      █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
                                                      ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
                                                      ███████║██████╔╝██║   ██║██║   ██║   ██║   
                                                      ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║   
                                                      ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║   
                                                      ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   

                                                                      =...........+    
                                                                  +.##%%%1@###%%#**==.#
                                                                @@-@@%%00%%%#11+%@00..@@.
                                                                @.@@@1%%@%%@%0%+=110*%@@#.
                                                              @@+.*%0@#1010@1%1@%%0%10@+..+        
                                                              0@*.*%000001@0@00110@%@@@+:.#            
                              "Every decision you make          %@.*%@@0110001@@00@0@0##*-.*    # Developer's Info         
                            in this game mirrors the           %#+.#%@@@@@@@@@@@@@@@@@@%#*.*%%    student.developer = "Marc";     
                              question of autonomy,          @@%..:#@@@@@@@@@@@@@@@@@@%....*#    student.labSection = "G-5L";
                              morality, and the limits         #=...*@@@@@@@%%%%%@@@@@@%....=*    student.name = "Marc Tristan A. Victoria";
                            of human agency in a world       @@#%+.#@@@@@@@@@@@@@@@@@@%-.*%  
                            shaped by intellegence           @#@.@@##%#%#%#%@@@%%#####*%@@.%                
                              greater than mankind."          @@.@-:%  #@@@%%%%%@@%*  %.#@.         "In this post-apocalyptic world,
                                                              @@.@%%+% %@@-%@@@%-@@% %-##@.       will you succumb to illusion
                                                                @:.-%%#%%@@@#@@@@@@%%%%##..:         or face the painful reality?"
                                                                *%.-%@@@@@@@#@@@#@@@@@@@%..%+   
                                                                *@@--*##%%%#-%@@:%%%%##*:=@@+   
                                                              @@%@@@#@@@@@*####*%@@@@@+%@@*
                                                              @#%%@@%.#@@@@@@@@@@@=-@@@%%%@
                                                                *@%%%*=:%@@@@@@@@@*.*%%%@*    # Copyright (c)
                                                                  *%@-@@@+###%@%###-%#%-@@#   Some ASCII ART has been modified for use.
                                              "INSPIRATIONS:     *#=@@@+:*========+.+%@%#*%     Original artworks belong to its respective artists.
                                              The Matrix and    @#.=-%@#.####%#*#%.#@#=+.#    (see ascii_references.txt for the comprehensive list)
                                          The Truman Show"       @.+#@%+.===========+###..@    
                                                              ---...#%%@+=#########:*@@%....=.=                    
                                                          %:+*#....:+#@#@@@%@%@@@@%%@:.... .=::.%                
                                                        #..*%%%@--.::-=*%%@@@@@@@@@#=-......:#***-..+                
                                                    =.-*--#%%%%@#+---==++*#%#@@#@*-.........+#*###*..-:..               
                                                .:+**##*+#%@@@%@%#+=====+++#@@@@@#.....  ...####*%#*::=+++-:.*               
                                          :.-+##%%%=####%@@@@@@%%*++=====@@@@@@@@@+. .. ..##%#####%+-==-###*+=:..*             
                                  -..:=+*##%%%%%%%%%%%%%@@@@@@@%%@++===*@@@@@@@@@@@%.. ..-*#%%%###%%%%%%%######**+=-:...      
                                  -@%%%%%@@@@@@@@@@@@@@@@@@@@@@@%%%%===%@@@@@@@@@@@@@@#...+*%%%%%%%%%%%+%%%%%%%%%%%%#####%.        
                                .=@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@%%%#@@@@@@@@@@@@@@@@%%#**#%@%%%%%%%%%%%%%%%%%%%@@@@%%%@@:.       

""")
    while True:
        back = input("Type Y to go back to main menu: ")
        if back == "Y":
            return
        else:
            print("Invalid Input")