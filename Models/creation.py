
from Models.tournoi import Tournament
from Models.round import Round
from Models.players import Player
from Models.matchs import Match
from Models.database import *
from operator import *
from Models.View import *

player_one = Player("p1","p1","04/05/2014","gender","1")
player_two = Player("p2","p2","04/05/2014","gender","2")
player_three = Player("p3","p3","04/05/2014","gender","3")
player_four = Player("p4","p4","04/05/2014","gender","4")
player_five = Player("p5","p5","04/05/2014","gender","5")
player_six = Player("p6","p6","04/05/2014","gender","6")
player_seven = Player("p7","p7","04/05/2014","gender","7")
player_eight = Player("p8","p8","04/05/2014","gender","8")

players_list = [player_one,player_two,player_three,player_four,player_five,player_six,player_seven,player_eight]

players_dict = {}
for i in players_list:
    players_dict["Player " + str(players_list.index(i)+1)] = i.id

def create_a_tournament():
    input("Création d'un nouveau tournoi, appuyez sur une touche pour continuer :\n")
    name = input("Entrez le nom du tournoi :\n")
    place = input("Entrez le lieu du tournoi : \n")
    date = input("Entrez la date du tournoi : \n")
    time_control = input("Sélectionnez le mode de contrôle du temps :\n" +
                         "1 - bullet \n"
                         "2 - blitz \n"
                         "3 - coup rapide\n")
    description = input("Description générale du tournoi : ")
    # player_list = player_dictionary_select()
    new_tournament = Tournament(name, place, date, time_control, description, players_dict)
    database_item_insertion(new_tournament.serialized_form, db_tournament)
    return new_tournament


def add_a_player():
    """Prompt for adding a player."""
    print("Création d'un nouveau joueur...\n")
    family_name = input("Nom du joueur : \n")
    first_name = input("Prénom du joueur : \n")
    birth_date = input("Date de naissance du joueur (DD/MM/YYYY): \n")
    gender = input("Genre (F/H): \n")
    rank = input("Classement (chiffre positif) : \n")
    player = Player(family_name, first_name, birth_date, gender, rank)
    print(player.name + " a bien été enregistré(e). id = " + player.id)
    serialized_player = player.player_serialization()
    database_item_insertion(serialized_player, db_players)
    return serialized_player


def player_dictionary_select():
    player_count = 0
    player_list_tournament = {}
    while player_count < 8:
        player_count += 1
        player = "a"
        while player == "a":
            user_input_player_id_key = input(
                "Enter player " + str(player_count) + " id :\n"
                "id = firstname + first letter from family_name + day of birth"
                "example : Mark Zuck born on 09/03/1987 -> id = MarkZ09\n")
            player = search_player_in_data_base(user_input_player_id_key, db_players)
        new_player = player_instance_creation_from_data_base(player)
        print("Player added : " + str(new_player))
        player_list_tournament[player_count] = new_player.id
    return player_list_tournament


def round_creation_run_function(round_count_number, tournament_played):
    round_name = "Round " + str(round_count_number)
    print(round_name + " started...")
    round_one = Round(round_name, tournament_played)
    database_item_insertion(round_one.serialized_form, db_rounds)
    return round_one


def secondary_round_run_function(round_number, tournament_played):
    round_name = "Round " + str(round_number)
    print(round_name + " started...")
    round_played = Round(round_name, tournament_played)
    database_item_insertion(round_played.serialized_form, db_rounds)
    return round_played


def players_list_round_creation(tournament_played):
    player_list = []
    for player in tournament_played.players_list.values():
        new_player = search_player_in_data_base(player, db_players)
        player_list.append(player_instance_creation_from_data_base(new_player))
    player_list = player_list
    return player_list


def player_instance_creation_from_data_base(dict_player):
    family_name = dict_player["family_name"]
    first_name = dict_player["first_name"]
    age = dict_player["birth_date"]
    rank = dict_player["rank"]
    gender = dict_player["gender"]
    new_player = Player(family_name, first_name, age, gender, rank)
    return new_player


def match_instance_creation_from_data_base(dict_match, round_of_the_match):
    name = dict_match["match_name"]

    p_one_id = dict_match["player_one"]
    player_one_creation = search_player_in_data_base(p_one_id,db_players)
    player_one = player_instance_creation_from_data_base(player_one_creation)

    p_two_id = dict_match["player_two"]
    player_two_creation = search_player_in_data_base(p_two_id,db_players)
    player_two = player_instance_creation_from_data_base(player_two_creation)
    score = dict_match["result"]
    new_match = Match(name, player_one, player_two, round_of_the_match, score)
    return new_match


