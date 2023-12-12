from cells import Cell
from cells import Clue
from cells import ClueCell
from cells import BlackCell
from cells import WhiteCell
from puzzle import Puzzle
from solve import SolveUnInt
from solve import SolveInt
import copy
import timeit


cells = []
# 5X5 sample:
# row 1
cells.append(BlackCell((0, 0)))
cells.append(BlackCell((0, 1)))
cells.append(ClueCell((0, 2), Clue('DOWN', 4, 22), None)) 
cells.append(ClueCell((0, 3), Clue('DOWN', 4, 12), None)) 
cells.append(BlackCell((0, 4)))
# row 2
cells.append(BlackCell((1, 0)))
cells.append(ClueCell((1, 1), Clue('DOWN', 2, 15), Clue('RIGHT', 2, 12))) 
cells.append(ClueCell((1, 4), Clue('DOWN', 2, 9), None))
# row 3
cells.append(ClueCell((2, 0), None, Clue('RIGHT', 4, 13)))
# row 4
cells.append(ClueCell((3, 0), None, Clue('RIGHT', 4, 29)))
# row 5
cells.append(BlackCell((4, 0)))
cells.append(ClueCell((4, 1), None, Clue('RIGHT', 2, 4))) 
cells.append(BlackCell((4, 4)))
puzzle = Puzzle(5, 5, cells)
# unintelligent agent:
unintelligent_agent = SolveUnInt(copy.deepcopy(puzzle)) 
unintelligent_start = timeit.default_timer() 
unintelligent_agent.solve()
unintelligent_stop = timeit.default_timer() 
unintelligent_time = unintelligent_stop - unintelligent_start
print("Unintelligent agent solved the puzzle in: \t", str(unintelligent_time))

# intelligent agent:
intelligent_agent = SolveInt(copy.deepcopy(puzzle)) 
intelligent_start = timeit.default_timer() 
intelligent_agent.solve()
intelligent_stop = timeit.default_timer()
intelligent_time = intelligent_stop - intelligent_start

print("Unintelligent agent solved the puzzle in: \t", str(unintelligent_time))
print("Intelligent agent solved the puzzle in: \t", str(intelligent_time))

