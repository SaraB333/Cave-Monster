import random

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
        print(f"\n{self.name} - HP: {self.hp}")
        print("Inventory:", ", \n".join(self.inventory) if self.inventory else "Empty\n")


def describe_location(player):
    """
    Function to display the current location and available actions
    """
    locations = {
        "start": "You are at the entrance of a dark forest. There is a path you can see ahead. It leads into the forest.",
        "forest": "You have entered the forest. It's almost too dark to see. You can barely make out an apple tree with shiny red apples on it. It's quiet... too quiet.",
        "cave": "It's even darker than the forest (somehow).. You hear growling inside.. It's getting louder."
    }
    print(locations[player.location]) # Tell the user where they are in the game
    available_actions(player) # Tell the player what they can do


def available_actions(player):
    """
    Function to set which actions are available to users in given locations
    """
    if player.location == "start":
        print("1. Enter the dark forest...")
        print("2. Check your status")
    elif player.location == "forest":
        print("1. Explore deeper into the forest...")
        print("2. Eat a shiny red apple??")
        print("3. Check your status")
        print("4. Return to the start")
    elif player.location == "cave":
        print("1. Fight the monster!!")
        print("2. Run back to the forest...")

    print("\nPlease input the NUMBER of the action you wish to take.")
    action = input("Choose an action:\n") # Input for player to use for actions
    handle_action(player, action) # Actions the users input above


def handle_action(player, action):
    """
    Function to handle user input and game progression through 3 levels
    """
    if player.location == "start":
        if action == "1":
            print("\nYou walk into the forest. The light of day fades the more you walk...")
            player.location = "forest"
        elif action == "2":
            player.show_status()
        else:
            print("\nInvalid action. Please ensure you are inputting a number for an action that is avalable. Only a number will be accepted.\n")
    elif player.location == "forest":
        if action == "1":
            print("\nYou venture deeper and discover a mysterious cave... of course you go in!!")
            player.location = "cave"
        elif action == "2":
            apple_heal = random.randint(1, 5) # Amount apple will heal player by
            player.heal_player(apple_heal)
            if player.hp >= 100: # Ensures the player never goes above full health
                print("\nYou are at full health.\n")
            else:
                print("\n")
                print(f"The apple healed you by {apple_heal}") # Tells the user how much the player is healed
        elif action == "3":
            player.show_status()
        elif action == "4":
            print("\nYou head back to where you started.. nothing has changed.")
            player.location = "start"
        else:
            print("\nInvalid action. Please ensure you are inputting a number for an action that is avalable. Only a number will be accepted.\n")
    elif player.location == "cave":
        if action == "1":
            fight_monster(player)
        elif action == "2":
            print("\nYou run back to the forest covered in sweat and other bodily fluids... how did they get there?! You're not scared...")
            player.location = "forest"
        else:
            print("\nInvalid action. Please ensure you are inputting a number for an action that is avalable. Only a number will be accepted.\n")

    if player.still_alive():
        describe_location(player) # Describes the location only if the player is still alive
    else:
        print("\n")
        print(f"{player.name} has perished. Game over.")
    

def fight_monster(player):
    """
    Function to handle fighting the monster in the cave. 
    Options for attack or run
    Handles damage from monster and to monster
    Handles damage to player
    """
    monster_hp = 50 # Starting hp of Monster
    print("A feral beast emerges from the shadows. There's no chance of taming this thing... KILL IT!!!\n")
    while monster_hp > 0 and player.still_alive():
        print("Please input either 'a' or 'r' only.")
        action = input("Do you want to (a)ttack or (r)un?\n").lower() # Ensures the input will be accepted if the user inputs a capital letter
        if action == "a":
            damage = random.randint(5, 20) # Amount player will damage monster
            monster_hp -= damage
            print(f"You dealt {damage} damage to the monster.. Will it be enough??")
            if monster_hp > 0: # If monster is alive, it will attack the player
                monster_attack = random.randint(10, 25) # Amount monster will damage player
                player.take_damage(monster_attack)
                print(f"The monster dealt {monster_attack} damage to you.")
                print("\n")
            else:
                print("You defeated the monster!! You loot it's bloody corpse.")
                player.add_item("Monster's treasure")


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