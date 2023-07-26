### Global varibales defined
name = ""

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
    name == 'Flynn'
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
    print("Choose your path wisely hero")