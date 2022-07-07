"""This program gives the solution for advent of code 2021 day 3.
"""

__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


from typing import Counter


def read_data(data):
    """Reads data and puts it into list.
      
      Args:
        txt document

      Returns:
        list of strings
    """
    with open(data, 'r') as f:
        lines = f.readlines()
        list = [str(entry.strip()) for entry in lines]
    return list


def power(list, power_type):
    """Counts ones and zeros of digits in list of binary integers.

        Reads the first charactar of the strings in a list of strings.
        If it got the argument 'gamma' it adds a 1 to a binary number if it
        counted more ones than zeros and vice versa. if it got the argument
        epsilon it does it the other way around. Then it does the same for the
        other 11 characters of the strings. At the End it transforms the binary
        number into a decimal number.
    
    Args:
      list of strings
      'gamma' or 'epsilon'
    
    Returns:
      dec int      
    """
    binary_list = ""
    for i in range(len(list[0])): #iterates through digits in first element
        count_zero = 0
        count_one = 0
        for j in list:  #iterates through elements in list
            if j[i] == '0':
                count_zero += 1
            elif j[i] == '1':
                count_one += 1
        if count_zero < count_one:
            if power_type == 'gamma':
                binary_list += '1'
            else:
                binary_list += '0'
        else:
            if power_type == 'gamma':
                binary_list += '0'
            else:
                binary_list += '1'
    return int(binary_list, 2)
  

def life_support_rating(list, gas, empty_list, j):
    """counts 1 or 0 and returns the life_support element
    
    Counts how many 1 and 0 are ont the first position of all numbers in the
    list. If gas == 'oxygen' and most numbers had a 1 on the first position it
    creates a new list with those numbers, respectively with zero.
    If gas == cotwo it does it the other way around.
    Then it takes this list and does the same for the second position and so on.
    It terminates when there is only one element left and returns it.

    Args:
    list of strings
    'oxygen' or 'cotwo'
    empty list
    0

    Returns:
    string
    """
    if len(list) == 1:
        return list[0]
    else:
        counter_zero = 0
        counter_one = 0
        for i in list: # iterates through elements in list
            if i[j] == '0':
                counter_zero += 1
            else:
                counter_one += 1
        if gas == "oxygen":
            for i in list: #iterates through elements in list
                if counter_one >= counter_zero:
                    if i[j] == '1':
                        empty_list.append(i)
                else:
                    if i[j] == '0':
                        empty_list.append(i)
        else:
            for i in list: # iterates through elements in list
                if counter_zero <= counter_one:
                    if i[j] == '0':
                        empty_list.append(i)
                else:
                    if i[j] == '1':
                        empty_list.append(i)
        list = empty_list
        empty_list = []
        gas = gas
        j += 1
        return life_support_rating(list, gas, empty_list, j)


def main():

    data = read_data("data.txt")
    gamma = power(data, 'gamma')
    epsilon = power(data, 'epsilon')
    power_consumption = gamma * epsilon
    print("power_consumption = ", power_consumption)

    empty_list = []
    oxygen = life_support_rating(data, "oxygen", empty_list, 0)
    empty_list = []
    cotwo = life_support_rating(data, "cotwo", empty_list, 0)
    oxygen = int(oxygen, 2)
    cotwo = int(cotwo, 2)
    life_support = oxygen * cotwo
    print("life_support_rating = ", life_support)


if __name__ == '__main__':
    main()
