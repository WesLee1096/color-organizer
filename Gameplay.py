
all_stacks = []


max_ht = 4
stack_amt = 4
color_amt = 3

def check_win(all_stacks):

    # List to ensure that all colors are together for win
    colors_already_used = []

    # Go through all the stacks
    for a in range(len(all_stacks)):
        # Check non empty stacks if everything is the same
        if (all_stacks[a] != []):
            # Check if we have encountered this color before
            if (all_stacks[a][0] in colors_already_used):
                return '0'
            # New color - add it to the list of encountered colors
            else:
                colors_already_used.append(all_stacks[a][0])
            # Compare first element of the list to the others
            for b in range(1, len(all_stacks[a])):
                # 2+ colors - incomplete
                if all_stacks[a][0] != all_stacks[a][b]:
                    return '0'
    # All stacks must be good if we reache this point
    return '1'

# Ensure the attempted move is valid - look at top/last part of stack/list
#   Remember user # is 1 more than index number, adjusted when passing
def check_valid_move(all_stacks, origin, target):

    # Valid option 1 - moving to an empty stack
    if (all_stacks[int(target)] == []):
        print("empty stack, this move is ok")
        return '1'
    # Invalid option 1 - stack would go beyond max height allowed
    #   If target is already at max - it CANNOT take any more
    elif (len(all_stacks[int(target)]) == max_ht):
        print("Invalid: target stack is full")
        return '0'
    # Valid option 2 - moving color to a stack with the same color on top
    #   look at last element of both stacks -- -1 index
    #   note unsure if should use origin[-1] or just get the color - like in case im moving it and its temporarily not part of the list anymore
    elif (all_stacks[int(origin)][-1] == all_stacks[int(target)][-1]):
        print("matching color, this move is ok")
        return '1'
    # Invalid move if not valid option 1 or 2
    else:
        print("Invalid move")
        return '0'

# Print out all stacks
def show_stacks(all_stacks):
    # Go through all stacks to print them 
    for a in range(len(all_stacks)):
        # Empty stack - indicate it as so
        if all_stacks[a] == []:
            print("\nStack {}: (empty)".format(a+1))
        # Not empty - display the contents, contents separated by space insetad of newline
        else:
            print("\nStack {}:".format(a+1), end = ' ')
            for b in range(len(all_stacks[a])):
                #Print out stack results, separated by tb instead of newline
                print("{}".format(all_stacks[a][b]), end = '\t\t')
    # Extra space for visibility
    print("")

def move_ball(origin_stack, new_stack):
    # Get ball from to of origin stack
    temp_ball = origin_stack[-1]
    # Remove this ball
    origin_stack.pop()
    # Add this ball to new stack
    new_stack.append(temp_ball)

def play_game(all_stacks):

    player_choice = ''
    moves = 0
    #Play until we reach the end
    while (check_win(all_stacks) == '0'):
        show_stacks(all_stacks)
        print("Options:")
        print(" - Enter the number of the stack you are moving FROM")
        print(" - Quit to main menu (q/Q/quit/Quit)")
        print("Moves: {}".format(moves))
        player_choice = input("Input: ")

        # Player wants to quit
        if (player_choice == 'q' or player_choice == 'Q' or player_choice == 'Quit' or player_choice == 'quit'):
            # Confirm if user wants to do this - to prevent accidental quitting
            quit_choice = input("Are you sure you want to quit (y/n): ")

            if (quit_choice == 'Y' or quit_choice == 'y'):
                # Notify user and return / terminate function
                print("Quitting game...thanks for playing I hope you had fun!")
                return '0'
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
                    if (check_valid_move(all_stacks, int(player_choice)-1, int(target_choice)-1) == '0'):
                        print("Illegal move, try again")
                    # Move the ball!!!!
                    else:
                        print("Moving ball...")
                        move_ball(all_stacks[int(player_choice)-1], all_stacks[int(target_choice)-1])
                        valid_target = True
                        # Increase move counter
                        moves += 1
                # Invalid input
                else:
                    print("Sorry, it must be a number that corresponds to a different stack")
                # temporary - spacing so it's easier to read
                print("")

    if (check_win(all_stacks) == '1'):
        print("Congratulations you have beat the game in {} moves!".format(moves))
        return moves
    else:
        print("Error 1: reached end of gameplay without win?")

    


   






