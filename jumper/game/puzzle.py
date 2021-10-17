import random

class Puzzle:
    """ A code template for the puzzle which is a secret
    word randomly chosen from a list.

    Stereotype: Information Holder
    """

    def __init__(self):
        """ class contructor,
        Args: self (Puzzle) an instance of the Puzzle 
        
        """
        word = ["horse", "letter", "camera","television", "money", "mountain", "flower"]
        

        self.word = word.random(word)
        self.word = self.chosen_word.append()



    def player_chose_letter(self):
        """Let the user to chose a letter from a-z.
        """

        guess = input("Guess a letter [a-z] : ")

    