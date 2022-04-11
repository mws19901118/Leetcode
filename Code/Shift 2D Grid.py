class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])                                                  #Get the dimensions.
        right, down = k % n, (k // n) % m                                               #Get the distance to shift right and down. 
        shifted = [grid[i - 1][n - right:] + grid[i][:n - right] for i in range(m)]     #Shift right each row and use elements from end of last row to fill the shifted beginning.
        return shifted[m - down:] + shifted[:m - down]                                  #Shift down and return.
