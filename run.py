import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = []
        self.location = "start"
