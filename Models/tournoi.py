
    # création du tournoi
# ajout de huit joueurs
# génération de paires pour le premier tour
# réception des résultats
# répéter jusqu'à ce que les 4 tours soient joués

from players import player

TIME_CONTROL = {
    1 : "bullet",
    2 : "blitz",
    3 : "coup rapide"
}


class Tournament :
    def __init__(self):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds = rounds
        self.time_control = TIME_CONTROL
        self.players_list : list[players] = append_players()
        self.description = self.view.description

    def start_rounds(self):
        self.rounds





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