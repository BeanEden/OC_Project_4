from Models.player_database import *
from Models.players import *
from Views.tournament import *
from Models.tournoi import *
from Controllers.add_player import *


def create_a_tournament():
    name = input("Entrez le nom du tournoi :")
    place = input("Entrez le lieu du tournoi :")
    date = input("Entrez la date du tournoi :")
    time_control = input("Sélectionnez le mode de contrôle du temps :"
                         "1 - bullet"
                         "2 - blitz"
                         "3 - coup rapide")
    player_dictionary = Player.player_dictionary_select()
    description = input("Description générale du tournoi")
    new_tournament = Tournament(name, place, date, "rounds", time_control, player_dictionary, description)
    serialized_tournament = new_tournament.tournament_serialization()
    tournament_insertion(serialized_tournament)

    # tournament_insertion(serialized_tournament)
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






create_a_tournament()