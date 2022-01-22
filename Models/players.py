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

    def __repr__(self):
        # return repr([self.name, self.birth_date, self.gender, self.rank, self.score])
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
            "player_id": self.id,
            "family_name": self.family_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
        }
        return serialized_player

    def score_add(self, value):
        self.score = self.score + value


def player_dictionary_select():
    player_count = 0
    player_list_tournament = []
    while player_count < 8:
        player_count += 1
        player_name = input("Enter player " + str(player_count) + " id :"
                            "id = firstname + first letter from family_name + day of birth"
                            "example : Mark Zucchin born on 19/03/1987 -> id = MarkZ19")
        player = search_player_in_data_base(player_name)
        new_player = player_instance_creation_from_data_base_tournoi(player)
        print("Player added : ")
        print(new_player)
        player_list_tournament.append(new_player)
    return player_list_tournament


def add_a_player():
    """Prompt for adding a player."""
    print("Création d'un nouveau joueur...")
    family_name = input("Nom du joueur : ")
    first_name = input("Prénom du joueur : ")
    birth_date = input("Date de naissance du joueur (DD/MM/YYYY): ")
    gender = input("Genre (F/H): ")
    rank = input("Classement (chiffre positif) : ")

    player = Player(family_name, first_name, birth_date, gender, rank)
    print(player.name + " a bien été enregistré(e). id = " + player.id)
    serialized_player = player.player_serialization()
    player_insertion(serialized_player)
    return serialized_player

def player_instance_creation_from_data_base_tournoi(dict_player):
    family_name = dict_player["family_name"]
    first_name = dict_player["first_name"]
    age = dict_player["birth_date"]
    rank = dict_player["rank"]
    gender = dict_player["gender"]
    new_player = Player(family_name=family_name, first_name=first_name, birth_date=age, gender=gender, rank=rank)
    # new_player = new_player.player_serialization()
    return new_player

# add_a_player()

if __name__ == '__main__':
    print("players.py exécuté")
else:
    pass
