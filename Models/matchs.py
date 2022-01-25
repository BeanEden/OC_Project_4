from players import Player
from round import Round
from Models.database import *

class Match :
    def __init__(self, name, joueur_1, joueur_2, round_played):
        self.name = name
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        # self.opponents = joueur_1 + " vs " + joueur_2
        # self.players = player_list
        self.result = "result not defined yet"
        self.opponents = self.opponents_function()
        self.round = round_played.name
        self.tournament_name = round_played.tournament_name
        self.id = self.name[0] + self.name[-1] + self.round[0:1] + " " + self.tournament_name
        self.serialized_form = self.match_serialization()

    def __repr__(self):
        return repr([self.name, self.joueur_1, self.joueur_2, self.result])

    # def show(self):
    #     print("Le ", self.name,"oppose ", self.opponents)

    # def result(self,score):
    #     if score = 1 :
    def opponents_function(self):
        joueur_1_name = self.joueur_1.name
        joueur_2_name = self.joueur_2.name
        opponents = str(self.name + " : " + joueur_1_name + " vs " + joueur_2_name)
        return opponents

    def match_serialization(self):
        serialized_match = {
            "tournament_id": self.tournament_name,
            "round_name": self.round,
            "match_name": self.name,
            "player_1" : self.joueur_1,
            "player_2" : self.joueur_2,
            "result": self.result,
            "id_key": self.id,
        }

    def matches_database_update(self):
        database_check_removal(self.serialized_form, db_matches)
        database_item_insertion(self.serialized_form, db_matches)
# class MatchView:
#     def resultat_match(self):
#         print("Déclarez le vainqueur :\n"
#             "   1 - " + self.joueur_1.name + "\n"
#             "   2 - " + self.joueur_2.name + "\n"
#             "   3 - Match Nul\n")
#         result = int(input())
#         return result

    def score_attribution(self, result):
        if result == 1 :
            self.joueur_1.score_add(1)
            self.result = str(self.joueur_1.name+" wins")
        elif result == 2 :
            self.joueur_2.score_add(1)
            self.result = str(self.joueur_2.name+" wins")
        elif result == 3 :
            self.joueur_1.score_add(0.5)
            self.joueur_2.score_add(0.5)
            self.result = "match_nul"
        return self.result

if __name__ == '__main__':
    print("matchs.py exécuté")
else :
    pass
