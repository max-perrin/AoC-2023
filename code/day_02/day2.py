"""Day 02 AoC 2023

Challenges :
[1] game is possible if number of cubes given is < to maximum possible
    ==> result is sum of all possible games' IDs
[2] for each game, multiply the minimal number of cube (= max value)
    for each color with the other colors
    ==> result is sum of all games' color count multiplication
"""
import os
import re

script_path = os.path.dirname(__file__)
input_path = os.path.join(script_path, 'input.txt')

MAX_CUBES = {
    "red": "12",
    "green": "13",
    "blue": "14",
}

RE_NUMBER_COLOR_PAIR = r"\d+\s(?:blue|red|green)"

def is_game_possible(input_line: str) -> int:
    """ Checks if all values for a color in a game (= line) are
        inferior to the max possible.
        For this, split each combination (3 blue, 5 red for instance)
        into a value and a color, and compare the value to the associated
        color's maximum value.

    Args:
        line_input (str): raw line of the input file
    
    Returns:
        game_id (int): game ID if game is possible, 0 otherwise
    """
    game_id = 0
    combinations = re.findall(RE_NUMBER_COLOR_PAIR, input_line)
    for pair in combinations:
        if all(int(pair.split(' ')[0]) <= int(MAX_CUBES[pair.split(' ')[1]]) for pair in combinations):
            game_id = int(re.findall(r"\d+", input_line)[0])
    return game_id

def power_minimum_cubes(input_line: str) -> int:
    """ Give the minimal number of cubes possible for each line/game.
        i.e. the maximal value for each color
        (max value = at least this much cubes, so minimum cubes)
        and returns the power of all minimal values.

    Args:
        line_input (str): raw line of the input file
    
    Returns:
        returned_power_values (int): multipl. of all colors values
    """
    returned_power_value = 1
    for color in MAX_CUBES.keys():
        line_color_values = re.findall(rf"\d+\s(?:{color})", input_line)
        int_line_color_values = [int(i.split(' ')[0]) for i in line_color_values]
        returned_power_value *= max(int_line_color_values) if max(int_line_color_values) > 0 else 1
    return returned_power_value

def puzzle():
    sum_valid_ids = 0
    sum_minimal_cubes = 0
    with open(input_path, "r") as input:
        full_input_list = input.read().split('\n')
        for single_line in full_input_list:
            sum_valid_ids += is_game_possible(single_line)
            sum_minimal_cubes += power_minimum_cubes(single_line)
    return sum_valid_ids, sum_minimal_cubes

print(puzzle()[0], puzzle()[1], sep='\n')