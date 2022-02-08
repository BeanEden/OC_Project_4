from Models.database import *
from Controller.menu import *
from Controller.creation import ItemCreation

# player_one = Player("p1","p1","04/05/2014","gender","1")
# player_two = Player("p2","p2","04/05/2014","gender","2")
# player_three = Player("p3","p3","04/05/2014","gender","3")
# player_four = Player("p4","p4","04/05/2014","gender","4")
# player_five = Player("p5","p5","04/05/2014","gender","5")
# player_six = Player("p6","p6","04/05/2014","gender","6")
# player_seven = Player("p7","p7","04/05/2014","gender","7")
# player_eight = Player("p8","p8","04/05/2014","gender","8")
#
# players_list = [player_one,player_two,player_three,player_four,player_five,player_six,player_seven,player_eight]
# player_list_serialization(players_list,db_players)

print_data_base(db_players.get_all())


creation = ItemCreation()
test = creation.opponents_list_construction("p5p5", "t11")
print(test)

matches_p_one = db_matches.query_2("tournament_id","t11", "player_one", "p5p5")
matches_p_two = db_matches.query_2("tournament_id","t11", "player_two", "p5p5")

print_data_base(matches_p_two)
print_data_base(matches_p_one)