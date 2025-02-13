
class Element:
   
    # I got this method from my TA Sivert Steinholt
    # Makes an empty list with a type. Type is either row, column or box
    def __init__(self, type):
        self.list = []
        self.type = type
            
    # Check if a given value is in that element-list
    def has_value(self, value):
        if value in self.list:
            return True        
        return False
    
    # Remove a given value from the element-list
    def remove_square(self, num ):
        self.list.remove(num)

    # Add the given value to the element-list
    def update_list(self, num):
        self.list.append(num)

            
