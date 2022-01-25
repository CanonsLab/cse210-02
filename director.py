from card import Card

class Director:
    def __init__(self):
        """Set the variables to earn and lose points.
        
        Attributes
            self (Card) = call the Class Card
            self (win) = Earns points if the player guessed correctly
            self (is playing) = Whether or not the game is being played.
            self (lose) = Loses points if the player guessed incorrectly 
        """

        self.card = Card()
        self.is_playing = True
        self.win = 100
        self.lose = -75
        
        
    def start_game(self):
        """Execute the functions to run the game"""
        
        while self.is_playing == True:
            self.card.pick()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
            if self.card.points == 1000 or self.card.points > 1000:
                print("You are a winner!! :)")
                play_again = input("Do you want to play again? (y/n): ")
                if play_again == "y":
                    self.is_playing = True
                    self.card.points = 300
                else:
                    self.is_playing = not True

            elif self.card.points == 0 or self.card.points < 0:
                print("You are a loser :( Keep trying.")
                play_again = input("Do you want to play again? (y/n): ")
                if play_again == "y":
                    self.is_playing = True
                    self.card.points = 300
                else:
                    self.is_playing = not True


            else:
                self.is_playing = True
            

    def get_inputs(self):
        """Display the current card.

        Attribute:
            self (guess_card) = Get the input of the user.
        """
    
        print(f"\nThe card is: {self.card.current}")
        self.guess_card = input("Higher or lower? (h/l): ")
       
    
        
    def do_updates(self):
        """Add or subtract points to the user."""
       
        if self.card.current > self.card.next and self.guess_card == "l" \
        or self.card.current < self.card.next and self.guess_card == "h":
            self.card.points += self.win 
       
        elif self.card.current > self.card.next and self.guess_card == "h" \
             or self.card.current < self.card.next and self.guess_card == "l":
            self.card.points += self.lose


    def do_outputs(self):
       
        """Display to the user the results."""
        print(f"Next card was: {self.card.next}")
        print(f"Your score is: {self.card.points}")
        