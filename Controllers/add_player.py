from Models.player_database import *
from Models.players import *

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
    # serialized_player = {
    #     "family_name": family_name,
    #     "first_name": first_name,
    #     "birth_date": birth_date,
    #     "gender": gender,
    #     "rank": rank,
    # }
    serialized_player = player.player_serialization()
    player_insertion(serialized_player)
    return serialized_player
#
# add_a_player()