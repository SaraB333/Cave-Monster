import random

class Player:
    # Player class to handle player attributes and actions
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
        Heals the player when they eat an apple (up to full health (100)).
        """
        self.hp += heal
        if self.hp >= 100:
            self.hp = 100

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
        "cave": "You find a cave. It is even darker than the forest (somehow).. You hear growling inside.. It's getting louder."
    }
    print(locations[player.location])
    available_actions(player)


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
    action = input("Choose an action:\n")
    handle_action(player, action)


def handle_action(player, action):
    """
    Function to handle user input and game progression through 3 levels
    """
    if player.location == "start":
        if action == "1":
            print("You walk into the forest. The light of day fades the more you walk...")
            player.location = "forest"
        elif action == "2":
            player.show_status()
        else:
            print("Invalid action. Please ensure you are inputting a number for an action that is avalable. Only a number will be accepted.")
    elif player.location == "forest":
        if action == "1":
            print("You venture deeper and discover a mysterious cave... of course you go in!!")
            player.location = "cave"
        elif action == "2":
            apple_heal = random.randint(1, 5)
            player.heal_player(apple_heal)
            if player.hp >= 100:
                print("You are at full health.\n")
            else:
                print(f"The apple healed you by {apple_heal}")
        elif action == "3":
            player.show_status()
        elif action == "4":
            print("You head back to where you started.. nothing has changed.")
            player.location = "start"
        else:
            print("Invalid action. Please ensure you are inputting a number for an action that is avalable. Only a number will be accepted.")
    elif player.location == "cave":
        if action == "1":
            print("placeholder")
            # CREATE A FUNCTION FOR FIGHTING THE MONSTER AND INPUT HERE
        elif action == "2":
            print("You run back to the forest covered in sweat and other bodily fluids... how did they get there?! You're not scared...")
            player.location = "forest"
        else:
            print("Invalid action. Please ensure you are inputting a number for an action that is avalable. Only a number will be accepted.")

    describe_location(player)
    


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