"""
file: ball_puzzle.py
description: a program that sorts colored balls using stacks
language: python3
author: Aidan Hearn
"""

#Import Statements
import ball_puzzle_animate
from cs_stack import CSStack
#from node_types import FrozenNode - Caleb said I didn't need to import

#Stacks
red_stack = CSStack()
green_stack = CSStack()
blue_stack = CSStack()
stack_list = [red_stack, green_stack, blue_stack]

def move_ball(canHold: CSStack, canGoal: CSStack) -> None:
    """
    The move function that is called in main_move
    :precondition: stacks used are not empty
    :param canHold: stack having an element removed (.pop), CSStack type
    :param canGoal: stack having an element added, adds the element being popped from other stack, CSStack type
    :return: None, does not return anything
    """
    canGoal.push(canHold.pop())

def main_move(move_count:int = 0) -> int:
    """
    Alters the stacks to sort them by color, tracks how many moves will happen
    :precondition: for each while statement within main_move, the stack being manipulated cannot be empty
    :return: Returns move_count (an integer), number of moves made by the puzzle
    """
    red_count = 0 #will be used later for optimization

    while not stack_list[0].is_empty():
        if stack_list[0].peek() == "G":
            move_ball(stack_list[0], stack_list[1])
            ball_puzzle_animate.animate_move(stack_list, 0, 1)
            move_count += 1

        elif stack_list[0].peek() == "B":
            move_ball(stack_list[0], stack_list[2])
            ball_puzzle_animate.animate_move(stack_list, 0, 2)
            move_count += 1

        elif stack_list[0].peek() == "R":
            move_ball(stack_list[0], stack_list[2])
            ball_puzzle_animate.animate_move(stack_list, 0, 2)
            move_count += 1
            red_count += 1 #counts how many red balls are added into third stack

    while not stack_list[2].is_empty():
        if stack_list[2].peek() == "R":
            move_ball(stack_list[2], stack_list[0])
            ball_puzzle_animate.animate_move(stack_list, 2, 0)
            move_count += 1
            red_count -= 1 #counts how many red balls are moved from third to first stack

        else:
            if red_count != 0: #this eliminates extra moves needed if there are no more red balls (moves blue less)
                move_ball(stack_list[2], stack_list[1])
                ball_puzzle_animate.animate_move(stack_list, 2, 1)
                move_count += 1
            else: #this eliminates extra moves needed if there are no more red balls (moves blue less)
                break

    while not stack_list[1].is_empty() and stack_list[1].peek() == "B":
        if stack_list[1].peek() == "B":
            move_ball(stack_list[1], stack_list[2])
            ball_puzzle_animate.animate_move(stack_list, 1, 2)
            move_count += 1

    return move_count

def main() -> None:
    """
    Main function to prompt the user, solve the puzzle, and produce animation
    :return: None, does not return anything
    """
    rgb_string = str(input("Input initial string (R,G,B) of balls in first can: "))
    for j in rgb_string:
        stack_list[0].push(str(j))
    ball_puzzle_animate.animate_init(rgb_string)
    ball_count = main_move() #all my movement and animation is called here, didn't want a super long main function
    print("Puzzle solved in " + str(ball_count) + " moves!")
    print("Close the window to quit")
    ball_puzzle_animate.animate_finish()

if __name__ == '__main__':
    main()
