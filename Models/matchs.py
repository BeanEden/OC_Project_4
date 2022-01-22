from players import Player

class Match :
    def __init__(self, name, joueur_1, joueur_2):
        self.name = name
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        # self.opponents = joueur_1 + " vs " + joueur_2
        # self.players = player_list
        self.result = "result not defined yet"

    def __repr__(self):
        return repr([self.name,self.joueur_1,self.joueur_2, self.result])

    # def show(self):
    #     print("Le ", self.name,"oppose ", self.opponents)

    # def result(self,score):
    #     if score = 1 :
    def opponents(self):
        joueur_1_name = self.joueur_1.name
        joueur_2_name = self.joueur_2.name
        print(self.name + " : " + joueur_1_name + " vs " + joueur_2_name)

# class MatchView:
    def resultat_match(self):
        print("Déclarez le vainqueur :\n"
            "   1 - " + self.joueur_1.name + "\n"
            "   2 - " + self.joueur_2.name + "\n"
            "   3 - Match Nul\n")
        result = int(input())
        return result

    def score_attribution(self):
        result = self.resultat_match()
        while result != [1, 2, 3]:
            print("Resaississez le résultat du match : ")
            self.resultat_match()

        if result == 1 :
            self.joueur_1.score_add(1)
            self.result = str(self.joueur_1.name+"wins")
        elif result == 2 :
            self.joueur_2.score_add(1)
            self.result = str(self.joueur_2.name+"wins")
        elif result == 3 :
            self.joueur_1.score_add(0.5)
            self.joueur_2.score_add(0.5)
            self.result = "match_nul"
        return self.result

if __name__ == '__main__':
    print("matchs.py exécuté")
else :
    pass
