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
        self.id = self.id_player()
        self.serialization = self.player_serialization()

    def __repr__(self):
        return repr([self.name, self.id, self.rank, self.score])

    def id_player(self):
        """id = firstname + first letter from family_name + day of birth"""
        id_key_one = self.first_name
        id_key_two = self.family_name[0]
        id_key_three = self.birth_date[0:2]
        self.id = id_key_one+id_key_two+id_key_three
        return self.id

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

    def player_database_update(self):
        database_check_removal(self.serialization, db_players)
        database_item_insertion(self.serialization, db_players)









# add_a_player()

if __name__ == '__main__':
    print("players.py exécuté")
else:
    pass
