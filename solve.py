from cells import Cell
from cells import Clue
from cells import ClueCell
from cells import BlackCell
from cells import WhiteCell
from puzzle import Puzzle
import copy

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class SolveUnInt:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    
    def backtracking_search(self, puzzle):
        return self.recursive_backtracking(copy.deepcopy(puzzle))

    def recursive_backtracking(self, set):
        if set.is_checked():
            return set
        clue = set.select_unassigned_clue()
        if clue is not None:
            value_sets = set.return_value_sets(clue)
            for value_set in value_sets:
                if copy.deepcopy(set).clue_is_checked(clue, copy.deepcopy(value_set)):
                    set.assign_clue(clue, value_set)   
                    set.print_board()
                    result = self.recursive_backtracking(copy.deepcopy(set))
                    if result is not None:
                        return result
        return None
    
    def solve(self):
        solution = self.backtracking_search(self.puzzle)   
        if solution is not None:
            self.puzzle = solution
            self.puzzle.print_board()
        else:
            print("no solution found")  
            
class SolveInt:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    
    def backtracking_search(self, puzzle):
        return self.recursive_backtracking(copy.deepcopy(puzzle))

    def recursive_backtracking(self, set):
        if set.is_checked():
            return set
        clue = set.select_unassigned_clue_mrv()
        if clue is not None:
            value_sets = set.return_value_sets(clue)
            for value_set in value_sets:
                if copy.deepcopy(set).clue_is_checked(clue, copy.deepcopy(value_set)):
                    set.assign_clue(clue, value_set)   
                    set.print_board()
                    result = self.recursive_backtracking(copy.deepcopy(set))
                    if result is not None:
                        return result
        return None
    
    def solve(self):
        solution = self.backtracking_search(self.puzzle)   
        if solution is not None:
            self.puzzle = solution
            self.puzzle.print_board()
        else:
            print("no solution found")           
    
        