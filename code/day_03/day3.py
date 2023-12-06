"""Day 03 AoC 2023"""
import os
import re


script_path = os.path.dirname(__file__)
input_path = os.path.join(script_path, 'input.txt')


RE_SPECIAL_CHAR = r"[^\.\n0-9]"


def is_digit(full_input_list, start, end):
    return bool(re.search(r"\d", full_input_list[start][end]))


def has_adjacent_char(line, start, end, full_input_list) -> bool:
    """ Checks number's neighbours (up, down, side and diagonal)"""
    string_to_be_checked = ""
    if line > 0:
        if start > 0:
            string_to_be_checked += full_input_list[line - 1][start - 1]
        if end < len(full_input_list[line - 1]):
            string_to_be_checked += full_input_list[line - 1][end]
        string_to_be_checked += full_input_list[line - 1][start:end]
    if line < len(full_input_list) - 1:
        if start > 0:
            string_to_be_checked += full_input_list[line + 1][start - 1]
        if end < len(full_input_list[line + 1]):
            string_to_be_checked += full_input_list[line + 1][end]
        string_to_be_checked += full_input_list[line + 1][start:end]
    if start > 0:
        string_to_be_checked += full_input_list[line][start - 1]
    if end < len(full_input_list[line]):
        string_to_be_checked += full_input_list[line][end]
    return bool(re.findall(RE_SPECIAL_CHAR, string_to_be_checked))


def has_adjacent_number(line, index, full_input_list) -> int:
    """ Small explaination of this shitty code:

    If there is a digit in radius, we take its coordinates,
        and if they are two and distinct (reason why we split cases for upper and lower lines),
        we get the full number from input.txt and multiply them, then return result.

    For this, we use "valid_col" that will tell us where there is a digit.
    But if there is a digit at "index -1" and "index +1" but not "index", we have to take
        this as two digits distinct
    """
    indexes = []
    returned_value = 0

    if line > 0:
        valid_col = []
        if index > 0:
            if is_digit(full_input_list, line - 1, index - 1):
                valid_col.append(-1)
        if index < len(full_input_list[line - 1]):
            if is_digit(full_input_list, line - 1, index + 1):
                valid_col.append(1)
        if is_digit(full_input_list, line - 1, index):
            valid_col.append(0)
        if len(valid_col) == 1 or len(valid_col) == 3 or (len(valid_col) == 2 and 0 in valid_col):
            indexes.append((line - 1, index + min(valid_col), index + max(valid_col)))
        elif len(valid_col) == 2:
            indexes.append((line - 1, index - 1, index - 1))
            indexes.append((line - 1, index + 1, index + 1))

    if line < len(full_input_list) - 1:
        valid_col = []
        if index > 0:
            if is_digit(full_input_list, line + 1, index - 1):
                valid_col.append(-1)
        if index < len(full_input_list[line + 1]):
            if is_digit(full_input_list, line + 1, index + 1):
                valid_col.append(1)
        if is_digit(full_input_list, line + 1, index):
            valid_col.append(0)
        if len(valid_col) == 1 or len(valid_col) == 3 or (len(valid_col) == 2 and 0 in valid_col):
            indexes.append((line + 1, index + min(valid_col), index + max(valid_col)))
        elif len(valid_col) == 2:
            indexes.append((line + 1, index - 1, index - 1))
            indexes.append((line + 1, index + 1, index + 1))

    if index > 0:
        if is_digit(full_input_list, line, index - 1):
            indexes.append((line, index - 1, index - 1))
    if index < len(full_input_list[line]):
        if is_digit(full_input_list, line, index + 1):
            indexes.append((line, index + 1, index + 1))

    if(len(indexes) == 2):
        returned_value = 1
        lines = [indexes[0][0], indexes[1][0]]
        for i in range(len(lines)):
            line = indexes[i][0]
            for match in re.finditer(r"(\d+)", full_input_list[line]):
                start, end = match.start(), match.end()
                if(start <= indexes[i][1] and end >= indexes[i][2]):
                    returned_value *= int(full_input_list[line][start:end])
    return returned_value


def puzzle():
    line = 0
    sum_part_numbers = 0
    sum_gears = 0
    with open(input_path, "r") as input:
        full_input_list = input.read().split('\n')

        for single_line in full_input_list:
            line_numbers = re.findall(r"\d+", single_line)
            line_indexes = [item.span() for item in re.finditer(r"\d+", single_line)]
            line_values = dict(zip(line_numbers, line_indexes))
            for number in line_numbers:
                if(has_adjacent_char(line, line_values[number][0], line_values[number][1], full_input_list)):
                    sum_part_numbers += int(number)

            for star in re.finditer(r"\*", single_line):
                sum_gears += has_adjacent_number(line, star.start(), full_input_list)
            line += 1

    return sum_part_numbers, sum_gears

print(puzzle())