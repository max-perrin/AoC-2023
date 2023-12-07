"""Day 04 AoC 2023"""
import os
import re


script_path = os.path.dirname(__file__)
input_path = os.path.join(script_path, 'input.txt')


def winning_numbers(single_line_split: list[str]) -> int:
    """Checks numbers that exist in the elf's side and the drawer's one.
    We take second and third index of the list split, because first index is "Card ???:"

    Return:
        winning_numbers (int): count of numbers common to both sides
    """
    card_points = 0
    elfs_card = set(re.findall(r"\d+", single_line_split[1]))
    my_card = set(re.findall(r"\d+", single_line_split[2]))
    winning_numbers = elfs_card.intersection(my_card)
    if(len(winning_numbers) > 0):
        card_points += 2 ** (len(winning_numbers) - 1)
    return len(winning_numbers)


def first_part_count(winning_numbers: int) -> int:
    points_count = 0
    if(winning_numbers > 0):
        points_count += 2 ** (winning_numbers - 1)
    return points_count


def second_part_count(winning_numbers: int, line: int, cards_won_count: list[int]) -> list[int]:
    """ If we have Z winning numbers on the Nth card, and we have X times the Nth card:
        we will win X time the N+1 card, X time the N+2 card, ... until the N + Z card.
    
    For instance : we have 2 cards '30' and there is 5 winning numbers on the card '30',
        we will get 2 cards '31', 2 cards '32', ... and 2 cards '35'.

    We fill the list of total cards (each card is 1 minimum, because we have the original one)
        and we will calculate the total in the function below.
    """
    if(winning_numbers > 0):
        for card_index in range(winning_numbers):
            if((line + card_index) < len(cards_won_count)):
                cards_won_count[line + card_index] += cards_won_count[line - 1]
    return cards_won_count

def second_part_points(cards_won_count: list[int]) -> int:
    total_points = 0
    for cards in cards_won_count:
        total_points += cards
    return total_points


def puzzle():
    first_part_points = 0
    cards_won_count = []

    with open(input_path, "r") as input:
        full_input_list = input.read().split('\n')
        cards_won_count.extend([1]*(len(full_input_list)))
        
        for single_line in full_input_list:
            split_parts_card = re.split(r'\:|\|', single_line)
            card_line = int(re.findall(r"\d+", split_parts_card[0])[0])

            first_part_points += first_part_count(winning_numbers(split_parts_card))
            cards_won_count = second_part_count(winning_numbers(split_parts_card), card_line, cards_won_count)

    return first_part_points, second_part_points(cards_won_count)

print(puzzle())