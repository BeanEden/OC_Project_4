from Models.tournoi import Tournament
from Models.tournoi import create_a_tournament
from Models.round import Round

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
    print(player_list)
    round_count=1
    round_name = "Round "+ str(round_count)
    round_one = Round(round_name,player_list).round_original()


tournament_execution()




