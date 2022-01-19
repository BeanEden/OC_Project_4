from tinydb import TinyDB, Query
from Models.players import *

db_players = TinyDB("db_players.json")
# players_table = db.table("players")
# players_table.truncate()	# clear the table first
# players_table.insert_multiple(serialized_players)
db_tournament = TinyDB("db_tournament.json")

def player_insertion(serialized_players):
    db_players.insert(serialized_players)

def tournament_insertion(new_tournament):
    db_tournament.insert(new_tournament)

def print_player_data_base(data_base) :
    # lambda x : print(x),full_table
    # return mise_en_forme
    for player in data_base:
        print(player)

def search_in_data_base(nom) :
    player = Query()
    player_db = db_players.search(player.family_name == nom)
    # player = player[-1]
    return player_db

def clear_all_database(data_base):
    data_base.truncate()

print(print_player_data_base(db_players))
# print(search_in_data_base("Joueur 1 test"))