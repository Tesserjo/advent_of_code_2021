class Board:
    """A bingo board

    The Board contains of a dictionary where every value can be highlited.
    It can be checked wheather all values in a row or all values in a column
    have been highlited. If this is the case the sum of all unhighlited can be
    calculated.
    
    Attributes:
        dict: A dictionary with x/y - coordinates as keys and int and boolean 
            as values.
        column: A boolean indicating every boolean in a column is true.
        row: A boolean indicating every boolean in a column is true.
        sum_unmarked: value of the sum of all values which are still unmarked.
    """
    def __init__(self, name, dict):
        """inits the Bingo class."""
        self.name = name
        self.dict = dict
        self.column = False
        self.row = False
        self.sum_unmarked = 0

    
    def bingo(self, number):
        """Checks if an int is on the board and highlightes it.
          Args:
            integer
        """
        for i in range(5):
            for j in range(5):
                if self.dict[i,j][0] == number:
                    self.dict[i,j][1] = True

    
    def check_row(self):
        """Checks if all values in a row have been highlited."""
        row = 0
        for i in range(5):
            for j in range(5):
                if self.dict[i,j][1] == True:
                    row += 1
                    if row == 5:
                        self.row = True
            row = 0

    
    def check_column(self):
        """Checks if all values in a column have been highlited."""
        column = 0
        for i in range(5):
            for j in range(5):
                if self.dict[j,i][1] == True:
                    column += 1
                    if column == 5:
                        self.column = True
            column = 0

   
    def calc_unmarked(self):
        """Calculates the sum of all unmarked values."""
        for i in range(5):
            for j in range(5):
                if self.dict[i,j][1] == False:
                    self.sum_unmarked += self.dict[i,j][0]