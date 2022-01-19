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
        return repr([self.name, self.birth_date, self.gender, self.rank, self.score])

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
            serialized_player_tournament = []
            for player in self.players_dictionary:
                serialized_player_tournament.append(player.player_serialization())
            return serialized_player_tournament

    def player_dictionary_select():
        player_count = 0
        player_dictionary = {}
        player_list_tournament = []
        while player_count < 2:
            player_count += 1
            player_name = input(("Enter player ", player_count, "name :"))
            player = search_in_data_base(player_name)
            new_player = Player.player_list_tournoi(player)
            player_list_tournament.append(new_player)
            # player_key = "Player " + str(player_count)
            # player_dictionary[player_key]=new_player
        # print(player_dictionary)
        print(player_list_tournament)
        return player_list_tournament

    def player_list_tournoi(dict_player):
        family_name = dict_player["family_name"]
        first_name = dict_player["first_name"]
        name = first_name + " " + family_name
        age = dict_player["birth_date"]
        rank = dict_player["rank"]
        gender = dict_player["gender"]
        score = 0
        new_player = Player(family_name=family_name, first_name=first_name, birth_date=age, gender=gender, rank=rank,
                            score=score)
        # new_player = [name, age, rank, score]
        return new_player