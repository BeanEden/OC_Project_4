from Models.View import *
from Models.creation import *
from operator import *


def print_data_base(data_base):
    for item in data_base:
        print(item)
# clear_all_database(db_tournament)
# clear_all_database(db_matches)
# clear_all_database(db_rounds)


print_data_base(db_tournament.get_all())
print()
print_data_base(db_rounds.get_all())
print()
print_data_base(db_matches.get_all())
print()
print_data_base(db_players.get_all())


def main_menu():
    print_main_menu()
    user_input = 0
    while user_input != 5:
        try:
            user_input = int(input())
        except ValueError:
            main_menu()
        if user_input == 1:
            tournament_menu()
        elif user_input == 2:
            add_a_player()
            main_menu()
        elif user_input == 3:
            update_player_select_menu()
        elif user_input == 4:
            consulting_menu()


def tournament_menu():
    print_tournament_menu()
    user_input_tournament_menu = 0
    while user_input_tournament_menu != 3:
        try:
            user_input_tournament_menu = int(input())
        except ValueError:
            tournament_menu()
        if user_input_tournament_menu == 1:
            tournament_created_played = create_a_tournament()
            tournament_round_start_menu(tournament_created_played, 1)
        elif user_input_tournament_menu == 2:
            load_a_tournament_menu()
    main_menu()


def load_a_tournament_menu():
    print_load_a_tournament()
    tournament = "item not found"
    while tournament == "item not found":
        user_input_load_tournament_menu = input()
        tournament = db_tournament.search_player_in_data_base(user_input_load_tournament_menu)
    new_tournament = tournament_instance_creation_from_database(tournament)
    last_round = new_tournament.tournament_last_round()
    round_count = last_round["round_name"]
    round_count = round_count[-1]
    tournament_round_start_menu(new_tournament, round_count)


def consulting_menu():
    print_consulting_menu()
    user_input_consulting_menu = 0
    while user_input_consulting_menu != 4:
        user_input_consulting_menu = int(input())
        if user_input_consulting_menu == 1:
            consulting_specific_menu("Player", db_players)
        elif user_input_consulting_menu == 2:
            consulting_tournament_menu()
        elif user_input_consulting_menu == 3:
            consulting_specific_menu("Round", db_rounds)
        elif user_input_consulting_menu == 4:
            consulting_specific_menu("Match", db_matches)
    main_menu()


def consulting_tournament_menu():
    print_consulting_tournament_menu()
    user_input_consulting_tournament_menu = 0
    while user_input_consulting_tournament_menu != 3:
        user_input_consulting_tournament_menu = int(input())
        if user_input_consulting_tournament_menu == 1:
            specific_tournament_load()
        elif user_input_consulting_tournament_menu == 2:
            print_data_base(db_tournament)
            print("Press a key to go back to round menu\n")
            input()
            consulting_menu()
    consulting_menu()


def specific_tournament_load():
    print_load_a_tournament()
    tournament = "item not found"
    while tournament == "item not found":
        user_input_load_tournament_menu = input()
        tournament = db_tournament.search_player_in_data_base(user_input_load_tournament_menu)
    print(tournament)
    print("Press a key to go back to round menu\n")
    input()
    consulting_menu()


def consulting_specific_menu(item, database):
    print_consulting_item_menu(item)
    user_input_consulting_player_menu = 0
    while user_input_consulting_player_menu != 4:
        user_input_consulting_player_menu = int(input())
        if user_input_consulting_player_menu == 1:
            specific_item_load(item, database)
        elif user_input_consulting_player_menu == 2:
            if item == "Player":
                specific_tournament_players_load()
            else:
                specific_tournament_item_load(database)
        elif user_input_consulting_player_menu == 3:
            print_data_base(database)
            print("Press a key to go back to round menu\n")
            input()
            consulting_menu()

    consulting_menu()


def specific_item_load(item, database):
    print_load_specific_item(item)
    item_searched = "item not found"
    while item_searched == "item not found":
        user_input_load_item = input()
        specific_item = database.search_player_in_data_base(user_input_load_item)
        print(specific_item)
        print("Press a key to go back to round menu\n")
        input()
        consulting_menu()


def specific_tournament_item_load(database):
    print_load_a_tournament()
    query = Query()
    tournament = "item not found"
    while tournament == "item not found":
        user_input_load_tournament_menu = input()
        item = database.search(query.tournament_id == str(user_input_load_tournament_menu))
        print_data_base(item)
        print("Press a key to go back to round menu\n")
        input()
        consulting_menu()


