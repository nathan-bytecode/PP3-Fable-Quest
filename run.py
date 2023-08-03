# Importing the libary
import sys
import pyfiglet

# Global varibales defined
name = ""
weapon = ""
# ASCII Art
sword_art = """     
        (Sword: effective aganist orcs who wield hammers.)
         />_________________________________
[########[]_________________________________>
         \>

"""
bow_art = """        
        (Bow: effective agansit bandits who wield daggers.)                           
           4   ".                                        
           4    ^.                                       
           4     $                                       
           4     'b                                      
           4      "b.                                    
           4        $                                    
           4        $r                                   
           4        $F                                   
-$b========4========$b====*P=-                           
           4       *$$F                                  
           4        $$"                                  
           4       .$F                                   
           4       dP                                    
           4      F                                      
           4     @                                       
           4    .                                        
           J.                                            
          '$$    
"""
staff_art = """   
        (Staff: effective agansit trolls who wield spears.)
           /\
          //\\
         //  \\
     ^   \\  //   ^
    / \   )  (   / \
    ) (   )  (   ) (
    \  \_/ /\ \_/  /
     \__  _)(_  __/
        \ \  / /
         ) \/ (
         | /\ |
         | )( |
         | )( |
         | \/ |
         )____(
        /      \
        \______/
"""
troll_art = """   
        (Bandit)
           \\\|||///
         .  ======= 
        / \| O   O |
        \ / \`___'/ 
         #   _| |_
        (#) (     )  
         #\//|* *|\\ 
         #\/(  *  )/   
         #   =====  
         #   (   ) 
         #   || ||
        .#---'| |`----.
        `#----' `-----'
"""
bandit_art = """    
        (Orc)
        _____
    .-,;='';_),-.
     \_\(),()/_/
       (,___,)
      ,-/`~`\-,___
     / /).:.('--._)
    {_[ (_,_)
        | Y |
       /  |  \
       """ """ 
"""
orc_art = """    
       (Troll)

           ."`".
       .-./ _=_ \.-.
      {  (,(oYo),) }}
      {{ |   "   |} }
      { { \(---)/  }}
      {{  }'-=-'{ } }
      { { }._:_.{  }}
      {{  } -:- { } }
jgs   {_{ }`===`{  _}
     ((((\)     (/))))

"""

sword_of_ancients = """
/     __|(Sword of the Ancients)|__)
|     |
|     |                               /\ 
|     |                              / |\
|     |                             / /\ \
|     |                            / /  \ \
|     |                           / /    \ \
|     |                          /_/      \_\
|     |                          \    '`    /
|     |                           )   ||   ( 
|_____|___________________________|_  ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |                           |   ||   | 
|     |               /           |   ||   |           \
|     |              /(           |   ||   |           )\
|     |              |`\_         |   ||   |         _/'|
|     |              |`. `-._     |   ||   |     _,-' ,'|
|     |              (   ` . `-._ |  _--_  | _,-' , '   )
|     |               `|._   ` . `-./.__.\.-' , '   _,-'
|_____|________________|  `-._   ` | /  \ | '   _,-'
|     |                       `-._/ |_()_| \_,-'   
|     |                    ___.-'   ______   `-,
|     |                   '-----.  |______|   /
|     |                          \  ______   /
|_____|__________________________|__\>__  |>     
|     |                         <|   <   >|      
|     |                            `.____.'       
|     |                              V   V        
|     |                                           
|     |_____________________________________________________   ________
 \__________________________________________________________| |________) 
"""

inn_art = """                 
         (Inn)
                                       /\
                                  /\  //\\
                           /\    //\\///\\\        /\
                          //\\  ///\////\\\\  /\  //\\
             /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
            / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
           /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
          /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
         / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
        / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
       /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
      /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\
     / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
    / ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
"""

