import random

class Dealer:
    """A code template for a person who throws dice. The responsibility of this 
    class of objects is to throw the dice, keep track of the values, the score 
    and determine whether or not it can throw again.
    
    Attributes:
        score_list (list): A list numbers representing the result of scores.
        result: A result of random number 1 to 13.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.score_list = []
        self.result = random.randint(1, 13)
        self.result2 = random.randint(1, 13)
        self.num_deals = 0
        self.low = 1
        self.high = 13 
        self.score = 100
        self.score0 = 0
        self.score1 = -75
        
    def can_show(self):
        """Determines whether or not the Dealer can show again according to 
        the rules. 

        Args: 
            self (Dealer): An instance of Dealer.
        
        Returns:
            boolean: True if the list of card has at least a hundred, or a negative seventy-five, or 
            the number of deals is zero; false if otherwise.
        """
        return (self.score_list.count(100) > 0 or self.score_list.count(-75) > 0 
                or self. num_deals == 0)

    def get_points(self):
        """Calculates the total number of points for the current deal. hundreds 
        are worth 100 points, negative seventy-five are worth -75 points. 

        Args: 
            self (Dealer): An instance of Dealer.
        
        Returns:
            number: The total points for the current deal.
        """
        return self.score_list.count(100) * 100 - self.score_list.count(-75) * 75
        
    def show_card(self):
        """Show the car by randomly generating numbers 1 to 13. 

        Args: 
            self (Dealer): An instance of Dealer.
        """
        self.score_list.clear()
        if self.low != self.high:
                self.result = random.randint(self.low, self.high)
        #else:
            #self.result = self.low

        self.result = random.randint(1, 13)
        self.result2 = random.randint(1, 13)
        print(f"The card is: {self.result}")
        self.feedback = input(str("Higher or lower? [h/l] ").lower())
                
        if self.feedback == "h":
            self.high = self.result - 1
            
            if self.result2 > self.result:
                self.score = 100
                self.score_list.append(self.score)

            elif self.result2 == self.result:
                self.score0 = 0
                self.score_list.append(self.score0)

            else:
                self.score = -75
                self.score_list.append(self.score1)
                    
        elif self.feedback =="l":
            self.low = self.result + 1
            
            if self.result2 < self.result:
                self.score = 100
                self.score_list.append(self.score)

            elif self.result2 == self.result:
                self.score0 = 0
                self.score_list.append(self.score0)

            else:
                self.score = -75
                self.score_list.append(self.score1)         

        self.num_deals += 1

