from tinydb import TinyDB
from tinydb import Query


db_players = TinyDB("db_players.json")
# players_table = db_players.table("players")
# players_table.truncate()	# clear the table first
# players_table.insert_multiple(serialized_players)
db_tournament = TinyDB("db_tournament.json")

def player_insertion(serialized_players):
    db_players.insert(serialized_players)

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

def player_check_removal(serialized_player, database):
    query = Query()
    search_field = "player_id"
    check = serialized_player[search_field]
    try:
        database.remove(query.player_id == check)
    except None:
        print("player not in the database")
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