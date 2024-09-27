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
    Function to display the current location
    """
    locations = {
        "start": "You are at the entrance of a dark forest. There is a path you can see ahead. It leads into the forest.",
        "forest": "You have entered the forest. It's almost too dark to see. You can barely make out an apple tree with shiny red apples on it. It's quiet... too quiet.",
        "cave": "You find a cave. It is darker than the forest (somehow) and cold.. You hear growling inside.. It's getting louder."
    }
    print(locations[player.location])


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