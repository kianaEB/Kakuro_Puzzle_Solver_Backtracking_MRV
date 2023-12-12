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
# cells.append(BlackCell((0, 0)))
# cells.append(BlackCell((0, 1)))
# cells.append(ClueCell((0, 2), Clue('DOWN', 4, 22), None)) 
# cells.append(ClueCell((0, 3), Clue('DOWN', 4, 12), None)) 
# cells.append(BlackCell((0, 4)))
# # row 2
# cells.append(BlackCell((1, 0)))
# cells.append(ClueCell((1, 1), Clue('DOWN', 2, 15), Clue('RIGHT', 2, 12))) 
# cells.append(ClueCell((1, 4), Clue('DOWN', 2, 9), None))
# # row 3
# cells.append(ClueCell((2, 0), None, Clue('RIGHT', 4, 13)))
# # row 4
# cells.append(ClueCell((3, 0), None, Clue('RIGHT', 4, 29)))
# # row 5
# cells.append(BlackCell((4, 0)))
# cells.append(ClueCell((4, 1), None, Clue('RIGHT', 2, 4))) 
# cells.append(BlackCell((4, 4)))
# puzzle = Puzzle(5, 5, cells)

#---------------------------------------------------------------------------

#****** Easy Kakuro Set1 ******

# #row1
# cells.append(BlackCell((0, 0)))
# cells.append(BlackCell((0, 1)))
# cells.append(ClueCell((0, 2), Clue('DOWN', 4, 30), None))
# cells.append(ClueCell((0, 3), Clue('DOWN', 2, 4), None))
# cells.append(ClueCell((0, 4), Clue('DOWN', 3, 24), None))
# cells.append(BlackCell((0, 5)))
# cells.append(ClueCell((0, 6), Clue('DOWN', 2, 4), None))
# cells.append(ClueCell((0, 7), Clue('DOWN', 2, 16), None))

# #row2
# cells.append(BlackCell((1, 0)))
# cells.append(ClueCell((1, 1), Clue('DOWN', 2, 16), Clue('RIGHT', 3, 19)))
# cells.append(ClueCell((1, 5), Clue('DOWN', 3, 9), Clue('RIGHT', 2, 10)))

# #row3
# cells.append(ClueCell((2, 0), None, Clue('RIGHT', 7, 39)))

# #row4
# cells.append(ClueCell((3, 0), None, Clue('RIGHT', 2, 15)))
# cells.append(ClueCell((3, 3), Clue('DOWN', 3, 23), Clue('RIGHT', 2, 10)))
# cells.append(ClueCell((3, 6), Clue('DOWN', 4, 10), None))
# cells.append(BlackCell((3, 7)))

# #row5
# cells.append(BlackCell((4, 0)))
# cells.append(ClueCell((4, 1), None, Clue('RIGHT', 2, 16)))
# cells.append(ClueCell((4, 4), Clue('DOWN', 3, 6), Clue('RIGHT', 2, 4)))
# cells.append(ClueCell((4, 7), Clue('DOWN', 2, 16), None))

# #row6
# cells.append(BlackCell((5, 0)))
# cells.append(ClueCell((4, 1), Clue('DOWN', 2, 14), None))
# cells.append(ClueCell((5, 2), Clue('DOWN', 2, 16), Clue('RIGHT', 2, 9)))
# cells.append(ClueCell((5, 5), Clue('DOWN', 2, 4), Clue('RIGHT', 2, 12)))

# #row7
# cells.append(ClueCell((6, 0), None, Clue('RIGHT', 7, 35)))

# #row8
# cells.append(ClueCell((7, 0), None, Clue('RIGHT', 2, 16)))
# cells.append(ClueCell((7, 3), None, Clue('RIGHT', 3, 7)))
# cells.append(BlackCell((7, 7)))

# puzzle = Puzzle(8, 8, cells)

#---------------------------------------------------------------------------

#****** Medium Kakuro Set1 ******

# #row1
# cells.append(BlackCell((0, 0)))
# cells.append(BlackCell((0, 1)))
# cells.append(BlackCell((0, 2)))
# cells.append(BlackCell((0, 3)))
# cells.append(ClueCell((0, 4), Clue('DOWN', 7, 40), None))
# cells.append(ClueCell((0, 5), Clue('DOWN', 2, 3), None))
# cells.append(BlackCell((0, 6)))
# cells.append(BlackCell((0, 7)))

# #row2
# cells.append(BlackCell((1, 0)))
# cells.append(BlackCell((1, 1)))
# cells.append(BlackCell((1, 2)))
# cells.append(ClueCell((1, 3), Clue('DOWN', 3, 8), Clue('RIGHT', 2, 6)))
# cells.append(BlackCell((1, 6)))
# cells.append(BlackCell((1, 7)))

