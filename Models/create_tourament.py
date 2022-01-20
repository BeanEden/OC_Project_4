from Models.database import *
from Models.tournoi import *


def create_a_tournament():
    name = input("Entrez le nom du tournoi :")
    place = input("Entrez le lieu du tournoi :")
    date = input("Entrez la date du tournoi :")
    time_control = input("Sélectionnez le mode de contrôle du temps :"
                         "1 - bullet"
                         "2 - blitz"
                         "3 - coup rapide")
    player_list = player_dictionary_select()
    description = input("Description générale du tournoi")
    # player_dictionary = player_serialization_tournament(player_dictionary)
    new_tournament = Tournament(name, place, date, "rounds", time_control, player_list, description)
    serialized_tournament = new_tournament.tournament_serialization()
    tournament_insertion(serialized_tournament)
    return serialized_tournament

#
# def tournament_list(self):
#     name = input("Entrez le nom du tournoi :")
#     place = input("Entrez le lieu du tournoi :")
#     date = input("Entrez la date du tournoi :")
#     time_control = input("Sélectionnez le mode de contrôle du temps :"
#                          "1 - bullet"
#                          "2 - blitz"
#                          "3 - coup rapide")
#     player_dictionary = Player.player_dictionary_select()
#     description = input("Description générale du tournoi")



def player_serialization_tournament(list):
    serialized_player_tournament = []
    for player in list:
        serialized_player_tournament.append(player.player_serialization())
    return serialized_player_tournament

# player_dictionary_select()
# # create_a_tournament()
if __name__ == '__main__':
    print("database.py lancé")
else :
    pass