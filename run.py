### Global varibales defined
name = ""
weapon = ""

### Functions go on outer level to later be called upon
def training():
    if choice == "yes":
        weapon = ""
        while weapon != "no":
            try:
                weapon = input("Choose weapon: [sword/bow/staff]\n")
                weapon = weapon.lower().strip()
        
                if weapon == "sword":
                    print("Sword: effective aganist orcs who weild hammers.")
                    weapon = input("Do you want to learn about another weapon? [yes/no]\n")
                elif weapon == "bow":
                    print ("Bow: effective agansit bandits who weild daggers.")
                    weapon = input("Do you want to learn about another weapon? [yes/no]\n")
                elif weapon == "staff":
                    print("Staff: effective agansit trolls who weild spears.")
                    weapon = input("Do you want to learn about another weapon? [yes/no]\n")
                elif weapon == "no":
                    print("I hope you've learned each weapon for what lies ahead!")
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
        weapon = input("You encounter a group of orcs, what weapon do you use? [sword, bow or staff]\n")

        if weapon == "sword":
            print("Victory! A sword is effective agansit orcs! Move forward hero!\n")
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
        weapon = input("You encounter a group of trolls, what weapon do you use? [sword, bow or staff]\n")

        if weapon == "sword":
            print("Game over. Trolls weild spears. You get peirced.")
        elif weapon == "bow":
            print("Game over. Trolls weild spears. You get peirced.")
        elif weapon == "staff":
            print("Victory! A staff is effective agansit trolls! Move forward hero!\n")
            return
        else:
            raise ValueError

    except ValueError:
        print("Invalid answer. Try again!")
        stage_two()

def stage_three():
    try:
        weapon = input("You encounter a group of bandits, what weapon do you use? [sword, bow or staff]\n")

        if weapon == "sword":
            print("Game over. Bandits weild daggers. You get sliced.")
        elif weapon == "bow":
            print("Victory! A bow with arrows are effective agansit bandits! Move forward hero!\n")
        elif weapon == "staff":
            print("Game over. Bandits weild daggers. You get sliced.")
            return
        else:
            raise ValueError

    except ValueError:
            print("Invalid answer. Try again!")
            stage_three()

def crossroads():
    go = input("You come to a cross roads mid way up Forbidden Mountain, do you go back for more glory? Go right to rest at the Inn? Or go forward to more difficult battles? [back, right, forward]\n")
    if go == "back":
        print("You go back./n")
        stage_three()

    elif go == "rest":
        print("You decided to rest at an Inn.")
        Inn()

    elif go =="forward":
        print("The difficulty has just gotten harder hero, multiple groups of enemies joined together are ahead. Choose the effective weapons for each attack wisely.\n")
        stage_four()

def inn():
    try:
        decide = input("You arrive at an Inn. After a hard days battle, will you rest? Look at the training manual? Or leave? [rest/look/leave]\n")
        if decide == "rest":
            print("You sleep through the night and wake up well replenished./n")
        elif decide == "look":
            print("You open up the training manual to refresh your battle strategy.")
            print("Sword: effective aganist orcs who weild hammers.")
            print ("Bow: effective agansit bandits who weild daggers.")
            print("Staff: effective agansit trolls who weild spears./n")
        elif decide == "leave":
            print("You leave the Inn. The difficulty has just gotten harder hero, multiple groups of enemies joined together are ahead. Choose the effective weapons for each attack wisely.\n")
            stage_four()
        else:
            raise ValueError

    except ValueError:
            print("Invalid answer. Try again!")
            inn()

