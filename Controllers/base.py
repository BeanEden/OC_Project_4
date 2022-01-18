from Models.players import *
from Models.round import *
from Models.tournoi.py import *
from Models.matchs.py import *
from Views.match.py import *
from operator import *

class Controller:

    def __init__(self, player, view):
        # models
        self.players: Player

        # views
        self.view = view

    def run(self):
        self.start_a_tournament()




    def start_a_tournament(self):
        "lance la vue"
        if self.confirmation_creation_tournoi() == "y":
            self.tournament = create_a_tournament(self)
        # else menu()

    def round_original(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        nombre_joueurs = len(original_classment)
        top_half = original_classment[0:nombre_joueurs/2]
        bottom_half = original_classment[nombre_joueurs/2:nombre_joueurs]
        # for i in range[0:nombre_joueurs/2]:
            match_1 = top_half[0] + "vs" + bottom_half[0]
            match_2 = top_half[1] + "vs" + bottom_half[1]
            self.view.confirmation.match()


    def round_2(self):
        original_classment = sorted(self.player_list, key=attrgetter('rank'), reverse=True)
        round_classment = sorted(original_classment, key=attrgetter('score'), reverse=True)
        nombre_joueur_2 = len(round_classment)
        for i in range[0:round_classment]:
            print(top_half[i] + "vs" + bottom_half[i])

