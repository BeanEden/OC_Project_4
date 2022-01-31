# from Models.players import Player
from Models.matchs import Match
from operator import *
from Models.database import *
from Models.creation import *
import datetime

class Round:
    def __init__(self, name, tournament):
        self.name = name
        self.tournament = tournament
        self.player_list = self.tournament.players_list
        self.player_number = len(self.player_list)
        self.matches_number = int(self.player_number / 2)
        self.start_time = datetime. datetime. now()
        self.end_time = "unfinished"
        self.round_duration = ""
        self.status = "open"
        self.count = name[-1]
        self.tournament_name = tournament.id
        # self.matches_list = self.round_match_list_definition(self.count)
        self.matches_list = []
        self.id = self.name[0] + self.count + " " + tournament.id
        self.matches_list_serialized = []
        self.serialized_form = self.round_serialization()

    def __repr__(self):
        return repr([self.name, self.matches_list])

    def round_serialization(self):
        serialized_round = {
            "tournament_id": self.tournament_name,
            "round_name": self.name,
            # "matches_list": self.matches_list,
            # "players_list": player_list_serialization(self.player_list, "Player ", db_players),
            "start_time": str(self.start_time),
            "end_time": self.end_time,
            "id_key": self.id,
        }
        return serialized_round

    def round_time_over(self):
        if self.status != "over":
            self.end_time = datetime. datetime. now()
        return self.end_time

    def round_duration(self):
        if self.end_time != "unfinished" :
            self.round_duration = int(self.end_time) - int(self.start_time)
        return self.round_duration

    def round_one_method(self, player_list_instances):
        original_classment = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
        top_half = original_classment[0:self.matches_number]
        bottom_half = original_classment[self.matches_number:self.player_number]
        match_list = []
        for i in range(0, self.matches_number):
            match_count = i+1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, top_half[i], bottom_half[i], self)
            database_item_insertion(match_i.serialized_form, db_matches)
            match_list.append(match_i)
        # print(match_list)
        self.matches_list = match_list
        return self.matches_list

    def secondary_rounds_method(self, player_list_instances):
        original_classment = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
        round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
        match_list = []
        for i in range(0, self.matches_number, 1):
            match_count = i + 1
            match_name = "Match " + str(match_count)
            player_one_rank = i
            while round_classment[player_one_rank] in match_list:
                player_one_rank += 1
            player_two_rank = player_one_rank + 1
            match_i = Match(match_name, round_classment[player_one_rank], round_classment[player_two_rank], self)
            check = round_two_player_check(match_i)
            while check == "already happened":
                player_two_rank += 1
            match_i = Match(match_name, round_classment[i], round_classment[i + 1], self)
            database_item_insertion(match_i.serialized_form, db_matches)
            match_list.append(match_i)
        self.matches_list = match_list
        return self.matches_list

    def round_match_list_definition(self, round_count, player_list):
        if round_count == 1:
            self.matches_list = self.round_one_method(player_list)
        else:
            self.matches_list = self.secondary_rounds_method(player_list)
        return self.matches_list

    def round_check(self):
        for match in self.matches_list:
            if match.result == "result not defined yet":
                self.status = "open"
            else:
                self.status = "complete"
        return self.status

def round_two_player_check(match):
    query = Query()
    item = db_matches.search(query.tournament_id == str(match.tournament_name) and (
                query.player_one == str(match.player_one.id) or query.player_two == str(match.player_two.id)))
    if match.player_two.id in item:
        return "already happened"
    else:
        return "new"

    # def secondary_rounds_method(self):
    #     original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
    #     round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
    #     # print(round_classment)
    #     opponents_list = self.tournament.opponents_list
    #     # # tournament_list =
    #     # # for match in tournament_list:
    #     # #     opponents_list.append(match)
    #     # print(opponents_list)
    #     match_list = []
    #     for i in range(0, self.matches_number, 1):
    #         match_count = i + 1
    #         match_name = "Match " + str(match_count)
    #         index_used = []
    #         occurence = opponents_list[0]
    #         while occurence in opponents_list:
    #             index_pone = 0
    #             while index_pone in index_used:
    #                 index_pone += 1
    #                 index_used.append(index_pone)
    #             # player_one = round_classment[index_pone]
    #             index_ptwo = index_pone + 1
    #             # player_two = round_classment[index_ptwo]
    #             match_i = Match(match_name, round_classment[index_pone], round_classment[index_ptwo], self)
    #             occurence = match_i.opponents
    #         match_i = Match(match_name, round_classment[i], round_classment[i + 1], self)
    #         print(match_i.opponents)
    #         match_list.append(match_i)
    #     self.matches_list = match_list
    #     player_list_serialization(self.matches_list, "Match ", db_matches)
    #     return self.matches_list

    #
    # def secondary_rounds_method(self):
    #     original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
    #     round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
    #     # print(round_classment)
    #     # # tournament_list =
    #     # # for match in tournament_list:
    #     # #     opponents_list.append(match)
    #     # print(opponents_list)
    #     match_list = []
    #     for i in range(0, self.matches_number, 1):
    #         match_count = i + 1
    #         match_name = "Match " + str(match_count)
    #         index_used = []
    #         while occurence in opponents_list:
    #             index_pone = 0
    #             while index_pone in index_used:
    #                 index_pone += 1
    #                 index_used.append(index_pone)
    #             # player_one = round_classment[index_pone]
    #             index_ptwo = index_pone + 1
    #             # player_two = round_classment[index_ptwo]
    #             match_i = Match(match_name, round_classment[index_pone], round_classment[index_ptwo], self)
    #             occurence = match_i.opponents
    #         match_i = Match(match_name, round_classment[i], round_classment[i + 1], self)
    #         print(match_i.opponents)
    #         match_list.append(match_i)
    #     self.matches_list = match_list
    #     player_list_serialization(self.matches_list, "Match ", db_matches)
    #     return self.matches_list