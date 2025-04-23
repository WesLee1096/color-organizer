#import pygame
import random
import Gameplay
import Navigation


    
def main():


    # Opening stuff - show welcome message
    welcome = Navigation.welcome_message()

    # Default stuff for now
    # List for possible colors
    available_colors = ['Red', 'Blue', 'Yellow', 'Green', 'Orange', 'Purple']
 
    

    #print("Easy: 3 colors, 4 balls each, max height: 4")
    
    color_amount = 3
    pile_amount = color_amount + 1
    max_height = 4

    # Colors we will be using - might be smaller than available if using low difficulty
    color_list = ['Red', 'Blue', 'Yellow']

    #Create stacks
    # for now it is manual

    stack1 = ['Red',    'Red',      'Red',          'Blue']
    stack2 = ['Yellow', 'Yellow',   'Yellow',       'Blue']
    stack3 = ['Blue',   'Yellow',   'Red',          'Blue']
    stack4 = []

    #Test for completed game
    #stack1 = ['Red', 'Red', 'Red', 'Red']
    #stack2 = []
    #stack3 = []
    #stack4 = ['Yellow', 'Yellow', 'Yellow', 'Yellow']

    # Big list that contains all the stacks - might change later to just 2d list
    all_stacks = [stack1, stack2, stack3, stack4]

    # Display main menu
    main_menu_selection = '0'
    while (int(main_menu_selection) != 5):
        main_menu_selection = Navigation.main_menu()
        # Play game
        if (int(main_menu_selection) == 1):
            play = Gameplay.play_game(all_stacks)
        # Show records - implement later
        elif (int(main_menu_selection) == 2):
            print("Displaying best records")
        # Rules
        elif (int(main_menu_selection) == 3):
            rules = Navigation.show_rules()
        # Controls -- implement later
        elif (int(main_menu_selection) == 4):
            print("Displaying controls -- much later probably")
        # Quit - navigation function ensures it must be valid
        else:
            # Warning/Confirmation message
            quit_choice = Navigation.quit_confirmation()
            # User indicates any reasonable form of y/yes
            if (quit_choice == True):
                break
            # Changes mind - reset choice
            else:
                main_menu_selection = 0
        # Extra space for visibility
        print("")

if __name__ == '__main__':
    main()


