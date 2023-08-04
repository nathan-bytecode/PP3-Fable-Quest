# Fable Quest

## A Python text based command line game.
This application is a Python adventure text game. The game asks the users input if they would like to play and then the story of the game starts. This game is won by the user's input of selecting the right answers ie weapons.

### - By Nathan Nicholson

[Live site](https://fable-quest-bab5245d5c1f.herokuapp.com/)

[Repository](https://github.com/nathan-bytecode/fable-quest)

## Flow
### Pre-project Planning
For project 3 I decided to make an adventure text based game in Python using the command line. 

Once I decided this I typed the story out on windows notepad and within the layout of the story the process of if else statements nested within eachother began to become clear to follow. The game flow is controlled by processing through a total of fourteen functions.

(This is only one notepad print screen, I did not include them all here as I found it would seem like similiar repeated information which would give a bad readme experience.)
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

Due to the difficulty increasing, the player is brought back to the Inn if they get defeated by selecting the wrong answers. So the Inn is kind of like a mid-game checkpoint. If the player is smart, they should now revise the trianing manual.
![Stage Four defeat](/assets/images/stagefour-defeat-inn-look.png)

### Stage Four function
As mentioned above the stages have becoming more difficult. If defeated the player returns to the Inn. If successful, the player moves on to stage five. Here's an example of a typo which is implemented for all stages.
![Stage Four invalid answer](/assets/images/stagefour-invalid-answer.png)

### Stages Five and Six functions
Here's a print screen of stage five and six as the user progresses successfully.
![Stage Five and Six](/assets/images/stagefive-stagesix.png)

### Mid-story function
As the player succeeds through all three stages of stage four to six, they are met with a mid-story scene. A dialogue from the game's villian Arbitar is disclosed along with the character's ASCII Art.
![Arbitar](/assets/images/midstory.png)

### Stages Seven, Eight and Nine functions
The game's strategy takes a slight shift. As the final boss Arbitar attacks with weapons which were previously used by different enemy encounters. This will challenge the player to recall what each previous opposition used as a weapon rather than the player focusing on weather the enemy was a orc, troll, or bandit. If the player is consistenly correct in all three moves, Arbitar is defeated.
![Boss fight](/assets/images/stageseven-stageeight-stagenine.png)

### Champion ASCII Art
As Arbitar the villian is defeated, an ASCII Art of the player as a champion is displayed to celebrate their victory.
![Champion](/assets/images/champion.png)

### Final Story function
If the player is victorious against Arbitar a final story concludes and the player is met with a final moral decision to make. The "have mercy" input leads to the game being won.
![Have Mercy decision](/assets/images/finalstory-victory.png)

If the player decides to input "final blow", it's actually the wrong move and therefore they lose the game.
![Final blow decision](/assets/images/finalstory-defeat.png)

## Features left to implement
- I wanted to do some sort of hit points for the player. Example, "Wrong move hero, you just lost one hitpoint. You have four remaning"
- I would have like to include at the Inn scene, if the user selects 'rest' that they get restored all of their hitpoints health.
- I wanted to include after reaching the villian's camp at the top of Forbidden Mountain, they find a sheild which provides an extra bonus hitpoint.
- I would have liked to include a timer and a how many attempts of correct and incorrect decisions were made by the player.
- I would have like to include an option to save the player's record for furture game tries.

## Technologies Used
### Python
Used to create the application.

### Heroku
Used to deploy and host the app.

### Github
Used to display ReadMe file and store code.

### Gitpod
Used as platform for IDE.

### Git
Used to record version control.

## Testing
### Google Sheets
For testing I did a manual checklist through Google Sheets.
![Testing one](/assets/images/testing-one.png)
![Testing two](/assets/images/testing-two.png)
![Testing three](/assets/images/testing-three.png)

### Python Linter Code
To check if my formatting was approved.
![Linter](/assets/images/Python%20Linter%20Code%20Formatting%20test.png)

## Bugs
- I identified a bug with the ASCII Art image display of the staff. No matter what I could not seem to adjust it correctly.

- I identified a bug with a never ending "Invalid answer. Try again" message in one of the functions. Thanks to Stackflow and YouTube, I resolved this.

- I identified a bug at the end when the game is lost,  the user is returned to the Inn. I fixed this.

- Not really a bug as much as it is a user expeirence, but I would have liked to find out how to clear the terminal after each action to keep things clear and clean.


## Deployment
Navigate to heroku.com & log in.

Click "new" and create a new App.

Give the application a name and then choose your region and Click "Create app".

On the next page click on the Settings tab to adjust the settings.

Click on the 'config vars' button.

Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.

Buildpacks now need to be added.

These install future dependancies that we need outside of the requirements file.

Select Python first and then node.js and click save.

Make sure they are in this order.

Then go to the deploy section and choose your deployment method.

To connect with github select github and confirm.

Search for your repository select it and click connect.

You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes.

For this option choose the branch to deploy and click enable automatic deploys.

This can be changed at a later date to manual.

Manual deployment deploys the current state of a branch.

Click deploy branch.

We can now click on the open App button above to view our application.

