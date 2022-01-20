

class Match :
    def __init__(self, name, joueur_1, joueur_2):
        self.name = name
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.opponents = joueur_1 + " vs " + joueur_2
        # self.players = player_list

    def __repr__(self):
        return (self.name,self.opponents,self.result)

    def show(self):
        print("Le ", self.name,"oppose ", self.opponents)

    # def result(self,score):
    #     if score = 1 :

# class MatchView:
    def resultat_match(self):
        result = input((
            "Déclarez le vainqueur :"
            " 1 - ", self.joueur_1,
            " 2 - ", self.joueur_2,
            " 3 - Match Nul")
        )
        return result


if __name__ == '__main__':
    print("matchs.py exécuté")
else :
    pass
