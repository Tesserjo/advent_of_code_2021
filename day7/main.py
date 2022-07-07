"""This program gives the solution for advent of code 2021 day 7.
"""

from data_functions import read_data, get_numbers


__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


def find_position(list, fuel = 0):
    """Searches for the ideal way to allign all crab-submarines
    
    Args:
      list of integers

    Returns:
      integer
    """
    max_pos = max(list)
    print(max_pos)
    sum_fuel = 0
    for i in range(max_pos + 1):
        sum_fuel = 0
        for j in list:
            new_fuel = abs(j - i)
            extra_fuel = 0
            for k in range(new_fuel):
                extra_fuel += k   
            new_fuel += extra_fuel
            sum_fuel += new_fuel
        if fuel == 0:
            fuel = sum_fuel
        else:
            if fuel > sum_fuel:
                fuel = sum_fuel
    return fuel


def main():
    data = read_data('data.txt')
    data = get_numbers(data)
    fuel = find_position(data)
    print(fuel)


if __name__ == '__main__':
    main()
