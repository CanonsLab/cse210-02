import random


class Card:

    def __init__(self):
        self.value = 0
        self.points = 0

    def pick(self):
        self.value = random.randint(1, 6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0