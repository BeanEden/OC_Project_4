from tinydb import TinyDB, Query


class Database:
    def __init__(self, db_name):
        self.db = TinyDB(str(db_name) + ".json")

    def clear_database(self):
        self.db.truncate()

    def database_check_removal(self, serialized_item):
        query = Query()
        try:
            self.db.remove(query.id_key == serialized_item["id_key"])
        except IndexError:
            print("item_id not found in the database")

    def database_item_insertion(self, serialized_item):
        self.database_check_removal(serialized_item)
        self.db.insert(serialized_item)

    def query_2(self, var_1, val_1, var_2, val_2):
        q = Query()
        return self.db.search((q[str(var_1)] == str(val_1)) & (q[str(var_2)] == str(val_2)))

    def search_in_data_base(self, id_key):
        query = Query()
        item = self.db.search(query.id_key == str(id_key))
        try:
            item = item[-1]
        except IndexError:
            print("No such item in the database")
            item = "item not found"
        return item

    def search_in_data_base_bis(self, value, id_key):
        query = Query()
        item = self.db.search(query[value] == str(id_key))
        try:
            item = item[-1]
        except IndexError:
            print("No such item in the database")
            item = "item not found"
        return item

    def update_player_field(self, player_id, field_changed, new_input):
        query = Query()
        self.db.update({field_changed: new_input}, query.id_key == str(player_id))

    def get_all(self):
        return self.db.all()

    def player_list_serialization(self, item_list):
        print(item_list)
        for item in item_list:
            item = item.serialized_form
            self.db.database_item_insertion(item)

db_players = Database("db_players")
db_tournament = Database("db_tournament")
db_rounds = Database("db_rounds")
db_matches = Database("db_matches")
# db_tournament.clear_database()

if __name__ == '__main__':
    print("database.py executed")
else:
    pass