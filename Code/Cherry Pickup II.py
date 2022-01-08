class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                  #Get the dimensions of grid.
        cherryDict = {(0, n - 1): grid[0][0] + grid[0][-1]}                             #Store cherries picked by the pair of columns of robots in first row.
        for i in range(1, m):                                                           #Traverse top down.
            newCherryDict = defaultdict(int)                                            #Store the cherries picked so far by the pair of columns of robots in current row.
            for (x, y), val in cherryDict.items():
                robot1 = [a for a in [x - 1, x, x + 1] if a >= 0 and a < n]             #Generate all available columns for robot 1 in this row.
                robot2 = [b for b in [y - 1, y, y + 1] if b >= 0 and b < n]             #Generate all available columns for robot 2 in this row.
                for a, b in product(robot1, robot2):
                    newVal = val + grid[i][a] + grid[i][b] * (a != b)                   #For each pair of columns of robot, calculate new value of cherries picked so far. If robots are in same column, only add it once.
                    newCherryDict[(a, b)] = max(newCherryDict[a, b], newVal)            #Add or update the value by pair of columns of robots.
            cherryDict = newCherryDict                                                  #Replace cherryDict with newCherryDict.
        return max(cherryDict.values())                                                 #Return the max value of cherries in last row.
