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

players_list_id = {}

for i in players_list:
    players_list_id["Player" + str(players_list.index(i)+1)]=i.id


db_test = Database("db_test")
view = View()
creation = ItemCreation(db_test)
menu = Controller(view, creation)

db_test.player_list_serialization("Player", players_list)

# creation.create_a_tournament()
# new_tournament = Tournament("t5","","5","","",players_list_id)
# self.database.database_item_insertion("Tournament", new_tournament.serialized_form)
#
tournament = menu.database.search_in_data_base("Tournament", "t22")
new_tournament = menu.creation.tournament_instance_creation_from_database(tournament)

# score_test = menu.creation.player_score_generator_round(player_eight, new_tournament, "R1 t11")
# print(score_test)

score_test = menu.creation.player_score_generator_round(player_four, new_tournament, "R2 t22")
print(score_test)
#
# # player_list = creation.players_list_round_creation(new_tournament)
# #
# round_one = creation.round_creation_run_function(1, new_tournament)
# creation.round_match_list_definition(round_one, player_list)
# matches_list = creation.match_list_generator(new_tournament, round_one)
# # print(matches_list)
#
# round_two = creation.round_creation_run_function(2, new_tournament)
# creation.round_match_list_definition(round_two, player_list)
# matches_list_two = creation.match_list_generator(new_tournament, round_two)
# # print(matches_list_two)
#
#
# pairs_two = menu.creation.possible_pairs(new_tournament.id, players_list)
# match_up_list = menu.creation.list_comb_recursive(pairs_two)


# round_three = creation.round_creation_run_function(3, new_tournament)
# creation.round_match_list_definition(round_three, player_list)
# matches_list_three = creation.match_list_generator(new_tournament, round_three)
# # print(matches_list_three)
#
# round_four = creation.round_creation_run_function(4, new_tournament)
# creation.round_match_list_definition(round_four, player_list)
# matches_list_four = creation.match_list_generator(new_tournament, round_four)
# print(matches_list_four)

# print_data_base(creation.database.list_match_pairs("t44"))
# print(db_test.get_all("Round"))
# print(matches_list_four)

# score_test = creation.player_list_score_generator(new_tournament)
# score_test = creation.player_list_sorting(score_test, True)

# liste_matches_t44 = db_test.list_query_one("Match", "tournament_id", "t44")
# print(liste_matches_t44)
# print_data_base(score_test)
#
tournament_test_1 = Tournament("tt","","1","","",players_list)
tournament_test_2 = Tournament("tt","","2","","",players_list)

round_one_t1 = creation.round_creation_run_function(1, tournament_test_1)
creation.round_match_list_definition(round_one_t1, players_list, tournament_test_1)
matches_list_t1 = creation.match_list_generator(tournament_test_1, round_one_t1)
match1t1 = Match("Match 1", player_eight, player_four,round_one_t1,1)
match2t1 = Match("Match 2", player_seven, player_three,round_one_t1,1)
match3t1 = Match("Match 3", player_six, player_two,round_one_t1,1)
match4t1 = Match("Match 4", player_five, player_one,round_one_t1,1)


round_one_t2 = creation.round_creation_run_function(1, tournament_test_2)
creation.round_match_list_definition(round_one_t2, players_list, tournament_test_2)
matches_list_t2 = creation.match_list_generator(tournament_test_2, round_one_t2)
match1t2 = Match("Match 1", player_eight, player_four,round_one_t2,1)
match2t2 = Match("Match 2", player_seven, player_three,round_one_t2,1)
match3t2 = Match("Match 3", player_six, player_two,round_one_t2,1)
match4t2 = Match("Match 4", player_five, player_one,round_one_t2,1)


round_two_t1 = creation.round_creation_run_function(2, tournament_test_1)
pairs_t1 = menu.creation.possible_pairs(tournament_test_2.id, players_list)
match_up_list_t1 = menu.creation.list_comb(pairs_t1)
print(match_up_list_t1)

round_two_2 = creation.round_creation_run_function(2, tournament_test_2)
pairs = menu.creation.possible_pairs(tournament_test_2.id, players_list)
match_up_list = menu.creation.list_comb_recursive(pairs)
print(match_up_list)