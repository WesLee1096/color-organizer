# Display welcome message when game is launched
def welcome_message():
    print("Welcome to color stack game - im bad at names")
    print(" Goal: organize the balls according to color")
  
# Double check if user wants to quit - to prevent accidental exits
def quit_confirmation():
    confirm = False
    quit_choice = input("Are you sure you want to quit (y/n): ")
    # User indicates any reasonable form of y/yes
    if (quit_choice == 'y' or quit_choice == 'Y' or quit_choice == 'yes'
or quit_choice == 'Yes' or quit_choice == 'YES'):
        confirm = True
        print("Thanks for playing!")
    return confirm

def show_rules():
    print(" Goal: organize the balls according to color")
    print(" - Rule 1: no stack cannot exceed the max height - at any time")
    print(" - Rule 2: you can only move a ball to an empty stack or one that has the same color ball at the top")
    print("     Example: if you're moving a red ball, the stack you are moving it to must be empty or have a red ball at the top")
    print(" - Rule 3: if possible, you want to finish the game with the least amount of moves")
    print(" Note: Currently there is only 1 preset but later we hope to add randomized setups")

def game_selection():
    selection = 0
    available_options = 2
    while (int(selection) <= 0 or int(selection) > available_options):
        print("Available:")
        print("   1. Easy preset 1")
        print("   2. Random (Easy)")
        selection = input("What game mode would you like to play: ")
    return int(selection)


def main_menu():
    menu_selection = 0

    # Available options
    option_list = ['Play', 'Record', 'Rule', 'Control', 'Quit']
    # Number of options
    number_of_options = len(option_list)

    # Main menu - i might change how this is done later
    while (int(menu_selection) <= 0 or int(menu_selection) > number_of_options):
        print("Main Menu:") 
        print("  1. Play game on default setting")
        print("  2. Show best record")
        print("  3. Rules")
        print("  4. Controls")
        print("  5. Quit")

        menu_selection = input("Enter a number for your choice: ")

        if (int(menu_selection) < 1 or int(menu_selection) > number_of_options):
            print("**Error: Invalid choice, please try again")
        # Extra space for visibility
        print("")
    return menu_selection

        #if (int(menu_selection < 1 or menu_selection ))
        # maybe just while() and break for valid options
