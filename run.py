import random
import time
import os
from colorama import init, Fore, Style

init()  # Initialize colorama


class Player:
    """
    Player class to handle player attributes and actions
    """
    def __init__(self, name):
        """
        Defines the initial player conditions
        """
        self.name = name
        self.hp = 100
        self.inventory = []
        self.location = "start"

    def heal_player(self, heal):
        """
        Function for increasing players hp after apple eaten
        """
        self.hp += heal
        if self.hp >= 100:
            self.hp = 100

    def take_damage(self, amount):
        """
        Function for reducing players hp after damage is taken
        """
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def add_item(self, item):
        """
        Function for adding loot if monster is defeated
        """
        self.inventory.append(item)

    def still_alive(self):
        """
        Function to determine if the player is still alive
        """
        return self.hp > 0

    def show_status(self):
        """
        Displays player conditions to user
        """
        print(f"\n{self.name} - HP: {Fore.GREEN}{self.hp}{Style.RESET_ALL}")
        print("Inventory:", ", \n".join(self.inventory)
              if self.inventory else "Empty\n")


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def play_again():
    """
    Function to ask the player if they want to play again or exit.
    """
    while True:
        choice = input("\nWould you like to play " +
                       "again? (yes/no):\n").lower().strip()
        if choice == "yes":
            clear()
            main()  # Restart the game by calling main()
            break
        elif choice == "no":
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


def describe_location(player):
    """
    Function to display the current location and available actions
    """
    locations = {
        "start": ("You are at the entrance of a dark forest. There is a path "
                  + "you can see ahead.\nIt leads into the forest."),
        "forest": ("It's almost too dark to see.\nYou can barely make out an "
                   + "apple tree with shiny red apples on it." +
                   "\nIt's quiet... too quiet."),
        "cave": ("It's even darker than the forest (somehow).. " +
                 "You hear growling inside..\nIt's getting louder.")
    }
    print(locations[player.location])
    # Tells the user where they are in the game
    time.sleep(1.5)
    # Adds a time delay
    available_actions(player)
    # Tells the player what they can do


def available_actions(player):
    """
    Function to set which actions are available to users in given locations
    """
    if player.location == "start":
        print("\n1. Enter the dark forest...")
        print("2. Check your status")
    elif player.location == "forest":
        print("\n1. Explore deeper into the forest...")
        print("2. Eat a shiny red apple??")
        print("3. Check your status")
        print("4. Return to the start")
    elif player.location == "cave":
        print("\n1. Fight the monster!!")
        print("2. Run back to the forest...")

    print("\nPlease input the NUMBER of the action you wish to take.")
    action = input("Choose an action:\n")
    # Input for player to use for actions
    handle_action(player, action)
    # Actions the users input above


def handle_action(player, action):
    """
    Function to handle user input and game progression through 3 levels
    """
    if player.location == "start":
        if action == "1":
            clear()
            print("\nYou walk into the forest.")
            print("The light of day fades the more you walk...")
            player.location = "forest"
        elif action == "2":
            clear()
            player.show_status()
        else:
            print("\nInvalid action. Please ensure you input a number" +
                  " for an action that is avalable.")
            print("Only a number will be accepted.\n")
    elif player.location == "forest":
        if action == "1":
            clear()
            print("\nYou venture deeper and discover a mysterious cave...")
            print("Of course you go in!!")
            player.location = "cave"
        elif action == "2":
            clear()
            apple_heal = random.randint(1, 5)
            # Amount apple will heal player by
            player.heal_player(apple_heal)
            if player.hp >= 100:
                # Ensures the player never goes above full health
                print("\n")
                print(f"{Fore.GREEN}You are at full health.{Style.RESET_ALL}")
                # Adds colour to the text for a better player experience
                print("\n")
            else:
                print("\n")
                print(f"The apple healed you by {Fore.GREEN}{apple_heal}"
                      + "{Style.RESET_ALL}")
                # Tells the user how much the player is healed
                print("\n")
        elif action == "3":
            clear()
            player.show_status()
        elif action == "4":
            clear()
            print("\nYou head back to where you started.. " +
                  "nothing has changed.")
            player.location = "start"
        else:
            print("\nInvalid action. Please ensure you input a number" +
                  " for an action that is avalable.")
            print("Only a number will be accepted.\n")
    elif player.location == "cave":
        if action == "1":
            clear()
            fight_monster(player)
        elif action == "2":
            clear()
            print("\nYou run back to the forest covered in sweat" +
                  " and other bodily fluids...\nHow did they get there?! "
                  + "You're not scared...")
            player.location = "forest"
        else:
            print("\nInvalid action. Please ensure you input a number" +
                  " for an action that is avalable.")
            print("Only a number will be accepted.\n")

    if player.still_alive():
        describe_location(player)
        # Describes the location only if the player is still alive
    else:
        print("\n")
        print(f"{Fore.RED}{player.name} has perished...{Style.RESET_ALL}")
        play_again()


def fight_monster(player):
    """
    Function to handle fighting the monster in the cave.
    Options for attack or run
    Handles damage from monster and to monster
    Handles damage to player
    """
    monster_hp = 50
    # Starting hp of Monster
    print("\nA feral beast emerges from the shadows." +
          "\nThere's no chance of taming this thing... KILL IT!!!\n")
    while monster_hp > 0 and player.still_alive():
        print("Please input either 'a' or 'r' only.")
        action = input("Do you want to (a)ttack or (r)un?\n").lower()
        # Ensures the input will be accepted if the user inputs uppercase
        if action == "a":
            damage = random.randint(5, 15)
            # Amount player will damage monster
            monster_hp -= damage
            print("\n")
            print(f"You dealt {Fore.RED}{damage}{Style.RESET_ALL} " +
                  "damage to the monster.. Will it be enough??")
            if monster_hp > 0:
                # If monster is alive, it will attack the player
                monster_attack = random.randint(10, 25)
                # Amount monster will damage player
                player.take_damage(monster_attack)
                print("The monster dealt" +
                      f" {Fore.RED}{monster_attack}{Style.RESET_ALL}"
                      + " damage to you.")
                print("\n")
            else:
                print("\nYou defeated the monster!! " +
                      "You loot it's bloody corpse.")
                player.add_item("Monster's treasure")
                # Adds monsters loot to players inventory
                player.show_status()
                print(f"Congratulations, {player.name}!" +
                      "\nYou have defeated the monster and won the game!" +
                      "\nYou bring the treasure back home and the town" +
                      " builds\n" +
                      f"a statue in {player.name}'s honour! Wow!")
                play_again()
        elif action == "r":
            print("\nYou escape back to the forest." +
                  "\nThose apples look extra juicy...")
            player.location = "forest"
            return
        else:
            print("Invalid action. Please input either 'a' or 'r' only.")

    if not player.still_alive():
        print("You have been slain by the monster..")
        time.sleep(1.5)
        print("You fade out to the sound of your own bones crunching...")
        time.sleep(1.5)
        print("GAME OVER")


def main():
    """
    Name input for user
    Run all program functions
    """
    print("Welcome Adventurer! What is your name?")
    name = input("Enter your character's name:\n").strip()
    while not name:
        print("Name cannot be blank.")
        name = input("Enter your character's name:\n").strip()

    player = Player(name)
    describe_location(player)


main()
