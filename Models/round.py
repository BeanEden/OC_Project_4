# from Models.players import Player
from Models.matchs import Match
from operator import *


class Round:
    def __init__(self, name, player_list):
        self.name = name
        self.player_number = len(player_list)
        self.matches_number = int(self.player_number / 2)
        # self.matchs_list = matchs_list
        # self.start_time = start_time
        # self.end_time = end_time
        self.player_list = player_list
        self.status = "open"
        self.matches_list = []
        self.count = name[-1]

    def __repr__(self):
        return repr([self.name, self.matches_list])

    def round_player_list(self):
        return self.player_list

    def round_status_generated(self):
        self.status = "matches generated"
        return self.status

    def round_status_closed(self):
        self.status = "matches generated"
        return self.status

    def round_one_method(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        top_half = original_classment[0:self.matches_number]
        bottom_half = original_classment[self.matches_number:self.player_number]
        match_list = []
        for i in range(0, self.matches_number):
            match_count = i+1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, top_half[i], bottom_half[i])
            print(match_i.opponents)
            match_list.append(match_i)
        # print(match_list)
        self.matches_list = match_list
        return self.matches_list

    def round_match_list_method(self, list_match_played_in_round_argument):
        for i in list_match_played_in_round_argument:
            i.score_attribution()
        return self.matches_list

    def secondary_rounds_method(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
        match_list = []
        for i in range(0, self.matches_number, 1):
            match_count = i + 1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, round_classment[i], round_classment[i+1])
            print(match_i.opponents)
            match_list.append(match_i)
        # print(match_list)
        self.matches_list = match_list
        return self.matches_list

    def round_match_list_definition(self, round_count):
        matches_list = []
        if round_count == 1:
            self.matches_list = self.round_one_method()
        else:
            self.matches_list = self.secondary_rounds_method()
        return self.matches_list

    def round_check(self):
        for match in self.matches_list:
            if match.result == "result not defined yet":
                self.status = "open"
            else :
                self.status = "complete"
        return self.status

    # def start_round_1(self,player_list):
    #
    #
#     # def tri_player(list):
# player_list_test = [['Prenom*Joueur 1 test', '25/01/2022', 'H', '1', 0],
#                    ['Prenom 4Joueur 4 test', '25/04/2022', 'F', '4', 0],
#                    ['Prenom 5Joueur 5 test', '25/05/2022', 'F', '5', 0],
#                    ['Prenom 6Joueur 6 test', '25/06/2022', 'H', '6', 0]]
#
# p_one = Player("Joueur 1","name ","14/06/25","H",1)
# p_deux = Player("Joueur 2","name ","14/06/25","H",2)
# p_trois = Player("Joueur 3","name ","14/06/25","H",3)
# p_quatre = Player("Joueur 4","name ","14/06/25","H",4)
#
# p_list_test = [p_one,p_deux,p_trois,p_quatre]
# #
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
