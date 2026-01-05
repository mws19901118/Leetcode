class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)                                                 #Get the dimension.
        nonPositiveCount, absMin, absSum = 0, inf, 0                    #Initialize the non-positive number count, minimum of abs of each number and sum of abs of each number.
        for i, j in product(range(n), range(n)):                        #Traverse matrix.
            nonPositiveCount += int(matrix[i][j] <= 0)                  #Update nonPositiveCount.
            absMin = min(absMin, abs(matrix[i][j]))                     #Update absMin.
            absSum += abs(matrix[i][j])                                 #Update absSum.
        return absSum - (absMin if nonPositiveCount & 1 else 0) * 2     #Since we can move the non-positive sign inside matrix without modifying the count of non-negative numbers. So, just move all non-positive signs into adjacent areas.
                                                                        #Next flip them: if the count of non-positive sign is even, we can flip all of them to non-negative and the result is absSum; otherwise, there is one left and desinate it to be the number of absMin, so the result is absSum - absMin * 2.
