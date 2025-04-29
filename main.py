#import pygame
import random
import Gameplay
import Navigation
import Setup


    
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
    

    # Display main menu
    main_menu_selection = '0'
    while (int(main_menu_selection) != 5):
        # Reset all stacks
        all_stacks = []
        # Show main menu
        main_menu_selection = Navigation.main_menu()
        # Play game
        if (int(main_menu_selection) == 1):
            # User picks which setup
            choose_game_mode = Navigation.game_selection()
            print("chocie: {}".format(choose_game_mode))
            # Easy preset 1
            if (choose_game_mode == 1):
                print("OK")
                all_stacks = Setup.easy_preset_1()
            elif (choose_game_mode == 2):
                all_stacks = Setup.random_setup(color_list, 4, 4, 4)

            #display = Setup.display_setup_details(color_list, 4, 4)

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


