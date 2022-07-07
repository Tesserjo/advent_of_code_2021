"""This program contains the solution for advent of code 2021 day 8.
Documentation is not finished yet.
"""

from data_functions import read_data, get_numbers
import collections as cl



__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"


def output_strings(list):
    new_list = []
    for i in list:
        x = i[1].split(' ')
        x.pop(0)
        new_list.append(x)
    return new_list

def output_all(list):
    new_list = []
    for i in list:
        x = i[0].split(' ')
        x.pop(-1)
        y = i[1].split(' ')
        y.pop(0)
        new_list.append(x + y)
    return new_list


def count_uniques(list):
    one = 0
    four = 0
    seven = 0
    eight = 0
    for i in list:
        for j in i:
            if len(j) == 2:
                one += 1
            elif len(j) == 3:
                seven += 1
            elif len(j) == 4:
                four += 1
            elif len(j) == 7:
                eight += 1
    return one + four + seven + eight

def output_strings(list):
    new_list = []
    for i in list:
        x = i[1].split(' ')
        x.pop(0)
        new_list.append(x)
    return new_list


def deduction(list):
    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    for j in list:
        if len(j) == 2:
            one = j
        elif len(j) == 3:
            seven = j
        elif len(j) == 4:
            four = j
        elif len(j) == 7:
            eight = j
    for j in list:
        if len(j) == 5:
            if all(elem in j for elem in one):
                three = j
        elif len(j) == 6:
            if all(elem in j for elem in four):
                nine = j
            elif all(elem in j for elem in one):
                zero = j
            else:
                six = j
    for j in list:
        if len(j) == 5:
            if j != three:
                if all(elem in nine for elem in j):
                    five = j
                else:
                    two = j
    return [zero, one, two, three, four, five, six, seven, eight, nine]
    

def add_output(list):
    result = 0
    for i in list:
        sum = ''
        x = deduction(i)
        for j in range(10, len(i)):
            if cl.Counter(i[j]) == cl.Counter(x[0]):
                sum += '0'
            elif cl.Counter(i[j]) == cl.Counter(x[1]):
                sum += '1'
            elif cl.Counter(i[j]) == cl.Counter(x[2]):
                sum += '2'
            elif cl.Counter(i[j]) == cl.Counter(x[3]):
                sum += '3'
            elif cl.Counter(i[j]) == cl.Counter(x[4]):
                sum += '4'
            elif cl.Counter(i[j]) == cl.Counter(x[5]):
                sum += '5'
            elif cl.Counter(i[j]) == cl.Counter(x[6]):
                sum += '6'
            elif cl.Counter(i[j]) == cl.Counter(x[7]):
                sum += '7'
            elif cl.Counter(i[j]) == cl.Counter(x[8]):
                sum += '8'
            elif cl.Counter(i[j]) == cl.Counter(x[9]):
                sum += '9'
        result += int(sum)
    return result          




def main():
    data = read_data('data.txt')
    data = output_all(data)
    result = add_output(data)
    print(result)


if __name__ == '__main__':
    main()