# #row3
# cells.append(BlackCell((2, 0)))
# cells.append(BlackCell((2, 1)))
# cells.append(ClueCell((2, 2), None, Clue('RIGHT', 3, 7)))
# cells.append(ClueCell((2, 6), Clue('DOWN', 2, 3), None))
# cells.append(ClueCell((2, 7), Clue('DOWN', 2, 14), None))

# #row4
# cells.append(BlackCell((3, 0)))
# cells.append(ClueCell((3, 1), Clue('DOWN', 2, 6), None))
# cells.append(ClueCell((3, 2), Clue('DOWN', 2, 4), Clue('RIGHT', 2, 10)))
# cells.append(ClueCell((3, 5), Clue('DOWN', 3, 24), Clue('RIGHT', 2, 9)))

# #row5
# cells.append(ClueCell((4, 0), None, Clue('RIGHT', 7, 28)))

# #row6
# cells.append(ClueCell((5, 0), None, Clue('RIGHT', 2, 3)))
# cells.append(ClueCell((5, 3), Clue('DOWN', 2, 17), Clue('RIGHT', 2, 17)))
# cells.append(BlackCell((5, 6)))
# cells.append(BlackCell((5, 7)))

# #row7
# cells.append(BlackCell((6, 0)))
# cells.append(BlackCell((6, 1)))
# cells.append(ClueCell((6, 2), None, Clue('RIGHT', 3, 23)))
# cells.append(BlackCell((6, 6)))
# cells.append(BlackCell((6, 7)))

# #row8
# cells.append(BlackCell((7, 0)))
# cells.append(BlackCell((7, 1)))
# cells.append(ClueCell((7, 2), None, Clue('RIGHT', 2, 16)))
# cells.append(BlackCell((7, 5)))
# cells.append(BlackCell((7, 6)))
# cells.append(BlackCell((7, 7)))

# puzzle = Puzzle(8, 8, cells)

#---------------------------------------------------------------------------

#****** Hard Kakuro Set1 ******

# #row1
# cells.append(BlackCell((0, 0)))
# cells.append(ClueCell((0, 1), Clue('DOWN', 2, 10), None))
# cells.append(ClueCell((0, 2), Clue('DOWN', 3, 10), None))
# cells.append(BlackCell((0, 3)))
# cells.append(BlackCell((0, 4)))
# cells.append(BlackCell((0, 5)))
# cells.append(BlackCell((0, 6)))
# cells.append(BlackCell((0, 7)))
# cells.append(ClueCell((0, 8), Clue('DOWN', 3, 23), None))
# cells.append(ClueCell((0, 9), Clue('DOWN', 2, 16), None))

# #row2
# cells.append(ClueCell((1, 0), None, Clue('RIGHT', 2, 4)))
# cells.append(ClueCell((1, 3), Clue('DOWN', 2, 17), None))
# cells.append(BlackCell((1, 4)))
# cells.append(BlackCell((1, 5)))
# cells.append(BlackCell((1, 6)))
# cells.append(ClueCell((1, 7), Clue('DOWN', 3, 17), Clue('RIGHT', 2, 16)))

# #row3
# cells.append(ClueCell((2, 0), None, Clue('RIGHT', 3, 23)))
# cells.append(ClueCell((2, 4), Clue('DOWN', 5, 20), None))
# cells.append(BlackCell((2, 5)))
# cells.append(ClueCell((2, 6), Clue('DOWN', 5, 30), Clue('RIGHT', 3, 24)))

# #row4
# cells.append(BlackCell((3, 0)))
# cells.append(ClueCell((3, 1), None, Clue('RIGHT', 3, 13)))
# cells.append(ClueCell((3, 5), Clue('DOWN', 3, 20), Clue('RIGHT', 3, 23)))
# cells.append(BlackCell((3, 9)))

# #row5
# cells.append(BlackCell((4, 0)))
# cells.append(BlackCell((4, 1)))
# cells.append(BlackCell((4, 2)))
# cells.append(ClueCell((4, 3), None, Clue('RIGHT', 4, 11)))
# cells.append(BlackCell((4, 8)))
# cells.append(BlackCell((4, 9)))

# #row6
# cells.append(BlackCell((5, 0)))
# cells.append(BlackCell((5, 1)))
# cells.append(BlackCell((5, 2)))
# cells.append(ClueCell((5, 3), Clue('DOWN', 3, 6), Clue('RIGHT', 3, 23)))
# cells.append(BlackCell((5, 7)))
# cells.append(BlackCell((5, 8)))
# cells.append(BlackCell((5, 9)))

# #row7
# cells.append(BlackCell((6, 0)))
# cells.append(BlackCell((6, 1)))
# cells.append(ClueCell((6, 2), Clue('DOWN', 3, 7), Clue('RIGHT', 4, 25)))
# cells.append(ClueCell((6, 7), Clue('DOWN', 2, 3), None))
# cells.append(ClueCell((6, 8), Clue('DOWN', 3, 9), None))
# cells.append(BlackCell((6, 9)))

