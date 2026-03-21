class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i, j in product(range(k // 2), range(k)):                                                            #Traverse the top half rows.
            grid[x + i][y + j], grid[x + k - 1 - i][y + j] = grid[x + k - 1 - i][y + j], grid[x + i][y + j]      #Do the flip with the bottom half rows.
        return grid
