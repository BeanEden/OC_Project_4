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
        self.rounds_list = []
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
        self.rounds_list.append(round_played)
        for match in round_played.matches_list:
            self.match_list.append(match)
            self.opponents_list.append(match.pair_up)
            self.opponents_list.append(match.pair_up_reverse)
            print(self.opponents_list)
        # self.rounds_dictionary[round_played.name] = round_played
        # player_list_serialization(self.round_played, "Round ", db_rounds)
        database_item_insertion(round_played.serialized_form, db_rounds)
        # self.serialized_round_list[round_played.name] = round_played
        # return self.serialized_round_list

    def tournament_serialization(self):
        serialized_tournament = {
            "tournament_name": self.name,
            "tournament_place": self.place,
            "tournament_date": self.date,
            "tournament_turn_number": self.turn_number,
            "tournament_rounds": player_list_serialization(self.rounds_list, "Round ",db_rounds),
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
