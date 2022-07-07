"""A set of functions to play bingo."""

from Board import Board


def create_board_list(dict):
    """Creates a list of bingo-boards
    
      Args:
        dictionary

      Returns:
        list of boards
    """
    board_list = []
    class_dict = {}
    for i in range(100):
        for j in range(5):
            for k in range(5):
                class_dict[j,k] = dict[i,j,k]
        board_list.append(Board(i, class_dict))
        class_dict = {}
    return board_list


def play_game(list, board_list, game_two = False):
    """checks wich board won a game of bingo.
    
      Args:
        list of integers
        list of boards
      
      Returns:
        integer
    """
    for i in list:
        for j in board_list:
            j.bingo(i)
            j.check_row()
            j.check_column()
            if j.column == True:
                j.calc_unmarked()
                if game_two == True:
                  return j
                else:
                  result = j.sum_unmarked * i
                  return result
            elif j.row == True:
                if game_two == True:
                  return j
                else:
                  j.calc_unmarked()
                  result = j.sum_unmarked * i
                  return result


def play_game_two(list, board_list):
    """Plays bing and removes all the winner boards until only one is left.
    

    Args:
    list of integers
    list of boards

    Returns:
    list with on board-object
    """

    while len(board_list) != 1:
        bingo = play_game(list, board_list, True)
        board_list.remove(bingo)
    return board_list

