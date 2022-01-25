# from Models.base import *

def print_main_menu():
    print("===================================\n"
        "MENU\n"
        "===================================\n"
        " 1 - Start a tournament\n"
        " 2 - Add a player\n"
        " 3 - Update a player\n"
        " 4 - Consult a tournament / player / matches report\n"
        " 5 - Exit\n"
        "===================================\n"
        "Enter a choice and press enter :\n")


def print_tournament_menu():
    print("===================================\n"
        "TOURNAMENT MENU\n"
        "===================================\n"
        " 1 - Create a new tournament\n"
        " 2 - Use an already existing tournament\n"
        " 3 - Exit\n"
        "===================================\n"
        "Enter a choice and press enter :\n")


def print_consulting_menu():
    print("===================================\n"
        "CONSULTING MENU\n"
        "===================================\n"
        " 1 - Tournament\n"
        " 2 - Match list\n"
        " 3 - Player\n"
        " 4 - Exit\n"
        "===================================\n"
        "Enter a choice and press enter :\n")


def print_consulting_tournament_menu():
    print("===================================\n"
        "TOURNAMENT CONSULTING MENU\n"
        "===================================\n"
        " 1 - Consult a specific Tournament\n"
        " 2 - Whole tournament database\n"
        " 3 - Go back to consulting choices\n"
        " 4 - Exit to main menu\n"
        "===================================\n"
        "Enter a choice and press enter :\n")



def print_consulting_player_menu():
    print("===================================\n"
        "PLAYER CONSULTING MENU\n"
        "===================================\n"
        " 1 - Consult a specific player\n"
        " 2 - Whole player database\n"
        " 3 - Go back to consulting choices\n"
        " 4 - Exit to main menu\n"
        "===================================\n"
        "Enter a choice and press enter :\n")


def print_consulting_match_menu():
    print("===================================\n"
        "MATCH LIST CONSULTING MENU\n"
        "===================================\n"
        " 1 - Consult a specific Match table\n"
        " 2 - Whole match database\n"
        " 3 - Go back to consulting choices\n"
        " 4 - Exit to main menu\n"
        "===================================\n"
        "Enter a choice and press enter :\n")

def print_tournament_round_start_menu(round_count):
    print("===================================\n"
          "TOURNAMENT MENU - ROUND " + str(round_count) + "\n"
          "===================================\n"
          " 1 - Start round " + str(round_count) + "\n"
          " 2 - See player list\n"
          " 3 - See tournament infos\n"
          " 4 - Update a player infos\n"
          " 5 - Exit to main menu\n"
          "===================================\n"
          "Enter a choice and press enter :\n")

def print_round_menu(round_count):
    print("===================================\n"
        "ROUND " + str(round_count) + " MENU\n"
        "===================================\n")
    # if round_status == "open":
    #     print(" 1 - Generate matches\n")
    # else:
    #     print(" 1 - See matches list")
    print(
    " 1 - See detailed matches list\n"
    " 2 - Enter results\n"
    " 3 - Consult tournament previous rounds\n"
    " 4 - Update a player\n"
    " 5 - Exit to tournament menu\n"
    "===================================\n"
    "Enter a choice and press enter :\n")


def print_select_a_match_for_result(round_count, matchs_list):
    print("===================================\n"
    "ROUND " + str(round_count) + " RESULTS\n"
    "===================================\n"
    " 1 - " + str(matchs_list[0].opponents) + " - " + str(matchs_list[0].result) + "\n"
    " 2 - " + str(matchs_list[1].opponents) + " - " + str(matchs_list[1].result) + "\n"
    " 3 - " + str(matchs_list[2].opponents) + " - " + str(matchs_list[2].result) + "\n"
    " 4 - " + str(matchs_list[3].opponents) + " - " + str(matchs_list[3].result) + "\n"                                     
    " 5 - Exit to round_menu\n"
    "===================================\n"
    "Enter a choice and press enter :\n")

def print_round_complete(round_count, matchs_list, next_round_count):
    print("===================================\n"
        "ROUND " + str(round_count) + " COMPLETE\n"
        "===================================\n"
        + str(matchs_list[0]) + "\n"
        + str(matchs_list[1]) + "\n"
        + str(matchs_list[2]) + "\n"
        + str(matchs_list[3]) + "\n"
        "===================================\n")


def print_enter_match_result(match):
    print("===================================\n"
        + match.name + "\n"
        "===================================\n")
    if match.result != "result not defined yet":
        print("!!!! Result already defined previously !!!! \n"
        "Previous result selected : " + str(match.result) + "\n"      
        "Selecting a new result will overwrite the previous one\n")

    print("Enter results :\n"
        "   1 - " + match.joueur_1.name + " wins \n"
        "   2 - " + match.joueur_2.name + " wins \n"
        "   3 - Match Nul\n"
        "   4 - Exit to match_select\n"
    "===================================\n"
    "Enter a choice and press enter :\n")


def print_match_list(matchs_list, round_count):
    print("===================================\n"
    "ROUND " + str(round_count) + " MATCHES\n"
    "===================================\n"
    "Match name - player : name - id - rank - score - match result\n"
    " 1 - " + str(matchs_list[0]) + "\n"
    " 2 - " + str(matchs_list[1]) + "\n"
    " 3 - " + str(matchs_list[2]) + "\n"
    " 4 - " + str(matchs_list[3]) + "\n"                                     
    "===================================\n"
    "Press a key to go back to round menu\n")


def print_player_list(player_list) :
    print("===================================\n"
    "PLAYER LIST\n"
    "===================================\n")
    print("Player_name - id - rank - score")
    for players in player_list:
        print(players)
    "===================================\n"

def print_tournament_over_menu(tournament_played):
    print("===================================\n"
    "TOURNAMENT " + tournament_played.name + "OVER\n"
    "===================================\n")
    "1 - See player list"
    "2 - See round list"
    "3 - See match list"
    "4 - See tournament details"
    "5 - Update a player"
    "6 - Go back to main menu"
    "===================================\n"

def print_player_list_order_select():
    print("===================================\n"
    "PLAYERS LIST ORDER CHOICE\n"
    "===================================\n"
    "1 - Alphabetical order player list (on family_name)"
    "2 - Rank order"
    "3 - Go back to previous menu"
    "===================================\n"
    "Enter an available choice and press enter :\n")


def print_player_list_by_order(players_list, order_choice):
    "===================================\n"
    "PLAYERS LIST " + order_choice + "\n"
    "===================================\n"
    for player in players_list:
        print(player)
    "===================================\n"
    "Press a key to go back to tournament consulting menu\n"


# def print_match )
    #
    # @staticmethod
    # def do_1():
    #     print(Doing 1)
    #
    # @staticmethod
    # def do_2():
    #     print(Doing 2)
    #
    # @staticmethod
    # def do_3():
    #     print(Doing 3)
    #
    # @staticmethod
    # def do_4():
    #     print(Doing 4)
    #
    # @staticmethod
    # def do_5():
    #     print(Doing 5)
    #
    # @staticmethod
    # def do_6():
    #     print(Exiting...)