arbitar_art = """  
         (Arbitar)
                          .
                      _._ |`,
                    .'\  `"*-.
                   /\/L__.-*' \
                  :.'L:  ._  `.y.
                  /\//.\'  `*-'*+.
                  `:.-.`.  -' ,-. \
                    |`,\;    :`*-._;
                    `._      |   (.L
                      |':    , .*'  ;
                      |  `.        /
                    __:  / `-.;  .'
                  .'//  '  (  :`'.-*.-.
                .' ,/ __..--**"`: .' .'`+.
              .'   :'" ._.+.+*+".'  /  /|/`.
            .'     `*"'    _   /   /  / ; / \
           /\     (,     .' \.' ' ,  : / .   .
          /\ `.    ;    /  .'  /     ',      |
          * `-.`-._|_.+:   | .'  ,  /   .    |
         / `-. `-.L:.`-._ '|/     .'   /     |
       .' /   `+.__| `-.   '  _.-'    '      |
      /  :    /    :"..-' /    _.-*'         |
     /    . .'    / \ \.+'"--*'              |
    :      `.  :"*-*' /: `._.     .'         |
     `.      \ `;`   :  `-.___.-*'           ;
       `.   ."`.|`   |                      /
         `-:   /`.__.:                    .'
            `.: / .'/|\                  /|
             /". / . |`\               .' |
        .+*-:  |:  : :| \            .'   |
       +--:'   ||  | .:  `.        .'     |
       `*-._.-*|   |   \  \`+.__.-'       '
               :   :  . \  `. `.         /
               .    \    \   `. `*-._   /
                 `  /\ .  `.   `.   .-*:
                .  :  \     :.   `*-.  :
                 \ |   . `   \`-._      \
                  ;,          \   *-._.',
                )     .   `  `.      /
                 \          `   `-.  .
                   `.     \   \       |
"""

hero_art = """
 
        (Champion)
            
                   _______
             ..-'`       ````---.
           .'          ___ .'````.'SS'.
          /        ..-SS####'.  /SSHH##'.
         |       .'SSSHHHH##|/#/#HH#H####'.
        /      .'SSHHHHH####/||#/: \SHH#####\
       /      /SSHHHHH#####/!||;`___|SSHH###\
    -..__    /SSSHHH######.         \SSSHH###\
    `.'-.''--._SHHH#####.'           '.SH####/
      '. ``'-  '/SH####`/_             `|H##/
      | '.     /SSHH###|`'==.       .=='/\H|
      |   `'-.|SHHHH##/\__\/        /\//|~|/
      |    |S#|/HHH##/             |``  |
      |    \H' |H#.'`              \    |
      |        ''`|               -     /
      |          /H\          .----    /
      |         |H#/'.           `    /
      |          \| | '..            /
      |    ^~DLF   /|    ''..______.'
       \          //\__    _..-. | 
        \         ||   ````     \ |_
         \    _.-|               \| |_
         _\_.-'   `'''''-.        |   `--.
     ''``    \            `''-;    \ /
              \      .-'|     ````.' -
              |    .'  `--'''''-.. |/
              |  .'               \|
              |.'    
"""

# Functions go on outer level to later be called upon
def training():
    if choice == "yes":
        weapon = ""
        while weapon != "no":
            try:
                weapon = input("Choose weapon: [sword/bow/staff]\n")
                weapon = weapon.lower().strip()
                if weapon == "sword":
                    print(sword_art)
                    print("Do you want to learn about another weapon?")
                    weapon = input("[yes/no]\n")
                elif weapon == "bow":
                    print(bow_art)
                    print("Do you want to learn about another weapon?")
                    weapon = input("[yes/no]\n")
                elif weapon == "staff":
                    print(staff_art)
                    print("Do you want to learn about another weapon?")
                    weapon = input("[yes/no]\n")
                elif weapon == "no":
                    print("I hope you've trained with each weapon!")
                    print("Get ready for battle!")
                    return
                else:
                    raise ValueError

            except ValueError:
                print("Invalid answer. Try again!")
    else:
        print("Get ready for battle!")
        return


def stage_one():
    try:
        print("You encounter a group of orcs.")
        print(orc_art)
        print("What weapon do you use?")
        weapon = input("[sword/bow/staff]\n")

        if weapon == "sword":
            print("Victory! A sword is effective agansit orcs!")
            print("Move forward hero!")
        elif weapon == "bow":
            print("Game over. Orcs weild hammers. You get smashed.")
        elif weapon == "staff":
            print("Game over. Orcs weild hammers. You get smashed.")
            return
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_one()


def stage_two():
    try:
        print("You encounter a group of trolls.")
        print(troll_art)
        print("What weapon do you use?")
        weapon = input("[sword/bow/staff]\n")

        if weapon == "sword":
            print("Game over. Trolls weild spears. You get pierced.")
        elif weapon == "bow":
            print("Game over. Trolls weild spears. You get pierced.")
        elif weapon == "staff":
            print("Victory! A staff is effective agansit trolls!")
            print("Move forward hero!")
            return
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_two()


