from Models.database import *


class Match:
    def __init__(self, name, player_one, player_two, round_played):
        self.name = name
        self.player_one = player_one
        self.player_two = player_two
        self.result = "result not defined yet"
        self.score = 0
        self.opponents = str(self.name + " : " + self.player_one.name + " vs " + self.player_two.name)
        self.pair_up = [player_one.name,player_two.name]
        self.pair_up_reverse = [player_two.name,player_one.name]
        self.round = round_played.name
        self.tournament_name = round_played.tournament_name
        self.id = self.name[0] + self.name[-1] + "R" + str(round_played.count) + " " + self.tournament_name
        self.serialized_form = self.match_serialization()

    def __repr__(self):
        return repr([self.name, self.player_one, self.player_two, self.result])

    def match_serialization(self):
        serialized_match = {
            "tournament_id": self.tournament_name,
            "round_name": self.round,
            "match_name": self.name,
            "player_one": self.player_one.serialized_form,
            "player_two": self.player_two.serialized_form,
            "result": self.result,
            "id_key": self.id,
        }
        return serialized_match

    def matches_database_update(self):
        database_check_removal(self.serialized_form, db_matches)
        database_item_insertion(self.serialized_form, db_matches)

    def result_attribution(self, result):
        if result == 1:
            self.score = 1
            self.result = str(self.player_one.name+" wins")
        elif result == 2:
            self.score = 2
            self.result = str(self.player_two.name+" wins")
        elif result == 3:
            self.score = 3
            self.result = "match_nul"
        return self.result

    def score_attribution(self):
        if self.score == 1:
            self.player_one.score_add(1)
        elif self.result == 2:
            self.player_two.score_add(1)
        elif self.score == 3:
            self.player_one.score_add(0.5)
            self.player_two.score_add(0.5)


if __name__ == '__main__':
    print("matchs.py exécuté")
else:
    pass
