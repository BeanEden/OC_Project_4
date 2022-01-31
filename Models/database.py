from tinydb import TinyDB
from tinydb import Query


db_players = TinyDB("db_players.json")
db_tournament = TinyDB("db_tournament.json")
db_rounds = TinyDB("db_rounds.json")
db_matches = TinyDB("db_matches.json")



def database_item_insertion(serialized_item, database):
    database_check_removal(serialized_item,database)
    database.insert(serialized_item)

def search_player_in_data_base(id_key,database):
    query = Query()
    item = database.search(query.id_key == str(id_key))
    try:
        item = item[-1]
    except IndexError:
        print("No such item in the database")
        item = "a"
    return item

def database_check_removal(serialized_item, database):
    query = Query()
    search_field = "id_key"
    check = serialized_item[search_field]
    try:
        database.remove(query.id_key == check)
    except :
        print("item_id not found in the database")

def player_list_serialization(item_list, str_item_name, database):
    serialized_item_dictionary = {}
    item_count = 1
    for item in item_list:
        serialized_item_dictionary[(str_item_name + str(item_count))] = item.serialized_form
        database_item_insertion(item.serialized_form, database)
        item_count += 1
    return serialized_item_dictionary

def update_player_field(database, player_id, field_changed, new_input):
    player = Query()
    database.update({field_changed:new_input}, player.id == player_id)

def print_data_base(data_base):
    # lambda x : print(x),full_table
    # return mise_en_forme
    for item in data_base:
        print(item)

def print_dictionary(serialized_item):
    for key,value in serialized_item.items():
        print(str(key) + " : " + str(value))

def clear_all_database(data_base):
    data_base.truncate()

# clear_all_database(db_players)
print_data_base(db_players)

if __name__ == '__main__':
    print("database.py lancé")
else :
    pass