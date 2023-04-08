class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])                                              #Get the dimensions.
        result = 0                                                                #Initialize result.
        for i in range(m):                                                        #Traverse each row.
            stack, dp = [-1], [0] * (n + 1)                                       #Initialize the stack and dp for current row. Stack store the indexes of histogram that in a desending order(initially -1) and dp is the number of submatrices whose down right corner is current cell.
            for j in range(n):                                                    #Traverse each column in current row.
                if i > 0 and mat[i][j]:                                           #Build the histogram of 1's so far on the column.
                    mat[i][j] += mat[i - 1][j]
                while len(stack) > 1 and mat[i][j] < mat[i][stack[-1]]:           #While stack has more than 1 element and the histogram at stack top is higher than the current histogram, pop stack.
                    stack.pop()
                dp[j] = dp[stack[-1]] + mat[i][j] * (j - stack[-1])               #Set dp[j]; because mat[i][stack[-1]] <= mat[i][j], all submatrices whose down right corner is mat[i][stack[-1]] can be extended to mat[i][j]; then for each column from stack[-1] + 1 to j, there are mat[i][j] submatrices since the histograms are all larget than or equal to mat[i][j].  
                stack.append(j)                                                   #Append j to stack.
                result += dp[j]                                                   #Add dp[j] to result.
        return result                                                             #Return result.
