from tinydb import TinyDB, Query
from Models.players import *

db_players = TinyDB("db_players.json")
# players_table = db.table("players")
# players_table.truncate()	# clear the table first
# players_table.insert_multiple(serialized_players)


def player_insertion(serialized_players):
    db_players.insert(serialized_players)


def print_player_data_base(data_base) :
    # lambda x : print(x),full_table
    # return mise_en_forme
    for player in data_base:
        print(player)

def search_in_data_base(nom) :
    player = Query()
    player = db_players.search(player.family_name == nom)
    return player

def clear_all_database(data_base):
    data_base.truncate()