def stage_four():
    print("You encounter a group of bandits and trolls.")
    print("They trolls first attack, then the bandits.")
    print("What order of weapons do you use? \n")
    try:
        weapon = input("[sword then staff/ staff then sword/ sword then bow/ bow then sword / staff then bow / bow then staff?]\n")

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
    try:
        weapon = input("[sword then staff/ staff then sword/ sword then bow/ bow then sword / staff then bow / bow then staff?]\n")

        if weapon == "sword then staff":
            print("Victory! Move forward hero!\n")
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
    try:
        weapon = input("[sword then staff/ staff then sword/ sword then bow/ bow then sword / staff then bow / bow then staff?]\n")

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
    print("You succesfully made it to the top of Forbidden Mountain by deafting Arbitar's army on the way!")
    print("Now you must defeat Arbitar!\n")
    print(f"Arbitar: A hero named {answer} has come to challenge me?!")
    print("Hahaha do not make me laugh!")
    print("With the Sword of the Ancients I can easily shapeshift my weapon to any of my choosing!")
    print("Prepare to taste my blade!")
    stage_seven()

def stage_seven():
    print("Arbitar releases a relentless flurry of attacks! All your expeience has amounted to this battle! Choose wisely hero!")
    try:
        weapon = input("Arbitar attacks in the form of a dagger, what weapon do you use? [sword, bow or staff]\n")

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
        weapon = input("Arbitar attacks in the form of a spear, what weapon do you use? [sword, bow or staff]\n")

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
        weapon = input("Arbitar attacks in the form of a hammer, what weapon do you use? [sword, bow or staff]\n")

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
    print("Arbitar: How can this be? A new champion has emerged! Have mercy on me champion of Albion!")
    print("You have a moral decision now to make hero. Do you swing the final blow and rid Albion of Arbitar?")
    print("Or do you have mercy and let him live?")

    try:
        action = input ("[final blow/ have mercy]\n")

        if action == "final blow":
            print("You have taken the more sinister way by executing Arbitar, darkness has entered your heart.")
            print("You steal the Sword of the Ancients for yourself but cannot control its power.")
            print("You take your final breath and lose the right to be known as a champion of Albian. You lose. Game over")
        elif action == "have mercy":
            print("You have banished Arbitar and showed kindness.")
            print("Now because you are not corrupted by bloodshed, you can rightfully restore the Sword of the Ancients.")
            print("Congratulations champion of Albian!")
            print("The land is a safe place to dwell again and the reputation of The Hero's Guild has been restored. Game won!")
        else:
            raise ValueError
    
    except ValueError:
        print("Invalid answer. Try again!")
        final_story()

    

### Welcome message
print("Welcome to Fable Quest, an adventure text based game.")
print("To win, you must select the correct weapons to use.")
print("Would you like to play? [yes/no]")

### Prompt user input
answer = input("> ")

if(answer.lower().strip() == "yes"):
    ### If "yes", prompt user for name
   answer = input('Noble choice! What is your name hero?\n')
elif(answer == "no"):
    ### If "no", print goodbye message and quit program
    print("Not all have what it takes to be a hero. Goodbye")
    quit()
else:
    ### If neither "yes" or "no", print invalid answer message
    print("Invalid answer. Try again running the program again.")
    quit()
    ### All answer input outcomes have been tested to ensure user experience

try:
    if answer == "":
        ### If user gives an empty string, I have assigned a default name
        raise ValueError
    else:
        name == answer
except ValueError:
    print("The mysterious type, ey? OK, I'll call you Flynn!")
    answer == 'Flynn'
finally:
    ### finally keyword exceutes the program regardless if there's an error or not

    ### Background story with the usage of an f-string for the user's name
    print("Long ago in the land of Albion a hero once held in high honor")
    print("who desired more power and was drawn to the dark side.")
    print("This fallen hero known as Arbitar went to Forbidden Mountain")
    print("and removed the Sword of the Ancients by defeating the order known as The Hero's Guild.")
    print("Through Arbitar's actions he released the creatures of havoc in the forms of orcs and trolls.")
    print("Arbitar has set up camp all the way to the top of Forbidden Mountain.")
    print(f"Now you hero {answer}, must defeat Arbitar's army")
    print("of bandits, orcs and trolls and restore the Sword of the Ancients back to its rightful place.")
    print("Choose your path wisely hero.\n")

print("Would you like to train at The Hero's Guild before leaving for your conquest? [yes/no]")
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