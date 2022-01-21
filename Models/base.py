from Models.tournoi import Tournament
from Models.tournoi import create_a_tournament
from Models.round import Round
from Models.players import Player

# class Controller:
#
#     def __init__(self, player, view):
#         # models
#         self.players: Player
#
#         # views
#         self.view = view
#
#     def run(self):
#         self.start_a_tournament()
#
#
#
#
#     def start_a_tournament(self):
#         "lance la vue"
#         if self.confirmation_creation_tournoi() == "y":
#             self.tournament = create_a_tournament(self)


def tournament_execution():
    tournament = create_a_tournament()
    player_list = tournament.player_list_tournament()
    return player_list

def round_one(player_list):
    round_count=1
    round_name = "Round "+ str(round_count)
    round_one = Round(round_name,player_list)
    matches_round_one = round_one.round_original()
    matches_list = round_one.round_score(matches_round_one)
    print(round_one)

   # round_one.round_score(round_one)

# player_list = tournament_execution()
p_one = Player("Joueur 1","name ","14/06/25","H",1)
p_deux = Player("Joueur 2","name ","14/06/25","H",2)
p_trois = Player("Joueur 3","name ","14/06/25","H",3)
p_quatre = Player("Joueur 4","name ","14/06/25","H",4)

p_list_test = [p_one,p_deux,p_trois,p_quatre]

round_one(p_list_test)


