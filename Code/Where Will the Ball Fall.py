class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])                                            #Get the demensions.

        @cache                                                                    #Cache the result of moving ball.
        def move(x: int, y: int, direction: int) -> int:
            if y < 0 or y >= n:                                                   #If y is out of left boundary or right boundary, return -1 cause ball will stuck against boundary.
                return -1
            if x == m:                                                            #If x == m, the ball falls at column y, so return y.
                return y        
            if direction == 0:                                                    #If the ball enters from top, move it to adjacent cell with direction based on the direction of current cell.
                return move(x, y + grid[x][y], grid[x][y])
            else:                                                                 #Otherwise if the ball enters from side, and the direction is same with cell direction, move the ball to the lower cell.
                return move(x + 1, y, 0) if grid[x][y] == direction else -1       #If the direction is opposite with cell direction, the ball will stuck in a V shape.

        return [move(0, x, 0) for x in range(n)]                                  #Return the destionations of each ball.
