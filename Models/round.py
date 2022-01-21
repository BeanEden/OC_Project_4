from Models.players import  Player
from Models.matchs import Match
# from matchs import *
from operator import *
player_dic= {'Player 1': {'family_name': 'Joueur 1 test', 'first_name': 'Prenom*', 'birth_date': '25/01/2022', 'gender': 'H', 'rank': '1'}, 'Player 2': {'family_name': 'Joueur 2 test', 'first_name': 'Prenom 2', 'birth_date': '25/02/2022', 'gender': 'F', 'rank': '2'}, 'Player 3': {'family_name': 'Joueur 3 test', 'first_name': 'Prenom 3', 'birth_date': '25/03/2022', 'gender': 'H', 'rank': '3'}, 'Player 4': {'family_name': 'Joueur 4 test', 'first_name': 'Prenom 4', 'birth_date': '25/04/2022', 'gender': 'F', 'rank': '4'}, 'Player 5': {'family_name': 'Joueur 5 test', 'first_name': 'Prenom 5', 'birth_date': '25/05/2022', 'gender': 'F', 'rank': '5'}, 'Player 6': {'family_name': 'Joueur 6 test', 'first_name': 'Prenom 6', 'birth_date': '25/06/2022', 'gender': 'H', 'rank': '6'}, 'Player 7': {'family_name': 'Joueur 7 test', 'first_name': 'Prenom 7', 'birth_date': '25/07/2022', 'gender': 'H', 'rank': '7'}, 'Player 8': {'family_name': 'Joueur 8 test', 'first_name': 'Prenom 8', 'birth_date': '25/08/2022', 'gender': 'F', 'rank': '8'}}



class Round() :
    def __init__(self, name, player_list):
        self.name = name
        self.player_number=len(player_list)
        self.matches_number = int(self.player_number / 2)
        # self.matchs_list = matchs_list
        # self.start_time = start_time
        # self.end_time = end_time
        self.player_list = player_list
        self.open = False
        self.matches_list = []

    def __repr__(self):
        return repr([self.name, self.matches_list])

    def round_player_list(self):
        return self.player_list

    def round_original(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        top_half = original_classment[0:self.matches_number]
        bottom_half = original_classment[self.matches_number:self.player_number]
        match_list = []
        for i in range(0,self.matches_number):
            match_count = i+1
            match_name = "Match "+ str(match_count)
            match_i = Match(match_name, top_half[i], bottom_half[i])
            print(match_i.opponents())
            match_list.append(match_i)
        print(match_list)
        self.matches_list = match_list
        return self.matches_list

    def round_score(self,round):
        for i in round:
            result = i.resultat_match()
            i.score_attribution(result)
        return self.matches_list

    def round_secondaires(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
        match_list = []
        for i in range(0,self.matches_number,1):
            match_count = i + 1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, round_classment[i], round_classment[i+1])
            print(match_i.opponents())
            match_list.append(match_i)
        print(match_list)
        self.matches_list = match_list
        return self.matches_list

    # def start_round_1(self,player_list):
    #
    #
    # def tri_player(list):
player_list_test = [['Prenom*Joueur 1 test', '25/01/2022', 'H', '1', 0],
                   ['Prenom 4Joueur 4 test', '25/04/2022', 'F', '4', 0],
                   ['Prenom 5Joueur 5 test', '25/05/2022', 'F', '5', 0],
                   ['Prenom 6Joueur 6 test', '25/06/2022', 'H', '6', 0]]

p_one = Player("Joueur 1","name ","14/06/25","H",1)
p_deux = Player("Joueur 2","name ","14/06/25","H",2)
p_trois = Player("Joueur 3","name ","14/06/25","H",3)
p_quatre = Player("Joueur 4","name ","14/06/25","H",4)

p_list_test = [p_one,p_deux,p_trois,p_quatre]
#
#
# test_d = Round("test",p_list_test)
# # test_pl_d = test_d.player_list
# # number = test_d.matches_number
# # print(number)
# #
# # test_o = Round("testdeux",player_list_test)
# # test_pl = test_o.player_list
# # print(test_pl)
# #
# test_rd = test_d.round_original()
# for i in test_rd :
#     result = i.resultat_match()
#     i.score_attribution(result)
#
# print(p_one.score)