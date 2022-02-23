from Controller.menu import Controller
from Controller.creation import ItemCreation
from Views.View import View
from Models.database import Database

database = Database("database")


def main():
    view = View()
    creation = ItemCreation(database)
    program = Controller(view, creation)
    program.main_menu()


if __name__ == '__main__':
    main()
else:
    pass
