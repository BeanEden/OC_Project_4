class Tournament:

    def __init__(self, name, place, date, time_control, description, tournament_players_list, rounds_list=[], status=1):
        self.name = name
        self.place = place
        self.date = date
        self.turn_number = 4
        self.rounds_list = rounds_list
        self.time_control = time_control
        self.players_list = tournament_players_list
        self.description = description
        self.status = status
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
            "tournament_status": self.status
        }
        return serialized_tournament

    def tournament_append_round(self, round_played):
        if round_played.id in self.rounds_list:
            pass
        else:
            self.rounds_list.append(round_played.id)

    def close_tournament(self):
        self.status = 0


if __name__ == '__main__':
    print("tournament.py executed")
else:
    pass
