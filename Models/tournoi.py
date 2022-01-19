
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
    def __init__(self, name, place,date, rounds, time_control, players_dictionary, description):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds = rounds
        self.time_control = time_control
        self.players_list : players_dictionary
        self.description = description

    def start_rounds(self):
        self.rounds

    def confirmation_creation_tournoi(self):
        """Confirme la création d'un nouveau tournoi"""
        validation = input("Créer un nouveau tournoi (y/n) ?")
        return validation





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