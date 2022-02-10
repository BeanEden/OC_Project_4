from Controller.menu import Controller
from Controller.creation import ItemCreation
from Views.View import View
from Models.database import Database

db_test = Database("db_test")

def main():
    view = View()
    creation = ItemCreation(db_test)
    program = Controller(view, creation)
    program.main_menu()


if __name__ == '__main__':
    main()
else:
    pass
