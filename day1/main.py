"""Docstring: This program gives the solution for advent of code 2021 day 1.
"""




__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


from typing import Counter


def read_data():
    """Docstring: reads data and puts it into list
    returns list."""

    with open('data.py', 'r') as f:
        lines = f.readlines()
        list = [int(entry.strip()) for entry in lines]
    return list


def count_increased(list):
    """Docstring: gets list with integers and counts how many are bigger then
    predecesser."""
    x = 0 # Checks if it's the first entry.
    counter = 0 # Counts how many entrys are bigger than predecessor.
    predecessor = 0
    for i in list:
        if x == 0:
            predecessor = i
            x = 1
        else:
            if predecessor < i:
                counter += 1
            predecessor = i
    return counter


def main():
    """Counts how many tiles are bigger than thier predecessor
    """
    print(dec(count_increased(read_data())))

if __name__ == '__main__':
    main()
