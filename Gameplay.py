
all_stacks = []
color_list = []
origin_stack = []
target_stack = []

max_ht = 4
stack_amt = 4
color_amt = 3

def check_win(all_stacks):
    # Go through all the stacks
    for a in range(len(all_stacks)):
        # Check if stack is empty, just move on
        if all_stacks[a] == []:
            print("Stack {} is empty".format(a+1))
        # Check non empty stacks if everything is the same
        else:
            # Compare first element of the list to the others
            for b in range(1, len(all_stacks[a])):
                # Matching colors so far
                if all_stacks[a][0] == all_stacks[a][b]:
                    print("Good so far")
                # Different color detected - the game isnt over yet
                else:
                    print("Stack {}: 2+ colors detected, not done yet".format(a+1))
                    return '0'
        # If we reached this point, the stack must be good
        print("Stack {} must be good".format(a+1))
    # If we reaached this point, all the stacks must be good
    print("All stacks must be good at this point")

    return '1'

    input("")

# Ensure the attempted move is valid - look at top/last part of stack/list
def check_valid_move(all_stacks, origin_stack, target_stack):
    
    # Valid option 1 - moving to an empty stack
    if (target_stack == []):
        print("empty stack, this move is ok")
        return '1'
    # Invalid option 1 - stack would go beyond max height allowed
    #   If target is already at max - it CANNOT take any more
    elif (len(target_stack) == max_ht):
        print("Invalid: target stack is full")
        return '0'
    # Valid option 2 - moving color to a stack with the same color on top
    #   look at last element of both stacks -- -1 index
    #   note unsure if should use origin[-1] or just get the color - like in case im moving it and its temporarily not part of the list anymore
    elif (origin_stack[-1] == target_stack[-1]):
        print("matching color, this move is ok")
        return '1'
    # Invalid move if not valid option 1 or 2
    else:
        print("Invalid move")
        return '0'

# Print out all stacks
#def show_stacks(all_stacks):
    # Go through all stacks to print them 
   # for a in range(len(all_stacks)):

def play_game(all_stacks):

    player_choice = ''
    #Play until we reach the end
    while (check_win(all_stacks) == '0'):
        print("Options:")
        print(" - Enter the number of the stack you are moving FROM")
        print(" - Quit (q/Q/quit/Quit)")
        player_choice = input("Input: ")

        # Player wants to quit
        if (player_choice == 'q' or player_choice == 'Q' or player_choice == 'Quit' or player_choice == 'quit'):
            # Confirm if user wants to do this - to prevent accidental quitting
            quit_choice = input("Are you sure you want to quit (y/n): ")

            if (quit_choice == 'Y' or quit_choice == 'y'):
                # Notify user and return / terminate function
                print("Quitting game...thanks for playing I hope you had fun!")
                return
        # Player selects origin stack - convert choice str -> int
        #   Ensure its a number and it corresponds to an existing stack
        elif (player_choice.isdigit() and int(player_choice) >= 1 and int(player_choice) <= stack_amt):   
            # Ensure valid choice
            valid_target = False
            while (valid_target == False):
                # Choose a target stack to drop ball into
                target_choice = input("Pick a stack to drop into or type b to go back: ")
                # User wants to go back, just get out of this loop
                if (target_choice == 'b' or target_choice == 'B' or target_choice == 'back' or target_choice == 'Back'):
                    print("returning")
                    valid_target = True
                # Ensure target and origin stack are different
                elif (target_choice == player_choice):
                    print("Sorry, the target stack cannot be the same as the origin stack")
                # Ensure its a number and corresponds to an existing stack
                elif (target_choice.isdigit() and int(target_choice) >= 1 and int(player_choice) <= stack_amt):
                    # Ensure it's a valid moves
                    print("Moving ball...")
                    valid_target = True
                # Invalid input
                else:
                    print("Sorry, it must be a number that corresponds to a different stack")
                # temporary - spacing so it's easier to read
                print("")

    


   






