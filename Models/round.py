# from Models.players import Player
from Models.matchs import Match
from operator import *
from Models.database import *
import datetime

class Round:
    def __init__(self, name, tournament):
        self.name = name
        self.player_list = tournament.players_list
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
        self.serialized_form = self.round_serialization()
        self.matches_list_serialized = self.round_match_list_serialized()

    def __repr__(self):
        return repr([self.name, self.matches_list])

    # def round_serialization(self):
    #     serialized_round = {
    #         "tournament_id": self.tournament_name,
    #         "round_name": self.name,
    #         "matches_list": self.matches_list,
    #         "players_list": self.player_list,
    #         "start_time": self.start_time,
    #         "end_time" : self.end_time,
    #         "id_key": self.id,
    #     }
    #     return serialized_round

    def round_serialization(self):
        serialized_round = {
            "tournament_id": self.tournament_name,
            "round_name": self.name,
            "matches_list": player_list_serialization(self.matches_list, "Match ", db_matches),
            "players_list": player_list_serialization(self.player_list, "Player ",db_players),
            "start_time": self.start_time,
            "end_time" : self.end_time,
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

    def round_database_update(self):
        database_check_removal(self.serialized_form, db_rounds)
        database_item_insertion(self.serialized_form, db_rounds)

    def round_one_method(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        top_half = original_classment[0:self.matches_number]
        bottom_half = original_classment[self.matches_number:self.player_number]
        match_list = []
        for i in range(0, self.matches_number):
            match_count = i+1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, top_half[i], bottom_half[i], self)
            print(match_i.opponents)
            match_list.append(match_i)
        # print(match_list)
        self.matches_list = match_list
        return self.matches_list

    def secondary_rounds_method(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
        match_list = []
        for i in range(0, self.matches_number, 1):
            match_count = i + 1
            match_name = "Match " + str(match_count)
            match_i = Match(match_name, round_classment[i], round_classment[i + 1], self)
            print(match_i.opponents)
            match_list.append(match_i)
        # print(match_list)
        self.matches_list = match_list
        return self.matches_list

    def round_match_list_definition(self, round_count):
        if round_count == 1:
            self.matches_list = self.round_one_method()
        else:
            self.matches_list = self.secondary_rounds_method()
        return self.matches_list

    def round_check(self):
        for match in self.matches_list:
            if match.result == "result not defined yet":
                self.status = "open"
            else:
                self.status = "complete"
        return self.status

    def round_score_attribution(self):
        for i in self.matches_list:
            i.score_attribution()

    def round_match_list_serialized(self):
        serialized_matches_list = player_list_serialization(self.matches_list,"Match ", db_matches)
        return serialized_matches_list

    def add_serialized_round(self):
        for match in self.matches_list :
