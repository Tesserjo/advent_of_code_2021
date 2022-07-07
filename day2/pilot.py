"""Docstring: This program gives the solution for advent of code 2021 day 2.
"""




__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


from typing import Counter


def read_data():
    """Docstring: reads data and puts it into list
    returns list."""

    with open('data.py', 'r') as f:
        lines = f.readlines()
        list = [str(entry.strip()) for entry in lines]
    return list


def make_tuple_list(list):
    """Docstring: gets list with strings and transforms into list with tuples
    containing a string and an integer."""
    tuple_list = []
    for i in list:
        direction = i.rstrip(i[-1])
        direction = direction.rstrip(direction[-1])
        speed = int(i[-1])
        tuple = (direction, speed)
        tuple_list.append(tuple)
    return tuple_list


def navigate (tuple_list):
    """Docstring: gets list with tuples. """
    position = 0
    depth = 0
    for i in tuple_list:
        if i[0] == "forward":
            position += i[1]
        elif i[0] == "up":
            depth -= i[1]
        else:
            depth += i[1]
    result = position * depth
    return result



def main():
    """Counts how many tiles are bigger than thier predecessor
    """
    print(navigate(make_tuple_list(read_data())))

if __name__ == '__main__':
    main()
