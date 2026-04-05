class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {'L': (-1, 0), 'U': (0, 1), 'R': (1, 0), 'D': (0, -1)}    #Define 4 directions.
        x, y = 0, 0                                                            #Initialize coordinates.
        for d in moves:                                                        #Traverse moves.
            x += directions[d][0]                                              #Update x.
            y += directions[d][1]                                              #Update y.
        return not x and not y                                                 #Return if the robot returns to the origin.
