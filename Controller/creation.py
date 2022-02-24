import datetime
from Models.tournament import Tournament
from Models.round import Round
from Models.players import Player
from Models.matches import Match
from operator import attrgetter


class ItemCreation:

    def __init__(self, database):
        self.database = database

    def create_a_tournament(self):
        input("Creating a new tournament, press a key to continue :\n")
        name = input("Enter the tournament name :\n")
        place = input("Enter tournament place : \n")
        date = input("Enter tournament date (DD/MM/YYYY) : \n")
        time_control = self.time_control_definition()
        description = input("Enter tournament general description:\n")
        player_list = self.player_dictionary_select()
        new_tournament = Tournament(name, place, date, time_control, description, player_list)
        self.database.database_item_insertion("Tournament", new_tournament.serialized_form)
        return new_tournament

    def time_control_definition(self):
        time_control = input("Select time control mode :\n"
                                 "1 - bullet \n"
                                 "2 - blitz \n"
                                 "3 - coup rapide\n")
        if time_control == "1":
            time_control = "bullet"
        elif time_control == "2":
            time_control = "blitz"
        elif time_control == "3":
            time_control = "coup rapide"
        else:
            self.time_control_definition()
        return time_control

    def add_a_player(self):
        """Prompt for adding a player."""
        print("Creating a new player...\n")
        family_name = input("Player's family name : \n")
        first_name = input("Player's first name : \n")
        birth_date = input("Birth date (DD/MM/YYYY): \n")
        gender = input("Genre (F/H): \n")
        rank = input("Ranking (positive number) : \n")
        player = Player(family_name, first_name, birth_date, gender, rank)
        print(player.name + " registered. id = " + player.id)
        serialized_player = player.player_serialization()
        self.database.database_item_insertion("Player", serialized_player)
        return serialized_player

    def player_dictionary_select(self):
        player_count = 0
        player_list_tournament = {}
        while player_count < 8:
            player_count += 1
            player = "item not found"
            while player == "item not found":
                user_input_player_id_key = input(
                    "Enter player " + str(player_count) + " id :\n"
                    "id = firstname + family_name[0] + birth_date[0:1]\n"
                    "example : Mark Zuck born on 09/03/1987 -> id = MarkZ09\n")
                player = self.database.search_in_data_base("Player", user_input_player_id_key)
                # print(player)
            new_player = self.player_instance_creation_from_data_base(player)
            print("Player added to tournament : " + str(new_player) + "\n")
            player_list_tournament["Player " + str(player_count)] = new_player.id
        return player_list_tournament

    def round_create_function(self, round_count_number, tournament_played):
        round_name = "Round " + str(round_count_number)
        print(round_name + " started...")
        start_time = datetime.datetime.now()
        round_one = Round(round_name, tournament_played, start_time)
        tournament_played.tournament_append_round(round_one)
        self.database.database_item_insertion("Round", round_one.serialized_form)
        return round_one

    def players_list_round_creation(self, tournament_played):
        player_list = []
        tournament_player_list = tournament_played.players_list
        for player in tournament_player_list.values():
            new_player = self.database.search_in_data_base("Player", player)
            player_instance = self.player_instance_creation_from_data_base(new_player)
            player_list.append(player_instance)
        return player_list

    @staticmethod
    def player_instance_creation_from_data_base(dict_player):
        family_name = dict_player["family_name"]
        first_name = dict_player["first_name"]
        age = dict_player["birth_date"]
        rank = dict_player["rank"]
        gender = dict_player["gender"]
        new_player = Player(family_name, first_name, age, gender, rank)
        return new_player

    def match_instance_creation_from_data_base(self, dict_match, round_of_the_match, tournament):
        name = dict_match["match_name"]
        p_one_id = dict_match["player_one"]
        player_one_creation = self.database.search_in_data_base("Player", p_one_id)
        player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
        self.player_score_generator_round(player_one_instance, tournament, round_of_the_match.id)
        p_two_id = dict_match["player_two"]
        player_two_creation = self.database.search_in_data_base("Player", p_two_id)
        player_two_instance = self.player_instance_creation_from_data_base(player_two_creation)
        self.player_score_generator_round(player_two_instance, tournament, round_of_the_match.id)
        score = dict_match["result"]
        new_match = Match(name, player_one_instance, player_two_instance, round_of_the_match, score)
        return new_match

    @staticmethod
    def round_instance_creation_from_data_base(dict_round, tournament):
        name = dict_round["round_name"]
        start_time = dict_round["start_time"]
        end_time = dict_round["end_time"]
        new_round = Round(name, tournament, start_time, end_time)
        return new_round

    @staticmethod
    def tournament_instance_creation_from_database(dict_tournament):
        name = dict_tournament["tournament_name"]
        place = dict_tournament["tournament_place"]
        date = dict_tournament["tournament_date"]
        time_control = dict_tournament["tournament_time_control"]
        description = dict_tournament["tournament_description"]
        rounds_list = dict_tournament["tournament_rounds"]
        player_list = dict_tournament["tournament_player_dictionary"]
        status = dict_tournament["tournament_status"]
        new_tournament = Tournament(name, place, date, time_control, description, player_list, rounds_list, status)
        return new_tournament

    def match_list_generator(self, tournament, round_played):
        match_list = []
        item = self.database.query_2("Match", "tournament_id", tournament.id, "round_id", round_played.id)
        # print(item)
        for match in item:
            match = self.match_instance_creation_from_data_base(match, round_played, tournament)
            match_list.append(match)
        match_list = sorted(match_list, key=attrgetter('name'), reverse=False)
        return match_list

    def player_score_generator_round(self, player, tournament, id_round_of_the_match):
        item_full = []
        item_two_full = []
        round_list = tournament.rounds_list
        check_list = round_list.index(id_round_of_the_match)+1
        for round_number in range(0, check_list):
            round_id = round_list[round_number]
            try:
                item = self.database.query_2("Match", "round_id", round_id, "player_one", str(player.id))
                item_full.append(item[-1])
            except IndexError:
                pass
            try:
                item_two = self.database.query_2("Match", "round_id", round_id, "player_two", str(player.id))
                item_two_full.append(item_two[-1])
            except IndexError:
                pass
        for match in item_full:
            if match["result"] == 1:
                player.score += 1
            elif match["result"] == 3:
                player.score += 0.5
        for match in item_two_full:
            if match["result"] == 2:
                player.score += 1
            elif match["result"] == 3:
                player.score += 0.5
        return player.score

    def player_list_score_generator(self, tournament):
        player_list = []
        tournament_player_list = tournament.players_list
        last_round = tournament.rounds_list[-1]
        for player in tournament_player_list.values():
            player_one_creation = self.database.search_in_data_base("Player", player)
            player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
            self.player_score_generator_round(player_one_instance, tournament, last_round)
            player_list.append(player_one_instance)
        return player_list

    def opponents_list_construction(self, player_id, tournament_id):
        item = self.database.query_2("Match", "player_one", player_id, "tournament_id", tournament_id)
        item_two = self.database.query_2("Match", "player_two", player_id, "tournament_id", tournament_id)
        opponents_list = []
        for match in item:
            opponents_list.append(match["player_two"])
        for match in item_two:
            opponents_list.append(match["player_one"])
        return opponents_list

    def round_match_list_definition(self, round_played, player_list, tournament_played):
        if int(round_played.count) == 1:
            round_played.matches_list = self.round_one_method(round_played, player_list)
        else:
            round_played.matches_list = self.secondary_rounds_method(round_played, tournament_played)
        return round_played.matches_list

    def possible_opponents_list(self, player, ranked_list, round_played):
        player_opponents_list = \
            self.opponents_list_construction(player.id, round_played.tournament_name)
        list_difference = []
        for item in ranked_list:
            if item not in player_opponents_list:
                list_difference.append(item)
        return list_difference

    @staticmethod
    def player_list_sorting(player_list_instances, boolean_order=True):
        player_list_instances = sorted(player_list_instances, key=attrgetter('rank'), reverse=boolean_order)
        player_list_instances = sorted(player_list_instances, key=attrgetter('score'), reverse=boolean_order)
        return player_list_instances

    @staticmethod
    def player_list_tournament_rank(tournament_players_list, boolean_choice=True):
        player_rank_order = sorted(tournament_players_list, key=attrgetter('rank'), reverse=boolean_choice)
        return player_rank_order

    @staticmethod
    def player_list_tournament_alphabetical(tournament_players_list, boolean_choice=False):
        player_alphabetical_order = sorted(tournament_players_list, key=attrgetter('name'), reverse=boolean_choice)
        return player_alphabetical_order

    def secondary_rounds_method(self, round_played, tournament_played):
        player_list = self.player_list_score_generator(tournament_played)
        round_ranking = self.player_list_sorting(player_list, False)
        match_list = []
        match_count = 0
        players_list = []
        for i in round_ranking:
            players_list.append(i.id)
        pairs = self.possible_pairs(round_played.tournament_name, players_list)
        match_up_list = self.list_comb_recursive(pairs)
        for j in match_up_list:
            match_count += 1
            match_name = "Match " + str(match_count)
            player_one_creation = self.database.search_in_data_base("Player", j[0])
            player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
            self.player_score_generator_round(player_one_instance, tournament_played, round_played.id)
            player_two_creation = self.database.search_in_data_base("Player", j[1])
            player_two_instance = self.player_instance_creation_from_data_base(player_two_creation)
            self.player_score_generator_round(player_two_instance, tournament_played, round_played.id)
            match_i = Match(match_name, player_one_instance, player_two_instance, round_played, 0)
            print(match_i)
            self.database.database_item_insertion("Match", match_i.serialized_form)
            match_list.append(match_i)
        round_played.matches_list = match_list
        return match_list

    def possible_pairs(self, tournament_id, players_list):
        players = players_list
        pairs = self.database.list_match_pairs(tournament_id)
        possible_match_ups = []
        for i in range(8):
            for j in range(i+1, 8):
                if [players[i], players[j]] not in pairs:
                    possible_match_ups.append([players[i], players[j], i+j])
        possible_match_ups.sort(key=lambda x: x[2], reverse=True)
        return possible_match_ups

    @staticmethod
    def check_player_exist(list_matches, match):
        for i in list_matches:
            if match[0] == i[0] or match[0] == i[1] or match[1] == i[0] or match[1] == i[1]:
                return False
        return True

    # def try_recursive(self, list_comb, list2, i, count_number):
    #         for i in range(i + 1, len(list_comb)):
    #             if len(list2) > count_number:
    #                 list2.pop()
    #             if self.check_player_exist(list2, list_comb[i]):
    #                 list2.append(list_comb[i])
    #                 count_number += 1
    #                 return self.try_recursive(list_comb, list2, i+1, count_number)

    def try_recursive(self, list_comb, list2, i, count_number):
        for i in range(i, len(list_comb)):
            if len(list2) > count_number:
                list2.pop()
            if self.check_player_exist(list2, list_comb[i]):
                list2.append(list_comb[i])
                count_number += 1
                j = i+1
                return self.try_recursive(list_comb, list2, j, count_number)


    def list_comb_recursive(self, list_comb):
        list2 = []
        count_number = 0
        i = 0
        self.try_recursive(list_comb, list2, i, count_number)
        return list2


    # def list_comb_recursive(self, list_comb):
    #     list2 = []
    #     count_number = 0
    #     for i in range(len(list_comb)):
    #         if len(list2) > count_number:
    #             list2.pop()
    #         list2.append(list_comb[i])
    #         count_number += 1
    #         i += 1
    #         self.try_recursive(list_comb, list2, i, count_number)
    #         return list2
    #     return -1


    def round_one_method(self, round_played, player_list_instances):
        original_ranking = self.player_list_sorting(player_list_instances, True)
        top_half = original_ranking[0:round_played.matches_number]
        bottom_half = original_ranking[round_played.matches_number:round_played.player_number]
        match_list = []
        match_count = 0
        while match_count < round_played.matches_number:
            top_player = top_half[match_count]
            bottom_player = bottom_half[match_count]
            match_count += 1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, top_player, bottom_player, round_played, 0)
            self.database.database_item_insertion("Match", match_i.serialized_form)
            print(match_i)
            match_list.append(match_i)
        round_played.matches_list = match_list
        return match_list

    def boolean_choice_menu(self):
        user_choice = input("Order :"
                            "0 = Ascending\n"
                            "1 = Descending \n")
        if int(user_choice) == 0:
            return False
        elif int(user_choice) == 1:
            return True
        else:
            self.boolean_choice_menu()

    def player_list_score_and_sorting(self, tournament_played):
        player_list = self.player_list_score_generator(tournament_played)
        player_list = self.player_list_sorting(player_list, False)
        return player_list
