from hilo_game import card
import random

class director:
    def __init__(self):
        """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (int): A random number between 1 and 13.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
        self.next_card = random.radint(1,13)
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to play again

        Args:
            self (Director): An instance of Director.
        """
        
        play_again=input("Play again? [y/n] ")
        self.is_playing = (play_again =="y") and self.points> 0
       
    def do_updates(self):
        if not self.is_playing:
            return 
        next_card=self.next_card.pick()
        self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the next card value. Also display the score. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        next_card = 0
        
        next_card=self.next_card.pick()
        next_card= f"{next_card} "

        print(f"Next card was: {next_card}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
    