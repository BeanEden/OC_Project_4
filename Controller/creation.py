
from Models.tournament import Tournament
from Models.round import Round
from Models.players import Player
from Models.matches import Match
from Models.database import *
from operator import *

# player_one = Player("p1", "p1", "04/05/2014", "gender", "1")
# player_two = Player("p2", "p2", "04/05/2014", "gender", "2")
# player_three = Player("p3", "p3", "04/05/2014", "gender", "3")
# player_four = Player("p4", "p4", "04/05/2014", "gender", "4")
# player_five = Player("p5", "p5", "04/05/2014", "gender", "5")
# player_six = Player("p6", "p6", "04/05/2014", "gender", "6")
# player_seven = Player("p7", "p7", "04/05/2014", "gender", "7")
# player_eight = Player("p8", "p8", "04/05/2014", "gender", "8")
#
# players_list = [player_one, player_two, player_three, player_four, player_five, player_six, player_seven, player_eight]
#
# players_dict = {}
# for i in players_list:
#     players_dict["Player " + str(players_list.index(i)+1)] = i.id


class ItemCreation:

    def __init__(self, database):
        self.database = database


    def create_a_tournament(self):
        input("Creating a new tournament, press a key to continue :\n")
        name = input("Enter the tournament name :\n")
        place = input("Enter tournament place : \n")
        date = input("Enter tournament date (DD/MM/YYYY) : \n")
        time_control = input("Select time control mode :\n" +
                             "1 - bullet \n"
                             "2 - blitz \n"
                             "3 - coup rapide\n")
        description = input("Enter tournament general description:\n")
        player_list = self.player_dictionary_select()
        new_tournament = Tournament(name, place, date, time_control, description, player_list)
        self.database.database_item_insertion("Tournament", new_tournament.serialized_form)
        return new_tournament

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
                print(player)
            new_player = self.player_instance_creation_from_data_base(player)
            print("Player added to tournament : " + str(new_player))
            player_list_tournament["Player " + str(player_count)] = new_player.id
        return player_list_tournament

    def round_creation_run_function(self, round_count_number, tournament_played):
        round_name = "Round " + str(round_count_number)
        print(round_name + " started...")
        round_one = Round(round_name, tournament_played)
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

    def player_instance_creation_from_data_base(self, dict_player):
        family_name = dict_player["family_name"]
        first_name = dict_player["first_name"]
        age = dict_player["birth_date"]
        rank = dict_player["rank"]
        gender = dict_player["gender"]
        new_player = Player(family_name, first_name, age, gender, rank)
        return new_player

    def match_instance_creation_from_data_base(self, dict_match, round_of_the_match):
        name = dict_match["match_name"]
        p_one_id = dict_match["player_one"]
        player_one_creation = self.database.search_in_data_base("Player", p_one_id)
        player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
        p_two_id = dict_match["player_two"]
        player_two_creation = self.database.search_in_data_base("Player", p_two_id)
        player_two_instance = self.player_instance_creation_from_data_base(player_two_creation)
        score = dict_match["result"]
        new_match = Match(name, player_one_instance, player_two_instance, round_of_the_match, score)
        return new_match

    def round_instance_creation_from_data_base(self, dict_round, tournament):
        name = dict_round["round_name"]
        new_round = Round(name, tournament)
        new_round.start_time = dict_round["start_time"]
        if dict_round["end_time"] != "unfinished":
            new_round.end_time = dict_round["end_time"]
        return new_round

    def tournament_instance_creation_from_database(self, dict_tournament):
        name = dict_tournament["tournament_name"]
        place = dict_tournament["tournament_place"]
        date = dict_tournament["tournament_date"]
        time_control = dict_tournament["tournament_time_control"]
        description = dict_tournament["tournament_description"]
        player_list = dict_tournament["tournament_player_dictionary"]
        new_tournament = Tournament(name, place, date, time_control, description, player_list)
        return new_tournament

    def match_list_generator(self, tournament, round_played):
        match_list = []
        item = self.database.query_2("Match", "tournament_id", tournament.id, "round_id", round_played.id)
        print(item)
        for match in item:
            match = self.match_instance_creation_from_data_base(match, round_played)
            match_list.append(match)
        match_list = sorted(match_list, key=attrgetter('name'), reverse=False)
        return match_list

    def player_score_generator(self, player, tournament):
        item = self.database.query_2("Match", "tournament_id",str(tournament.id),"player_one", str(player.id))
        item_two = self.database.query_2("Match", "tournament_id", str(tournament.id),"player_two", str(player.id))
        for match in item:
            if match["result"] == 1:
                player.score += 1
            elif match["result"] == 3:
                player.score += 0.5
        for match in item_two:
            if match["result"] == 2:
                player.score += 1
            elif match["result"] == 3:
                player.score += 0.5

    def player_list_score_generator(self, tournament):
        player_list = []
        tournament_player_list = tournament.players_list
        for player in tournament_player_list.values():
            player_one_creation = self.database.search_in_data_base("Player", player)
            player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
            self.player_score_generator(player_one_instance, tournament)
            player_list.append(player_one_instance)
        return player_list

    def opponents_list_construction(self, player_id, tournament_id):
        # item = db_matches.query_2("tournament_id", tournament_id, "player_one", player_id)
        item = self.database.query_2("Match", "player_one", player_id, "tournament_id", tournament_id)
        # item_two = db_matches.query_2("tournament_id", tournament_id, "player_two", player_id)
        item_two = self.database.query_2("Match", "player_two", player_id, "tournament_id", tournament_id)
        opponents_list = []
        for match in item:
            opponents_list.append(match["player_two"])
        for match in item_two:
            opponents_list.append(match["player_one"])
        return opponents_list

    # def opponents_list_construction(self, player_id, tournament_id):
    #     item = db_matches.search_in_data_base_bis("tournament_id", tournament_id)
    #     print(item)
    #     opponents_list = []
    #     for match in item:
    #         print(match)
    #         if match["player_one"] == player_id:
    #             opponents_list.append(match["player_two"])
    #         elif match["player_two"] == player_id:
    #             opponents_list.append(match["player_one"])
    #     return opponents_list


    def round_match_list_definition(self, round_played, player_list):
        if int(round_played.count) == 1:
            round_played.matches_list = self.round_one_method(round_played, player_list)
        else:
            round_played.matches_list = self.secondary_rounds_method(round_played, player_list)
        return round_played.matches_list

    def secondary_rounds_method(self, round_played, player_list_instances):
        original_ranking = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
        round_ranking = sorted(original_ranking, key=attrgetter('score'), reverse=True)
        print(round_ranking)
        match_list = []
        match_count = 0
        while match_count < round_played.matches_number:
            player_one_instance = round_ranking[0]
            player_one_opponents_list = \
                self.opponents_list_construction(player_one_instance.id, round_played.tournament_name)
            print(player_one_opponents_list)
            player_two_rank = 1
            player_two_instance = round_ranking[player_two_rank]
            print(player_two_instance)
            while player_two_instance.id in player_one_opponents_list:
                player_two_rank += 1
                player_two_instance = round_ranking[player_two_rank]
                print(player_two_instance)
            round_ranking.remove(player_one_instance)
            round_ranking.remove(player_two_instance)
            match_count += 1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, player_one_instance, player_two_instance, round_played, 0)
            print(match_i)
            self.database.database_item_insertion("Match", match_i.serialized_form)
            match_list.append(match_i)
        round_played.matches_list = match_list
        print(match_list)
        return match_list

    def possible_opponents_list(self, player, ranked_list, round_played):
            player_opponents_list = \
                self.opponents_list_construction(player.id, round_played.tournament_name)
            list_difference = []
            for item in ranked_list:
                if item not in player_opponents_list:
                    list_difference.append(item)
            return list_difference


    # def secondary_rounds_method(self, round_played, player_list_instances):
    #     original_ranking = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
    #     round_ranking = sorted(original_ranking, key=attrgetter('score'), reverse=True)
    #     bis_list = round_ranking
    #     match_list = []
    #     match_count = 0
    #     while match_count < round_played.matches_number:
    #         try :
    #             player_one_instance = bis_list[0]
    #             player_one_opponents_list = \
    #                 self.opponents_list_construction(player_one_instance.id, round_played.tournament_name)
    #             player_two_rank = 1
    #             player_two_instance = bis_list[player_two_rank]
    #             while player_two_instance.id in player_one_opponents_list:
    #                     player_two_rank += 1
    #                     player_two_instance = bis_list[player_two_rank]
    #                 bis_list.remove(player_one_instance)
    #                 bis_list.remove(player_two_instance)
    #                 match_count += 1
    #                 match_name = "Match " + str(match_count)
    #                 match_i = Match(match_name, player_one_instance, player_two_instance, round_played, 0)
    #                 self.database.database_item_insertion("Match", match_i.serialized_form)
    #                 match_list.append(match_i)
    #         except IndexError :
    #             match_count -= 1
    #             previous_match = match_list[-1]
    #             bis_list.append(previous_match.player_two)
    #             match_list.pop

    # def tournament_pairs(self, tournament_played_id):
    #     match_list = self.database.list_match_pairs(tournament_played_id)
    #     print(match_list)
    #     pairs_list = []
    #     for i in match_list :
    #         p_one_id = i[0]
    #         player_one_creation = self.database.search_in_data_base("Player", p_one_id)
    #         player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
    #         p_two_id = i[1]
    #         player_two_creation = self.database.search_in_data_base("Player", p_two_id)
    #         player_two_instance = self.player_instance_creation_from_data_base(player_two_creation)
    #         list.append([player_one_instance, player_two_instance])
    #     return list

    def possible_pairs(self, tournament):
        players = []
        for i in tournament.players_list.values():
            players.append(i)
        pairs = self.database.list_match_pairs(tournament.id)
        possible_match_ups = []
        for i in range(8):
            for j in range(i+1, 8):
                if [players[i], players[j]] not in pairs:
                    possible_match_ups.append([players[i], players[j], i+j])

        possible_match_ups.sort(key=lambda x: x[2], reverse=True)
        return possible_match_ups

    def check_player_exist(self, list_matchs, match):
        for i in list_matchs:
            if match[0] == i[0] or match[0] == i[1] or match[1] == i[0] or match[1] == i[1]:
                return False
        return True

    def list_comb(self, list_comb):
        list2 = []
        for i in range(len(list_comb)):
            if len(list2) > 0: list2.pop()
            list2.append(list_comb[i])
            for j in range(i + 1, len(list_comb)):
                if (len(list2) > 1): list2.pop()
                if self.check_player_exist(list2, list_comb[j]):
                    list2.append(list_comb[j])
                    for k in range(j + 1, len(list_comb)):
                        if (len(list2) > 2): list2.pop()
                        if self.check_player_exist(list2, list_comb[k]):
                            list2.append(list_comb[k])
                            for l in range(k + 1, len(list_comb)):
                                if (len(list2) > 3): list2.pop()
                                if self.check_player_exist(list2, list_comb[l]):
                                    list2.append(list_comb[l])
                                    return list2
        return -1

        list_comb(d2)
        # for i in range(len(round_ranking)) :
        #     list = self.possible_opponents_list(round_ranking[i], round_ranking, round_played)
        #     if len(list)>0:
        #         player_one_rank = i
        #         for j in round_ranking
        #     else :
        #         player_two_instance = i
        #
        #
        #     while player_two_instance.id in player_one_opponents_list:
        #         player_two_rank += 1
        #         player_two_instance = round_ranking[player_two_rank]
        #
        #     while player_two_instance not in player_one_opponents_list:
        #         bis_list.remove(player_one_instance)
        #         bis_list.remove(player_two_instance)
        #         player_three_instance = bis_list[0]
        #         player_three_opponents_list = \
        #             self.opponents_list_construction(player_three_instance.id, round_played.tournament_name)
        #         player_four_rank = 1
        #         player_four_instance = bis_list[player_four_rank]
        #         # while player_four_instance in player_three_opponents_list :
        #         #     player_four_rank
        #         if player_four_instance not in player_three_opponents_list:
        #             player_three_rank = player_two_rank + 1
        #
        #         player_three_instance = round_ranking[player_three_rank]
        #         player_one_opponents_list = \
        #             self.opponents_list_construction(player_one_instance.id, round_played.tournament_name)
        #
        #
        # list = []
        #
        # for i in range (len_)
        #
        #
        #     print(player_two_instance)
        #     round_ranking.remove(player_one_instance)
        #     round_ranking.remove(player_two_instance)
        #
        #
        #     match_count += 1
        #     match_name = "Match " + str(match_count)
        #     match_i = Match(match_name, player_one_instance, player_two_instance, round_played, 0)
        #     print(match_i)
        #     self.database.database_item_insertion("Match", match_i.serialized_form)
        #     match_list.append(match_i)
        # round_played.matches_list = match_list
        # print(match_list)
        # return match_list



    def round_one_method(self, round_played, player_list_instances):
        original_ranking = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
        top_half = original_ranking[0:round_played.matches_number]
        bottom_half = original_ranking[round_played.matches_number:round_played.player_number]
        match_list = []
        match_count = 0
        while match_count < round_played.matches_number:
            match_count += 1
            match_name = "Match " + str(match_count)
            top_player = top_half[0]
            bottom_player = bottom_half[0]
            match_i = Match(match_name, top_player, bottom_player, round_played, 0)
            top_half.remove(top_player)
            bottom_half.remove(bottom_player)
            self.database.database_item_insertion("Match", match_i.serialized_form)
            match_list.append(match_i)
        round_played.matches_list = match_list
        return match_list
