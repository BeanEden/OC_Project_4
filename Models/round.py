from players import *
from matchs import *


class Round :
    def __init__(self):
        self.name = "Round" + str(define_round_number())
        self.matchs_list = matchs_list
        self.start_time = start_time
        self.end_time = end_time
        self.open_over = open_over


    def define_round_number (self):
        self.round_number
        round_number += 1
        return round_number

    # def start_round_1(self,player_list):
    #
    #
    # def tri_player(list):


