"""This program gives the solution for advent of code 2021 day 6.2.
"""

from data_functions import read_data, get_numbers



__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


def group_fish(data):
    """Groups the fish of a given population.
    
    Args:
      list of integers

    Retruns
      list of integers  
    """
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    for i in data:
        if i == 0:
            zero += 1            
        elif i == 1:
            one += 1
        elif i == 2:
            two += 1
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
        elif i == 6:
            six += 1
        elif i == 7:
            seven += 1
        elif i == 8:
            eight += 1
    list = [zero, one, two, three, four, five, six, seven, eight]
    return list


def reproduction(p, time, day = 0):
    """Calculates the population of fish after a set amount of time.

    Args:
      list of integers
      integer

    Returns:
      integer
    """
    while day != time:
        p = [p[1], p[2], p[3], p[4], p[5], p[6], p[0] + p[7], p[8], p[0]]
        return reproduction(p, time, day+1)
    return sum(p)


def main():
    data = read_data('data.txt')
    data = get_numbers(data)
    pool = group_fish(data)
    r = reproduction(pool, 256)
    print(r)    


if __name__ == '__main__':
    main()
