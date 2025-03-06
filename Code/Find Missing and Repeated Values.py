class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)                                  #Get n.
        visited = set()                                #Store visited numbers in a set.
        result = []                                    #Initialize result.
        for i, j in product(range(n), range(n)):       #Traverse grid.
            if grid[i][j] in visited:                  #If current number is already visited, append it to result.
                result.append(grid[i][j])
            visited.add(grid[i][j])                    #Add current number to result.
        for x in range(1, n * n + 1):                  #Traverse from 1 to n ** 2.
            if x not in visited:                       #If x is not visited, append it to result.
                result.append(x)
        return result
