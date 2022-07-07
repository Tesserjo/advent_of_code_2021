""" A set of functions to restructure data."""


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





def transform_data(list):
    """Gets a list of integers and transforms it into a dictionary.
      
      Args:
        list of integers

      Returns:
        dictionary
    """
    first = True
    new_list = []
    board_nr = 0
    x = 0
    y = 0
    dict = {}
    for i in list:
        z = i.split()
        if z == []:
            pass
        else:
            new_list.append(z)            
    for i in new_list:
        if first == True:
            first = False
            pass
        else:      
            for j in i:
                dict[board_nr,x,y] = [int(j), False]
                y += 1                
            y = 0
            x += 1
        if x == 5:
            board_nr += 1
            x = 0
    return dict