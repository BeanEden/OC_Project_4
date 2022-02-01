from Models.database import *
from Models.creation import *

TIME_CONTROL = {
    1: "bullet",
    2: "blitz",
    3: "coup rapide"
}


class Tournament:
    def __init__(self, name, place, date, time_control, description, players_list):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds_list = []
        self.time_control = time_control
        self.players_list = players_list
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

    def tournament_append_round(self, round_played):
        self.rounds_list.append(round_played.id)
        database_item_insertion(self.serialized_form, db_tournament)

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

    def tournament_last_round(self):
        if len(self.rounds_list) != 0:
            last_round = self.rounds_list[-1]
            last_round = search_player_in_data_base(last_round, db_rounds)
        else:
            last_round = None
        return last_round


if __name__ == '__main__':
    print("database.py lancé")
else:
    pass
