from Models.player_database import *

class TournamentView:

    def confirmation_creation_tournoi(self):
        """Confirme la création d'un nouveau tournoi"""
        validation = input("Créer un nouveau tournoi (y/n) ?")
        return validation

    def create_a_tournament(self):
        name = input("Entrez le nom du tournoi :")
        place = input("Entrez le lieu du tournoi :")
        date = input("Entrez la date du tournoi :")
        time_control = input("Sélectionnez le mode de contrôle du temps :"
                             "1 - bullet"
                             "2 - blitz"
                             "3 - coup rapide")
        player_list = player_list_select(self)
        description = input("Description générale du tournoi")

    def player_list_select(self):
        player_count = 0
        player_dictionary = {}
        while (player_count < 8) :
            player_count +=1
            player = input("Enter player ",player_count,"name")
            search_in_data_base(player)
            player_dictionary["Player ",player_count] = player

        return player_dictionary


    def start_round(self):
        print("Commencer le round 1 ?")

