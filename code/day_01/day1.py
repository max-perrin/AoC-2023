"""Day 01 AoC 2023

Challenge : concatenate the first and last integers of each line
            (double the integer if is single), and sum all lines results.
"""
import os
import re

script_path = os.path.dirname(__file__)
input_path = os.path.join(script_path, 'input.txt')

integers_letters = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

RE_FIRST_PUZZLE = r"\d"
RE_SECOND_PUZZLE = r"(?=(\d|" + "|".join(list(integers_letters.keys())) + "))"

def line_result_int_str(line_input: str) -> int:
    """ Gets the joined ints (int or str format, depends on the exercize)
        and returns concatenation of first and last int.

    Args:
        line_input (str): line of the input file - joined ints to be cleaned
    
    Returns:
        result (int): line result
                    (concatenation of the line's first and last int)
    """
    for word in integers_letters.keys():
        line_input = line_input.replace(word, integers_letters[word])
    result = line_input[0]
    if len(line_input) > 1:
        result = int(result + line_input[-1])
    else:
        result = int(result + line_input[0])
    return result

def puzzle(regex_to_match: any):
    sum_all_lines = 0
    with open(input_path, "r") as input:
        full_input_list = input.read().split('\n')
        for single_line in full_input_list:
            only_int_and_str = re.findall(regex_to_match, single_line)
            sum_all_lines += line_result_int_str("".join(only_int_and_str))
    return sum_all_lines

print(puzzle(RE_FIRST_PUZZLE))
print(puzzle(RE_SECOND_PUZZLE))