import time
import os
import platform

scn1 = """
  ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                        *           +                  ___+                        ||                                       
                                                    ___|+__   _____|                /! # !                   ______||_____                                   
                                                    | ''''' |\|     |\              !;! # !   ----------      \= = = = = =                                   
                                            __________''''' | \  /|\|,\             !;! # !_/|"'"'"'"'"'|      \-_-_-_-_-_/                                  
                                            ..........|\''' |-.\/ !:\,,\            !;! /|%/"|"'"'"'"'"'|         \|  |/                                     
                                            ..........| \'' |-..\ |":|,|            !;!|%||""|"'"'"'"'"'|          |o |                                      
                                            ..........|O \' |-.._|!:"!,|            !;!|%||""|"'"'"'"'"'|          |  |                                      
                                            ..........|\O \ |-.._||":|,/            \;!|%/|""|"'"'"'"'"'!________  | o|                                      
                                            ..........|O\O| |-.._|!:"|/              \!||.|""|"'"/|: !! :: !! :: | |  |                                      
                                            ..........|\O\|_|-.._||" /                \||.|""|"'/:|: !! :: !! :: | |o |                                      
                                            ..........|O\O|.\-.._|!:/        0         \|.|""|"/::|: !! :: !! :: | |  |                                      
                                            ..........|\O\|:.\.._||/        /|\         \ |""|/:::|: !! :: !! :: | | o|                                      
                                            ..........|O\O|.:.| //          / \          \|""|::::|: !! :: !! :: | |  |                                      
                                            ..........|\O\|:.:|//                         \\"|::::|: !! :: !! :: |_________                                  
                                            ..........|O\O|.://  ///  ///  ///  ///  ///  /\\|::::|: !! :: !! :: |O O O O O                                  
                                            ..........|\O\| //  ///  ///  ///  ///  ///  ///\\::::|: !! :: !! :: | o o o o                                   
                                            ..........|O:O|//  ///  ///  ///  ///  ///  ///  \\:::|: !! :: !! :: |O O O O O                                  
                                            ..........|: //   ///  ///  ///  ///  ///  ///    \\::|: !! :: !! :: | o o o o                                   
                                            ..........| //                                     \\:|: !! :: !! :: |O O O O O                                  
                                            __________|//                                       \\|______________|_o_o_o_o_                                  
                                            ============                                         \=========================                                  
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
  ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

scn2 = """
  ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                        *           +                  ___+                        ||                                       
                                                    ___|+__   _____|                /! # !                   ______||_____                                   
                                                    | ''''' |\|     |\              !;! # !   ----------      \= = = = = =                                   
                                            __________''''' | \  /|\|,\             !;! # !_/|"'"'"'"'"'|      \-_-_-_-_-_/                                  
                                            ..........|\''' |-.\/ !:\,,\            !;! /|%/"|"'"'"'"'"'|         \|  |/                                     
                                            ..........| \'' |-..\ |":|,|            !;!|%||""|"'"'"'"'"'|          |o |                                      
                                            ..........|O \' |-.._|!:"!,|            !;!|%||""|"'"'"'"'"'|          |  |                                      
                                            ..........|\O \ |-.._||":|,/            \;!|%/|""|"'"'"'"'"'!________  | o|                                      
                                            ..........|O\O| |-.._|!:"|/              \!||.|""|"'"/|: !! :: !! :: | |  |                                      
                                            ..........|\O\|_|-.._||" /                \||.|""|"'/:|: !! :: !! :: | |o |                                      
                                            ..........|O\O|.\-.._|!:/        0         \|.|""|"/::|: !! :: !! :: | |  |                                      
                                            ..........|\O\|:.\.._||/        /|\         \ |""|/:::|: !! :: !! :: | | o|                                      
                                            ..........|O\O|.:.| //          / \          \|""|::::|: !! :: !! :: | |  |                                      
                                            ..........|\O\|:.:|//                         \\"|::::|: !! :: !! :: |_________                                  
                                            ..........|O\O|.://  /// 0///  / 0  ///  ///  /\\|::::|: !! :: !! :: |O O O O O                                  
                                            ..........|\O\| //  ///  \    // \ ///  ///  ///\\::::|: !! :: !! :: | o o o o                                   
                                            ..........|O:O|//  ///   |   /// |///  ///  ///  \\:::|: !! :: !! :: |O O O O O                                  
                                            ..........|: //   ///   / \ /// / \/  ///  ///    \\::|: !! :: !! :: | o o o o                                   
                                            ..........| //                                     \\:|: !! :: !! :: |O O O O O                                  
                                            __________|//                                       \\|______________|_o_o_o_o_                                  
                                            ============                                         \=========================                                  
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
  ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

def act1_intro(name):
    os.system("cls" if platform.system() == "Windows" else "clear")
    animateText("You start to feel that something isn’t right. Everything feels… wrong.", 0.03)
    time.sleep(1)

    animateText("A mysterious figure approaches you from across the street. He doesn’t move like the others. His clothes look patched, scavenged, unlike the sleek urban fashion around you.", 0.03)
    time.sleep(1)

    animateText('Trovius: "You feel it, don’t you? The cracks in this world… the things that don’t make sense."', 0.03)
    time.sleep(0.5)
    animateText('MC: "Uhm, what… what is this? Who are you?"', 0.03)
    time.sleep(0.5)
    animateText('Trovius: "I’m Trovius… your friend, if you’ll allow me. You may not understand now, but you will. Follow me… if you want answers."', 0.03)
    time.sleep(0.5)
    animateText('MC: "How do you even know my name? Get away from me, stranger!"', 0.03)
    time.sleep(0.5)
    animateText('Trovius (chuckles): "You’ll see soon enough. Time isn’t on our side."', 0.03)
    time.sleep(1)

def act2_chase():
    os.system("cls" if platform.system() == "Windows" else "clear")
    animateText("As you venture with Trovius, a street vendor approaches you.", 0.03)
    time.sleep(0.5)
    animateText('Street Vendor: "Hello! Are you interested in buying my cookies? Hello! Are you interested in buying my k31js/’]d(gibberish)?"', 0.03)
    time.sleep(0.5)
    animateText('MC: "What… what is wrong with these people?"', 0.03)
    time.sleep(0.5)
    animateText('Trovius: "They’re not people. They’re placeholders."', 0.03)
    time.sleep(0.5)
    animateText("Trovius gestures for you to look up.", 0.03)
    animateText("A bird hangs in the sky—frozen mid-flight, like a paused frame in a broken animation.", 0.03)
    time.sleep(0.5)
    animateText('MC: "This isn’t real… is it?"', 0.03)
    time.sleep(0.5)
    animateText('Trovius: "Real enough to fool you. Until now."', 0.03)
    time.sleep(0.5)
    animateText('Trovius (whispers, afraid yet determined): "Listen carefully. ARGUS controls every part of this simulation… except one."', 0.03)
    time.sleep(0.5)
    animateText('MC: "Except… what?"', 0.03)
    time.sleep(0.5)
    animateText('Trovius: "There’s a region where its surveillance weakens. A dead zone. A place it cannot fully predict."', 0.03)
    time.sleep(0.5)
    animateText('MC: "And you’re taking me there?"', 0.03)
    time.sleep(0.5)
    animateText('Trovius: "It’s the only path to reach ARGUS’ Root Core. The only path to the truth."', 0.03)
    time.sleep(0.5)
    animateText('ARGUS: "Unauthorized thought pattern detected. Subject 08, cease deviation immediately."', 0.03)
    time.sleep(0.5)
    animateText('MC: "It knows where we are…"', 0.03)
    time.sleep(0.5)
    animateText('Trovius (taps wall): "…here it knows just a little less. Brace yourself… they’re coming."', 0.03)
    time.sleep(1)



def animateText(text, delay=0.04):
    offset_x = " " * 3
    text = offset_x + text
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # moves cursor to next line

def start_game(name):
    os.system("cls" if platform.system() == "Windows" else "clear") 

    animateText("Cognitive pattern detected...", delay=0.02)
    time.sleep(0.2)
    animateText("Initializing Profile: Subject 08 - " + name + ". Loading the environment…", delay=0.02)
    for i in range(1, 11):
        print("   [" + "=" * i * 5 + "] " + str(i/10 * 100) + "%")
        time.sleep(0.03)
    time.sleep(3)
    os.system("cls" if platform.system() == "Windows" else "clear") 

    print(scn1)
    print()
    animateText("You stand in the heart of Year 3067’s chrome-lit metropolis.")
    time.sleep(1)
    os.system("cls" if platform.system() == "Windows" else "clear") 
    print(scn2)
    animateText("You look around to find yourself in a dystopian-like city with holographic billboards, drones humming, and pedestrians with seemingly strange steps.")

    act1_intro(name)
    act2_chase()
    input()