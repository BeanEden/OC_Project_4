from Models.database import *


class Player:

    def __init__(self, family_name, first_name, birth_date, gender, rank):
        self.family_name = family_name
        self.first_name = first_name
        self.name = str(self.first_name + " " + self.family_name)
        self.birth_date = birth_date
        # self.age = date -
        self.gender = gender
        self.rank = rank
        self.score = 0
        self.id = self.first_name + self.family_name[0] + self.birth_date[0:2]
        self.serialized_form = self.player_serialization()
        self.opponents_list = []

    def __repr__(self):
        return repr([self.name, self.id, self.rank, self.score])

    def player_serialization(self):
        serialized_player = {
            "id_key": self.id,
            "family_name": self.family_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
        }
        return serialized_player

    def score_add(self, value):
        self.score = self.score + value

    def opponent_add(self, opponent):
        self.opponents_list.append(opponent)
        return self.opponents_list


if __name__ == '__main__':
    print("players.py exécuté")
else:
    pass
