# Cave Monster

This project is a simple Text-Based Adventure Game where the player navigates through different locations, encounters challenges, and makes choices that affect the game's outcome. The player will move through 3 areas: start, forest and cave. at the start nothing happens, in the forest you can either go further or eat an apple, and in the cave you will fight a monster.

![Responsice Mockup]()

## Features 

### Existing Features

- __Player Creation__

  - The user can enter a unique name for their adventurer.

![Player]()

- __Start__

  - Here you can check you status or move into the forest.

![Start]()

- __Forest__

  - Here the user has 3 options:
    - Check status
    - Eat apple
    - Go further

![Forest]()

- __Cave__

  - Here the user has 2 options:
    - Fight Monster
    - Run
  - If fight is chosen, the user has the option to attack or run
  - If run is chosen the user goes back to the forest

![Cave]()

- __Monster Fight__

  - In the final cave, players can choose to attack the monster or run back to the forest. Damage is randomized, and both the player and the monster take turns attacking.

![Fight]()

### Features Left to Implement

- More levels / areas
- Find weapons
- Find more powerful healing as you go on
- Find armor
- Fight more monsters
- More colour added as the player levels up and encounters more loot
- inventory you can interact with

## Testing 

- All testing was completed using the terminal input "python3 run.py". This runs the program in the terminal showing all errors and good code. 

- *Name input*
  - I tested this in the terminal by adding a print statement after the input.

- *Show players status* 
  - For this function I tested it in the terminal after the name input and players initial conditions were created. This was in the *main* function as that is the function to run the game.

- *Locations*
  - I tested the function for location descriptions (start to begin with, the others were tested later on as more functionality was added.) in the *main* function as before with a print statement. 

- *Available actions*
  - this was added to the function *describe_location* for testing. When I ran the program it showed my actions so it was working. The actions for further locations were tested when the functionality was added later. 

- *Handling actions*
  - function for handling actions was tested again by running the program and selecting each of the options. At first the actions for start were tested, and further actions were tested as functionality was added.

- *Monster fight*
  - This was a tricky one to get right as it needed other functions, but I had made a good flow chart before coding anything so I made the extra fucntions prior to the fight function. This made it easier to sus out what to do. 
  - The attack option was built first, and I tested it in the terminal thoroughly before moving on to the run option.
  - The run option was a lot easier, though I had a problem with the location not updating, until an extensive google showed me I needed a return statement there. Once that was in it ran perfectly

- *Healing from apples*
  - I needed to make sure this had a cap so the player can't go over 100hp. This was easily done. Tested with print statements and run in the terminal. Also tested by actioning this many times when testing the program to ensure it never went over 100. 

- *Looks*
  - The program had random spacing all over and it took quite a few run throughs of the game going over every option to make it more readable and consistant. With f strings, \n does not work so a work-around I found was to add a seperate print statement with only a new line ("\n") inside.

- *Game difficulty*
  - The game was so easy I was finding it hard to test the monster winning sceanario, so to test this I made the monsters attack a lot higher. Once I was satisfied it was running fine, I changed the monsters attack back, and changed the players attack to be lower so that the game wasn't so easy.

### Validator Testing 

################# NEEDS LOOKING AT ##################

### Unfixed Bugs

None that I know of.

## Deployment


################# NEEDS LOOKING AT ##################

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 


## Credits 

- Code Institute
  - For providing the learning resources and guidance that helped in building this project, particularly the Python Essentials module.

- Python Documentation
  - For the official documentation that supported understanding of Python’s standard libraries and constructs. [Python Official Documentation - random](https://docs.python.org/3/library/random.html)