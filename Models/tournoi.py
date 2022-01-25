from Models.players import player_dictionary_select
from operator import *
from Models.database import *

TIME_CONTROL = {
    1: "bullet",
    2: "blitz",
    3: "coup rapide"
}
ROUND_NAMES = {
    "Round 1": "Round 1",
    "Round 2": "Round 2",
    "Round 3": "Round 3",
    "Round 4": "Round 4"
}


class Tournament:
    def __init__(self, name, place, date, time_control, players_list, description):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds_list = []
        self.time_control = time_control
        self.players_list = players_list
        self.description = description
        self.last_round = ""
        self.serialized_form = self.tournament_serialization()
        self.id = name+date

    def __repr__(self):
        return repr([
            self.name,
            self.place,
            self.date,
            self.rounds_list,
            self.time_control,
            self.players_list,
            self.description,
            self.id
        ])

    def player_list_tournament(self):
        return self.players_list



    def tournament_append_round(self, round_played):
        self.rounds_list.append(round_played)
        # return self.rounds_list
    #
    # def confirmation_creation_tournoi(self):
    #     """Confirme la création d'un nouveau tournoi"""
    #     validation = input("Créer un nouveau tournoi (y/n) ?")
    #     return validation

    def tournament_serialization(self):
        serialized_tournament = {
            "tournament_name": self.name,
            "tournament_place": self.place,
            "tournament_date": self.date,
            "tournament_turn_number": self.turn_number,
            "tournament_rounds": self.rounds_list,
            "tournament_time_control": self.time_control,
            "tournament_player_dictionary": self.players_list,
            "tournament_description": self.description,
            "id_key": self.id
        }
        return serialized_tournament

    def tournament_last_round(self):
        if len(self.rounds_list) != 0:
            self.last_round = self.rounds_list[-1]
        else :
            self.last_round = None
        return self.last_round

    def tournament_database_update(self):
        database_check_removal(self.serialized_form, db_tournament)
        database_item_insertion(self.serialized_form, db_tournament)



def create_a_tournament():
    input("Création d'un nouveau tournoi, appuyez sur une touche pour continuer :\n")
    name = input("Entrez le nom du tournoi :\n")
    place = input("Entrez le lieu du tournoi : \n")
    date = input("Entrez la date du tournoi : \n")
    time_control = input("Sélectionnez le mode de contrôle du temps :\n" +
                         "1 - bullet \n"
                         "2 - blitz \n"
                         "3 - coup rapide\n")
    description = input("Description générale du tournoi : ")
    player_list = player_dictionary_select()
    # player_list_serialized = player_serialization_tournament(player_list)
    new_tournament = Tournament(name, place, date, time_control, player_list, description)
    # serialized_tournament = new_tournament.tournament_serialization()
    # tournament_insertion(serialized_tournament)
    return new_tournament


def player_serialization_tournament(player_list_argument):
    serialized_player_tournament = []
    for player in player_list_argument:
        serialized_player_tournament.append(player.player_serialization())
    return serialized_player_tournament


if __name__ == '__main__':
    print("database.py lancé")
else:
    pass
