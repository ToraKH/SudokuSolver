from element import Element

class Square:

    # Square keeps track of their row, column, box and value
    def __init__(self, row, column, box, value):
        self.row = row
        self.column = column
        self.box = box
        self.value = value
     
    
    # Gives a readable representation of every square
    def __str__(self):
        return str(self.value)


    # Checks if the given value exists in the row, column or box, which is not legal, 
    def num_legal(self, row_list, column_list, box_list, value):

        # Checks the element in row-list with index from Square
        if row_list[self.row].has_value(value):
            return False

        # Checks the element in column-list with index from Square
        if column_list[self.column].has_value(value):
            return False
    
        # Checks the element in box-list with index from Square
        if box_list[self.box].has_value(value):
            return False
        
        # If value is legal, return true
        return True


    # Sets value of square to given value, and adds value to element-lists 
    def place_number(self, row_list, column_list, box_list, num):
        
        self.value = num

        row_list[self.row].update_list(num)
        column_list[self.column].update_list(num)
        box_list[self.box].update_list(num)


    
     


