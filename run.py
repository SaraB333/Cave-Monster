import random

class Player:
    """
    Player class to handle player attributes and actions
    """
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = []
        self.location = "start"

    def show_status(self):
        print(f"\n{self.name} - HP: {self.hp}")
        print("Inventory:", ", ".join(self.inventory) if self.inventory else "Empty")


def describe_location(player):
    """
    Function to display the current location and available actions
    """
    locations = {
        "start": "You are at the entrance of a dark forest. There is a path you can see ahead. It leads into the forest.",
        "forest": "You have entered the forest. It's almost too dark to see. You can barely make out an apple tree with shiny red apples on it. It's quiet... too quiet.",
        "cave": "You find a cave. It is darker than the forest (somehow) and cold.. You hear growling inside.. It's getting louder."
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