from Models.player_database import *
import datetime

class Player():

    def __init__(self, family_name, first_name, birth_date, gender, rank, score=0):
        self.family_name = family_name
        self.first_name = first_name
        self.name = str(self.first_name + self.family_name)
        self.birth_date = birth_date
        # self.age = date -
        self.gender = gender
        self.rank = rank
        self.score = score

    def __repr__(self):
        return repr({
        "family_name" : self.family_name,
        "first_name" : self.first_name,
        "birth_date" : self.birth_date,
        "gender" : self.gender,
        "rank" : self.rank
    })

    def player_serialization(self):
            serialized_player = {
            "family_name": self.family_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
        }
            return serialized_player

    def player_serialization_tournament(self):
            serialized_player_tournament = {

            }