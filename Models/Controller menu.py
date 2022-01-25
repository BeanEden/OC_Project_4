from Models.menu import *
from Models.base import *
from Models.players import add_a_player
from operator import *

def main_menu():
    print_main_menu()
    user_input = 0
    while user_input != 5:
        user_input = int(input())
        if user_input == 1:
            tournament_menu()
        elif user_input == 2:
            add_a_player()
            main_menu()
        elif user_input == 3:
            print("Executing menu item 3")
        elif user_input == 4:
            print_consulting_menu()


def tournament_menu():
    print_tournament_menu()
    user_input_tournament_menu = 0
    while user_input_tournament_menu != 3:
        user_input_tournament_menu = int(input())
        if user_input_tournament_menu == 1:
            tournament_created_played = create_a_tournament()
            tournament_round_start_menu(tournament_created_played,1)
        elif user_input_tournament_menu == 2 :
            print("using an already existing")
    main_menu()


# # def consulting_menu():
# #     print_consulting_menu()
# #     user_input_consulting_menu = 0
# #     while user_input_consulting_menu != 4:
# #         user_input_consulting_menu = int(input())
# #         if user_input_consulting_menu == 1:
# #         consulting_tournament_menu()
# #         elif user_input_consulting_menu == 2:
# #         consulting_player_menu()
# #         elif user_input_consulting_menu == 3:
# #         consulting_match_menu()
# #     main_menu()
#
#
# def consulting_tournament_menu():
#     print_consulting_tournament_menu()
#     user_input_consulting_tournament_menu = 0
#     while user_input_consulting_tournament_menu != 4:
# #         user_input_consulting_tournament_menu = int(input())
# #         if user_input_consulting_tournament_menu == 1:
# #
# #         elif user_input_consulting_tournament_menu == 2:
# #
# #         elif user_input_consulting_tournament_menu == 3:
# #         print_consulting_menu()
# #     main_menu()
#
#
# def consulting_player_menu():
#     print_consulting_player_menu()
#     user_input_consulting_player_menu = 0
#     while user_input_consulting_player_menu != 4:
# #         user_input_consulting_player_menu = int(input())
# #         if user_input_consulting_player_menu == 1:
# #
# #         elif user_input_consulting_player_menu == 2:
# #
# #         elif user_input_consulting_player_menu == 3:
# #         print_consulting_menu()
# #     main_menu()
#
#
# def consulting_match_menu():
#     print_consulting_match_menu()
#     user_input_consulting_match_menu = 0
#     while user_input_consulting_match_menu != 4:
#         user_input_consulting_match_menu = int(input())
#         if user_input_consulting_match_menu == 1:
#
#         elif user_input_consulting_match_menu == 2:
#
#         elif user_input_consulting_match_menu == 3:
#         print_consulting_menu()
#     main_menu()
# while round_count < tourn
def tournament_round_start_menu(tournament_played, round_count_number):

    while int(round_count_number) <= int(tournament_played.turn_number):
        print_tournament_round_start_menu(round_count_number)
        user_input_tournament_round_start_menu = 0
        player_list = tournament_played.player_list_tournament()

        while user_input_tournament_round_start_menu != [1,2,3,4,5]:
            user_input_tournament_round_start_menu = int(input())
            print("Enter an available choice and press enter :\n")
        while user_input_tournament_round_start_menu != 5:
            if user_input_tournament_round_start_menu == 1:
                if tournament_played.tournament_last_round() is None :
                    round_one = round_creation_run_function(player_list,round_count_number)
                    tournament_played.tournament_append_round(round_one)
                    round_one.round_match_list_definition(round_count_number)
                    round_menu(round_one, tournament_played)
                else :
                    last_round = tournament_played.last_round
                    if last_round.status == "open":
                        round_menu(last_round, tournament_played)
                    else :
                        new_round = round_creation_run_function(player_list,round_count_number)
                        tournament_played.tournament_append_round(new_round)
                        new_round.round_match_list_definition(round_count_number)
                        round_menu(new_round, tournament_played)

            elif user_input_tournament_round_start_menu == 2:
                print_player_list(player_list)
                tournament_round_start_menu(tournament_played, round_count_number)
            elif user_input_tournament_round_start_menu == 3:
                print(tournament_played)
                tournament_round_start_menu(tournament_played, round_count_number)
            elif user_input_tournament_round_start_menu == 4:
                print(tournament_played)
                tournament_round_start_menu(tournament_played, round_count_number)
        main_menu()


