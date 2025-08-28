class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)                                                                                  #Get the dimensions.
        for i in range(2 * n - 1):                                                                     #Traverse the start of each diagonal.
            x, y = (i, 0) if i < n else (0, i - n + 1)
            diagonal = sorted([grid[x + j][y + j] for j in range(n - x - y)], reverse = i >= n)        #Grab each diagonal and sort in the reverse order of requirement.
            u, v = x, y                                                                                #Putback the numbers on diagonal.
            while u < n and v < n:
                grid[u][v] = diagonal.pop()
                u += 1
                v += 1
        return grid
