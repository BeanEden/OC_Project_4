class Round:
    status = 1

    def __init__(self, name, tournament, start_time="", end_time="unfinished"):
        self.name = name
        self.tournament = tournament
        self.player_list = self.tournament.players_list
        self.player_number = len(self.player_list)
        self.matches_number = int(self.player_number / 2)
        self.round_duration = ""
        self.count = name[-1]
        self.tournament_name = tournament.id
        self.start_time = start_time
        self.end_time = end_time
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
            "start_time": str(self.start_time),
            "end_time": str(self.end_time)
        }
        return serialized_round

    def round_check(self, matches_list):
        for match in matches_list:
            if match.result == "result not defined yet":
                self.status = 1
            else:
                self.status = 0
        return self.status


if __name__ == '__main__':
    print("round.py executed")
else:
    pass
