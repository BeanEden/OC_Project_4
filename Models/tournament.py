
from Controller.creation import *

TIME_CONTROL = {
    1: "bullet",
    2: "blitz",
    3: "coup rapide"
}


class Tournament:
    def __init__(self, name, place, date, time_control, description, tournament_players_list):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds_list = []
        self.time_control = time_control
        self.players_list = tournament_players_list
        self.description = description
        # self.last_round = self.tournament_last_round()
        self.id = self.name + self.date
        self.serialized_form = self.tournament_serialization()

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

    def tournament_serialization(self):
        serialized_tournament = {
            "id_key": self.id,
            "tournament_name": self.name,
            "tournament_place": self.place,
            "tournament_date": self.date,
            "tournament_turn_number": self.turn_number,
            "tournament_rounds": self.rounds_list,
            "tournament_time_control": self.time_control,
            "tournament_description": self.description,
            "tournament_player_dictionary": self.players_list,
        }
        return serialized_tournament

    def tournament_append_round(self, round_played):
        self.rounds_list.append(round_played.id)
        # db_tournament.database_item_insertion(self.serialized_form)


if __name__ == '__main__':
    print("tournament.py executed")
else:
    pass
