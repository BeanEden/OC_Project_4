
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
ROUND_NAMES = {
    "Round 1": "Round 1",
    "Round 2": "Round 2",
    "Round 3": "Round 3",
    "Round 4": "Round 4"
}


class Tournament :
    def __init__(self, name, place,date,rounds, time_control, players_dictionary, description):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds = rounds
        self.time_control = time_control
        self.players_dictionary = players_dictionary
        self.description = description


    def confirmation_creation_tournoi(self):
        """Confirme la création d'un nouveau tournoi"""
        validation = input("Créer un nouveau tournoi (y/n) ?")
        return validation


    def tournament_serialization(self):
            serialized_tournament = {
            "tournament_name": self.name,
            "tournament_place": self.place,
            "tournament_date": self.date,
            "tournament_turn_number": self.turn_number,
            "tournament_rounds": self.rounds,
            "tournament_time_control": self.time_control,
            "tournament_player_dictionary":self.players_dictionary,

            "tournament_description": self.description
        }
            return serialized_tournament

    def player_list_serialization(self):
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