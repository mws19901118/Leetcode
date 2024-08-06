class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)                                              #Get the dimension.
        source, destination = [], []
        for i, j in product(range(n), range(n)):                   #Traverse matrix to find out source cells, which have more than 1 stone, and destination cells, which have no stone.
            if grid[i][j] > 1:
                source.append((i, j))
            elif not grid[i][j]:
                destination.append((i, j))
        result = inf                                               #Initialize result.
        for p in permutations(destination):                        #Enumerate the permutation of destinations.
            moves, index = 0, 0                                    #Initialize moves for this permutation and index to traverse current permutation.
            for x, y in source:                                    #Traverse source.
                for u, v in p[index:index + grid[x][y] - 1]:       #Move stones from current source cell to the destination cells of current permutaion in order.
                    moves += abs(x - u) + abs(y - v)
                index += grid[x][y] - 1
            result = min(moves, result)                            #Update result.
        return result
