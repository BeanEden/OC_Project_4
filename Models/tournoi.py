
    # création du tournoi
# ajout de huit joueurs
# génération de paires pour le premier tour
# réception des résultats
# répéter jusqu'à ce que les 4 tours soient joués



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
    # player_list_serialized = player_serialization_tournament(player_list)
    new_tournament = Tournament(name, place, date, "rounds", time_control, player_list, description)
    serialized_tournament = new_tournament.tournament_serialization()
    tournament_insertion(serialized_tournament)
    return new_tournament

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
if __name__ == '__main__':
    print("player_database.py lancé")
else :
    pass
#
#
# Tournées (liste des instances des rondes)
# Joueurs (liste des indices corraspondants aux instances du joueur stockés en mémoire)
# contrôle du temps (bulllet, blitz ou coup rapide)
# description (remarques générales u directeur du tournoi)