def specific_tournament_players_load():
    print_load_a_tournament()
    tournament = "item not found"
    while tournament == "item not found":
        user_input_load_tournament_menu = input()
        tournament = db_tournament.search_player_in_data_base(user_input_load_tournament_menu)
        tournament_players_list = tournament["tournament_player_dictionary"]
        for item in tournament_players_list.values():
            print(db_players.search_player_in_data_base(item))
    print("Press a key to go back to round menu\n")
    input()
    consulting_menu()


def tournament_round_start_menu(tournament_played, round_count_number):
    while int(round_count_number) <= int(tournament_played.turn_number):
        db_tournament.database_item_insertion(tournament_played.serialized_form)
        print_tournament_round_start_menu(round_count_number)
        user_input_tournament_round_start_menu = 0
        player_list = players_list_round_creation(tournament_played)
        while user_input_tournament_round_start_menu != 5:
            try:
                user_input_tournament_round_start_menu = int(input())
            except ValueError:
                tournament_round_start_menu(tournament_played, round_count_number)
            if user_input_tournament_round_start_menu == 1:
                if tournament_played.tournament_last_round() is None:
                    round_one = round_creation_run_function(round_count_number, tournament_played)
                    tournament_played.tournament_append_round(round_one)
                    round_match_list_definition(round_one, player_list)
                    round_menu(round_one, tournament_played)
                else:
                    last_round = tournament_played.tournament_last_round()
                    if last_round["end_time"] != "unfinished":
                        new_round = round_creation_run_function(round_count_number, tournament_played)
                        tournament_played.tournament_append_round(new_round)
                        player_list = player_list_score_generator(tournament_played)
                        round_match_list_definition(new_round, player_list)
                        round_menu(new_round, tournament_played)
                    else:
                        continue_round = round_instance_creation_from_data_base(last_round, tournament_played)
                        round_menu(continue_round, tournament_played)
            elif user_input_tournament_round_start_menu == 2:
                if round_count_number == 0:
                    print_player_list(player_list)
                    input()
                    tournament_round_start_menu(tournament_played, round_count_number)
                else:
                    player_list = player_list_score_generator(tournament_played)
                    player_list = sorted(player_list, key=attrgetter('score'), reverse=True)
                    print_player_list(player_list)
                    input()
                    tournament_round_start_menu(tournament_played, round_count_number)
            elif user_input_tournament_round_start_menu == 3:
                print(tournament_played)
                tournament_round_start_menu(tournament_played, round_count_number)
            elif user_input_tournament_round_start_menu == 4:
                print(tournament_played)
                tournament_round_start_menu(tournament_played, round_count_number)
        main_menu()
    db_tournament.database_item_insertion(tournament_played.serialized_form)
    tournament_over_menu(tournament_played)


def round_menu(round_played, tournament_played):
    round_count_round_menu = round_played.count
    print(round_played.matches_list)
    matches_list = match_list_generator(tournament_played, round_played)
    print(matches_list)
    print_round_menu(round_count_round_menu)
    user_input_round_menu = 0
    round_status = round_played.round_check(matches_list)
    next_round_count = int(round_count_round_menu)+1
    if round_status == "complete":
        print("!! All the round matches results are selected !! \n"
              "Exit to tournament menu to continue to round " + str(next_round_count))
    else:
        pass
    while user_input_round_menu != 5:
        try:
            user_input_round_menu = int(input())
        except ValueError:
            round_menu(round_played, tournament_played)
        if user_input_round_menu == 1:
            print_match_list(matches_list, round_count_round_menu)
            input()
            round_menu(round_played, tournament_played)
        elif user_input_round_menu == 2:
            select_a_match_for_result(round_played, tournament_played)
            round_menu(round_played, tournament_played)
        elif user_input_round_menu == 3:
            print_all_round_complete(tournament_played)
            input()
            round_menu(round_played, tournament_played)
        elif user_input_round_menu == 4:
            print("function not defined yet")
    if round_played.status == "complete":
        db_rounds.database_item_insertion(round_played.serialized_form)
        print_round_complete(round_count_round_menu, matches_list)
        input()
        tournament_round_start_menu(tournament_played, next_round_count)
    else:
        print("Not all matches results have been selected\n"
              "Round " + round_count_round_menu + " continues\n")
        db_rounds.database_item_insertion(round_played.serialized_form)
        tournament_round_start_menu(tournament_played, round_count_round_menu)


def select_a_match_for_result(round_played, tournament):
    round_count = round_played.count
    matches_list = match_list_generator(tournament, round_played)
    print_select_a_match_for_result(round_count, matches_list)
    user_input_select_a_match_for_result = 0
    while user_input_select_a_match_for_result != 5:
        try:
            user_input_select_a_match_for_result = int(input())
        except ValueError:
            select_a_match_for_result(round_played, tournament)
        if user_input_select_a_match_for_result == 1:
            enter_match_result(matches_list[0], round_played, tournament)
        elif user_input_select_a_match_for_result == 2:
            enter_match_result(matches_list[1], round_played, tournament)
        elif user_input_select_a_match_for_result == 3:
            enter_match_result(matches_list[2], round_played, tournament)
        elif user_input_select_a_match_for_result == 4:
            enter_match_result(matches_list[3], round_played, tournament)
    db_matches.player_list_serialization(matches_list)
    round_menu(round_played, tournament)


