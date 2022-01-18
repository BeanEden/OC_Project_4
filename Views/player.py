"""Base view."""


class PlayerView:
    """Player view."""



    def prompt_for_flip_cards(self):
        """Request to return the cards."""
        print()
        input("Prêt à retourner les cartes ?")
        return True


    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")


    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True