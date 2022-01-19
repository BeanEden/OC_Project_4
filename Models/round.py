from players import *
from matchs import *
from operator import *

class Round() :
    def __init__(self, name, matchs_list, start_time, end_time, player_list):
        self.name = name
        self.matchs_list = matchs_list
        self.start_time = start_time
        self.end_time = end_time
        self.player_list = player_list
        self.open = False

    # "Round" + str(define_round_number())
    #
    # def define_round_number (self):
    #     self.round_number
    #     round_number += 1
    #     return round_number

    def round_original(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        nombre_joueurs = len(original_classment)
        top_half = original_classment[0:nombre_joueurs / 2]
        bottom_half = original_classment[nombre_joueurs / 2:nombre_joueurs]
        match_dict = {}
        for i in range[0:nombre_joueurs/2]:
            match_name = "Match "+ (i+1)
            match = top_half[i] + "vs" + bottom_half[i]
            match_dict[match_name] = match
            print(match)



        # self.view.confirmation.match()

    print


def original_classment(player_list):



def round_2(self):
    original_classment = sorted(player_list, key=attrgetter('rank'), reverse=True)
    round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
    nombre_joueur_2 = len(round_classment)
    for i in range[0:round_classment]:
        print(top_half[i] + "vs" + bottom_half[i])

    # def start_round_1(self,player_list):
    #
    #
    # def tri_player(list):


