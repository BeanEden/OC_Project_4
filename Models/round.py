import datetime


class Round:
    def __init__(self, name, tournament):
        self.name = name
        self.tournament = tournament
        self.player_list = self.tournament.players_list
        self.player_number = len(self.player_list)
        self.matches_number = int(self.player_number / 2)
        self.start_time = datetime. datetime. now()
        self.end_time = "unfinished"
        self.round_duration = ""
        self.status = "open"
        self.count = name[-1]
        self.tournament_name = tournament.id
        self.matches_list = []
        self.id = self.name[0] + self.count + " " + tournament.id
        self.matches_list_serialized = []
        self.serialized_form = self.round_serialization()

    def __repr__(self):
        return repr([self.name, self.matches_list])

    def round_serialization(self):
        serialized_round = {
            "id_key": self.id,
            "tournament_id": self.tournament_name,
            "round_name": self.name,
            # "matches_list": self.matches_list,
            # "players_list": player_list_serialization(self.player_list, "Player ", db_players),
            "start_time": str(self.start_time),
            "end_time": str(self.round_time_over())
        }
        return serialized_round

    def round_time_over(self):
        if self.status != "over":
            self.end_time = datetime. datetime. now()
        else:
            self.end_time = "unfinished"
        return self.end_time

    def round_duration(self):
        if self.end_time != "unfinished":
            self.round_duration = int(self.end_time) - int(self.start_time)
        return self.round_duration

    def round_check(self, matches_list):
        for match in matches_list:
            if match.result == "result not defined yet":
                self.status = "open"
            else:
                self.status = "complete"
        return self.status


if __name__ == '__main__':
    print("round.py executed")
else:
    pass