# #row8
# cells.append(BlackCell((7, 0)))
# cells.append(ClueCell((7, 1), Clue('DOWN', 2, 4), Clue('RIGHT', 3, 8)))
# cells.append(ClueCell((7, 5), None, Clue('RIGHT', 3, 7)))
# cells.append(ClueCell((7, 9), Clue('DOWN', 2, 4), None))

# #row9
# cells.append(ClueCell((8, 0), None, Clue('RIGHT', 3, 6)))
# cells.append(BlackCell((8, 4)))
# cells.append(BlackCell((8, 5)))
# cells.append(ClueCell((8, 6), None, Clue('RIGHT', 3, 6)))

# #row10
# cells.append(ClueCell((9, 0), None, Clue('RIGHT', 2, 3)))
# cells.append(BlackCell((9, 3)))
# cells.append(BlackCell((9, 4)))
# cells.append(BlackCell((9, 5)))
# cells.append(BlackCell((9, 6)))
# cells.append(ClueCell((9, 7), None, Clue('RIGHT', 2, 4)))

# puzzle = Puzzle(10, 10, cells)

#---------------------------------------------------------------------------

#****** Expert Kakuro Set1 ******

#row1
cells.append(BlackCell((0, 0)))
cells.append(BlackCell((0, 1)))
cells.append(BlackCell((0, 2)))
cells.append(ClueCell((0, 3), Clue('DOWN', 2, 3), None))
cells.append(ClueCell((0, 4), Clue('DOWN', 3, 23), None))
cells.append(ClueCell((0, 5), Clue('DOWN', 9, 45), None))
cells.append(ClueCell((0, 6), Clue('DOWN', 2, 6), None))
cells.append(BlackCell((0, 7)))
cells.append(BlackCell((0, 8)))
cells.append(BlackCell((0, 9)))

#row2
cells.append(BlackCell((1, 0)))
cells.append(BlackCell((1, 1)))
cells.append(ClueCell((1, 2), None, Clue('RIGHT', 4, 12)))
cells.append(ClueCell((1, 7), Clue('DOWN', 2, 4), None))
cells.append(BlackCell((1, 8)))
cells.append(BlackCell((1, 9)))

#row3
cells.append(BlackCell((2, 0)))
cells.append(ClueCell((2, 1), Clue('DOWN', 4, 20), None))
cells.append(ClueCell((2, 2), Clue('DOWN', 5, 32), Clue('RIGHT', 5, 21)))
cells.append(ClueCell((2, 8), Clue('DOWN', 5, 15), None))
cells.append(BlackCell((2, 9)))

#row4
cells.append(ClueCell((3, 0), None, Clue('RIGHT', 2, 3)))
cells.append(ClueCell((3, 3), Clue('DOWN', 2, 17), Clue('RIGHT', 2, 15)))
cells.append(ClueCell((3, 6), Clue('DOWN', 2, 5), Clue('RIGHT', 2, 4)))
cells.append(ClueCell((3, 9), Clue('DOWN', 4, 16), None))

#row5
cells.append(ClueCell((4, 0), None, Clue('RIGHT', 3, 24)))
cells.append(ClueCell((4, 4), Clue('DOWN', 2, 16), Clue('RIGHT', 2, 3)))
cells.append(ClueCell((4, 7), Clue('DOWN', 2, 4), Clue('RIGHT', 2, 7)))

#row6
cells.append(ClueCell((5, 0), None, Clue('RIGHT', 9, 45)))

#row7
cells.append(ClueCell((6, 0), None, Clue('RIGHT', 2, 17)))
cells.append(ClueCell((6, 3), Clue('DOWN', 2, 13), Clue('RIGHT', 2, 17)))
cells.append(ClueCell((6, 6), Clue('DOWN', 3, 24), Clue('RIGHT', 3, 6)))

#row8
cells.append(BlackCell((7, 0)))
cells.append(ClueCell((7, 1), None, Clue('RIGHT', 2, 16)))
cells.append(ClueCell((7, 4), Clue('DOWN', 2, 17), Clue('RIGHT', 2, 15)))
cells.append(ClueCell((7, 7), Clue('DOWN', 2, 13), Clue('RIGHT', 2, 6)))

#row9
cells.append(BlackCell((8, 0)))
cells.append(BlackCell((8, 1)))
cells.append(ClueCell((8, 2), None, Clue('RIGHT', 5, 32)))
cells.append(BlackCell((8, 8)))
cells.append(BlackCell((8, 9)))

#row10
cells.append(BlackCell((9, 0)))
cells.append(BlackCell((9, 1)))
cells.append(BlackCell((9, 2)))
cells.append(ClueCell((9, 3), None, Clue('RIGHT', 4, 30)))
cells.append(BlackCell((9, 8)))
cells.append(BlackCell((9, 9)))


puzzle = Puzzle(10, 10, cells)





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
