# Cave Monster

This project is a simple *Text-Based Adventure Game* where the player navigates through different locations, encounters challenges, and makes choices that affect the game's outcome. The player will move through 3 areas: start, forest and cave. at the start nothing happens, in the forest you can either go further or eat an apple, and in the cave you will fight a monster. The user will be given the option to fight or run from the monster. 

![Deployed Game](assets/images/main-program-screenshot.png)

## Features 

### Existing Features

- __Player Creation__

  - The user can enter a unique name for their adventurer.

![Player](assets/images/player-name.png)

- __Start__

  - Here you can check your status or move into the forest.

![Start](assets/images/start-area.png)

- __Forest__

  - Here the user has 4 options:
    - Check status (shows hp of player and inventory)
    - Eat apple
    - Go further
    - Go back to start

![Forest](assets/images/forest-area.png)

- __Cave__

  - Here the user has 2 options:
    - Fight Monster
    - Run
  - If fight is chosen, the user has the option to attack or run
  - If run is chosen the user goes back to the forest

![Cave](assets/images/cave-area.png)

- __Monster Fight__

  - In the final cave, players can choose to attack the monster or run back to the forest. Damage is randomized, and both the player and the monster take turns attacking.

![Fight](assets/images/fight.png)

![Attack](assets/images/attack.png)

![Run](assets/images/run.png)

- __Use of Player Class__

  - The Player class has all of the relevant attributes and actions associated with the player character, such as health (hp), inventory management, and movement between locations. By using this class, the game can track and manipulate player-specific information in an organized manner.

- __Clear function__
  - The clear function helps keep the terminal from getting too clogged up with the adventure as it unfolds. User experience is improved with clarity.

- __Play Again Option__
  - Function to ask the player if they want to play again or exit. This adds clarity for the user that the game has ended or they can start again. 

- __*if __name__ == "__main__":*__
  - This condition checks whether the script is being run directly or imported.
  - If the script is executed directly, __name__ will be equal to "__main__", and the block of code under this if statement will execute.
  - If the script is imported as a module, the block of code under this if statement will not execute.

### Features Left to Implement

- More levels / areas
- Find weapons
- Find more powerful healing as you go on
- Find armor
- Fight more monsters
- More colour added as the player levels up and encounters more loot
- inventory you can interact with

## Testing 

- All testing was completed using the terminal input "python3 run.py". This runs the program in the terminal showing all errors and good code. It was then all tested using the deployed version. 

- *Input testing general (ALL INPUTS)*
  - Things I tested:
    - the letters a, b, g, h, l, n
    - multiple letters abcde
    - the number 1, 7, 9
    - multiple numbers 12345
    - an empty ENTER with nothing entered
    - only spaces          
    - special characters ? ! @ / \ |

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

- *Deployment*
 - After deployment I realised I hadn't limited my text to 80 characters and changed the code to suit. I didn't realise at first the indentations were wrong until trying the deployed version again. I thought I had fixed the issue using the backslash method but quickly realised that wasn't the correct method to use when running the game in the terminal. When I ran the game through the validator it showed many errors, and one by one I fixed these until it showed as clean.

### Validator Testing 

- I ran the code through the [pep8 Validator](https://pep8ci.herokuapp.com/#) provided by the Code Institute.

![Validator](assets/images/validator-screenshot.png)

### Unfixed Bugs

- When inputting before the input is asked for the program still accepts the input and acts on it. 

## Deployment

- Created Heroku account
- Activated Student Account
- Ran 'Pip3 freeze > requirements.txt' to allow for Heroku deployment.
- Followed the video provided by the Code Institute detailing the steps involved [Code Institute Video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/)
- Folowed the following steps provided by the Code Institute:
  - When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:
  - 1. `heroku/python`
  - 2. `heroku/nodejs`
  - You must then create a _Config Var_ called `PORT`. Set this to `8000`
  - If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.
  - Connect your GitHub repository and deploy as normal.
- Set deployments to Automatic in Heroku

## Credits 

- Code Institute
  - The Python Essentials module was key in achieving this goal

- Python Documentation
  - For the official documentation on the random library. [Python Official Documentation - random](https://docs.python.org/3/library/random.html)

- Digital Ocean
  - For providing the documentation on time.sleep function used to add several time delays. [Digital Ocean](https://www.digitalocean.com/community/tutorials/python-time-sleep)

- PyPI
  - For providing documentation on colorama and how to use it. [PyPI](https://pypi.org/project/colorama/)

- Backslash use: '\'
  - I used this for the use of the '\' to keep my strings under 80 characters[pep8](https://stackoverflow.com/questions/2070684/how-can-i-make-my-python-code-stay-under-80-characters-a-line#:~:text=If%20the%20code%20exceeding%2080%20chars%20is%20a%20line%20of,to%20%22escape%22%20the%20newline.&text=You%20can%20also%20use%20the%20parenthesis%20to%20your%20advantage.)

- Tutor Support
  - The tutor support helped a lot in using the validator and understanding errors caused by the use of the backslash. Special thanks to Roo.

- Mentor Support
  - Rory helped me understand what parts of the project needed improving on and gave incredible pointers that helped to make the project a lot better.
  - Help with the end of program:
      - if __name__ == "__main__":
      - main()
  