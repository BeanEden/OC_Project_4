
class View:

    def print_main_menu(self):
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

    def print_update_select(self):
        print(
            "===================================\n"
            "UPDATE PLAYER SELECT\n"
            "===================================\n"
            "Enter a player id and press enter :\n"
            "Enter exit() to go back :\n")

    def print_update_player_menu(self):
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

    def print_update_field(self, field, field_detail):
        print("===================================\n"
              "UPDATE PLAYER " + field + " MENU\n"
              "===================================\n"
              "Enter the new " + field_detail + " and press enter :\n")

    def print_tournament_menu(self):
        print(
            "===================================\n"
            "TOURNAMENT MENU\n"
            "===================================\n"
            " 1 - Create a new tournament\n"
            " 2 - Use an already existing tournament\n"
            " 3 - Exit to main menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    def print_load_a_tournament(self):
        print(
            "===================================\n"
            "LOAD A TOURNAMENT\n"
            "===================================\n"
            "Enter a tournament id and press enter :\n"
            "Enter exit() to go back :\n")

    def print_consulting_menu(self):
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

    def print_consulting_tournament_menu(self):
        print("===================================\n"
              "TOURNAMENT CONSULTING MENU\n"
              "===================================\n"
              " 1 - Consult a specific tournament\n"
              " 2 - Whole tournament database\n"
              " 3 - Exit to main menu\n"
              "===================================\n"
              "Enter a choice and press enter :\n")

    def print_consulting_item_menu(self, item):
        print("===================================\n"
              + item.upper() + " CONSULTING MENU\n"
              "===================================\n"
              " 1 - Consult a specific " + item + "\n"
              " 2 - Consult a specific tournament " + item + " database\n"                                    
              " 3 - Whole " + item + " database\n"
              " 4 - Exit to main menu\n"
              "===================================\n"
              "Enter a choice and press enter :\n")

    def print_tournament_round_start_menu(self, round_count):
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

    def print_round_menu(self, round_count):
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

    def print_select_a_match_for_result(self, round_count, matches_list):
        print(
            "===================================\n"
            "ROUND " + str(round_count) + " RESULTS\n"
            "===================================\n"
            " 1 - " + str(matches_list[0].opponents) + " - " + str(matches_list[0].result) + "\n"
            " 2 - " + str(matches_list[1].opponents) + " - " + str(matches_list[1].result) + "\n"
            " 3 - " + str(matches_list[2].opponents) + " - " + str(matches_list[2].result) + "\n"
            " 4 - " + str(matches_list[3].opponents) + " - " + str(matches_list[3].result) + "\n"                                     
            " 5 - Exit to round_menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    def print_round_complete(self, round_played, matches_list):
        print(
            "===================================\n"
            "ROUND " + str(round_played.count) + " COMPLETE\n"
            "===================================\n"
            + str(matches_list[0]) + "\n"
            + str(matches_list[1]) + "\n"
            + str(matches_list[2]) + "\n"
            + str(matches_list[3]) + "\n"
            "Start time : " + str(round_played.start_time) + "\n"
            "End time : " + str(round_played.end_time) + "\n"
            "===================================\n"
            "Press a key to continue")

    def print_enter_match_result(self, match):
        print(
            "===================================\n"
            + match.name + "\n"
            "===================================\n")
        if match.result != "result not defined yet":
            print(
                "!!!! Result already defined previously !!!! \n"
                "Previous result selected : " + str(match.result) + "\n"      
                "Selecting a new result will overwrite the previous one\n")

        print(
            "Enter results :\n"
            "   1 - " + match.player_one.name + " wins \n"
            "   2 - " + match.player_two.name + " wins \n"
            "   3 - Match Nul\n"
            "   4 - Exit to match_select\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    def print_match_list(self, matches_list, round_count):
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

    def print_player_list(self, player_list):
        print(
            "===================================\n"
            "PLAYER LIST\n"
            "===================================\n"
            "Player_name - id - rank - score")
        for i in player_list:
            print(i)
        print("===================================\n"
              "Press a key to go back to round menu\n")

    def print_tournament_over_menu(self, tournament_played):
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

    def print_player_list_order_select(self):
        print(
            "===================================\n"
            "PLAYERS LIST ORDER CHOICE\n"
            "===================================\n"
            "1 - Alphabetical order player list (on family_name)\n"
            "2 - Rank order\n"
            "3 - Go back to previous menu\n"
            "===================================\n"
            "Enter an available choice and press enter :\n")

    def print_player_list_by_order(self, players_list, order_choice):
        print(
            "===================================\n"
            "PLAYERS LIST " + order_choice + "\n"
            "===================================\n")
        for player in players_list:
            print(player)
        print(
            "===================================\n"
            "Press a key to go back to tournament consulting menu\n")

    def print_tournament_list_database(self, tournament_list):
        print(
            "===================================\n"
            "TOURNAMENT LIST\n"
            "===================================\n")
        print("Player_name - id - rank - score")
        for tournament in tournament_list:
            print(tournament)
        print("===================================\n"
              "Press a key to go back to round menu\n")

    def print_match_list_database(self, match_list):
        print(
            "===================================\n"
            "MATCH LIST\n"
            "===================================\n")
        print("Player_name - id - rank - score")
        for match in match_list:
            print(match)
        print("===================================\n"
              "Press a key to go back to round menu\n")

    def print_round_list_database(self, round_list):
        print(
            "===================================\n"
            "ROUND LIST\n"
            "===================================\n")
        print("Player_name - id - rank - score")
        for round_item in round_list:
            print(round_item)
        print("===================================\n"
              "Press a key to go back to round menu\n")

    def print_load_specific_item(self, item):
        print("===================================\n"
              + item.upper() + " LOAD\n"
              "===================================\n"
              "Enter " + item + " id and press enter :\n"
              "Enter exit() to go back :\n")

    def print_tournament_info(self, tournament):
        for key, value in tournament.items():
            print(str(key) + " : " + str(value))

    def print_data_base(self, database):
        for i in database:
            print(i)
