
    # création du tournoi
# ajout de huit joueurs
# génération de paires pour le premier tour
# réception des résultats
# répéter jusqu'à ce que les 4 tours soient joués

from Models.player_database import *


TIME_CONTROL = {
    1 : "bullet",
    2 : "blitz",
    3 : "coup rapide"
}


class Tournament :
    def __init__(self, name, place,date, rounds, time_control, players_list, description):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds = rounds
        self.time_control = TIME_CONTROL
        self.players_list : players_dictionary
        self.description = self.view.description

    def start_rounds(self):
        self.rounds

    def confirmation_creation_tournoi(self):
        """Confirme la création d'un nouveau tournoi"""
        validation = input("Créer un nouveau tournoi (y/n) ?")
        return validation

    def create_a_tournament(self):
        name = input("Entrez le nom du tournoi :")
        place = input("Entrez le lieu du tournoi :")
        date = input("Entrez la date du tournoi :")
        time_control = input("Sélectionnez le mode de contrôle du temps :"
                             "1 - bullet"
                             "2 - blitz"
                             "3 - coup rapide")
        player_list = self.player_list_select
        description = input("Description générale du tournoi")

    def player_list_select():
        player_count = 0
        player_dictionary = {}
        while player_count < 8:
            player_count += 1
            player = input(("Enter player ", player_count, "name :"))
            search_in_data_base(player)
            player_dictionary["Player ",player_count] = player
        print(player_dictionary)
        return player_dictionary



#
# serialized_turnament = {
#     "name" : turnament.name,
#     "place" : turnament.place,
#     "date" : turnament.date,
#     "turn_number" : turnament.turn_number,
#     "turns" : turnament.turns,
#     "time_control" : turnament.TIME_CONTROL
#     "players" : turnament.players_list
# }
#
#
#
#
#
#
# Tournées (liste des instances des rondes)
# Joueurs (liste des indices corraspondants aux instances du joueur stockés en mémoire)
# contrôle du temps (bulllet, blitz ou coup rapide)
# description (remarques générales u directeur du tournoi)