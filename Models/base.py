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
round_count = 0

def tournament_execution():
    tournament = create_a_tournament()
    player_list = tournament.player_list_tournament()
    return player_list

def round_one(player_list):
    round_name = "Round "+ str(round_count)
    round_one = Round(round_name,player_list)
    matches_round_one = round_one.round_original()
    matches_list = round_one.round_score(matches_round_one)
    print(round_one)
    return round_one

def round_two(player_list,round_count):
    round_count += 1
    round_name = "Round " + str(round_count)
    round = Round(round_name,player_list)
    matches_round = round.round_secondaires()
    matches_list = round.round_score(matches_round)
    print(round)
    return round



# player_list = tournament_execution()
p_one = Player("Joueur 1","name ","14/06/25","H",1)
p_deux = Player("Joueur 2","name ","14/06/25","H",2)
p_trois = Player("Joueur 3","name ","14/06/25","H",3)
p_quatre = Player("Joueur 4","name ","14/06/25","H",4)

p_list_test = [p_one,p_deux,p_trois,p_quatre]

# r_one = round_one(p_list_test)
# r_two = round_two(p_list_test)

def tournament_execution_test():
    tournament = create_a_tournament()
    player_list = tournament.player_list_tournament()
    round_list = []
    round_list.append (round_one(player_list))
    round_count = 1
    while round_count <= tournament.turn_number:
        round_count += 1
        round_played = round_two(player_list, round_count)
        round_list.append(round_played)

tournament_execution_test()