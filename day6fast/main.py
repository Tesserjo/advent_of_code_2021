"""This program gives the solution for advent of code 2021 day 6.
"""

from data_functions import read_data, get_numbers
import numpy as np


__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


def fast_solution(array, time, day = 0):
    """This calculates how big the Lanternfishpopulation is after a set time
    
    Args:
      np.array
      int

    Returns:
      int
    """
    while day != time:
        day += 1
        babys = np.count_nonzero(array == 0)
        baby_array = np.repeat(8, babys)
        array[array == 0] = 7
        array = array - 1
        array = np.concatenate((array, baby_array))
        return fast_solution(array, time, day)
    return len(array)


def main():
    data = read_data('data.txt')
    data = get_numbers(data)
    array = np.array(data)
    fish = fast_solution(array, 80)
    print(fish)      


if __name__ == '__main__':
    main()
