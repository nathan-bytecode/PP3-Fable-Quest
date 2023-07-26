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
    print("Long ago....")