class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])                      #Get the dimensions.
        s = [0] * (n + 1)                                   #Intialize the prefix sum; in row i, s[j + 1] means the prefix sum from the top left corner to grid[i][j].
        result = 0
        for i in range(m):                                  #Traverse each row.
            prev = 0                                        #Store the prefix sum from top left corner to grid[i - 1][j - 1]; initially it is 0 as such submatrix does not exist.
            for j in range(n):                              #Traver current row.
                t = s[j + 1]                                #Store s[j + 1] temporarily.
                s[j + 1] += grid[i][j] + s[j] - prev        #Update s[j + 1] which is its previous value(the prefix sum from the top left corner to grid[i - 1][j]) plus s[j](the prefix sum from the top left corner to grid[i][j - 1]) plus grid[i][j] minus prev(the prefix sum from the top left corner to grid[i - 1][j - 1]).
                prev = t                                    #Replace prev with previous s[j + 1] for next calculation.
                if s[j + 1] <= k:                           #If s[j + 1] is smaller than or equal to k, increase result.
                    result += 1
                else:                                       #Otherwise, stop processing current row as the rest submatrices sums are all greater than k.
                    break
        return result
