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

main()