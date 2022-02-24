import datetime
from Models.matches import Match


class Controller:

    def __init__(self, view, creation):
        self.view = view
        self.creation = creation
        self.database = creation.database

    def main_menu(self):
        self.view.print_main_menu()
        user_input = 0
        while user_input != 5:
            try:
                user_input = int(input())
            except ValueError:
                self.main_menu()
            if user_input == 1:
                self.tournament_menu()
            elif user_input == 2:
                self.creation.add_a_player()
                self.main_menu()
            elif user_input == 3:
                self.update_player_select_menu()
            elif user_input == 4:
                self.consulting_menu()
        pass

    def tournament_menu(self):
        self.view.print_tournament_menu()
        user_input_tournament_menu = 0
        while user_input_tournament_menu != 3:
            try:
                user_input_tournament_menu = int(input())
            except ValueError:
                self.tournament_menu()
            if user_input_tournament_menu == 1:
                tournament_created_played = self.creation.create_a_tournament()
                self.tournament_round_start_menu(tournament_created_played, 1)
            elif user_input_tournament_menu == 2:
                self.load_a_tournament_menu()
        self.main_menu()

    def load_a_tournament_menu(self):
        self.view.print_load_a_tournament()
        tournament = "item not found"
        while tournament == "item not found":
            user_input_load_tournament_menu = input()
            tournament = self.database.search_in_data_base("Tournament", user_input_load_tournament_menu)
        self.view.print_tournament_info(tournament)
        new_tournament = self.creation.tournament_instance_creation_from_database(tournament)
        round_count = self.round_deciding_menu(new_tournament)
        if round_count <= new_tournament.turn_number:
            self.tournament_round_start_menu(new_tournament, round_count)
        else:
            self.tournament_over_menu(new_tournament)

    def round_deciding_menu(self, new_tournament):
        if len(new_tournament.rounds_list) > 0:
            last_round = new_tournament.rounds_list[-1]
            previous_round = self.database.search_in_data_base("Round", last_round)
            if previous_round["end_time"] != "unfinished":
                round_count = int(last_round[1]) + 1
            else:
                round_count = int(last_round[1])
        else:
            round_count = 1
        return round_count

    def consulting_menu(self):
        self.view.print_consulting_menu()
        user_input_consulting_menu = 0
        while user_input_consulting_menu != 5:
            try:
                user_input_consulting_menu = int(input())
            except ValueError:
                self.consulting_menu()
            if user_input_consulting_menu == 1:
                self.consulting_specific_menu("Player")
            elif user_input_consulting_menu == 2:
                self.consulting_tournament_menu()
            elif user_input_consulting_menu == 3:
                self.consulting_specific_menu("Round")
            elif user_input_consulting_menu == 4:
                self.consulting_specific_menu("Match")
        self.main_menu()

    def consulting_tournament_menu(self):
        self.view.print_consulting_tournament_menu()
        user_input_consulting_tournament_menu = 0
        while user_input_consulting_tournament_menu != 3:
            try:
                user_input_consulting_tournament_menu = int(input())
            except ValueError:
                self.consulting_tournament_menu()
            if user_input_consulting_tournament_menu == 1:
                self.specific_tournament_load()
            elif user_input_consulting_tournament_menu == 2:
                self.view.print_data_base(self.database.get_all("Tournament"))
                print("Press a key to go back to round menu\n")
                input()
                self.consulting_menu()
        self.consulting_menu()

    def specific_tournament_load(self):
        self.view.print_load_a_tournament()
        tournament = "item not found"
        while tournament == "item not found":
            user_input_load_tournament_menu = input()
            tournament = self.database.search_in_data_base("Tournament", user_input_load_tournament_menu)
        tournament_instance = self.creation.tournament_instance_creation_from_database(tournament)
        self.view.print_tournament_info(tournament)
        self.tournament_over_menu(tournament_instance)

    def consulting_specific_menu(self, item):
        self.view.print_consulting_item_menu(item)
        user_input_consulting_player_menu = 0
        while user_input_consulting_player_menu != 4:
            try:
                user_input_consulting_player_menu = int(input())
            except ValueError:
                self.consulting_specific_menu(item)
            if user_input_consulting_player_menu == 1:
                self.specific_item_load(item)
            elif user_input_consulting_player_menu == 2:
                if item == "Player":
                    self.specific_tournament_players_load()
                else:
                    self.specific_tournament_item_load(item)
            elif user_input_consulting_player_menu == 3:
                if item == "Player":
                    self.player_database_select_menu(item)
                else:
                    self.view.print_data_base(self.database.get_all(item))
                    print("Press a key to go back to round menu\n")
                    input()
                    self.consulting_menu()
        self.consulting_menu()

    def player_database_select_menu(self, item):
        player_list = self.database.get_all(item)
        player_instance_list = []
        for i in player_list:
            player_instance_list.append(self.creation.player_instance_creation_from_data_base(i))
        self.view.print_database_order_select()
        user_input_player_list_order_select = 0
        while user_input_player_list_order_select != 3:
            try:
                user_input_player_list_order_select = int(input())
            except ValueError:
                self.player_database_select_menu(item)
            if user_input_player_list_order_select == 1:
                choice = self.creation.boolean_choice_menu()
                player_list_ordered = self.creation.player_list_tournament_alphabetical(player_instance_list, choice)
                self.view.print_player_list_by_order(player_list_ordered, "ALPHABETICAL ORDER")
                self.view.print_sorted_database(player_list_ordered)
                input()
                self.consulting_specific_menu(item)
            elif user_input_player_list_order_select == 2:
                choice = self.creation.boolean_choice_menu()
                player_list_ordered = self.creation.player_list_tournament_rank(player_instance_list, choice)
                self.view.print_sorted_database(player_list_ordered, "RANK ORDER")
                input()
                self.consulting_specific_menu(item)
            self.consulting_specific_menu(item)
        self.consulting_specific_menu(item)

    def specific_item_load(self, item):
        self.view.print_load_specific_item(item)
        item_searched = "item not found"
        while item_searched == "item not found":
            user_input_load_item = input()
            specific_item = self.database.search_in_data_base(item, user_input_load_item)
            self.view.print_tournament_info(specific_item)
            print("Press a key to go back to round menu\n")
            input()
            self.consulting_menu()

    def specific_tournament_item_load(self, item):
        self.view.print_load_a_tournament()
        tournament = "item not found"
        while tournament == "item not found":
            user_input_load_tournament_menu = input()
            item = self.database.search_in_data_base_bis(item, "tournament_id", user_input_load_tournament_menu)
            self.view.print_data_base(item)
            print("Press a key to go back to round menu\n")
            input()
            self.consulting_menu()

    def specific_tournament_players_load(self):
        self.view.print_load_a_tournament()
        tournament = "item not found"
        user_input_load_tournament_menu = ""
        while tournament == "item not found":
            user_input_load_tournament_menu = input()
            tournament = self.database.search_in_data_base("Tournament", user_input_load_tournament_menu)
            tournament_players_list = tournament["tournament_player_dictionary"]
            for item in tournament_players_list.values():
                print(self.database.search_in_data_base("Player", item))
        self.player_list_order_select_menu(user_input_load_tournament_menu)
        self.consulting_menu()

    def tournament_round_start_menu(self, tournament_played, round_count_number):
        while int(round_count_number) <= int(tournament_played.turn_number):
            self.database.database_item_insertion("Tournament", tournament_played.serialized_form)
            self.view.print_tournament_round_start_menu(round_count_number)
            user_input_tournament_round_start_menu = 0
            player_list = self.creation.players_list_round_creation(tournament_played)
            while user_input_tournament_round_start_menu != 5:
                try:
                    user_input_tournament_round_start_menu = int(input())
                except ValueError:
                    self.tournament_round_start_menu(tournament_played, round_count_number)
                if user_input_tournament_round_start_menu == 1:
                    if len(tournament_played.rounds_list) > 0:
                        last_round = tournament_played.rounds_list[-1]
                        last_round = self.database.search_in_data_base("Round", last_round)
                        if last_round["end_time"] != "unfinished":
                            new_round = self.creation.round_create_function(round_count_number, tournament_played)
                            tournament_played.tournament_append_round(new_round)
                            self.database.database_item_insertion("Tournament", tournament_played.serialized_form)
                            player_list = self.creation.player_list_score_and_sorting(tournament_played)
                            self.creation.round_match_list_definition(new_round, player_list, tournament_played)
                            self.round_menu(new_round, tournament_played)
                        else:
                            continue_round = \
                                self.creation.round_instance_creation_from_data_base(last_round, tournament_played)
                            self.round_menu(continue_round, tournament_played)
                    else:
                        round_one = self.creation.round_create_function(round_count_number, tournament_played)
                        tournament_played.tournament_append_round(round_one)
                        self.database.database_item_insertion("Tournament", tournament_played.serialized_form)
                        self.creation.round_match_list_definition(round_one, player_list, tournament_played)
                        self.round_menu(round_one, tournament_played)
                elif user_input_tournament_round_start_menu == 2:
                    if round_count_number == 1:
                        player_list = self.creation.player_list_sorting(player_list)
                        self.view.print_player_list(player_list)
                        self.tournament_round_start_menu(tournament_played, round_count_number)
                    else:
                        player_list = self.creation.player_list_score_and_sorting(tournament_played)
                        self.view.print_player_list(player_list)
                        self.tournament_round_start_menu(tournament_played, round_count_number)
                elif user_input_tournament_round_start_menu == 3:
                    self.view.print_tournament_info(tournament_played.serialized_form)
                    self.tournament_round_start_menu(tournament_played, round_count_number)
                elif user_input_tournament_round_start_menu == 4:
                    self.update_player_select_menu()
            self.main_menu()
        tournament_played.close_tournament()
        self.database.database_item_insertion("Tournament", tournament_played.serialized_form)
        self.tournament_over_menu(tournament_played)

    def round_menu(self, round_played, tournament_played):
        round_count_round_menu = round_played.count
        matches_list = self.creation.match_list_generator(tournament_played, round_played)
        self.view.print_round_menu(round_count_round_menu)
        user_input_round_menu = 0
        round_status = round_played.round_check(matches_list)
        next_round_count = int(round_count_round_menu)+1
        if round_status == 0:
            print("!! All the round matches results are selected !!\n"
                  "Exit to tournament menu to continue to the next step")
        else:
            pass
        while user_input_round_menu != 5:
            try:
                user_input_round_menu = int(input())
            except ValueError:
                self.round_menu(round_played, tournament_played)
            if user_input_round_menu == 1:
                self.view.print_match_list(matches_list, round_count_round_menu)
                self.round_menu(round_played, tournament_played)
            elif user_input_round_menu == 2:
                self.select_a_match_for_result(round_played, tournament_played)
                self.round_menu(round_played, tournament_played)
            elif user_input_round_menu == 3:
                self.print_all_round_complete(tournament_played)
                self.round_menu(round_played, tournament_played)
            elif user_input_round_menu == 4:
                self.update_player_select_menu()
        if round_played.status == 0:
            round_played.end_time = datetime.datetime.now()
            serialized = round_played.serialized_form
            serialized["end_time"] = str(datetime.datetime.now())
            self.database.database_item_insertion("Round", serialized)
            self.creation.player_list_score_generator(tournament_played)
            self.view.print_round_complete(round_played, matches_list)
            self.tournament_round_start_menu(tournament_played, next_round_count)
        else:
            print("Not all matches results have been selected\n"
                  "Round " + round_count_round_menu + " continues\n")
            self.database.database_item_insertion("Round", round_played.serialized_form)
            self.tournament_round_start_menu(tournament_played, round_count_round_menu)

    def select_a_match_for_result(self, round_played, tournament):
        round_count = round_played.count
        matches_list = self.creation.match_list_generator(tournament, round_played)
        self.view.print_select_a_match_for_result(round_count, matches_list)
        user_input_select_a_match_for_result = 0
        while user_input_select_a_match_for_result != 5:
            try:
                user_input_select_a_match_for_result = int(input())
            except ValueError:
                self.select_a_match_for_result(round_played, tournament)
            if user_input_select_a_match_for_result == 1:
                self.enter_match_result(matches_list[0], round_played, tournament)
            elif user_input_select_a_match_for_result == 2:
                self.enter_match_result(matches_list[1], round_played, tournament)
            elif user_input_select_a_match_for_result == 3:
                self.enter_match_result(matches_list[2], round_played, tournament)
            elif user_input_select_a_match_for_result == 4:
                self.enter_match_result(matches_list[3], round_played, tournament)
        self.round_menu(round_played, tournament)

    def enter_match_result(self, match, round_played, tournament):
        self.view.print_enter_match_result(match)
        user_input_enter_match_result = 0
        while user_input_enter_match_result != 4:
            try:
                user_input_enter_match_result = int(input())
            except ValueError:
                self.enter_match_result(match, round_played, tournament)
            if user_input_enter_match_result == 1:
                match = Match(match.name, match.player_one, match.player_two, round_played, 1)
                self.database.database_item_insertion("Match", match.serialized_form)
                user_input_enter_match_result = 4
            elif user_input_enter_match_result == 2:
                match = Match(match.name, match.player_one, match.player_two, round_played, 2)
                self.database.database_item_insertion("Match", match.serialized_form)
                user_input_enter_match_result = 4
            elif user_input_enter_match_result == 3:
                match = Match(match.name, match.player_one, match.player_two, round_played, 3)
                self.database.database_item_insertion("Match", match.serialized_form)
                user_input_enter_match_result = 4
        self.select_a_match_for_result(round_played, tournament)

    def tournament_over_menu(self, tournament_played):
        self.view.print_tournament_over_menu(tournament_played)
        user_input_tournament_over_menu = 0
        while user_input_tournament_over_menu != 6:
            try:
                user_input_tournament_over_menu = int(input())
            except ValueError:
                self.tournament_over_menu(tournament_played)
            if user_input_tournament_over_menu == 1:
                self.player_list_order_select_menu(tournament_played.id)
            elif user_input_tournament_over_menu == 2:
                self.print_all_round_complete(tournament_played)
            elif user_input_tournament_over_menu == 3:
                self.print_all_round_complete(tournament_played)
            elif user_input_tournament_over_menu == 4:
                self.view.print_tournament_info(tournament_played.serialized_form)
            elif user_input_tournament_over_menu == 5:
                self.update_player_select_menu()
        self.main_menu()

    def player_list_order_select_menu(self, tournament_id):
        tournament = self.database.search_in_data_base("Tournament", tournament_id)
        new_tournament = self.creation.tournament_instance_creation_from_database(tournament)
        player_list = self.creation.player_list_score_generator(new_tournament)
        self.view.print_player_list_order_select()
        user_input_player_list_order_select = 0
        while user_input_player_list_order_select != 4:
            try:
                user_input_player_list_order_select = int(input())
            except ValueError:
                self.player_list_order_select_menu(tournament_id)
            if user_input_player_list_order_select == 1:
                choice = self.creation.boolean_choice_menu()
                player_list_ordered = self.creation.player_list_tournament_alphabetical(player_list, choice)
                self.view.print_player_list_by_order(player_list_ordered, "ALPHABETICAL ORDER")
                self.player_list_order_select_menu(tournament_id)
            elif user_input_player_list_order_select == 2:
                choice = self.creation.boolean_choice_menu()
                player_list_ordered = self.creation.player_list_tournament_rank(player_list, choice)
                self.view.print_player_list_by_order(player_list_ordered, "RANK ORDER")
                self.player_list_order_select_menu(tournament_id)
            elif user_input_player_list_order_select == 3:
                choice = self.creation.boolean_choice_menu()
                player_list_ordered = self.creation.player_list_sorting(player_list, choice)
                self.view.print_player_list_by_order(player_list_ordered, "SCORE ORDER")
                self.player_list_order_select_menu(tournament_id)
            self.tournament_over_menu(new_tournament)

    def update_player_select_menu(self):
        self.view.print_update_select()
        player = "item not found"
        while player == "item not found":
            user_input_player_id_key = input()
            if user_input_player_id_key == "exit()":
                self.main_menu()
            else:
                player = self.database.search_in_data_base("Player", user_input_player_id_key)
        self.player_update_field_menu(player)

    def player_update_field_menu(self, player):
        self.view.print_tournament_info(player)
        self.view.print_update_player_menu()
        user_input = 0
        while user_input != 6:
            try:
                user_input = int(input())
            except ValueError:
                self.player_update_field_menu(player)
            if user_input == 1:
                self.player_field_update_screen("family_name", player, "family_name")
            elif user_input == 2:
                self.player_field_update_screen("first_name", player, "first_name")
            elif user_input == 3:
                self.player_field_update_screen("birth_date", player, "birth_date (DD/MM/YYYY)")
            elif user_input == 4:
                self.player_field_update_screen("gender", player, "gender (F/H)")
            elif user_input == 5:
                self.player_field_update_screen("rank", player, "rank (positive number)")
        self.main_menu()

    def player_field_update_screen(self, field, player, field_detail):
        player_id = player["id_key"]
        self.view.print_update_field(field, field_detail)
        user_input = str(input())
        self.database.update_player_field("Player", player_id, field, user_input)
        print(str(player_id) + " " + field + " updated to " + user_input + "\n"
              "Press a key to continue...")
        input()
        self.player_update_field_menu(player)

    def print_all_round_complete(self, tournament):
        for rounds in tournament.rounds_list:
            previous_round_data = self.database.search_in_data_base("Round", rounds)
            previous_round = self.creation.round_instance_creation_from_data_base(previous_round_data, tournament)
            match_list = self.creation.match_list_generator(tournament, previous_round)
            self.view.print_round_complete(previous_round, match_list)
