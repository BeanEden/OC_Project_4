

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
        player_list = player_1.append()
        player_1 = input("Entrez le nom/prénom du joueur 1")
        player_2 = input("Entrez le nom/prénom du joueur 2")
        player_3 = input("Entrez le nom/prénom du joueur 3")
        player_4 = input("Entrez le nom/prénom du joueur 4")
        player_5 = input("Entrez le nom/prénom du joueur 5")
        player_6 = input("Entrez le nom/prénom du joueur 6")
        player_7 = input("Entrez le nom/prénom du joueur 7")
        player_8 = input("Entrez le nom/prénom du joueur 8")
        player_list =

        return player_list


    def start_round(self):
        print("Commencer le round 1 ?")

