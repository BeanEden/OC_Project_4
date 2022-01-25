from tinydb import TinyDB
from tinydb import Query


db_players = TinyDB("db_players.json")
db_tournament = TinyDB("db_tournament.json")
db_rounds = TinyDB("db_rounds.json")
db_matches = TinyDB("db_matches.json")

def database_item_insertion(serialized_item, database):
    database_check_removal(serialized_item,database)
    database.insert(serialized_item)
#
def search_player_in_data_base(id_key,database):
    query = Query()
    try:
        item = database.search(query.id_key == str(id))
        item = item[-1]
    except IndexError:
        print("No such item in the database")
        item = None
    return item


def database_check_removal(serialized_item, database):
    query = Query()
    search_field = "id_key"
    check = serialized_item[search_field]
    try:
        database.remove(query.id_key == check)
    except None:
        print("item_id not found in the database")



def update_player_field(database, player_id, field_changed, new_input):
    player = Query()
    database.update({field_changed:new_input}, player.id == player_id)

def print_player_data_base(data_base):
    # lambda x : print(x),full_table
    # return mise_en_forme
    for player in data_base:
        print(player)

def clear_all_database(data_base):
    data_base.truncate()


print_player_data_base(db_players)


if __name__ == '__main__':
    print("database.py lancé")
else :
    pass