def round_instance_creation_from_data_base(dict_round, tournament):
    name = dict_round["round_name"]
    # player_list = dict_round["player_list"]
    new_round = Round(name, tournament)
    new_round.start_time = dict_round["start_time"]
    if dict_round["end_time"] != "unifinished":
        new_round.end_time = dict_round["end_time"]
        new_round.round_duration()
    for match in dict_round["matches_list"]:
        new_round.matches_list.append(match_instance_creation_from_data_base(match, new_round))
    return new_round


def tournament_instance_creation_from_database(dict_tournament):
    name = dict_tournament["tournament_name"]
    place = dict_tournament["tournament_place"]
    date = dict_tournament["tournament_date"]
    time_control = dict_tournament["tournament_time_control"]
    description = dict_tournament["tournament_description"]
    player_list = dict_tournament["tournament_player_dictionary"]
    # for player in :
    #     player_list.append(player_instance_creation_from_data_base(player))
    new_tournament = Tournament(name, place, date, time_control, player_list, description)
    round_list = []
    # for i in dict_tournament["tournament_rounds"]:
    #     new_tournament.rounds_list.append(round_instance_creation_from_data_base(i, new_tournament))
    return new_tournament

def match_list_generator(tournament, round_played):
    query = Query()
    match_list = []
    item = db_matches.search(query.tournament_id == str(tournament.id) and query.round_name == str(round_played.name))
    for match in item :
        match = match_instance_creation_from_data_base(match, round_played)
        match_list.append(match)
    match_list = sorted(match_list, key=attrgetter('name'), reverse=False)
    return match_list

def player_score_generator(player, tournament):
    query = Query()
    match_list = []
    item = db_matches.search(query.tournament_id == str(tournament.id) and query.player_one == str(player.id))
    item_two = db_matches.search(query.tournament_id == str(tournament.id) and query.player_two == str(player.id))

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

def player_list_score_generator(tournament):
    player_list = []
    for player in tournament.players_list.values():
        player_one = player_instance_creation_from_data_base(search_player_in_data_base(player, db_players))
        player_score_generator(player_one, tournament)
        player_list.append(player_one)
    return player_list

def opponents_list_construction(player_id, tournament_id):
    query = Query()
    item = db_matches.search(query.tournament_id == str(tournament_id) and (query.player_one == str(player_id)))
    item_two = db_matches.search(query.tournament_id == str(tournament_id) and (query.player_two == str(player_id)))
    opponents_list = []
    for match in item :
        opponents_list.append(match["player_two"])
    for match in item_two:
        opponents_list.append(match["player_one"])
    return opponents_list

def round_match_list_definition(round_played, player_list):
    if int(round_played.count) == 1:
        round_played.matches_list = round_one_method(round_played,player_list)
    else:
        round_played.matches_list = secondary_rounds_method(round_played, player_list)
    return round_played.matches_list

def secondary_rounds_method(round_played, player_list_instances):
    original_classment = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
    round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
    match_list = []
    match_count = 0
    while match_count < round_played.matches_number :
        player_one = round_classment[0]
        player_one_opponents_list = opponents_list_construction(player_one.id, round_played.tournament_name)
        player_two_rank = round_classment.index(player_one) + 1
        player_two = round_classment[player_two_rank]
        while player_two.id in player_one_opponents_list:
            player_two_rank += 1
            player_two = round_classment[player_two_rank]
        round_classment.remove(player_one)
        round_classment.remove(player_two)
        match_count += 1
        match_name = "Match " + str(match_count)
        match_i = Match(match_name, player_one, player_two, round_played, 0)
        database_item_insertion(match_i.serialized_form, db_matches)
        match_list.append(match_i)
    round_played.matches_list = match_list
    return match_list

def round_one_method(round_played, player_list_instances):
    original_classment = sorted(player_list_instances, key=attrgetter('rank'), reverse=True)
    top_half = original_classment[0:round_played.matches_number]
    bottom_half = original_classment[round_played.matches_number:round_played.player_number]
    match_list = []
    for i in range(0, round_played.matches_number):
        match_count = i+1
        match_name = "Match " + str(match_count)
        match_i = Match(match_name, top_half[i], bottom_half[i], round_played, 0)
        database_item_insertion(match_i.serialized_form, db_matches)
        match_list.append(match_i)
    round_played.matches_list = match_list
    return match_list

def print_all_round_complete(tournament):
    for rounds in tournament.rounds_list :
        previous_round = search_player_in_data_base(rounds, db_rounds)
        previous_round = round_instance_creation_from_data_base(previous_round,tournament)
        match_list = match_list_generator
        round_count = previous_round.count
        print_round_complete(round_count,match_list)
