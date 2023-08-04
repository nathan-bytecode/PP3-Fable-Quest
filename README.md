# Fable Quest

## A Python text based command line game.
This application is a Python adventure text game. The game asks the users input if they would like to play and then the story of the game starts. This game is won by the user's input of selecting the right answers ie weapons.

### - By Nathan Nicholson

[Live site](https://fable-quest-bab5245d5c1f.herokuapp.com/)

[Repository](https://github.com/nathan-bytecode/fable-quest)

## Table of Contents
1.Pre-project Planning
2.Features Left to Implement
3.Technologies Used
4.Testing
5.Bugs
6.Deployment
7.Credits
8.Content
9.Acknowledgements

## Flow
### Pre-project Planning
For project 3 I decided to make an adventure text based game in Python using the command line. 

Once I decided this I typed the story out on windows notepad and within the layout of the story the process of if else statements nested within eachother began to become clear to follow.

![Notepad Screenshot](/assets/images/notepad1.png)

## Game-Flow
### Start-up
When the user loads the application they are met with the following.
![Start-up](/assets/images/start-up.png)

### Beginning story
If the user types "yes", they are asked to enter their name and so the story begins. If the user chooses not to enter any name, a default name is provided.
![Beginning story](/assets/images/beginning-story.png)

If the user types "no", a goodbye message is displayed.

### Training function
The user is asked to input if they would like to train before going forward in program.
If the user input is "yes", they are giving options to select from. The key to winning can be found in the description of each ASCII Art weapon and what they are effective towards. The game requires some memory as well as selecting the correct answers.
![Training sword](/assets/images/training-sword.png)
![Training bow](/assets/images/training-bow.png)
![Training staff](/assets/images/training-staff.png)

### Stage One function
If the user input is "no" to training or if its "no" to learn another weapon, the user moves on to stage one. The player is then challenge to select the correct weapon to move forward. For each of the three beginning stages, i've included ASCII Art images.
![Orc](/assets/images/stageone-orc.png)

If the player selects the wrong weapon, they lose the game and so the program is stopped.
![Orc defeat](/assets/images/stageone-gameover.png)

Also to note that for all functions or "stages", if the player inputs a typo, an invalid print message will display and they will be asked to try again.

### Stage Two function
If the player is successful from stage one they move forward onto stage two. Again the same syntax of if else statements are applied here, with the exception of a different enemy and therefore requires a different correct weapon answer to proceed in the game.
![Troll](/assets/images/stagetwo-troll.png)

### Stage Three function
As the player succeeds, the move onto stage three to encounter a different enemy.
![Bandit](/assets/images/stagethree-bandit.png)

### Crossroads function
The player then comes to a crossroads. A decision is to be made with three possible outcomes. 

If the player inputs "back", they go back to stage three and encounter the previous battle.
![Back](/assets/images/crossroads-back.png)
If the player selects the right answer again they move forward to the Inn scene.

If the player at the crossroads inputs "right", it takes them to the Inn scene.

If the player at the crossroads inputs "forward", it takes them to stage four. Stage four difficulty increases as two weapons have to be selected in a correct order for victory.
![Crossroads forward move](/assets/images/crossroads-forward-stagefour.png)

### Inn function
If during the crossroads decision making, the player inputs "right", they arrive at the Inn scene. The Inn gives three options. Rest and leave options are abit decieving as the player just moves forward onto stage four. Look is the best option as it gives the player the chance to recite what weapons are effective towards which is very much needed for the harder stages to follow. 
![Inn](/assets/images/crossroads-right.png)

Due to the difficulty increasing, the player is brought back to the Inn if they get defeated by selecting the wrong answers. So the Inn is kind of like a mid-game checkpoint. If the player is smart, they should now revise the triaing manual.
![Stage Four defeat](/assets/images/stagefour-defeat-inn-look.png)