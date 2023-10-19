# square floor ( )
# wall (#)
# box ($)
# storage locations  (.)
# player (@) // can move horizentally or veritcally. but not diagonally.
# cannot pass walls or boxes
# the player has to walk next to box in order to move it.
# the player cannot pull it.
# how to define pulling and pushing?
#
# pushing : if the ($) is in front  goes in direction of
# in order to push the target square has to be empty
#
# * the number of boxes equal the number of locations -> (.) the same as ($)
#
# goal ->  boxes are at storage locations. ($) at (.) all of them
#heuristic one: consider the distance between the minimum of the boxes and the targets + the distance  of where the current (@) is, to the nearest box

# the code is taken from the pacmanproblem and modified slightly
# here the professor just implements for heuristis the straigt line


from AI_problem import SearchProblem
class SokobanPuzzleProblem(SearchProblem):
    def __init__(self, grid, Sokoban, storage_locatoins):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.Sokoban = Sokoban
        self.storage_locatoins = storage_locatoins

    # since we need to output the solution path, it is stored in the state as
    # tuple(tuple(r,c), [tuple(r1,c1), tuple(r2,c2), ...])  where the first
    # tuple is the current position of pacman and the list is the path taken

    def getStartState(self):
        return (self.Sokoban, [self.Sokoban])

    def isGoalState(self, state):
        return state[0] == self.storage_locatoins

    def getSuccessors(self, state):
        moves = []
        path = state[1]

        def getMove(r, c):
            if self.grid[r][c] != '#' and  self.grid[r][c] !='$':  # not a wall and not a box
                newPath = list(path)
                move = (r, c)
                newPath.append(move)
                moves.append((move, newPath))

        if state[0][0] > 0:
            getMove(state[0][0] - 1, state[0][1])  # go up
        if state[0][0] < self.rows - 1:
            getMove(state[0][0] + 1, state[0][1])  # go down
        if state[0][1] > 0:
            getMove(state[0][0], state[0][1] - 1)  # go left
        if state[0][1] < self.columns - 1:
            getMove(state[0][0], state[0][1] + 1)  # go right
        return moves

    def getHeuristics(self):
        # straight-line distance between Sokoban and the boxes
        def straightLineDistance(state):
            Sokoban, storage_locatoins = state[0], self.storage_locatoins
            return ((storage_locatoins[1] - Sokoban[1]) ** 2 + (storage_locatoins[0] - Sokoban[0]) ** 2) ** 0.5

        return [straightLineDistance]

###

p_11_easy="""
###########
#         #
#         #
#  . . .  #
#    $    #
#    $    #
#    $    #
#         #
#    @    #
#         #
###########
"""
print(p_11_easy)
print ('hi')

#11
#21
#31