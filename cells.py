class Cell:
    def __init__(self, location, category):
        self.location = location
        self.category = category
    
class Clue:
    def __init__(self, direction, length, goal_sum):
        self.direction = direction
        self.length = length
        self.goal_sum = goal_sum

class ClueCell(Cell):
    def __init__(self, location, down_clue, right_clue):
        super().__init__(location, category = 'CLUE') 
        self.down_clue = down_clue
        if down_clue is not None:
            down_clue.location = self.location
        self.right_clue = right_clue
        if right_clue is not None:
            right_clue.location = self.location 
           
class BlackCell(Cell):
    def __init__(self, location):
        super().__init__(location, category = 'BLACK')
        
class WhiteCell(Cell):
    def __init__(self, location, value = 0):
        super().__init__(location, category = 'WHITE')  
        self.value = value
                           
                    
                