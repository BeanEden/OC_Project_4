from Models.player_database import *
from Models.players import *
from Views.tournament import *
from Models.tournoi import *
from Controllers.add_player import *

def create_a_tournament():
    name = input("Entrez le nom du tournoi :")
    place = input("Entrez le lieu du tournoi :")
    date = input("Entrez la date du tournoi :")
    time_control = input("Sélectionnez le mode de contrôle du temps :"
                         "1 - bullet"
                         "2 - blitz"
                         "3 - coup rapide")
    player_dictionary = player_dictionary_select()
    description = input("Description générale du tournoi")
    new_tournament = Tournament(
        name=name,
        place=place,
        date=date,
        time_control=time_control,
        players_dictionary=player_dictionary,
        description=description
    )

def player_dictionary_select():
    player_count = 0
    player_dictionary = {}
    while player_count < 8:
        player_count += 1
        player_name = input(("Enter player ", player_count, "name :"))
        player = search_in_data_base(player_name)
        new_player = player_list_tournoi(player)
        player_dictionary["Player",player_count]=new_player
    print(player_dictionary)
    return player_dictionary


def player_list_tournoi(dict_player):
    family_name = dict_player["family_name"]
    first_name = dict_player["first_name"]
    age = dict_player["birth"]
    rank = dict_player["rank"]
    score = 0
    new_player = Player(family_name=family_name,first_name=first_name, birth_date=age, rank=rank, score=score)
    return new_player

create_a_tournament()