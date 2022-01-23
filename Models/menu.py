# from Models.base import *

def print_main_menu():
    print("===================================\n"
        "MENU\n"
        "===================================\n"
        " 1 - Start a tournament\n"
        " 2 - Add a player\n"
        " 3 - Update a player\n"
        " 4 - Consult a tournament / player / matches report"
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
        " 3 - Go back to consulting choices"
        " 4 - Exit to main menu\n"
        "===================================\n"
        "Enter a choice and press enter :\n")


def print_consulting_player_menu():
    print("===================================\n"
        "PLAYER CONSULTING MENU\n"
        "===================================\n"
        " 1 - Consult a specific player\n"
        " 2 - Whole player database\n"
        " 3 - Go back to consulting choices"
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
          "TOURNAMENT MENU - ROUND" + round_count + "\n"
          "===================================\n"
          " 1 - Start Round " + round_count + "\n"
          " 2 - See player list\n"
          " 3 - See tournament infos\n"
          " 4 - Update a player infos"
          " 5 - Exit to main menu\n"
          "===================================\n"
          "Enter a choice and press enter :\n")

def print_round_menu(round_count, round_status):
    print("===================================\n"
        "ROUND " + round_count + " MENU\n"
        "===================================\n")
    if round_status == "open":
        print(" 1 - Generate matches\n")
    else:
        print(" 1 - See matches list")
    print(
    " 2 - Enter results\n"
    " 3 - Consult tournament previous rounds\n"
    " 4 - Update a player"
    " 5 - Exit tournament (to main menu)\n"
    "===================================\n"
    "Enter a choice and press enter :\n")


def print_select_a_match_for_result(round_count, matchs_list):
    print("===================================\n"
    "ROUND " + round_count + " RESULTS\n"
    "===================================\n"
    " 1 - " + matchs_list[0].opponents + matchs_list[0].result + "\n"
    " 2 - " + matchs_list[1].opponents + matchs_list[1].result + "\n"
    " 3 - " + matchs_list[2].opponents + matchs_list[2].result + "\n"
    " 4 - " + matchs_list[3].opponents + matchs_list[3].result + "\n"                                     
    " 5 - Exit to round_menu\n"
    "===================================\n"
    "Enter a choice and press enter :\n")


def print_enter_match_result(match):
    print("===================================\n"
        + match.name + "\n"
        "===================================\n")
    if match.result != "result not defined yet":
        print("!!!! Result already defined previously !!!! \n"
        "Previous result selected : " + match.result + "\n"      
        "Selecting a new result will overwrite the previous one\n")

    print("Enter results :\n"
        "   1 - " + match.joueur_1.name + " wins \n"
        "   2 - " + match.joueur_2.name + " wins \n"
        "   3 - Match Nul\n"
        "   4 - Exit to match_select\n"
    "===================================\n"
    "Enter a choice and press enter :\n")


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