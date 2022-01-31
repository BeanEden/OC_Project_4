from Models.database import *

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
        self.rounds_list = {}
        self.time_control = time_control
        self.players_list = players_list
        self.description = description
        self.last_round = ""
        self.id = self.name + self.date
        self.serialized_form = self.tournament_serialization()
        self.serialized_round_list = {}
        self.match_list = []
        self.opponents_list = []

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
        self.rounds_list["Round " + str(round_played.count)] = round_played.id


    def tournament_serialization(self):
        serialized_tournament = {
            "tournament_name": self.name,
            "tournament_place": self.place,
            "tournament_date": self.date,
            "tournament_turn_number": self.turn_number,
            "tournament_rounds": self.rounds_list,
            "tournament_time_control": self.time_control,
            "tournament_description": self.description,
            "tournament_player_dictionary": player_list_serialization(self.players_list, "Player ",db_players),
            "id_key": self.id
        }
        return serialized_tournament
    #
    # def tournament_serialization(self):
    #     serialized_tournament = {
    #         "tournament_name": self.name,
    #         "tournament_place": self.place,
    #         "tournament_date": self.date,
    #         "tournament_turn_number": self.turn_number,
    #         "tournament_rounds": self.rounds_list,
    #         "tournament_time_control": self.time_control,
    #         "tournament_description": self.description,
    #         "tournament_player_dictionary": self.players_list,
    #         "id_key": self.id
    #     }
    #     return serialized_tournament
    # def tournament_serialized(self):
    #     for players in self.players_list:


    def tournament_last_round(self):
        if len(self.rounds_list) != 0:
            self.last_round = self.rounds_list[-1]
        else:
            self.last_round = None
        return self.last_round

    def tournament_database_update(self):
        database_check_removal(self.serialized_form, db_tournament)
        database_item_insertion(self.serialized_form, db_tournament)

    def match_list(self):
        match_list = []
        for rounds in self.rounds_list:
            for matches in rounds.matches_list:
                match_list.append(matches)
        return match_list

    # def tournament_round_list_serialized(self):


if __name__ == '__main__':
    print("database.py lancé")
else:
    pass