def stage_three():
    try:
        print("You encounter a group of bandits.")
        print(bandit_art)
        print("What weapon do you use?")
        weapon = input("[sword/bow/staff]\n")

        if weapon == "sword":
            print("Game over. Bandits weild daggers. You get sliced.")
        elif weapon == "bow":
            print("Victory! A bow with arrows are effective agansit bandits!")
            print("Move forward hero!")
        elif weapon == "staff":
            print("Game over. Bandits weild daggers. You get sliced.")
            return
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_three()


def crossroads():
    print("You come to a cross roads mid way up Forbidden Mountain.")
    print("Do you go back for more glory?")
    print("Go right to rest at the Inn?")
    print("Or go forward to more difficult battles?")
    go = input("[back/right/forward]\n")
    if go == "back":
        print("You go back.")
        stage_three()

    elif go == "rest":
        print("You decided to rest at an Inn.")
        print(inn_art)
        Inn()

    elif go == "forward":
        print("The difficulty has just gotten harder hero.")
        print("Multiple groups of enemies joined together are ahead.")
        print("Choose the effective weapons for each attack wisely.")
        stage_four()


def inn():
    try:
        print("You arrive at an Inn after a hard days battle.")
        print(inn_art)
        print("Will you rest?")
        print("Will you look at the training manual?")
        print("Or will you leave?")
        decide = input("[rest/look/leave]\n")
        if decide == "rest":
            print("You sleep through the night and wake up well replenished.")
        elif decide == "look":
            print("You open up the training manual to refresh battle plans.")
            print("Sword: effective aganist orcs who weild hammers.")
            print("Bow: effective agansit bandits who weild daggers.")
            print("Staff: effective agansit trolls who weild spears./n")
        elif decide == "leave":
            print("The difficulty has just gotten harder hero.")
            print("Multiple groups of enemies joined together are ahead.")
            print("Choose the effective weapons for each attack wisely.")
            stage_four()

        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        inn()


def stage_four():
    print("You encounter a group of bandits and trolls.")
    print("They trolls first attack, then the bandits.")
    print("What order of weapons do you use?")
    print("[sword then staff/ staff then sword]")
    print("[sword then bow/bow then sword]")
    print("[staff then bow/bow then staff]")
    try:
        weapon = input("\n")

        if weapon == "sword then staff":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "staff then sword":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "sword then bow":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "bow then sword":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "staff then bow":
            print("Victory! Move forward hero!\n")
            stage_five()
        elif weapon == "bow then staff":
            print("Defeat. Return to the Inn.")
            inn()
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_four()


def stage_five():
    print("You encounter a group of orcs and trolls.")
    print("They orcs first attack, then the trolls.")
    print("What order of weapons do you use? \n")
    print("[sword then staff/staff then sword]")
    print("[sword then bow/bow then sword]")
    print("[staff then bow/bow then staff]")
    try:
        weapon = input("\n")

        if weapon == "sword then staff":
            print("Victory! Move forward hero!")
            stage_six()
        elif weapon == "staff then sword":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "sword then bow":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "bow then sword":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "staff then bow":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "bow then staff":
            print("Defeat. Return to the Inn.")
            inn()
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_five()


def stage_six():
    print("You encounter a group of bandits and orcs.")
    print("They bandits first attack, then the orcs.")
    print("What order of weapons do you use? \n")
    print("[sword then staff/staff then sword]")
    print("[sword then bow/bow then sword]")
    print("[staff then bow/bow then staff]")
    try:
        weapon = input("\n")

        if weapon == "sword then staff":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "staff then sword":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "sword then bow":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "bow then sword":
            print("Victory! Move forward hero!\n")
            mid_story()
        elif weapon == "staff then bow":
            print("Defeat. Return to the Inn.")
            inn()
        elif weapon == "bow then staff":
            print("Defeat. Return to the Inn.")
            inn()
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_six()


def mid_story():
    print(f"Well done hero {answer}!")
    print("You have defeated Arbitar's army on the way!")
    print("You successfully made it to the top of Forbidden Mountain")
    print("Now you must defeat Arbitar!")
    print(arbitar_art)
    print(f"Arbitar: A hero named {answer} has come to challenge me?!")
    print("Hahaha do not make me laugh!")
    print("With the Sword of the Ancients I can easily shapeshift my weapon!")
    print("Prepare to taste my blade!")
    stage_seven()


def stage_seven():
    print("Arbitar releases a relentless flurry of attacks!")
    print("All your experience has amounted to this battle!")
    try:
        print("Arbitar attacks in the form of a dagger!")
        print("What weapon do you use?")
        weapon = input("[sword/bow/staff]\n")

        if weapon == "sword":
            print("Wrong move! You are defeated! Return to the Inn.")
            inn()
        elif weapon == "bow":
            print("Correct move! Incoming next attack!")
            stage_eight()
        elif weapon == "staff":
            print("Wrong move! You are defeated! Return to the Inn.")
            inn()
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_seven()


