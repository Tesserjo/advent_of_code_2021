"""This program gives the solution for advent of code 2021 day 6.
"""

from lanternfish import Lanternfish
from data_functions import read_data, get_numbers
#import numpy as np


__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


""" A set of functions to restructure data."""


def initial_swarm(list):
    """Initiates the first swar of lanternfish.
    
    Args:
      list of integers

    Returns:
      List of Lanternfishes
    """
    swarm = []
    for i in list:
        fish = Lanternfish(i)
        swarm.append(fish)
    return swarm


def pass_day(list):
    """Passes a day for the swarm. Updates thir timers and produces more babys.

    Args:
      list of lanternfish
    
    Returns:
      updated list of lanternfish
    """
    baby_list = []
    for i in list:
        if i.timer == 0:
            baby = Lanternfish(8)
            i.reduce_timer()
            baby_list.append(baby)
        else:
            i.reduce_timer()
    for i in baby_list:
        list.append(i)
    return list


def go_forward(time, list, day = 0):
    """Goes forward in a set time and updates the swarm.

    Args:
      int
      list of lanternfishes
      int
    
    Returns:
      updated list of lanternfishes
    """
    while day != time:
        day += 1
        print("day ", day)
        print(len(list), " lanternfish")
        list = pass_day(list)
        return go_forward(time, list, day)
    return list


def main():
    data = read_data('data.txt')
    data = get_numbers(data)
    swarm = initial_swarm(data)
    swarm = go_forward(256, swarm)
    print(len(swarm))


if __name__ == '__main__':
    main()
