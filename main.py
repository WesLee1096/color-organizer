#import pygame
import random

print("HELLO")

def check_win(all_stacks):
    #Go through all the stacks
    for a in range(len(all_stacks)):
        #check if stack is empty, just move on
        if all_stacks[a] == []:
            print("Stack {} is empty".format(a+1))
        #Check non empty stacks if everything is the same
        else:
            #Compare first element of the list to the others
            for b in range(1, len(all_stacks[a])):
                if all_stacks[a][0] == all_stacks[a][b]:
                    print("Good so far")
                else:
                    print("Stack {}: 2+ colors detected, not done yet".format(a+1))
                    return '0'
            print("Stack {} must be good".format(a+1))

    print("All stacks must be good at this point")
    return '1'
    
def main():


    print("okkkksdiojadsiokljfilasdf")


    # List for possible colors
    available_colors = ['Red', 'Blue', 'Yellow', 'Green', 'Orange', 'Purple']
 

    print("Hello welcome to my 2nd simple game: Color organizer stacker")
    print(" Goal: organize the balls according to color")
    print(" Rule 1: no stack cannot exceed the max height - at any time")
    print(" Rule 2: you can only move a ball to an empty stack or one that has the same color ball at the top")
    print("    Example: if you're moving a yellow ball, the stack you are moving it to must have a yellow ball at the top")
    print(" Rule 3: the amount of stacks shall be 1 more thn the amount of colors - which depends on difficulty chosen")
    print("    This may not be the case when using the custom feature (coming soon...)")

    print("For this version at least there is 1 difficulty - easy")

    print("Easy: 3 colors, 4 balls each, max height: 4")
    
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

    all_stacks = [stack1, stack2, stack3, stack4]
    #check_win(stack1, stack2, stack3, stack4)
    #print("answer: {}".format(all_stacks[2][3]))
    
    #Call function to check if game is done yet
    winner = check_win(all_stacks)
    #Tell user if they won yet
    if winner == '0':
        print("Not yet, keep going")
    else:
        print("You win")
    #Note: stack 4 is empty
    #Default  - remmber reverse order since list/stack
    #3    blue    blue        blue
    #2    red     yellow      red
    #1    red     yellow      yellow
    #0    red     yellow      blue


 #   2   3       1           
  #  2   3       1
   # 2   3       1
    #2   3       1

    # May be different from the one we are using
    # Saller list may be used depending on chosen difficulty





    # Append colors to color list
   

if __name__ == '__main__':
    main()
   # Create stacks to hold the colored balls


