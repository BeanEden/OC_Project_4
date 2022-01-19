from Models.player_database import *

class Player :

    def __init__(self, family_name, first_name, birth_date, gender, rank, score=0):
        self.family_name = family_name
        self.first_name = first_name
        self.name = str(self.first_name + self.family_name)
        self.birth_date = birth_date
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


    def add_a_player():
        """Prompt for adding a player."""
        print("Création d'un nouveau joueur...")
        family_name = input("Nom du joueur : ")
        first_name = input("Prénom du joueur: ")
        birth_date = input("Date de naissance du joueur (DD/MM/YYYY): ")
        gender = input("Genre (F/H): ")
        rank = input("Classement (chiffre positif) : ")
        print("Player ",first_name, " ", family_name, " a bien été enregistré(e)")

        serialized_player = {
            "family_name": family_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "gender": gender,
            "rank": rank,
            "score": 0
        }
        player_insertion(serialized_player)
        return serialized_player

