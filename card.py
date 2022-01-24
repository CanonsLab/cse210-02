import random


class Card:
   
    def __init__(self):
        """Construct an instance of Card
        
        Attributes: 
            self (current card) = A random number between 1 to 13
            self (next card) = A random number between 1 to 13
            self (points) = Start points 300
            
        """
        self.current = random.randint(1, 13)
        self.next = random.randint(1, 13)
        self.points = 300
