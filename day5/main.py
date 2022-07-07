"""This program gives the solution for advent of code 2021 day 5.
"""


from data_functions import get_numbers, read_data, find_max
from math import sqrt


__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


def create_floor(width):
    """Creates a dictionary

    Args:
      integer

    Returns:
      dictionary
    """
    dict = {}
    for i in range(width + 1):
        for j in range(width +1):
            dict[i,j] = 0
    return dict


def vents(list, dict):
    """Searches vents on the ocean floor.

    Args:
      list of integers
      dictionary

    Returns:
      dictionary
    """
    for i in list:
        if i[0] == i[2]:            
            if i[1] < i[3]: 
                for j in range(i[1], i[3] + 1):
                    dict[i[0],j] += 1
            else:
                for j in range(i[1] ,i[3] - 1, -1):
                    dict[i[0],j] += 1
        if i[1] == i[3]:
            if i[0] < i[2]:
                for j in range(i[0], i[2] + 1):
                    dict[j,i[1]] += 1
            else:
                for j in range(i[0] ,i[2] - 1, -1):
                    dict[j,i[1]] += 1
    return dict


def vents_diagonal(list, dict):
    """
    Searches vents also diagonally.

    Args:
      list of integers
      dictionary

    Returns:
      dictionary

    """
    for i in list:
        diagonal_value = abs(i[0] - i[2])
        if i[0] == i[2]:            
            if i[1] < i[3]: 
                for j in range(i[1], i[3] + 1):
                    dict[i[0],j] += 1
            else:
                for j in range(i[1] ,i[3] - 1, -1):
                    dict[i[0],j] += 1
        elif i[1] == i[3]:
            if i[0] < i[2]:
                for j in range(i[0], i[2] + 1):
                    dict[j,i[1]] += 1
            else:
                for j in range(i[0] ,i[2] - 1, -1):
                    dict[j,i[1]] += 1
        elif abs(i[0] - i[2]) == abs(i[1] - i[3]):
            if i[0] < i[2] and i[1] < i[3]:
                for j in range(diagonal_value + 1):
                        dict[i[0] + j, i[1] + j] += 1
            elif i[0] < i[2] and i[1] > i[3]:
                for j in range(diagonal_value + 1):
                        dict[i[0] + j, i[1] - j] += 1
            elif i[0] > i[2] and i[1] < i[3]:
                for j in range(diagonal_value + 1):
                        dict[i[0] - j, i[1] + j] += 1
            elif i[0] > i[2] and i[1] > i[3]:
                for j in range(diagonal_value + 1):
                        dict[i[0] - j, i[1] - j] += 1          
    return dict    


def count_vents(dict):
    """Counts how many values in a dictionary are > 1
    
    Args:
      dictionary
    
    Returns
      integer
    """
    counter = 0
    for i in range(int(sqrt(len(dict)))):
        for j in range(int(sqrt(len(dict)))):
            if dict[i,j] > 1:
                counter += 1
    return counter        


def main():
    data = read_data("data.txt")
    data = get_numbers(data)
    floor = create_floor(find_max(data))
    floor = vents_diagonal(data, floor)
    result = count_vents(floor)
    print(result)


if __name__ == '__main__':
    main()
