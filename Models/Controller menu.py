from Models.menu import *
from Models.base import *


def main_menu():
    print_main_menu()
    user_input = 0

    while user_input != 5:
        user_input = int(input())
        if user_input == 1:
            tournament_menu()
        elif user_input == 2:
            print("Executing menu item 2")
        elif user_input == 3:
            print("Executing menu item 3")
        elif user_input == 4:
            print_consulting_menu()


# def consulting_menu():
#     print_consulting_menu()
#     user_input_consulting_menu = 0
#     while user_input_consulting_menu != 4:
#         user_input = int(input())
#         if user_input_consulting_menu == 1:
#
#         elif user_input_consulting_menu == 2:
#
#         elif user_input_consulting_menu == 3:
#     main_menu()


def tournament_menu():
    print_tournament_menu()
    user_input_tournament_menu = 0

    while user_input_tournament_menu != 3:
        user_input_tournament_menu = int(input())
        if user_input_tournament_menu == 1:
            tournament_execution_test()
        elif user_input_tournament_menu == 2 :
            print("using an already existing")
    main_menu()


main_menu()