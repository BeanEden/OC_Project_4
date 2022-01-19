



class Match :
    def __init__(self, name, joueur_1, joueur_2):
        self.name = name
        self.opponents = joueur_1 + " vs " + joueur_2
        # self.players = player_list
        # self.result = resultat_match

    def __repr__(self):
        return []

    def show(self):
        print("Le ", self.name,"oppose ", self.opponents)
    #
    #
    # def append_players_match(self,liste_joueurs_triée): :
    #     liste_joueurs_triés
    #
    #     resultat = input()
    #     print resultat


class MatchView:
    def resultat_match(self):
        result = input("Déclarez le vainqueur"
        "1 - Joueur 1" + player.name(player1) +
        "2 - Joueur 2" + player.name(player2) +
        "3 - Match Nul"
        )
        return result

