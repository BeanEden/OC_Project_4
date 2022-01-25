from tinydb import TinyDB
from tinydb import Query


db_players = TinyDB("db_players.json")
# players_table = db_players.table("players")
# players_table.truncate()	# clear the table first
# players_table.insert_multiple(serialized_players)
db_tournament = TinyDB("db_tournament.json")
db_rounds = TinyDB("db_rounds.json")
db_matches = TinyDB("db_matches.json")

def database_item_insertion(serialized_item, database):
    database.insert(serialized_item)

def tournament_insertion(new_tournament):
    db_tournament.insert(new_tournament)

def print_player_data_base(data_base):
    # lambda x : print(x),full_table
    # return mise_en_forme
    for player in data_base:
        print(player)
#
def search_player_in_data_base(id):
    player = Query()
    try:
        player = db_players.search(player.player_id == str(id))
        player = player[-1]
    except IndexError:
        print("No such item in the database")
        player = None
    return player

def clear_all_database(data_base):
    data_base.truncate()

def update_player_field(database, player_id, field_changed, new_input):
    player = Query()
    database.update({field_changed:new_input}, player.id == player_id)

def database_check_removal(serialized_item, database):
    query = Query()
    search_field = "id_key"
    check = serialized_item[search_field]
    try:
        database.remove(query.id_key == check)
    except None:
        print("item_id not found in the database")
# # print(search_in_data_base("Joueur 1 test"))

# player_name = input(("Enter player ", player_count, "name :"))
#             player = search_in_data_base(player_name)
#             # new_player = Player.player_list_tournoi(player)
#             new_player = Player(player)
#             player_list_tournament.append(new_player)

# print(search_in_data_base("Joueur 1 test"))

if __name__ == '__main__':
    print("database.py lancé")
else :
    pass