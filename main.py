from Controller.menu import Controller
from Controller.creation import ItemCreation
from Views.View import View



def main():
    view = View()
    creation = ItemCreation()
    program = Controller(view, creation)
    program.main_menu()


if __name__ == '__main__':
    main()
else:
    pass
