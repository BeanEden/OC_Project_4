class Player :

    def __init__(self, family_name, first_name, birth_date, gender, rank, score=0):
        self.family_name = family_name
        self.first_name = first_name
        self.name = str(first_name + family_name)
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

    def add_a_player(self):
        """Prompt for adding a player."""
        print("Création d'un nouveau joueur:")
        self.family_name = input("Nom du joueur : ")
        self.first_name = input("Prénom du joueur: ")
        self.birth_date = input("Date de naissance du joueur (DD/MM/YYYY): ")
        self.gender = input("Genre (F/H): ")
        self.rank = input("Classement (chiffre positif) : ")
        return print("Player ",self.first_name, " ", self.family_name, " a bien été enregistré(e)")

    def serialization_player(self,family_name, first_name, birth_date, gender, rank, score=0):

        serialized_player = {
            "family_name" : Player.family_name,
            "first_name" : Player.first_name,
            "birth_date" : Player.birth_date,
            "gender" : Player.gender,
            "rank" : Player.rank,
            "score" : Player.score
        }
        return serialized_player

# from tinydb import TinyDB
#
# db = TinyDB(‘db.json’)
# players_table = db.table("players")
# players_table.truncate()	# clear the table first
# players_table.insert_multiple(serialized_players)
#
# serialized_players = players_table.all()


