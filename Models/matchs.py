from players import Player

class Match :
    def __init__(self, name, joueur_1, joueur_2):
        self.name = name
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        # self.opponents = joueur_1 + " vs " + joueur_2
        # self.players = player_list

    def __repr__(self):
        return repr([self.name,self.joueur_1,self.joueur_2])

    # def show(self):
    #     print("Le ", self.name,"oppose ", self.opponents)

    # def result(self,score):
    #     if score = 1 :
    def opponents(self):
        joueur_1_name = self.joueur_1.name
        joueur_2_name = self.joueur_2.name
        print("Le ", self.name,"oppose ", joueur_1_name, " et ",joueur_2_name)

# class MatchView:
    def resultat_match(self):
        result = input((
            "Déclarez le vainqueur :"
            " 1 - ", self.joueur_1,
            " 2 - ", self.joueur_2,
            " 3 - Match Nul")
        )
        return result

    def score_attribution(self, result):
        if result == "1" :
            self.joueur_1.score_add(1)
        elif result == "2" :
            self.joueur_2.score_add(1)
        elif result == "3" :
            self.joueur_1.score_add(0.5)
            self.joueur_2.score_add(0.5)
        else :
            print("resaisir le resultat")

if __name__ == '__main__':
    print("matchs.py exécuté")
else :
    pass
