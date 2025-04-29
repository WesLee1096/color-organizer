import random
import Gameplay

all_stacks = []
game_settings = []

# Game details vary by difficulty selected
def difficulty_settings(difficulty):
    if (difficulty == "Easy"):
        print("ok")

def easy_preset_1():
    
    stack1 = ['Red',    'Red',      'Red',          'Blue']
    stack2 = ['Yellow', 'Yellow',   'Yellow',       'Blue']
    stack3 = ['Blue',   'Yellow',   'Red',          'Blue']
    stack4 = []
    all_stacks = [stack1, stack2, stack3, stack4]

    return all_stacks


def display_setup_details(color_list, stack_max_ht, stack_amt):
    print("Generating random setup")

    # Print out details for current game setup
    print("\nDetails:")
    print(" - Stacks    : {}".format(stack_amt))
    print(" - Colors    :", end = ' ')
    for a in range(len(color_list)):
        print("{}".format(color_list[a]), end = '   ')
    print("\n - Max height: {}".format(stack_max_ht))


# Random setup tool - quickl check if there are remaining colors to be made
#   theres probably a better way to do this but for now lets just do this
def all_zero(lista):
    # Returns true if everything is 0, else false
    return all(element == 0 for element in lista)


def random_setup(color_list, stack_max_ht, stack_amt, amt_per_color):
    # Create all the stacks
    # For now we are assuming all stacks filled to max ht
    # Except the last stack which is empty
          
    # 2d list that will contain all the stacks
    all_stacks = []

    # List for how many of each color we have left to place
    #    For now it's simple since its equal
    color_available = [amt_per_color] * len(color_list)
    # How many colors we need to finish (may not need?)
    color_amt = len(color_list)

    # Until we used we used up all the colors
    while (all_zero(color_available) == False):
        # Fill every stack except the last one
        for a in range(stack_amt-1):
            new_stack = []
            # Fill each stack until full
            for b in (range(stack_max_ht)):
                valid_ball = False
                # Check if this is valid
                while (valid_ball == False):
                    # Pick a random color
                    new_ball = random.randint(0, len(color_list)-1)
                    # Make sure we are not already out of this color
                    # there might be a better way to do this
                    if (color_available[new_ball] != 0):
                        # Update counter to reflect incoming change
                        color_available[new_ball] -= 1
                        # Add ball
                        new_stack.append(color_list[new_ball])
                        # Move on to the next slot
                        valid_ball = True
            # add this stack to all stacks
            all_stacks.append(new_stack)
    # add final empty stack
    empty_stack = []
    all_stacks.append(empty_stack)
    

    return all_stacks


       
   

        #Ensure its solvable
        # IF it isnt, call randomsetup again until we get it right
       