def stage_eight():
    try:
        print("Arbitar attacks in the form of a spear!")
        print("What weapon do you use?")
        weapon = input("[sword/bow/staff]\n")

        if weapon == "sword":
            print("Wrong move! You are defeated! Return to the Inn.")
            inn()
        elif weapon == "bow":
            print("Wrong move! You are defeated! Return to the Inn.")
            inn()
        elif weapon == "staff":
            print("Correct move! Incoming next attack!")
            stage_nine()
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_eight()


def stage_nine():
    try:
        print("Arbitar attacks in the form of a hammer!")
        print("What weapon do you use?")
        weapon = input("[sword/bow/staff]\n")
        if weapon == "sword":
            print("Correct move! Arbitar is defeated!")
            final_story()
        elif weapon == "bow":
            print("Wrong move! You are defeated! Return to the Inn.")
            inn()
        elif weapon == "staff":
            print("Wrong move! You are defeated! Return to the Inn.")
            inn()
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_nine()


def final_story():
    print("Arbitar: How can this be? A new champion has emerged!")
    print("Have mercy on me O' Champion of Albion!")
    print(hero_art)
    print("You have a moral decision now to make hero.")
    print("Do you swing the final blow and rid Albion of Arbitar?")
    print("Or do you have mercy and let him live?")

    try:
        action = input("[final blow/have mercy]\n")

        if action == "final blow":
            print("You have taken the more sinister way by executing Arbitar.")
            print("Darkness has entered your heart.")
            print("You steal the Sword of the Ancients for yourself.")
            print("Its power is too much for you to control.")
            print("You lose the right to be known as a champion of Albian.")
            print("You take your final breath.")
            print("You lose. Game over.")
        elif action == "have mercy":
            print("You have banished Arbitar and showed kindness!")
            print("Now because you are not corrupted by vengence")
            print("You can rightfully restore the Sword of the Ancients!")
            print("Congratulations Champion of Albian!")
            print("The land is a safe place to dwell again!")
            print("The reputation of The Hero's Guild has been restored!")
            print("Game won!")
            sys.exit()
        else:
            raise ValueError
    except ValueError:
        print("Invalid answer. Try again!")
        final_story()


# Welcome message
print("Welcome to Fable Quest, an adventure text based game.")
print("To win, you must select the correct weapons to use.")
print("Would you like to play? [yes/no]")

# Prompt user input
answer = input("> ")

if (answer.lower().strip() == "yes"):
    # If "yes", prompt user for name
    answer = input('Noble choice! What is your name hero?\n')
elif (answer == "no"):
    # If "no", print goodbye message and quit program
    print("Not all have what it takes to be a hero. Goodbye")
    sys.exit()
else:
    # If neither "yes" or "no", print invalid answer message
    print("Invalid answer. Try again running the program again.")
    quit()
    # All answer input outcomes have been tested to ensure user experience

try:
    if answer == "":
        # If user gives an empty string, I have assigned a default name
        raise ValueError
    else:
        name == answer
except ValueError:
    print("The mysterious type, ey? OK, I'll call you Cloud!")
    answer == 'Cloud'
finally:
    # finally keyword runs the program regardless if there's an error or not

    # Background story with the usage of an f-string for the user's name
    print("Long ago in the land of Albion a hero once held in high honor")
    print("who desired more power and was drawn to the dark side.")
    print("This fallen hero known as Arbitar went to Forbidden Mountain.")
    print("Arbitar defeated the order known as The Hero's Guild")
    print("and removed the Sword of the Ancients.")
    print("Through Arbitar's actions he released")
    print("The creatures of havoc in the forms of orcs and trolls.")
    print("Arbitar has set up camp at the top of Forbidden Mountain.")
    print(f"Now you hero {answer}, must defeat Arbitar's army")
    print("Of bandits, orcs and trolls")
    print("To restore the Sword of the Ancients back to its rightful place.")
    print("Choose your path wisely hero.")

print("Would you like to train at The Hero's Guild")
print("Before leaving for your conquest? [yes/no]")
choice = input("> ")
training()
stage_one()
stage_two()
stage_three()
crossroads()
inn()
stage_four()
stage_five()
stage_six()
mid_story()
stage_seven()
stage_eight()
stage_nine()
final_story()
sys.exit()