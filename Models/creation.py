
from Models.tournoi import Tournament
from Models.round import Round
from Models.players import Player
from Models.matchs import Match
from Models.database import *


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
    player_list = player_dictionary_select()
    new_tournament = Tournament(name, place, date, time_control, description,player_list)
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
    player_list_tournament = []
    while player_count < 8:
        player_count += 1
        player_id_key = input("Enter player " + str(player_count) + " id :\n"
                            "id = firstname + first letter from family_name + day of birth"
                            "example : Mark Zuck born on 09/03/1987 -> id = MarkZ09\n")
        player = search_player_in_data_base(player_id_key, db_players)
        new_player = player_instance_creation_from_data_base(player)
        print("Player added : " + str(new_player))
        player_list_tournament.append(new_player)
    return player_list_tournament


def round_creation_run_function(player_list, round_count_number, tournament_played):
    round_name = "Round " + str(round_count_number)
    print(round_name + " started...")
    round_one = Round(round_name, player_list, tournament_played)
    # matches_round_one = round_one.round_one_method()
    return round_one


def secondary_round_run_function(player_list, round_number, tournament_played):
    round_name = "Round " + str(round_number)
    print(round_name + " started...")
    round_played = Round(round_name, player_list,tournament_played)
    matches_round = round_played.secondary_rounds_method()
    matches_list = round_played.round_match_list_method(matches_round)
    return round_played


def player_instance_creation_from_data_base(dict_player):
    family_name = dict_player["family_name"]
    first_name = dict_player["first_name"]
    age = dict_player["birth_date"]
    rank = dict_player["rank"]
    gender = dict_player["gender"]
    new_player = Player(family_name=family_name, first_name=first_name, birth_date=age, gender=gender, rank=rank)
    return new_player


def match_instance_creation_from_data_base(dict_match, round_of_the_match):
    name = dict_match["match_name"]
    player_one = dict_match["player_1"]
    player_two = dict_match["player_2"]
    new_match = Match(name = name, player_one=player_one, player_two= player_two, round_played=round_of_the_match)
    new_match.result = dict_match["result"]
    return new_match


def round_instance_creation_from_data_base(dict_round, tournament):
    name = dict_round["round_name"]
    player_list = dict_round["player_list"]
    new_round = Round(name, player_list, tournament)
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
    player_list = []
    for player in dict_tournament["tournament_player_dictionary"]:
        player_list.append(player_instance_creation_from_data_base(player))
    new_tournament = Tournament(name, place, date, time_control, player_list, description)
    round_list = []
    for i in dict_tournament["tournament_rounds"]:
        new_tournament.rounds_list.append(round_instance_creation_from_data_base(i, new_tournament))
    return new_tournament


def tournament_add_database(tournament):
    serialized_players_list = item_list_add_database(tournament.players_list, db_players)
    tournament.players_list = serialized_players_list
    round_add_database(tournament)

    database_check_removal(tournament.serialized_form, db_tournament)
    database_item_insertion(tournament.serialized_form, db_tournament)


def item_list_add_database(item_list, database):
    serialized_item_list = []
    for item in item_list:
        serialized_item_list.append(item.serialized_form)
        database_item_insertion(item.serialized_form, database)
    return serialized_item_list


def round_add_database(tournament):
    serialized_rounds_list = []
    for i in tournament.rounds_list:
        serialized_matches_list = item_list_add_database(i.matches_list, db_matches)
        i.matches_list = serialized_matches_list
        database_item_insertion(i.serialized_form, db_rounds)
        serialized_rounds_list.append(i.serialized_form)
    return serialized_rounds_list