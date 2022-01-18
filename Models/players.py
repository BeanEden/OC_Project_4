class player :

    def __init__(self):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    def rank_update(rank):



serialized_player = {
    "name" : player.name
    "first_name" : player.first_name
    "birth_date" : player.birth_date
    "gender" : player.gender
    "rank" : player.rank
}


# from tinydb import TinyDB
#
# db = TinyDB(‘db.json’)
# players_table = db.table("players")
# players_table.truncate()	# clear the table first
# players_table.insert_multiple(serialized_players)
#
# serialized_players = players_table.all()




player = Player(name='John', age=22)