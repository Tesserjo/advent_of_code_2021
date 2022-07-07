"""This program gives the solution for advent of code 2021 day 4.
"""

from typing import Counter
from Board import Board
from data_functions import read_data
from data_functions import get_numbers
from data_functions import transform_data
from bingo import create_board_list
from bingo import play_game
from bingo import play_game_two

__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


def main():
    x = ''
    while x != '1' and x != '2':
       x = input("enter 1 for game one or 2 for game 2: ")
    data = read_data("data.txt")
    numbers = get_numbers(data)
    data = transform_data(data)
    board_list = create_board_list(data)
    if x == '1':
        #game1
        result = play_game(numbers, board_list)
        print(result)

    else:
        last_board = play_game_two(numbers, board_list)
        result = play_game(numbers, last_board)
        print(result)


if __name__ == '__main__':
    main()
