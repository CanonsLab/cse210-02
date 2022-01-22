import random


class Card:

    def __init__(self):
        """Constructs a new instance of card.

        Args:
            self (card): An instance of card.
        """
        self.value = random(1,13)
        self.points = 300

    def pick(self):
        next_card = random.randint(1, 13)
        guess_card = input("Higher or lower? [h/l] ")
        if guess_card=="l" and self.value > next_card:
            self.points+=100
        else:
            self.points-=75

        if guess_card=="h" and self.value<next_card:
            self.points+=100
        else: 
            self.points-=75



        