def round_menu(round_played, tournament_played):
    round_count_round_menu = round_played.count
    matches_list = round_played.matches_list
    print_round_menu(round_count_round_menu)
    user_input_round_menu = 0
    round_played.round_check()
    if round_played.status == "complete":
        print("!! Tous les résultats du round ont été saisis !! \n"
            "exit to tournament menu to start round 2")
    else:
        pass
    while user_input_round_menu != 5:
        user_input_round_menu = int(input())

        if user_input_round_menu == 1:
            print_match_list(matches_list, round_count_round_menu)
            fake_input = str(input())
            round_menu(round_played, tournament_played)
            # round_menu(round_played, tournament_played)
        # elif user_input_round_menu == 1 and round_status != "open" :
        #     print(round_played.matches_list)

        elif user_input_round_menu == 2:
            select_a_match_for_result(round_played, tournament_played)
            round_menu(round_played, tournament_played)

        elif user_input_round_menu == 3:
            print(tournament_played.rounds_list)

        elif user_input_round_menu == 4:
            print("function not defined yet")

    if round_played.status == "complete" :
        next_round_count = str(int(round_count_round_menu) + 1)
        print_round_complete(round_count_round_menu, matches_list,next_round_count)
        tournament_round_start_menu(tournament_played, next_round_count)

    else:
        print("l'ensemble des résultats n'a pas été sélectionné\n"
              " le round 1 continue\n")
        tournament_round_start_menu(tournament_played, round_count_round_menu)




def select_a_match_for_result(round_played,tournament):
    round_count = round_played.count
    matches_list = round_played.matches_list
    print_select_a_match_for_result(round_count, matches_list)
    user_input_select_a_match_for_result = 0
    while user_input_select_a_match_for_result != 5:
        user_input_select_a_match_for_result = int(input())
        if user_input_select_a_match_for_result == 1:
            enter_match_result(matches_list[0],round_played,tournament)
        elif user_input_select_a_match_for_result == 2:
            enter_match_result(matches_list[1],round_played,tournament)
        elif user_input_select_a_match_for_result == 3:
            enter_match_result(matches_list[2], round_played,tournament)
        elif user_input_select_a_match_for_result == 4:
            enter_match_result(matches_list[3], round_played,tournament)
    round_menu(round_played, tournament)

def enter_match_result(match, round_played, tournament):
    print_enter_match_result(match)
    user_input_enter_match_result = 0
    while user_input_enter_match_result != 4:
        user_input_enter_match_result = int(input())
        if user_input_enter_match_result == 1:
            match.score_attribution(1)
            user_input_enter_match_result = 4
        elif user_input_enter_match_result == 2:
            match.score_attribution(2)
            user_input_enter_match_result = 4
        elif user_input_enter_match_result == 3:
            match.score_attribution(3)
            user_input_enter_match_result = 4
    select_a_match_for_result(round_played, tournament)

main_menu()

def tournament_over_menu(tournament_played):
    print_tournament_over_menu(tournament_played)
    user_input_tournament_over_menu = 0
    while user_input_tournament_over_menu != 5:
        user_input_tournament_over_menu = int(input())
        if user_input_tournament_over_menu == 1:
            player_list_argument = tournament_played.player_list_tournament
            previous_tournament_argument = tournament_over_menu(tournament_played)
            player_list_order_select_menu(player_list_argument, previous_tournament_argument)


def player_list_tournament_rank(players_list):
    player_rank_order = sorted(players_list, key=attrgetter('rank'), reverse=True)
    return player_rank_order

def player_list_tournament_alphabetical(players_list):
    player_alphabetical_order = sorted(players_list, key=attrgetter('name'), reverse=False)
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
    back = previous_select_menu