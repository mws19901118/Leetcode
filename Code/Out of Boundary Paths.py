class Solution:
    @cache                                                                                            #Cache result.
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:                      #If current starting position is out of bound, return 1 as we found a path.
            return 1
        if not maxMove:                                                                               #If maxMove is 0, return 0 as the ball can move no more.
            return 0
        return (self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)                          #Sum up the paths of each adjacent position with maxMove - 1, then return the modulo.
                + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1) 
                + self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn) 
                + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)) % (10 ** 9 + 7)
