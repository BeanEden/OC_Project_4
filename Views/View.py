
class View:

    @staticmethod
    def print_main_menu():
        print(
            "===================================\n"
            "MAIN MENU\n"
            "===================================\n"
            " 1 - Start a tournament\n"
            " 2 - Add a player\n"
            " 3 - Update a player\n"
            " 4 - Consult a tournament / player / matches report\n"
            " 5 - Exit program\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    @staticmethod
    def print_update_select():
        print(
            "===================================\n"
            "UPDATE PLAYER SELECT\n"
            "===================================\n"
            "Enter a player id and press enter :\n"
            "Enter exit() to go back :\n")

    @staticmethod
    def print_update_player_menu():
        print(
            "===================================\n"
            "UPDATE PLAYER MENU\n"
            "===================================\n"
            "Choose your field to update : \n"
            " 1 - family_name\n"
            " 2 - first_name\n"
            " 3 - birth_date\n"
            " 4 - gender\n"
            " 5 - rank\n"
            " 6 - Exit to main menu \n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    @staticmethod
    def print_update_field(field, field_detail):
        print("===================================\n"
              "UPDATE PLAYER " + field + " MENU\n"
              "===================================\n"
              "Enter the new " + field_detail + " and press enter :\n")

    @staticmethod
    def print_tournament_menu():
        print(
            "===================================\n"
            "TOURNAMENT MENU\n"
            "===================================\n"
            " 1 - Create a new tournament\n"
            " 2 - Use an already existing tournament\n"
            " 3 - Exit to main menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    @staticmethod
    def print_load_a_tournament():
        print(
            "===================================\n"
            "LOAD A TOURNAMENT\n"
            "===================================\n"
            "Enter a tournament id and press enter :\n"
            "Enter exit() to go back :\n")

    @staticmethod
    def print_consulting_menu():
        print(
            "===================================\n"
            "CONSULTING MENU\n"
            "===================================\n"
            " 1 - Player\n"
            " 2 - Tournament\n"
            " 3 - Round\n"
            " 4 - Match\n"
            " 5 - Exit\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    @staticmethod
    def print_consulting_tournament_menu():
        print("===================================\n"
              "TOURNAMENT CONSULTING MENU\n"
              "===================================\n"
              " 1 - Consult a specific tournament\n"
              " 2 - Whole tournament database\n"
              " 3 - Exit to main menu\n"
              "===================================\n"
              "Enter a choice and press enter :\n")

    @staticmethod
    def print_consulting_item_menu(item):
        print("===================================\n"
              + item.upper() + " CONSULTING MENU\n"
              "===================================\n"
              " 1 - Consult a specific " + item + "\n"
              " 2 - Consult a specific tournament " + item + " database\n"
              " 3 - Whole " + item + " database\n"
              " 4 - Exit to main menu\n"
              "===================================\n"
              "Enter a choice and press enter :\n")

    @staticmethod
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

    @staticmethod
    def print_round_menu(round_count):
        print("===================================\n"
              "ROUND " + str(round_count) + " MENU\n"
              "===================================\n"
              " 1 - See detailed matches list\n"
              " 2 - Enter results\n"
              " 3 - Consult tournament previous rounds\n"
              " 4 - Update a player\n"
              " 5 - Exit to tournament menu\n"
              "===================================\n"
              "Enter a choice and press enter :\n")

    @staticmethod
    def print_select_a_match_for_result(round_count, matches_list):
        print(
            "===================================\n"
            "ROUND " + str(round_count) + " RESULTS\n"
            "===================================\n"
            " 1 - " + str(matches_list[0].opponents) + " - "
            + str(matches_list[0].result) + "\n"
            " 2 - " + str(matches_list[1].opponents) + " - "
            + str(matches_list[1].result) + "\n"
            " 3 - " + str(matches_list[2].opponents) + " - "
            + str(matches_list[2].result) + "\n"
            " 4 - " + str(matches_list[3].opponents) + " - "
            + str(matches_list[3].result) + "\n"
            " 5 - Exit to round_menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    @staticmethod
    def print_round_complete(round_played, matches_list):
        if str(round_played.end_time) == "unfinished":
            status = " - ONGOING"
        else:
            status = " - COMPLETE"
        print(
            "===================================\n"
            "ROUND " + str(round_played.count) + status + "\n"
            "===================================\n"
            + str(matches_list[0]) + "\n"
            + str(matches_list[1]) + "\n"
            + str(matches_list[2]) + "\n"
            + str(matches_list[3]) + "\n"
            "Start time : " + str(round_played.start_time) + "\n"
            "End time : " + str(round_played.end_time) + "\n"
            "===================================\n"
            "Press a key to continue")
        input()

    @staticmethod
    def print_enter_match_result(match):
        print(
            "===================================\n"
            + match.name + "\n"
            "===================================")
        if match.result != "result not defined yet":
            print(
                "!!!! Result already defined previously !!!! \n"
                "Previous result selected : " + str(match.result) + "\n"
                "Selecting a new result will overwrite the previous one")
        print(
            "Enter results :\n"
            "   1 - " + match.player_one.name + " wins \n"
            "   2 - " + match.player_two.name + " wins \n"
            "   3 - Match Nul\n"
            "   4 - Exit to match_select\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    @staticmethod
    def print_match_list(matches_list, round_count):
        print(
            "===================================\n"
            "ROUND " + str(round_count) + " MATCHES\n"
            "===================================\n"
            "Match name - player : name - id - rank - score - match result\n"
            " 1 - " + str(matches_list[0]) + "\n"
            " 2 - " + str(matches_list[1]) + "\n"
            " 3 - " + str(matches_list[2]) + "\n"
            " 4 - " + str(matches_list[3]) + "\n"
            "===================================\n"
            "Press a key to go back to round menu\n")
        input()

    @staticmethod
    def print_player_list(player_list):
        print(
            "===================================\n"
            "PLAYER LIST\n"
            "===================================\n"
            "Player_name - id - rank - score")
        for i in player_list:
            print(i)
        print("===================================\n"
              "Press a key to go back to round menu\n")
        input()

    @staticmethod
    def print_tournament_over_menu(tournament_played):
        print(
            "===================================\n"
            "TOURNAMENT " + tournament_played.name + " OVER\n"
            "===================================\n"
            "1 - See player list\n"
            "2 - See round list\n"
            "3 - See match list\n"
            "4 - See tournament details\n"
            "5 - Update a player\n"
            "6 - Go back to main menu\n"
            "===================================\n"
            "Enter an available choice and press enter :\n")

    @staticmethod
    def print_player_list_order_select():
        print(
            "===================================\n"
            "PLAYERS LIST ORDER CHOICE\n"
            "===================================\n"
            "1 - Alphabetical order player list (on family_name)\n"
            "2 - Rank order\n"
            "3 - Score order\n"
            "4 - Go back to previous menu\n"
            "===================================\n"
            "Enter an available choice and press enter :\n")

    @staticmethod
    def print_database_order_select():
        print(
            "===================================\n"
            "PLAYERS LIST ORDER CHOICE\n"
            "===================================\n"
            "1 - Alphabetical order player list (on family_name)\n"
            "2 - Rank order\n"
            "3 - Go back to previous menu\n"
            "===================================\n"
            "Enter an available choice and press enter :\n")

    @staticmethod
    def print_player_list_by_order(players_list, order_choice):
        print(
            "===================================\n"
            "PLAYERS LIST " + order_choice + "\n"
            "===================================")
        for player in players_list:
            print(player)
        print(
            "===================================\n"
            "Press a key to go back to tournament consulting menu\n")
        input()

    @staticmethod
    def print_tournament_list_database(tournament_list):
        print(
            "===================================\n"
            "TOURNAMENT LIST\n"
            "===================================\n")
        print("Player_name - id - rank - score")
        for tournament in tournament_list:
            print(tournament)
        print("===================================\n"
              "Press a key to go back to round menu\n")
        input()

    @staticmethod
    def print_match_list_database(match_list):
        print(
            "===================================\n"
            "MATCH LIST\n"
            "===================================\n")
        print("Player_name - id - rank - score")
        for match in match_list:
            print(match)
        print("===================================\n"
              "Press a key to go back to round menu\n")
        input()

    @staticmethod
    def print_round_list_database(round_list):
        print(
            "===================================\n"
            "ROUND LIST\n"
            "===================================\n")
        print("Player_name - id - rank - score")
        for round_item in round_list:
            print(round_item)
        print("===================================\n"
              "Press a key to go back to round menu\n")
        input()

    @staticmethod
    def print_load_specific_item(item):
        print("===================================\n"
              + item.upper() + " LOAD\n"
              "===================================\n"
              "Enter " + item + " id and press enter :\n"
              "Enter exit() to go back :\n")

    @staticmethod
    def print_tournament_info(tournament):
        for key, value in tournament.items():
            print(str(key) + " : " + str(value))

    @staticmethod
    def print_data_base(database):
        for i in database:
            print(i)

    @staticmethod
    def print_sorted_database(instance_list):
        for i in instance_list:
            print(i.serialized_form)
