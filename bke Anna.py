import random
from bke import *

class MySmartAgent(EvaluationAgent):
    def evaluate(self, bord, my_symbol, opponent_symbol):
        getal = 3
        if bord[4] == my_symbol:
            getal += 6 
        if can_win(bord, my_symbol):
            getal += 9
        if is_winner(bord, my_symbol):
            getal = 50
        elif can_win(bord, opponent_symbol):
            getal = -50
        return getal

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, bord, my_symbol, opponent_symbol):
        return random.randint(1, 500)

my_random_agent = MyRandomAgent()
my_smart_agent = MySmartAgent ()
start(player_o=my_smart_agent, player_x=my_random_agent)


