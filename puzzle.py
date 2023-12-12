from cells import Cell
from cells import Clue
from cells import ClueCell
from cells import BlackCell
from cells import WhiteCell
from operator import itemgetter
import copy

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Puzzle:
    def __init__(self, height, width, cells):
        self.height = height
        self.width = width
        self.cells = cells
        self.clues = self.organize_clues()
        self.board = self.organize_board()
        self.print_board()
        
    def organize_clues(self):
        clues = []
        for cell in self.cells:
            if cell.category == 'CLUE':   
                if cell.down_clue is not None: 
                    clues.append(cell.down_clue)
                if cell.right_clue is not None: 
                    clues.append(cell.right_clue)
        return clues
    
    def organize_board(self):
        board = [ [WhiteCell((i, j)) for j in range(self.width)] for i in range(self.height) ]
        for cell in self.cells:
            board[cell.location[0]][cell.location[1]] = cell
        return board
    
    def print_board(self):
        board = self.board
        for i in range(self.height):
            print('|', end = "")
            for j in range(self.width):
                if board[i][j].category == 'BLACK':
                    print('   X   |', end = "")
                if board[i][j].category == 'WHITE':
                    if len( str(board[i][j].value) ) == 2:
                        print(' ' + str(board[i][j].value) + '    |', end = "")
                    else:    
                        print('  ' + str(board[i][j].value) + '    |', end = "")    
                if board[i][j].category == 'CLUE':
                    if board[i][j].down_clue is not None:
                        if len( str(board[i][j].down_clue.goal_sum) ) == 2:
                            print(' ' + str(board[i][j].down_clue.goal_sum) + '\\', end = "" )
                        else:
                            print('  ' + str(board[i][j].down_clue.goal_sum) + '\\', end = "") 
                    else:
                        print('  ' +'N' + '\\', end = "")
                    
                    if board[i][j].right_clue is not None:
                        if len( str(board[i][j].right_clue.goal_sum) ) == 2:
                            print(str(board[i][j].right_clue.goal_sum) + ' |', end = "")
                        else:
                            print(str(board[i][j].right_clue.goal_sum) + '  |', end = "") 
                    else:
                        print('N  |', end = "") 
            print('\n')
        print('\n\n')                        
                        
    #clue list   
    def get_cell_set(self, clue): 
        cell_set = []
        if clue.direction == 'DOWN':
            for i in range(clue.length):
                cell_set.append(self.board[clue.location[0] + i + 1][clue.location[1]]) 
        elif clue.direction == 'RIGHT':
            for i in range(clue.length): 
                cell_set.append(self.board[clue.location[0]][clue.location[1] + i + 1])
        return cell_set 
    
    
    def assign_clue(self, clue, value_set): 
        if clue.direction == 'DOWN':
            for i in range(clue.length):
                self.board[clue.location[0] + i + 1][clue.location[1]].value = value_set[i]
        elif clue.direction == 'RIGHT': 
            for i in range(clue.length):
                self.board[clue.location[0]][clue.location[1] + i + 1].value = value_set[i]
    
    def is_clue_assigned(self, clue):
        return self.clue_unassigned_count(clue) == 0
                                                             
    def clue_unassigned_count(self, clue):
        cell_set = self.get_cell_set(clue)
        unassigned_count = 0
        for cell in cell_set:
            if cell.value == 0: 
                unassigned_count += 1
        return unassigned_count 
    
    def is_complete(self): 
        is_complete = True
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].category == 'WHITE' and self.board[i][j].value == 0:
                    is_complete = False 
        return is_complete    
                
                
    def is_consistent(self):   
        for clue in self.clues:
            cell_set = self.get_cell_set(clue) 
            if self.is_clue_assigned(clue):
                current_sum = 0 
                values = []
                for cell in cell_set:
                    values.append(cell.value)
                    current_sum += cell.value
                if current_sum != clue.goal_sum or any(values.count(x) > 1 for x in values):
                    return False
        return True
                
    def is_checked(self):
        if self.is_complete() and self.is_consistent():
            return True
        
    def select_unassigned_clue(self):
        for clue in self.clues:
            if not self.is_clue_assigned(clue):
                return clue 
            
    #MRV
    def select_unassigned_clue_mrv(self):
        possible_clue = []
        fully_unassigned = []
        partially_unassigned = []
        
        for clue in self.clues:
            if not self.is_clue_assigned(clue):
                temp = self.clue_unassigned_count(clue)
                if temp == clue.length:
                    fully_unassigned.append((clue, temp))
                else:
                    partially_unassigned.append((clue, temp))
        
        partially_unassigned.sort(key = itemgetter(1))
        fully_unassigned.sort(key = itemgetter(1))       
        possible_clue = partially_unassigned + fully_unassigned
        return possible_clue[0][0]           
            
    def clue_is_checked(self, clue, value_set):
        self.assign_clue(clue, value_set)
        self.print_board() 
        return self.is_consistent()
             
    def sum_to_n(self, n, k, allowed_values):
        if k == 1 and n in allowed_values: 
            return [[n]]
        combos = []
        for i in allowed_values:
            allowed_values_copy = copy.deepcopy(allowed_values) 
            allowed_values_copy.remove(i)
            if n - i > 0:
                combos += [[i] + combo for combo in self.sum_to_n(n - i, k - 1, allowed_values_copy)]
        for combo in combos:
            if any(combo.count(x) > 1 for x in combo): 
                combos.remove(combo)
        return combos
    
    def getting_value_sets(self, clue, cell_set):
        value_sets = []
        assigned_cells = []
        unassigned_cells = []
        allowed_values = copy.deepcopy(DIGITS)
        
        for cell in cell_set:
            if cell.value == 0:
                unassigned_cells.append(cell)
            else:
                if cell.value in allowed_values:
                    allowed_values.remove(cell.value)
                assigned_cells.append(cell)        
        current_sum = 0
        for cell in assigned_cells:
            current_sum += cell.value
        net_goal_sum = clue.goal_sum - current_sum
        net_cell_count = clue.length - len(assigned_cells)
        unassigned_value_sets = self.sum_to_n(net_goal_sum, net_cell_count, allowed_values)
        for unassigned_value_set in unassigned_value_sets:
            variable_set = copy.deepcopy(cell_set) 
            value_set = []
            for cell in variable_set:
                if cell.value == 0:
                    value_set.append(unassigned_value_set.pop(0)) 
                else:
                    value_set.append(cell.value) 
            value_sets.append(value_set)
        return value_sets     
        
        
    def return_value_sets(self, clue):
        cell_set = self.get_cell_set(clue)
        value_sets = self.getting_value_sets(clue, cell_set) 
        return value_sets
            
                    
                                                      