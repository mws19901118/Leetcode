class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        leftTurn = {(-1, 0): (0, -1), (0, 1): (-1, 0), (1, 0): (0, 1), (0, -1): (1, 0)}            #Define the left turn result for each direction.
        rightTurn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}           #Define the right turn result for each direction.
        obstacleSet = set((x, y) for x, y in obstacles)                                            #Store obstacles in a set.
        x, y, u, v, result = 0, 0, 0, 1, 0                                                         #Initialize starting point, direction and result.
        for c in commands:                                                                         #Traverse commands.
            if c == -1:                                                                            #Update direction after right turn.
                u, v = rightTurn[(u, v)]
            elif c == -2:                                                                          #Update direction after left turn.
                u, v = leftTurn[(u, v)]
            else:
                for _ in range(c):                                                                 #Move forward.
                    x += u
                    y += v
                    if (x, y) in obstacleSet:                                                      #If run into an obstacle, take a step back.
                        x -= u
                        y -= v
                        break
                result = max(result, x * x + y * y)                                                #Update result.
        return result
