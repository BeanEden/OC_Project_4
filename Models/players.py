from Models.database import *


class Player():

    def __init__(self, family_name, first_name, birth_date, gender, rank):
        self.family_name = family_name
        self.first_name = first_name
        self.name = str(self.first_name + self.family_name)
        self.birth_date = birth_date
        # self.age = date -
        self.gender = gender
        self.rank = rank
        self.score = 0

    def __repr__(self):
        # return repr([self.name, self.birth_date, self.gender, self.rank, self.score])
        return repr({
            "name":self.name,
            "age":self.birth_date,
            "gender" : self.gender,
            "rank":self.rank,
            "score":self.score})

    def player_serialization(self):
        serialized_player = {
        "family_name": self.family_name,
        "first_name": self.first_name,
        "birth_date": self.birth_date,
        "gender": self.gender,
        "rank": self.rank,
    }
        return serialized_player


    def player_list_tournoi(dict_player):
        family_name = dict_player["family_name"]
        first_name = dict_player["first_name"]
        name = first_name + " " + family_name
        age = dict_player["birth_date"]
        rank = dict_player["rank"]
        gender = dict_player["gender"]
        # score = 0
        new_player = Player(family_name=family_name, first_name=first_name, birth_date=age, gender=gender, rank=rank)
        # new_player = new_player.player_serialization()
        # new_player["score"] = 0
        return new_player

    def score_add(self,value):
        self.score = self.score + value

def player_dictionary_select():
    player_count = 0
    player_dictionary = {}
    player_list_tournament = []
    while player_count < 4:
        player_count += 1
        player_name = input(("Enter player ", player_count, "name :"))
        player = search_player_in_data_base(player_name)
        new_player = Player.player_list_tournoi(player)
        print("Player added : ")
        print(new_player)
        # new_player = Player(player)
        player_list_tournament.append(new_player)
        # player_key = "Player " + str(player_count)
        # player_dictionary[player_key]=new_player
    # # print(player_dictionary)
    # print(player_list_tournament)
    return player_list_tournament


def add_a_player():
    """Prompt for adding a player."""
    print("Création d'un nouveau joueur...")
    family_name = input("Nom du joueur : ")
    first_name = input("Prénom du joueur: ")
    birth_date = input("Date de naissance du joueur (DD/MM/YYYY): ")
    gender = input("Genre (F/H): ")
    rank = input("Classement (chiffre positif) : ")
    print("Player ", first_name, " ", family_name, " a bien été enregistré(e)")
    player = Player(family_name, first_name, birth_date, gender, rank)
    serialized_player = player.player_serialization()
    player_insertion(serialized_player)
    return serialized_player



if __name__ == '__main__':
    print("players.py exécuté")
else :
    pass