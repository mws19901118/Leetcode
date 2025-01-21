class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])                                                                                                        #Get the length of each row.
        prefixSums = [[0], [0]]                                                                                                 #Initialize prefix sums for each row.
        for i, j in product(range(2), range(n)):                                                                                #Populate prefix sums for each row.
            prefixSums[i].append(prefixSums[i][-1] + grid[i][j])
        return min(max(prefixSums[0][-1] - prefixSums[0][i + 1], prefixSums[1][i] - prefixSums[1][0]) for i in range(n))        #After first bot traverse, assuming it moves down at index i, the optimal traverse for second bot is to take either grid[0][i + 1:] or grid[1][:i].
                                                                                                                                #So, we enumberate each index i for first bot, and find the min value of max(sum(grid[0][i + 1:]), sum(grid[1][:i])).
                                                                                                                                #Since we already computed prefix sums, sum(grid[0][i + 1:] = prefixSums[0][-1] - prefixSums[0][i + 1] and sum(grid[1][:i]) = prefixSums[1][i] - prefixSums[1][0]).
