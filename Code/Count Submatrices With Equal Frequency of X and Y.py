class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])                                        #Get the dimensions.
        s = [[0, 0] for _ in range(n + 1)]                                    #Intialize the prefix count of 'X' and 'Y'; in row i, s[j + 1] means the prefix count from the top left corner to grid[i][j].
        result = 0
        for i in range(m):                                                    #Traverse each row.
            prev = [0, 0]                                                     #Store the prefix count from top left corner to grid[i - 1][j - 1]; initially it is [0, 0] as such submatrix does not exist.
            for j in range(n):                                                #Traver current row.
                t = [s[j + 1][0], s[j + 1][1]]                                #Store s[j + 1] temporarily(store the value because the value might change).
                s[j + 1][0] += int(grid[i][j] == 'X') + s[j][0] - prev[0]     #Update s[j + 1][0] which is its previous value(the prefix count from the top left corner to grid[i - 1][j]) plus s[j](the prefix count from the top left corner to grid[i][j - 1]) plus 1 if grid[i][j] is 'X' minus prev(the prefix count from the top left corner to grid[i - 1][j - 1]).
                s[j + 1][1] += int(grid[i][j] == 'Y') + s[j][1] - prev[1]     #Update s[j + 1][1] which is its previous value(the prefix count from the top left corner to grid[i - 1][j]) plus s[j](the prefix count from the top left corner to grid[i][j - 1]) plus 1 if grid[i][j] is 'Y' minus prev(the prefix count from the top left corner to grid[i - 1][j - 1]).
                prev = t                                                      #Replace prev with previous s[j + 1] for next calculation.
                result += int(s[j + 1][0] and s[j + 1][0] == s[j + 1][1])     #Increase result if s[j + 1][0] and s[j + 1][1] are equal and greater than 0.
        return result
