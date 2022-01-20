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


def tournament_execution :
    tournament = create_a_tournament()





