from Models.database import *
from Models.players import Player
from Controller.menu import *
from Controller.creation import ItemCreation
from Controller.creation import *
from Views.View import *

player_one = Player("p1","p1","01/05/2014","gender","1")
player_two = Player("p2","p2","02/05/2014","gender","2")
player_three = Player("p3","p3","03/05/2014","gender","3")
player_four = Player("p4","p4","04/05/2014","gender","4")
player_five = Player("p5","p5","05/05/2014","gender","5")
player_six = Player("p6","p6","06/05/2014","gender","6")
player_seven = Player("p7","p7","07/05/2014","gender","7")
player_eight = Player("p8","p8","08/05/2014","gender","8")

players_list = [player_one,player_two,player_three,player_four,player_five,player_six,player_seven,player_eight]

db_test = Database("db_test")
view = View()
creation = ItemCreation(db_test)
menu = Controller(view, creation)

db_test.player_list_serialization("Player", players_list)
# print_data_base(db_test.get_all("Player"))
#
# print_data_base(db_test.get_all("Match"))
item = db_test.query_2("Match", "player_one", "p6p06", "tournament_id", "t11")
item_two = db_test.query_2("Match", "player_two", "p6p06", "tournament_id", "t11")

partial_item = db_test.search_in_data_base("Match", "p6p06")

print_data_base(item)
print_data_base(item_two)
# tournament = menu.database.search_in_data_base("Tournament", "t22")
# new_tournament = menu.creation.tournament_instance_creation_from_database(tournament)
# creation.create_a_tournament()
# player_list = creation.players_list_round_creation(new_tournament)
# round_one = creation.round_creation_run_function(1, new_tournament)
# new_tournament.tournament_append_round(round_one)
# creation.round_match_list_definition(round_one, player_list)
# matches_list = creation.match_list_generator(new_tournament, round_one)
#
# round_two = creation.round_creation_run_function(2, new_tournament)
# new_tournament.tournament_append_round(round_two)
# creation.round_match_list_definition(round_two, player_list)
# matches_list_two = creation.match_list_generator(new_tournament, round_two)
#
# round_three = creation.round_creation_run_function(3, new_tournament)
# new_tournament.tournament_append_round(round_three)
# creation.round_match_list_definition(round_three, player_list)
# matches_list_three = creation.match_list_generator(new_tournament, round_three)
#
# round_four = creation.round_creation_run_function(4, new_tournament)
# new_tournament.tournament_append_round(round_four)
# creation.round_match_list_definition(round_four, player_list)
# matches_list_four = creation.match_list_generator(new_tournament, round_four)
# #
#
#
#
# print(str(round_two) + "\n")
# print(str(round_three) + "\n")
# print(str(round_four) + "\n")