def enter_match_result(match, round_played, tournament):
    print_enter_match_result(match)
    user_input_enter_match_result = 0
    while user_input_enter_match_result != 4:
        try:
            user_input_enter_match_result = int(input())
        except ValueError:
            enter_match_result(match, round_played, tournament)
        if user_input_enter_match_result == 1:
            match = Match(match.name, match.player_one, match.player_two, round_played, 1)
            db_matches.database_item_insertion(match.serialized_form)
            user_input_enter_match_result = 4
        elif user_input_enter_match_result == 2:
            match = Match(match.name, match.player_one, match.player_two, round_played, 2)
            db_matches.database_item_insertion(match.serialized_form)
            user_input_enter_match_result = 4
        elif user_input_enter_match_result == 3:
            match = Match(match.name, match.player_one, match.player_two, round_played, 3)
            db_matches.database_item_insertion(match.serialized_form)
            user_input_enter_match_result = 4
    print_data_base(db_matches)
    select_a_match_for_result(round_played, tournament)


def tournament_over_menu(tournament_played):
    print_tournament_over_menu(tournament_played)
    user_input_tournament_over_menu = 0
    while user_input_tournament_over_menu != 6:
        try:
            user_input_tournament_over_menu = int(input())
        except ValueError:
            tournament_over_menu(tournament_played)
        if user_input_tournament_over_menu == 1:
            player_list_argument = tournament_played.player_list_tournament
            previous_tournament_argument = tournament_over_menu(tournament_played)
            player_list_order_select_menu(player_list_argument, previous_tournament_argument)
        elif user_input_tournament_over_menu == 2:
            print_all_round_complete(tournament_played)
        elif user_input_tournament_over_menu == 3:
            print_all_round_complete(tournament_played)
        elif user_input_tournament_over_menu == 4:
            print(tournament_played.serialized_form)
        elif user_input_tournament_over_menu == 5:
            print("Executing menu item 3")

    main_menu()


def player_list_tournament_rank(tournament_players_list):
    player_rank_order = sorted(tournament_players_list, key=attrgetter('rank'), reverse=True)
    return player_rank_order


def player_list_tournament_alphabetical(tournament_players_list):
    player_alphabetical_order = sorted(tournament_players_list, key=attrgetter('name'), reverse=False)
    return player_alphabetical_order


def player_list_order_select_menu(player_list, previous_select_menu):
    print_player_list_order_select()
    user_input_player_list_order_select = 0
    while user_input_player_list_order_select != 4:
        user_input_player_list_order_select = int(input())
        if user_input_player_list_order_select == 1:
            player_list_ordered = player_list_tournament_alphabetical(player_list)
            print_player_list_by_order(player_list_ordered, "ALPHABETICAL ORDER")
        elif user_input_player_list_order_select == 2:
            player_list_ordered = player_list_tournament_rank(player_list)
            print_player_list_by_order(player_list_ordered, "RANK ORDER")
    previous_select_menu


def update_player_select_menu():
    print_update_select()
    player = "item not found"
    while player == "item not found":
        user_input_player_id_key = input()
        if user_input_player_id_key == "exit()":
            main_menu()
        else:
            player = db_players.search_player_in_data_base(user_input_player_id_key)
    player_update_field_menu(player)


def player_update_field_menu(player_id):
    print_update_player_menu()
    user_input = 0
    while user_input != 6:
        user_input = int(input())
        if user_input == 1:
            player_field_update_screen("family_name", player_id, "family_name")
        elif user_input == 2:
            player_field_update_screen("first_name", player_id, "first_name")
        elif user_input == 3:
            player_field_update_screen("birth_date", player_id, "birth_date (DD/MM/YYYY)")
        elif user_input == 4:
            player_field_update_screen("gender", player_id, "gender (F/H)")
        elif user_input == 5:
            player_field_update_screen("rank", player_id, "rank (positive number)")
    main_menu()


def player_field_update_screen(field, player_id, field_detail):
    print_update_field(field, field_detail)
    user_input = str(input())
    db_players.update_player_field(player_id, field, user_input)
    print(str(player_id) + " " + field + " updated to " + user_input + "\n"
          "Press a key to continue...")
    input()
    player_update_field_menu(player_id)


main_menu()
