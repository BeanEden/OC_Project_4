from players import *
from matchs import *
from operator import *
player_dic= {'Player 1': {'family_name': 'Joueur 1 test', 'first_name': 'Prenom*', 'birth_date': '25/01/2022', 'gender': 'H', 'rank': '1'}, 'Player 2': {'family_name': 'Joueur 2 test', 'first_name': 'Prenom 2', 'birth_date': '25/02/2022', 'gender': 'F', 'rank': '2'}, 'Player 3': {'family_name': 'Joueur 3 test', 'first_name': 'Prenom 3', 'birth_date': '25/03/2022', 'gender': 'H', 'rank': '3'}, 'Player 4': {'family_name': 'Joueur 4 test', 'first_name': 'Prenom 4', 'birth_date': '25/04/2022', 'gender': 'F', 'rank': '4'}, 'Player 5': {'family_name': 'Joueur 5 test', 'first_name': 'Prenom 5', 'birth_date': '25/05/2022', 'gender': 'F', 'rank': '5'}, 'Player 6': {'family_name': 'Joueur 6 test', 'first_name': 'Prenom 6', 'birth_date': '25/06/2022', 'gender': 'H', 'rank': '6'}, 'Player 7': {'family_name': 'Joueur 7 test', 'first_name': 'Prenom 7', 'birth_date': '25/07/2022', 'gender': 'H', 'rank': '7'}, 'Player 8': {'family_name': 'Joueur 8 test', 'first_name': 'Prenom 8', 'birth_date': '25/08/2022', 'gender': 'F', 'rank': '8'}}

player_list = [
    Player()
]


class Round() :
    def __init__(self, name, player_list):
        self.name = name
        self.player_number=len(player_list)
        # self.matchs_list = matchs_list
        # self.start_time = start_time
        # self.end_time = end_time
        self.player_list = player_list
        self.open = False


    def round_original(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        top_half = original_classment[0:self.player_number / 2]
        bottom_half = original_classment[self.player_number / 2:self.player_number]
        match_list = []
        for i in range[0:self.player_number2]:
            match_name = "Match "+ (i+1)
            match_list.append(Match(match_name,top_half[i],bottom_half[i]))
            print(match_list)


    def round_2(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
        match_list = []
        for i in range[0:round_classment]:


    # def start_round_1(self,player_list):
    #
    #
    # def tri_player(list):


