from board import Board
from square import Square
from element import Element
from sudoku_reader import Sudoku_reader



class SudokuBoard(Board):

    def __init__(self, nums):

        # Sends the numbers to Board
        super().__init__(nums)

        # Creates empty lists containing 9 Element-lists each
        self.row_list = [Element("row") for _ in range(9)]
        self.column_list = [Element("column") for _ in range(9)]
        self.box_list = [Element("box") for _ in range(9)]

        # Sets up the squares on the board and links them to their elements
        self._set_up_nums()
        self._set_up_elems()


    # Prints the sudoku board. Inspired by __str__ in Board
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + " "
            r+= "\n" 
        return r
    
    
    # Creates a 2D-liste where every element is a Square-object
    def _set_up_nums(self):

        # Set up the squares on the board (ints into Square objects)
        for row in range(self.n_rows):

            for col in range(self.n_cols):

                boxnr = self.find_boxnr(row, col)
                value = self.nums[row][col]

                # Creates a Square object using the determined values
                square = Square(row, col, boxnr, value)
                self.nums[row][col] = square

    # Determines what the box indices are 
    def find_boxnr(self, row, col):

        x = None

        # Adds three by three rows and columns to the right box
        if row in range(0, 3): # Row 0-2
            if col in range (0, 3): # Column 0-2
                x = 0 # Gives box 0 etc...
            elif col in range (3, 6):
                x = 1
            elif col in range (6, 9):
                x = 2

        if row in range(3, 6):
            if col in range (0, 3):
                x = 3
            elif col in range (3, 6):
                x = 4
            elif col in range (6, 9):
                x = 5

        if row in range(6, 9):
            if col in range (0, 3):
                x = 6
            elif col in range (3, 6):
                x = 7
            elif col in range (6, 9):
                x = 8

        # Make sure x is assigned a value before returning
        if x is not None:
            return x
        
        else:
            # Handle the case where x is not assigned a value
            print(f"Error with indices: ({row}, {col})")
            
        
    # Links the squares and elements
    def _set_up_elems(self):

        # Iterates through the rows and columns
        for row in range(9): 

            for col in range(9):

                boxnr = self.find_boxnr(row, col)
                square = self.nums[row][col]

                # Adds the squares to their assigned row, column and box
                self.row_list[row].list.append(square.value)
                self.column_list[col].list.append(square.value)
                self.box_list[boxnr].list.append(square.value)


    # Inspired by the solving algorithm by Kylie Ying: https://www.youtube.com/watch?v=tvP_FZ-D9Ng
    # Finds the empty squares on the board
    def find_empty(self):

        # Iterates through the rows and columns
        for row in range(9):

            for col in range(9):

                square = self.nums[row][col]

                # If square is empty, return the position
                if square.value == 0:
                    return (row, col)

        # If there are no empty squares, return None       
        return (None, None)          


    # Inspired by the solving algorithm by Kylie Ying: https://www.youtube.com/watch?v=tvP_FZ-D9Ng
    def solve(self):

        # Finds empty squares if there are any
        find = self.find_empty()
        row, col = find

        # If no empty squares, the sudoku is solved
        if find == (None, None):
            return True
        
        
        boxnr = self.find_boxnr(row, col)
        square = self.nums[row][col]             

        # Tries the number 1-9, as they are the legal numbers in Sudoku
        for num in range(1, 10):

            # If the value is legal at that spot, update the square
            if square.num_legal(self.row_list, self.column_list, self.box_list, num):
                
                # Removes the last value at that square from the element-lists
                self.row_list[row].remove_square(square.value)
                self.column_list[col].remove_square(square.value)
                self.box_list[boxnr].remove_square(square.value)

                # Updates the square and element-lists with the new value
                square.place_number(self.row_list, self.column_list, self.box_list, num)

                # If sudoku is solved, return true
                if self.solve():
                    return True
                
            # If not a valid guess, try next number
         
        
        # If none of the numbers work, reset the square and element-lists:    
      
        # Removes the number that was previously on the square from row-list, column-list and box-list
        self.row_list[row].remove_square(square.value)
        self.column_list[col].remove_square(square.value)
        self.box_list[boxnr].remove_square(square.value)

        # Resets the value to zero so one can try a different value next time 
        square.place_number(self.row_list, self.column_list, self.box_list, 0)

        # Go back to try a bigger number on the last square
        return False
    





   
if __name__ == "__main__":
    
    board_nr = 1
    
    # Solves sudokus on file 'sudoku_10.csv'
    sudoku_reader = Sudoku_reader("sudoku_10.csv")      # EDIT this to get read other files

    # Solves the boards from 1 to 10
    while board_nr <= 10:                               # EDIT this to solve correct number of sudokus

        board_data = sudoku_reader.next_board()
        board = SudokuBoard(board_data)
        board.solve()

        # Prints out the first board. Change this number to print out another board
        if board_nr == 1:
            print(f"BOARD {board_nr}")
            print(board)
        print(f"Solved board nr {board_nr}")
        # Increments board number to solve next board
        board_nr += 1
    





    
    



  
   