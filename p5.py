"""
Tasks:
- Keep track of cards in hand
- Keep track of all cards played (suite/value/g or b)
- Keep track of number of cards each player has in order to keep track of score
- Create simple task to play
- Create a method to track the amount of cards other players have by counting how many cards they played/penalties
- Crate a function to determine the confidence score.
"""

import PGSS
from PGSS import utils
from PGSS.utils import Mathy

from PGSS.utils import Game

from PGSS import player
from PGSS.player import Player
player1 = Player()
player2 = Player()





"""Example"
print(Mathy.addTwo(5,5))
my_math = Mathy()
my_math.storeNumber(7)
print(my_math.addToSelf(10))
"""


prophet_points = 0
prophet_player = None




#def determine_play:


cards_played = []
#cards_played.append([suite, value, good/bad (boolean)])
#suites = heart, club, diamonds, spades

cards_hand = []
other_player_points = [0,0,0,0]
other_player_cards = [14, 14, 14, 14]
#test data

print(other_player_cards)

calculate_cards(False, 4, 2)

other_player_points = turn_points()

set_prophet(3)

post_turn(1)
print(other_player_points)

"""
post_turn(1)
post_turn(3)

set_prophet(2)
post_turn(2)

print(other_player_points)
"""

#format of cards played


## This is an example of using imports


