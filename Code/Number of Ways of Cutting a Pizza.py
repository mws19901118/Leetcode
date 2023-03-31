class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])                                                                                                                #Get the dimensions of pizza.
        division = 10 ** 9 + 7                                                                                                                          #Initialize division.
        count = [[0 for j in range(n + 1)] for i in range(m + 1)]                                                                                       #Since left piece or upper piece after cut will always be given away, count the number of apples from each row and column as top left corner to the bottom right corner.
        for i, j in product(reversed(range(m)), reversed(range(n))):
            count[i][j] = int(pizza[i][j] == 'A') + count[i + 1][j] + count[i][j + 1] - count[i + 1][j + 1]

        @cache                                                                                                                                          #Cache result.
        def dp(row: int, column: int, cut: int) -> int:                                                                                                 #Calculate the number of ways of cutting current row and column as top left corner to bottom right with "cut" pieces. 
            if cut == 1:                                                                                                                                #If cut is 1, directly return if count[row][column] is larger than 0, because every piece should have at lease one apple.
                return int(count[row][column] > 0)
            result = 0                                                                                                                                  #Initialize result.
            result += sum(dp(i, column, cut - 1) for i in range(row + 1, m) if count[row][column] - count[i][column])                                   #For each row from row + 1 to m - 1, if count[row][column] - count[i][column] > 0, then we can cut at row i with upper part having at least one apple, so continue dp at row i and add dp(i, column, cut - 1) to result. 
            result += sum(dp(row, j, cut - 1) for j in range(column + 1, n) if count[row][column] - count[row][j])                                      #For each column from column + 1 to n - 1, if count[row][column] - count[row][j] > 0, then we can cut at column j with left part having at least one apple, so continue dp at column j and add dp(row, j, cut - 1) to result.
            return result % division                                                                                                                    #Calculate the modulo.

        return dp(0, 0, k)                                                                                                                              #Return the result of dp(0, 0, k).
