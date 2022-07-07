"""Functions to read data from a textdocument and transform it into lists
"""

import re

__author__ = "Jonas Tesseraux"
__email__ = "jonastesseraux@freenet.de"

def read_data(data):
    """Reads data and puts it into list.
      
      Args:
        txt document

      Returns:
        list of strings
    """
    with open(data, 'r') as f:
        lines = f.readlines()
        list = [str(entry.strip()).split('|') for entry in lines]
    return list


def get_numbers(list):
    """Gets a list of strings and transforms it into a list of integers.

      Args:
        list of strings

        Returns
          list of integers
    """
    new_list = []
    for i in list:
        coordinates = [int(j) for j in re.findall(r'-?\d+\.?\d*', i)]
        new_list.append(coordinates)
    return new_list[0]